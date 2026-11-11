import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # .connect() Connect the socket to the server at localhost on port 5000, use for client
    s.connect((HOST, PORT))

    # Send the required message encoded to bytes
    message = "Hello from client!"
    s.sendall(message.encode('utf-8')) #encode data to utf-8 cuz TCP only send raw bits
    
    # .recv() Receive the response from the server and print it
    data = s.recv(1024)
    print(data.decode('utf-8')) #decode raw bits to readable text
