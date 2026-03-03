import socket

HOST = '0.0.0.0'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[*] Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[+] Connection from {addr}")
            data = conn.recv(1024)
            print(f"[>] Received: {data}")
            if b'ViolentPython' in data:
                conn.sendall(b'ViolentPython OK\r\n')
            else:
                conn.sendall(b'Unknown command\r\n')
