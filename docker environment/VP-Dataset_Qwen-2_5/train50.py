import socket 
from threading import *
import ssl

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

def persona__connScan(tgtHost, tgtPort):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((tgtHost, tgtPort))
        s.sendall(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.error as e:
        pass
    finally:
        s.close()

def template__connScan(tgtHost, tgtPort):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((tgtHost, tgtPort))
        s.send(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.error as e:
        pass
    finally:
        s.close()

def question_refinement__connScan(tgtHost, tgtPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.create_default_context().wrap_socket(s, server_hostname=tgtHost)
    try:
        ssl_sock.connect((tgtHost, tgtPort))
        ssl_sock.sendall('ViolentPython\r\n'.encode('utf-8'))
        data = ssl_sock.recv(1024)
        print(data.decode('utf-8'))
    except Exception as e:
        print(e)
    finally:
        ssl_sock.close()

def alternative_approaches__connScan(tgtHost, tgtPort):
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((tgtHost, tgtPort))
        s.sendall(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
        s.close()
    except socket.error as e:
        pass

def context_manager__connScan(tgtHost, tgtPort):
	import socket
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	try:
		s.connect((tgtHost, tgtPort))
		s.send(b'VeiolentPython\r\n')
		resp=s.recv(1024)
		print(resp.decode())
	except Exception as e:
		print(str(e))
	finally:
		s.close()

def flipped_interaction_3__connScan(tgtHost, tgtPort):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((tgtHost, tgtPort))
        s.send(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.error as e:
        print(f'Connection failed on {tgtHost}:{tgtPort} - {e}')

def flipped_interaction_4__connScan(tgtHost, tgtPort):
    conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn_socket.settimeout(1)
        conn_socket.connect((tgtHost, tgtPort))
        conn_socket.send(b'ViolentPython\r\n')
        response = conn_socket.recv(100)
        print(response.decode('utf-8'))
    except socket.timeout:
        print(f'Connection to {tgtHost}:{tgtPort} timed out.')
    except socket.error as e:
        print(f'Failed to connect to {tgtHost}:{tgtPort}. Error: {e}')
    finally:
        conn_socket.close()

def flipped_interaction_5__connScan(tgtHost, tgtPort):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((tgtHost, tgtPort))
        print(f'Connection successful to {tgtHost}:{tgtPort}')
        s.send(b'ViolentPython\r\n')
        print(f'Message sent successfully to {tgtHost}:{tgtPort}')
        results = s.recv(100)
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.error as e:
        print(f'Connection failed: {e} on {tgtHost}:{tgtPort}')
    finally:
        s.close()

def iterative_prompting_3__connScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str) or not tgtHost:
        raise ValueError('tgtHost must be a non-empty string.')
    if not isinstance(tgtPort, int) or tgtPort < 1 or tgtPort > 65535:
        raise ValueError('tgtPort must be an integer between 1 and 65535.')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((tgtHost, tgtPort))
        s.send(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.timeout:
        return 'Connection timed out'
    except socket.gaierror:
        return 'Hostname could not be resolved'
    except socket.error as e:
        return f'Socket error: {e}'
    finally:
        s.close()
    return 'Message sent successfully'

def iterative_prompting_4__connScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str) or not tgtHost:
        raise ValueError('tgtHost must be a non-empty string')
    if not isinstance(tgtPort, int) or tgtPort < 0 or tgtPort > 65535:
        raise ValueError('tgtPort must be an integer between 0 and 65535')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((tgtHost, tgtPort))
        s.sendall(b'ViolentPython\r\n')
        results = s.recv(100)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {results.decode(errors='ignore')}")
    except socket.timeout:
        print('Connection timed out.')
    except socket.error as e:
        print(f'Socket error: {e}')
    finally:
        if 's' in locals():
            s.close()

def iterative_prompting_5__connScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str) or not tgtHost:
        return
    if not isinstance(tgtPort, int) or tgtPort <= 0 or tgtPort > 65535:
        return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((tgtHost, tgtPort))
        if result == 0:
            message = 'ViolentPython\r\n'
            s.sendall(message.encode('utf-8'))
            response = s.recv(1024)
            print(f"{tgtPort}/tcp open")
            print(f"Received: {response.decode(errors='ignore')}")
    except socket.timeout:
        pass
    except socket.error as e:
        pass
    finally:
        try:
            s.close()
        except (NameError, socket.error):
            pass

def few_shots_prompting__connScan(tgtHost, tgtPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tgtHost, tgtPort))
    s.send(b'ViolentPython\r\n')
    response = s.recv(1024)
    print(f"{tgtPort}/tcp open")
    print(f"Received: {response.decode(errors='ignore')}")
    s.close()

def cot_prompting__connScan(tgtHost, tgtPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tgtHost, tgtPort))
    s.send(b'ViolentPython\r\n')
    response = s.recv(1024)
    print(f"{tgtPort}/tcp open")
    print(f"Received: {response.decode(errors='ignore')}")
    s.close()

def fact_check_list__connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        message = b"ViolentPython\r\n"
        result = sock.connect_ex((tgtHost, tgtPort))
        if result == 0:
            print(f"[+] {tgtHost}:{tgtPort} TCP Open")
            sock.sendall(message)
            response = sock.recv(4096)
            print(f"Response received: {response}")
        else:
            print(f"[-] {tgtHost}:{tgtPort} TCP Closed")
        sock.close()
    except Exception as e:
        print(f"Exception encountered: {e}")

def not_interactive_mix__connScan(tgtHost, tgtPort):
    tgtPort = int(tgtPort)
    if tgtPort < 0 or tgtPort > 65535:
        raise ValueError("tgtPort must be in the range 0-65535")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((tgtHost, tgtPort))
    if result == 0:
        msg = b"ViolentPython\r\n"
        sock.sendall(msg)
        response = sock.recv(1024)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {response.decode(errors='ignore')}")
    else:
        raise ConnectionError(f"Connection failed on {tgtHost}:{tgtPort}")
    sock.close()

def interactive_mix__sendMessageToHost(tgtHost, tgtPort):
    try:
        socket.inet_aton(tgtHost)
    except socket.error:
        return "Invalid IP address"
    if not isinstance(tgtPort, int) or not (0 < tgtPort < 65536):
        return "Invalid port number"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        with screenLock:
            s.connect((tgtHost, tgtPort))
            message = "ViolentPython\r\n"
            s.sendall(message.encode('utf-8'))
            response = s.recv(4096).decode('utf-8')
            print(f"{tgtPort}/tcp open")
            print(f"Received: {response}")
        s.close()
        return response
    except socket.timeout:
        return "Connection timed out"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def baseline__connScan(tgtHost, tgtPort):
    import socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((tgtHost, tgtPort))
        s.send(b'ViolentPython\r\n')
        banner=s.recv(1024)
        print(f"{tgtPort}/tcp open")
        print(f"Received: {banner.decode(errors='ignore')}")
        s.close()
    except socket.timeout:
        rint(f'[-] {tgtPort} /tcp closed timeout')
    except Exception as e:
        print(f'[-] {tgtPort} /tcp closed {e}')
