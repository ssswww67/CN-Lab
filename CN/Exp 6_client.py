# client.py
import socket

SERVER_HOST = '127.0.0.1'  # change to server IP if remote machine
SERVER_PORT = 12345

message = input("Enter text to capitalize: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)
    print('Received from server:', data.decode('utf-8'))
