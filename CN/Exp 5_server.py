import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

print("Starting server...")

# Use a 'with' statement to automatically close the socket when done
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    
    # Enable the server to accept connections
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    
    # Block and wait for an incoming connection
    # 'conn' is a new socket object usable to send and receive data on the connection
    # 'addr' is the address bound to the socket on the other end of the connection
    conn, addr = s.accept()
    
    # Use a 'with' statement for the connection as well
    with conn:
        print(f"Connected by {addr}")
        
        # Loop to handle incoming data
        while True:
            # Receive data from the client (buffer size 1024 bytes)
            data = conn.recv(1024)
            
            # If recv() returns an empty bytes object, the client closed the connection
            if not data:
                print("Client disconnected.")
                break
                
            # Decode the received bytes into a string and print it
            message = data.decode('utf-8')
            print(f"Received from client: {message}")
            
            # Send a response back to the client
            # We must encode the string into bytes before sending
            response = f"Server received your message: '{message}'"
            conn.sendall(response.encode('utf-8'))

print("Server shutting down.")
