import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5000

def handle_client(con, add):
    with con:
        print(f"[{time.strftime('%X')}]Connected by client address: {add}")
        
        # Receive data from the client (up to 1024 bytes) and decode it
        data = con.recv(1024)
        message = data.decode('utf-8')
        print(f"[{time.strftime('%X')}] Received from {add}: {message}")

        # Add delay
        time.sleep(2)
        
        # Send a response back to the correct client
        response = f"Server received: {message}"
        con.sendall(response.encode('utf-8'))
        print(f"[{time.strftime('%X')}] Finished handling {add}")

#AF_INET make socket use Ipv4, SOCK_STREAM make socket uset TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # .bind() and .connect() only take a tuple of (host, port)
    # .bind() Bind socket to 127.0.0.1 (local host of Ipv4) on port 5000, use for server
    s.bind((HOST, PORT))
    s.listen() #Set socket to listenning mode to listen to incomming request from client
    print(f"Server is listening on {HOST}:{PORT}...")

    while True:
        # Accept incoming client connection
        con, add = s.accept()
        
        # Create and start a threading.Thread for each accepted client connection
        thread = threading.Thread(target=handle_client, args=(con, add))
        thread.start()


