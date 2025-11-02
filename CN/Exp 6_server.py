# server.py
import socket

HOST = '0.0.0.0'   # listen on all interfaces
PORT = 12345       # non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # decode, transform, encode
            text = data.decode('utf-8')
            capitalized = text.upper()        # convert to uppercase (or use .capitalize() if required) 
            conn.sendall(capitalized.encode('utf-8'))
        print('Connection closed')
