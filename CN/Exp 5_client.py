import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

print("Starting client...")

try:
    # Create a socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Connecting to {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        print("Connected to server.")
        
        # Define the message to send
        message = "Hello, server!"
        
        # Encode the string into bytes and send it
        print(f"Sending: '{message}'")
        s.sendall(message.encode('utf-8'))
        
        # Look for the response
        # We'll receive up to 1024 bytes
        data = s.recv(1024)
        
        # Decode the received bytes into a string and print it
        print(f"Received from server: {data.decode('utf-8')}")
        
        # Add a small delay so the user can see the messages
        time.sleep(1)

except ConnectionRefusedError:
    print("Connection failed. Is the server running?")
except Exception as e:
    print(f"An error occurred: {e}")

print("Client shutting down.")
