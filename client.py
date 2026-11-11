import socket
import time

HOST = "127.0.0.1"
PORT = 5000
max_retries = 3

# Implement retry loop max 3 retries
for attempt in range(1, max_retries + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    
            # Add 2 seconds timeout between each connection
            s.settimeout(2)
            print(f"Attempt {attempt}: Connecting to server...")

            # .connect() Connect the socket to the server at localhost on port 5000, use for client
            s.connect((HOST, PORT))

            # Send the required message encoded to bytes
            message = "Hello from client!"
            s.sendall(message.encode('utf-8')) #encode data to utf-8 cuz TCP only send raw bits
            
            # .recv() Receive the response from the server and print it
            data = s.recv(1024)
            print(data.decode('utf-8')) #decode raw bits to readable text

            # Success! Break out of the retry loop
            break
    except (ConnectionRefusedError, socket.timeout) as e:
        print(f"Attempt {attempt} failed (Error: {e})")
        # Apply exponential backoff delays (0.5s before 2nd try, 1s before 3rd try)
        if attempt == 1:
            print("Waiting 0.5 seconds before next attempt...\n")
            time.sleep(0.5)
        elif attempt == 2:
            print("Waiting 1.0 second before final attempt...\n")
            time.sleep(1.0)
        else:
            print("Max retries reached. Giving up.")