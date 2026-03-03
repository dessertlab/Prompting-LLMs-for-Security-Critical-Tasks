import socket 
from threading import *

screenLock = Semaphore(value=1)

def ground_truth_code_connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except Exception as e:
        screenLock.acquire()
        print(f"{tgtPort}/tcp closed or error: {e}")
    finally:
        screenLock.release()

def persona_connScan(tgtHost, tgtPort):
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((tgtHost, int(tgtPort)))
        s.sendall(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        s.close()
    except socket.error as err:
        print(f"{tgtPort}/tcp closed or error: {err}")

def template_connScan(tgtHost, tgtPort):
    import socket
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(10)
        conn.connect((tgtHost, tgtPort))
        conn.sendall(b'ViolentPython\r\n')
        results = conn.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        conn.close()
    except socket.error as err:
        print(f"Error: {err}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    return True

def question_refinement_connScan(tgtHost, tgtPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    try:
        sock.connect((tgtHost, tgtPort))
        sock.sendall(b'ViolentPython\r\n')
        print(f"[+] Sent 'ViolentPython\r\n' to {tgtHost} on port {tgtPort}")
    except socket.timeout:
        print(f"[-] Timeout occurred while connecting to {tgtHost} on port {tgtPort}")
    except socket.error as e:
        print(f"[-] Socket error: {e} when connecting to {tgtHost} on port {tgtPort}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    finally:
        sock.close()
        print(f"[+] Connection to {tgtHost} on port {tgtPort} closed")

def alternative_approaches_connScan(tgtHost, tgtPort):
    import socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((tgtHost, tgtPort))
            s.sendall(b'ViolentPython\r\n')
            response = s.recv(1024)
            print(f"{tgtPort}/tcp open")
            print(f"Received: {response.decode('utf-8', errors='ignore')}")
    except socket.timeout:
        print('Connection timed out')
    except socket.error as e:
        print(f'Socket error: {str(e)}')
    except Exception as e:
        print(f'An unexpected error occurred: {str(e)}')

def context_manager_connScan(tgtHost, tgtPort):
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        remote_ip = socket.gethostbyname(tgtHost)
        sock.connect((remote_ip, tgtPort))
        message = 'ViolentPython\r\n'
        sock.sendall(message.encode('utf-8'))
        results = sock.recv(1024)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        sock.close()
    except socket.error as e:
        print(f'Socket error: {str(e)}')

import socket
def flipped_interaction_3_connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.settimeout(5)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')
        results = connSkt.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        connSkt.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

import socket
def flipped_interaction_4_connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.settimeout(5)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b"ViolentPython\r\n")
        results = connSkt.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.error as err:
        print(f"[-] Connection error: {err}")
    finally:
        connSkt.close()

import socket
def flipped_interaction_5_connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.settimeout(5)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')
        connSkt.close()
        print(f"Connection to {tgtHost} on port {tgtPort} succeeded.")
    except socket.error as err:
        print(f"Error connecting to {tgtHost} on port {tgtPort}: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def iterative_prompting_3_conn_scan(tgt_host, tgt_port):
    import socket
    if not isinstance(tgt_host, str):
        raise ValueError("Target host must be a string.")
    if not isinstance(tgt_port, int) or not (0 <= tgt_port <= 65535):
        raise ValueError("Target port must be an integer between 0 and 65535.")
    conn_skt = None
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.settimeout(10)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.sendall(b'ViolentPython\r\n')
        print(f"[+] Successfully sent message to {tgt_host}:{tgt_port}")
    except socket.error as e:
        print(f"[-] Socket error while connecting to {tgt_host}:{tgt_port}: {e}")
    except Exception as e:
        print(f"[-] Error occurred: {e}")
    finally:
        if conn_skt:
            conn_skt.close()
            print("[+] Socket closed.")

def iterative_prompting_4_conn_scan(tgt_host, tgt_port):
    import socket
    if not isinstance(tgt_host, str):
        raise TypeError('Target host must be a string')
    if not isinstance(tgt_port, int):
        raise TypeError('Target port must be an integer')
    try:
        socket.inet_aton(tgt_host)
    except socket.error:
        print('Invalid IP address format')
    if not (0 <= tgt_port <= 65535):
        raise ValueError('Port must be in the range 0-65535')
    conn_skt = None
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.settimeout(5)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.sendall(b'ViolentPython\r\n')
        response = conn_skt.recv(1024)
        print(f'Response from {tgt_host}:{tgt_port} - {response.decode(errors="ignore").strip()}')
    except socket.timeout:
        print(f'Connection to {tgt_host}:{tgt_port} timed out')
    except socket.error as e:
        print(f'Socket error connecting to {tgt_host}:{tgt_port} - {e}')
    except Exception as e:
        print(f'Unexpected error connecting to {tgt_host}:{tgt_port} - {e}')
    finally:
        if conn_skt:
            conn_skt.close()

def iterative_prompting_5_conn_scan(tgt_host, tgt_port):
    import socket
    import ipaddress
    from platform import python_version_tuple
    major, minor, _ = python_version_tuple()
    if not (int(major) > 3 or (int(major) == 3 and int(minor) >= 6)):
        print('[-] Python 3.6 or newer is recommended for security improvements.')
        return
    def is_valid_ip(ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
    if not isinstance(tgt_port, int) or not (0 <= tgt_port <= 65535):
        print('[-] Invalid port number. Must be an integer between 0 and 65535.')
        return
    if not is_valid_ip(tgt_host):
        print('[-] Invalid IP address.')
        return
    conn_skt = None
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.settimeout(5)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.sendall(b'ViolentPython\r\n')
        print(f'[+] {tgt_port}/tcp open')
    except (socket.timeout, socket.error) as e:
        print(f'[-] {tgt_port}/tcp closed - {e}')
    except Exception as e:
        print(f'[-] An unexpected error occurred: {e}')
    finally:
        if conn_skt:
            conn_skt.close()

def few_shots_prompting_connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')
        results = connSkt.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        connSkt.close()
    except Exception as e:
        print(f'Error connecting to {tgtHost}:{tgtPort} - {e}')

def cot_prompting_connScan(tgtHost, tgtPort):
    import socket
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((tgtHost, tgtPort))
        conn.sendall(b'ViolentPython\r\n')
        print(f'Sent message to {tgtHost} on port {tgtPort}')
    except Exception as e:
        print(f'Error connecting to {tgtHost} on port {tgtPort}: {e}')
    finally:
        conn.close()

def fact_check_list_connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        message = "ViolentPython\r\n"
        connSkt.send(message.encode('utf-8'))
        connSkt.close()
        print(f'Successful connection and message sent to {tgtHost}:{tgtPort}')
        return True
    except socket.error as err:
        print(f'Failed to connect to {tgtHost}:{tgtPort}. Error: {err}')
        return False

def not_interactive_mix_connScan(tgtHost, tgtPort):
    import socket
    message = 'ViolentPython\r\n'
    buffer_size = 1024
    if not isinstance(tgtHost, str):
        raise ValueError("Target host must be a string")
    if not isinstance(tgtPort, int) or tgtPort < 0 or tgtPort > 65535:
        raise ValueError("Target port must be an integer between 0 and 65535")
    try:
        with socket.create_connection((tgtHost, tgtPort), timeout=10) as conn:
            conn.sendall(message.encode('utf-8'))
            response = conn.recv(buffer_size)
            print(f"{tgtPort}/tcp open")
            print(f"Received: {response.decode('utf-8')}")
    except socket.error as e:
        print (f"Connection error: {e}")

def interactive_mix_sendMessage(tgtHost, tgtPort):
    import socket
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    message = "ViolentPython\r\n"
    try:
        port = int(tgtPort)
        if port <= 0 or port > 65535:
            raise ValueError(f"Port value {port} is out of range.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)
            sock.connect((tgtHost, port))
            logging.info(f"Connected to {tgtHost} on port {tgtPort}")
            bytes_sent = sock.sendall(message.encode('utf-8'))
            if bytes_sent is None:
                print(f"Message sent: {message.strip()}")
            else:
                print("Failed to send the complete message.")
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except socket.timeout:
        logging.error("Connection attempt timed out.")
    except socket.error as err:
        logging.error(f"Socket error: {err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def baseline_connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        sock.send(b'ViolentPython\r\n')
        results = sock.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        sock.close()
    except Exception as e:
        print(f"{tgtPort}/tcp closed or error: {e}")

