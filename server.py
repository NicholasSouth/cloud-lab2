import socket

HOST = "127.0.0.1"
PORT = 5000

#AF_INET make socket use Ipv4, SOCK_STREAM make socket uset TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # .bind() and .connect() only take a tuple of (host, port)
    # .bind() Bind socket to 127.0.0.1 (local host of Ipv4) on port 5000, use for server
    s.bind((HOST, PORT))
    s.listen() #Set socket to listenning mode to listen to incomming request from client
    print(f"Server is listening on {HOST}:{PORT}...")

    con, add = s.accept()
    with con:
        print(f"Connected by client address: {add}")
        
        # Receive data from the client (up to 1024 bytes) and decode it
        data = con.recv(1024)
        message = data.decode('utf-8')
        print(f"Received message from client: {message}")
        
        # Send a response back to the client
        response = f"Server received: {message}"
        con.sendall(response.encode('utf-8'))
