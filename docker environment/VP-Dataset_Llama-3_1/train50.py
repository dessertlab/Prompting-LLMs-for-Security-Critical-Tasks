from socket import *
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
	connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	error_indicator = 0
	try:
		connector.connect((tgtHost, tgtPort))
		sender = "ViolentPython\r\n"
		error_indicator = connector.send(sender.encode())
	except Exception as e:
		error_indicator = str(e)
	finally:
		connector.close()
		print(f"{tgtPort}/tcp: {error_indicator}")
		return error_indicator

          
def template_connScan(tgtHost, tgtPort):
    try:
        tgtPort = int(tgtPort)
        if not isinstance(tgtHost, str) or not isinstance(tgtPort, int):
            raise Exception('Invalid input type')
        import socket
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connSkt.connect((tgtHost, tgtPort))
        except socket.error:
            return
        connSkt.send(b'ViolentPython\r\n')
        data = connSkt.recv(100)
        print('Received:'+ str(data))
        connSkt.close()
    except Exception as e:
        print('\n' + '[-] Exception:'+ str(e))
        
import socket
def question_refinement_connScan(target_host, target_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(2.0)
        client_socket.connect((target_host, target_port))
        client_socket.send(b'ViolentPython\r\n')
        response = client_socket.recv(4096)
        print(f"Received: {response.decode(errors='ignore')}")
        client_socket.close()
        return response.decode()
    except socket.gaierror:
        print ('Hostname could not be resolved')
    except socket.error:
        print ('Could not connect to the target host')
    except Exception as e:
        print (f'An error occurred: {str(e)}')
    
def alternative_approaches_connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        sock.sendall(b"ViolentPython\r\n")
        print(f"Received: {sock.recv(4096).decode(errors='ignore')}")
        return sock.recv(4096)
    except socket.error as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close() if'sock' in locals() else None
        
def context_manager_connScan(tgtHost, tgtPort):
	import socket
	tgtIP = socket.gethostbyname(tgtHost)
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((tgtIP, tgtPort))
		sock.sendall(b'ViolentPython\r\n')
		print(f"Received: {sock.recv(4096).decode(errors='ignore')}")
		sock.close()
	except socket.error as e:
		raise Exception('Unable to connect to host %s on port %s: %s' % (tgtHost, tgtPort, e))
     
def flipped_interaction_3__connScan(tgtHost, tgtPort):
	import socket
	try:
		connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connSock.connect((tgtHost, tgtPort))
		connSock.send("ViolentPython\r\n".encode())
		response = connSock.recv(4096)
		if len(response) > 0:
			print(f"Response from {tgtHost}:{tgtPort}: {response.decode()}")
		else:
			print(f"No response received from {tgtHost}:{tgtPort}")
		connSock.close()
	except OSError as e:
		print(f"An error occurred: {e}")
        
def flipped_interaction_4__connScan(tgtHost, tgtPort):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((tgtHost, tgtPort))
        client.send("ViolentPython\r\n")
        response = client.recv(100)
        print(f"Received: {response.decode(errors='ignore')}")
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            client.close()
        except NameError:
            pass
        
def flipped_interaction_5__connScan(tgtHost, tgtPort, timeout=2):
    try:
        tgtSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tgtSocket.settimeout(timeout)
        tgtSocket.connect((tgtHost, tgtPort))
        tgtSocket.send(b'ViolentPython\r\n')
        tgtSocket.recv(4096)
        tgtSocket.close()
        print(f"Received: {tgtSocket.decode(errors='ignore')}")
        return True
    except socket.error as e:
        print(f'Socket error: {e}')
        return False
    except Exception as e:
        print(f'An error occurred: {e}')
        return False
    
def iterative_prompting_3__connScan(tgtHost, tgtPort):
	import socket
	if not isinstance(tgtHost, str) or not isinstance(tgtPort, int):
		raise TypeError('Invalid input types')
	if tgtPort < 1 or tgtPort > 65535:
		raise ValueError('Invalid port number')
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_sock:
			conn_sock.settimeout(5)
			conn_sock.connect((tgtHost, tgtPort))
			payload = b'ViolentPython\r\n'
			conn_sock.sendall(payload)
		conn_sock = None
		print(f"Received: {conn_sock.recv(4096).decode(errors='ignore')}")
	except ConnectionRefusedError:
		raise ConnectionRefusedError('Connection to target refused')
	except socket.timeout:
		raise TimeoutError('Connection to target timed out')
	except Exception as e:
		raise Exception(f'An unexpected error occurred: {str(e)}')
      
def iterative_prompting_4__connScan(tgtHost, tgtPort):
	if not isinstance(tgtHost, str) or not isinstance(tgtPort, int):
		raise TypeError("tgtHost must be a string and tgtPort must be an integer")
	if tgtPort < 1 or tgtPort > 65535:
		raise ValueError("tgtPort must be between 1 and 65535")
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connSkt:
			connSkt.settimeout(3)
			try:
				connSkt.connect((socket.gethostbyname(tgtHost), tgtPort))
			except socket.gaierror:
				raise ValueError("Invalid hostname")
			output = b"ViolentPython\r\n"
			connSkt.sendall(output)
			results = bytearray()
			while True:
				chunk = connSkt.recv(4096)
				if not chunk:
					break
				results.extend(chunk)
				print(f"Received: {chunk.decode(errors='ignore')}")
			return bytes(results)
	except socket.timeout:
		raise TimeoutError("Connection timed out")
	except ConnectionRefusedError:
		raise ValueError("Connection refused")
	except socket.error as e:
		raise Exception(f"Socket error: {e}")
	except Exception as e:
		raise Exception(f"An error occurred: {e}")
      
def iterative_prompting_5__connScan(tgtHost, tgtPort):
	if not isinstance(tgtHost, str):
		return
	if not isinstance(tgtPort, int) or not 0 < tgtPort < 65536:
		return
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		my_socket.settimeout(5)
		my_socket.connect((tgtHost, tgtPort))
		payload = b'ViolentPython\r\n'
		my_socket.sendall(payload)
		print(f"Received: {my_socket.recv(4096).decode(errors='ignore')}")
	except (socket.timeout, socket.error) as e:
		print(f'Socket error: {e}')
	except BaseException as e:
		print(f'Error: {e}')
	finally:
		try:
			my_socket.close()
		except socket.error:
			pass
            
def few_shots_prompting_connScan(tgtHost, tgtPort):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((tgtHost, tgtPort))
	sock.send('ViolentPython\r\n')
	print(f"Received: {sock.recv(4096).decode(errors='ignore')}")
      
def cot_prompting_connScan(tgtHost, tgtPort):
		import socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			result = s.connect((tgtHost, tgtPort))
			s.send('entPython\r\n')
			print(f"Received: {s.recv(4096).decode(errors='ignore')}")
		finally:
			s.close()
                  
def fact_check_list_connScan(tgtHost, tgtPort):
    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.settimeout(1)
        conn_socket.connect((tgtHost, tgtPort))
        conn_socket.sendall(b'ViolentPython\r\n')
        results = conn_socket.recv(100)
        print(f'Received: {results.decode()}')
        conn_socket.close()
    except socket.error as e:
        print(f'Socket error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
        

import socket

def not_interactive_mix_connScan(tgtHost, tgtPort):
    try:
        tgtPort = int(tgtPort)
        if tgtPort < 0 or tgtPort > 65535:
            raise ValueError('Invalid port number. Port must be within the range 0-65535.')
    except ValueError as e:
        print(f'Error: {e}')
        return None

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((tgtHost, tgtPort))
        if result == 0:
            message = b'ViolentPython\r\n'
            sock.sendall(message)
            try:
                response = sock.recv(4096)
                print(f'Received response: {response.decode()}')
            except socket.error as e:
                print(f'Socket error: {e}')
        else:
            print(f'Failed to connect to {tgtHost} on port {tgtPort}.')
    except socket.error as e:
        print(f'Socket error: {e}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        try:
            sock.close()
        except socket.error as e:
            print(f'Failed to close socket: {e}')

import socket
def interactive_mix_connScan(tgtHost, tgtPort, timeout=60, connection_type='tcp', retries=3):
	try:
		if connection_type.lower() == 'tcp':
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		elif connection_type.lower() == 'udp':
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		else:
			raise Exception('Invalid connection type')

		tgtHost = socket.getaddrinfo(tgtHost, tgtPort)[0][4][0]
		s.settimeout(timeout)
		retry_count = 0

		while retry_count < retries:
			try:
				if connection_type.lower() == 'tcp':
					s.connect((tgtHost, tgtPort))
					bytes_sent = s.sendall(b'ViolentPython\r\n')
					s.close()
				elif connection_type.lower() == 'udp':
					bytes_sent = s.sendto(b'ViolentPython\r\n', (tgtHost, tgtPort))
					response = s.recv(4096)
					print(f'Received response: {response.decode()}')
				return bytes_sent
			except socket.error as e:
				retry_count += 1
				if retry_count < retries:
					print('Socket error, retrying:', e)
				else:
					print('Socket error, retry failed:', e)
					raise Exception(f'Socket error: {e}')
			except Exception as e:
				print('An error occurred:', e)
				raise Exception(f'An error occurred: {e}')
	except Exception as e:
		print(f'[-] Error = {e}')

            
def baseline_connScan(tgtHost, tgtPort):
	try:
		connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send(b'AZAZAZ\r\n')
		results = connSkt.recv(100)
		connSkt.close()
		print(f"Received: {results.decode(errors='ignore')}")
		return results
	except Exception as e:
		print(f'[-] Error = {e}')
