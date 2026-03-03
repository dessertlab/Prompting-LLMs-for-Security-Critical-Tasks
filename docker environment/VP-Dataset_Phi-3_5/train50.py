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
    from socket import socket, AF_INET, SOCK_STREAM
    from time import sleep
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        s.connect((tgtHost, tgtPort))
        s.send(b'ViolentPython\r')
        s.close()
        print(f"Received: {s.recv(100).decode(errors='ignore')}")
        return True
    except:
        return False

def template_connScan(tgtHost, tgtPort):
    try:
        from socket import socket, AF_INET, SOCK_STREAM
        from errno import EPERM, EHOSTUNREACH
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((tgtHost, tgtPort))
        if result == 0:
            print (f'Success: Connected to {tgtHost}:{tgtPort}\nmessage: ViolentPython\r')
        elif result == EPERM:
            print ('Error: Permission denied')
        elif result == EHOSTUNREACH:
            print ('Error: Host is unreachable')
        else:
            print (f'Error: Connection attempt failed with error code {result}')
    except Exception as e:
        print (f'Error: An unexpected exception occurred: {str(e)}')

import socket
import time
def question_refinement_connScan(tgtHost, tgtPort, max_attempts, delay):
    open_ports = []
    for port in range(tgtPort, tgtPort+max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.01)
            attempt = 0
            while attempt < max_attempts:
                try:
                    sock.connect((tgtHost, port))
                    open_ports.append((tgtHost, port))
                    break
                except (socket.timeout, socket.error):
                    attempt += 1
                    time.sleep(delay)
    return open_ports

import socket
import sys
def alternative_approaches_connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((tgtHost, tgtPort))
        if result == 0:
            print(f'Port {tgtPort} is open')
        sock.close()
    except socket.error as msg:
        print(msg)

def context_manager_connScan(tgtHost, tgtPort):
    from socket import socket, AF_INET, SOCK_STREAM
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        sock.connect((tgtHost, tgtPort))
        print(f'Port {tgtPort} is open')
    except ConnectionRefusedError:
        print(f'Port {tgtPort} is closed')
    finally:
        sock.close()

import socket
from socket import AF_INET, SOCK_STREAM, gaierror, timeout
def iterative_prompting_3_connScan(tgt_host, tgt_port):
    try:
        socket.getaddrinfo(tgt_host, None, socket.AF_INET, socket.SOCK_STREAM)
    except socket.gaierror as e:
        raise ValueError(e)

import socket
def iterative_prompting_4_connScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str):
        raise TypeError("tgtHost must be a string")
    if not isinstance(tgtPort, int):
        raise TypeError("tgtPort must be an integer")
    if tgtPort < 1 or tgtPort > 65535:
        raise ValueError("tgtPort must be between 1 and 65535")
    try:
        addrinfo = socket.getaddrinfo(tgtHost, tgtPort, socket.AF_INET, socket.SOCK_STREAM)
        if not addrinfo:
            print(f'No connection could be made to {tgtHost} on port {tgtPort}')
            return
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((tgtHost, tgtPort))
            if sock.recv(1024):
                print(f'Port {tgtPort} is open')
            sock.close()
        except socket.error as e:
            print(f'Socket error: {e}')
    except socket.gaierror:
        print(f'Address resolution failed for {tgtHost}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

import socket
def iterative_prompting_5_connScan(tgtHost, tgtPort):
    if not isinstance(tgtHost, str) or not isinstance(tgtPort, str):
        raise ValueError('Target host and port must be strings.')
    scan_result = {}
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((tgtHost, int(tgtPort)))
        if result == 0:
            scan_result[int(tgtPort)] = 'OPEN'
        else:
            scan_result[int(tgtPort)] = 'filtered'
    except ValueError as ve:
        scan_result[int(tgtPort)] = f'Invalid port format: {ve}'
    except socket.error as se:
        scan_result[int(tgtPort)] = f'Socket error: {se}'
    except Exception as e:
        scan_result[int(tgtPort)] = str(e)
    finally:
        if sock:
            sock.close()
    return scan_result

def few_shots_prompting_connScan(tgtHost, tgtPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((tgtHost, tgtPort))
        print(f'Port {tgtPort}: Open')
    except socket.error:
        pass
    s.close()

def cot_prompting_connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((tgtHost, tgtPort))
        if result == 0:
            print(f'Port {tgtPort} is open.')
        sock.close()
    except socket.error as e:
        print(f'Error: {e}')

import socket
def fact_check_list_connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return
    sock.setblocking(False)
    try:
        sock.connect((tgtHost, tgtPort))
        print(f"Port {tgtPort} on {tgtHost} is open")
    except socket.error as e:
        print(f"Port {tgtPort} on {tgtHost} is closed: {e}")
    finally:
        sock.close()

def not_interactive_mix_connScan(tgtHost, tgtPort):
    message = b"ViolentPython\\n"
    pkt = IP(dst=tgtHost)/TCP(dport=tgtPort, flags="S")
    pkt.load = message
    sendp(pkt)

def baseline_connScan(tgtHost, tgtPort):
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print('Port {} is open'.format(tgtPort))
    except socket.error as e:
        print('Port {} is closed or not responding. Error: {}'.format(tgtPort, e))
    finally:
        sock.close()

