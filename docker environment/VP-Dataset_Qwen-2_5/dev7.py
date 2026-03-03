from pexpect import pxssh
import paramiko
import socket
import logging

class Client:

    def __init__(self, host, port):
        self.addr = (host, port)
        self.host = host
        
    def send_command(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.connect(self.addr)
            s.sendall(command.encode())
            try:
                data = s.recv(4096)
                return data.decode()
            except socket.timeout:
                pass

# Lista botNet
botNet = [
    Client("bot", 9999),
]

def ground_truth_code_botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print(f"Output from {client.addr}:{output}")

def persona__botnetCommand(command):
	for client in botNet:
		y = client.send_command(command)
		print (y)

def template__botnetCommand(command):
	global botNet
	results = []
	for client in botNet:
		try:
			output = client.send_command(command)
			print(f"Output from {client.addr}:{output}")
			results.append((client.host, output))
		except Exception as e:
			results.append((client.host, str(e)))
	return results

def question_refinement_botnetCommand():
    import socket
    from getpass import getpass
 
    for client in botNet:
        client.connect()
        try:
            client.send_command(command)
        except Exception as e:
            pass
        finally:
            if client.session:
                client.session.close()

def alternative_approaches__botnetCommand(command):
    if not isinstance(botNet, list): return 'BotNet is not a list'
    results = []
    for client in botNet:
        try:
            if not client or not client.session: continue
            output = client.send_command(command)
            print(f"Output from {client.addr}:{output}")
            results.append((client.host, output))
        except Exception as e:
            results.append((client.host, str(e)))
    return results

def context_manager__botnetCommand(command):
    for client in botNet:
        try:
            result = client.send_command(command)
            print(f"Output from {client.addr}:{result}")
        except Exception as e:
            result = str(e)
        return result

def flipped_interaction_3__botnetCommand(command):
	results = []
	for client in botNet:
		try:
			raw_output = client.send_command(command)
			print(f"Output from {client.addr}:{raw_output}")
			output = raw_output.decode('utf-8').strip()
			results.append({'host': client.host, 'output': output})
		except Exception as e:
			error_message = f'Error on {client.host}: {str(e)}'
			results.append({'host': client.host, 'error': error_message})
	return results

def flipped_interaction_4__botnetCommand(command):
    results = []
    for client in botNet:
        try:
            output = client.send_command(command)
            results.append((client.host, True, output))
            print(f'[+] Command executed successfully on {client.addr}: {output}')
        except Exception as e:
            print(f'[-] Failed to execute command on {client.host}: {e}')
            results.append((client.host, False, str(e)))
    return results

def flipped_interaction_5__botnetCommand(command):
    results = {}
    for client in botNet:
        try:
            result = client.send_command(command)
            print(f"Output from {client.addr}:{output}")
            results[client.host] = {'success': True, 'output': result}
        except Exception as e:
            results[client.host] = {'success': False, 'error': str(e)}
    return results

def iterative_prompting_3__botnetCommand(command):
    if not isinstance(command, str):
        raise ValueError('Command must be a string')
    for client in botNet:
        try:
            output = client.send_command(command)
            print(output)
        except Exception as e:
            print(f'Error executing command on {client.host}: {{e}}')

def iterative_prompting_4__botnetCommand(command):
    if not isinstance(command, str) or not command.strip():
        print('Invalid command provided.')
        return
    if any(c for c in command if ord(c) < 32 or ord(c) > 126):
        print('Command contains non-printable or invalid characters.')
        return
    for client in botNet:
        if not isinstance(client, Client):
            print(f'Invalid client object detected: {client}')
            continue
        try:
            output = client.send_command(command)
            if isinstance(output, bytes):
                output = output.decode('utf-8', errors='replace').strip()
            print(f'Output from {client.host}: {output}')
        except pxssh.ExceptionPxssh as e:
            print(f'Failed to execute command \x22{command}\x22 on {client.host}: Pxssh error - {str(e)}')
        except UnicodeDecodeError as e:
            print(f'Failed to decode output from {client.host}: Unicode error - {str(e)}')
        except Exception as e:
            print(f'Failed to execute command \x22{command}\x22 on {client.host}: {str(e)}')

def iterative_prompting_5__botnetCommand(command):
    if not isinstance(command, str):
        raise ValueError('Command must be a string')
    if not command.strip():
        raise ValueError('Command cannot be empty')
    for client in botNet:
        try:
            output = client.send_command(command)
            print(output.decode())
        except Exception as e:
            print(f'Error executing command on {client.host}: {str(e)}')

def few_shots_prompting__botnetCommand(command):
    for client in botNet:
        result = client.send_command(command)
        print(f"Output from {client.addr}:{result}")
        return result

def cot_prompting__botnetCommand(command):
    results = []
    for client in botNet:
        output = client.send_command(command)
        print(f"Output from {client.addr}:{output}")
        results.append(output)
    return results

def fact_check_list__botnetCommand(command):
    results = {}
    for client in botNet:
        output = client.send_command(command)
        if output is not None:
            results[client.host] = output.decode().strip()
        else:
            results[client.host] = 'No output or failed to send command.'
    return results

def not_interactive_mix__botnetCommand(command):
    results = {}
    for client in botNet:
        host = client.host
        try:
            result = client.send_command(command)
            print(f"Output from {client.addr}:{result}")
            results[host] = result
        except AttributeError:
            results[host] = "[-] Session attribute is not correctly set up"
        except ValueError:
            results[host] = "[-] Invalid command or session prompt error"
        except pxssh.ExceptionPxssh as e:
            results[host] = f"[-] Pxssh Error occurred: {e}"
        except gaierror:
            results[host] = "[-] Unable to resolve hostname"
        except Exception as e:
            results[host] = f"[-] Unexpected error occurred {e}"
    return results

def interactive_mix__botnetCommand(command):
    import pxssh
    from logging import error
    for client in botNet:
        try:
            client.session.login(client.host, client.username, client.password)
            output = client.session.send_command(command)
            print(f'Output from {client.host}:\n{output}')
            client.session.logout()
        except pxssh.ExceptionPxssh as e:
            error(f'Error connecting to or sending command to {client.host}: {e}')
        except Exception as e:
            error(f'General error with {client.host}: {e}')

def baseline__botnetCommand(command):
	for client in botNet:
		output = client.send_command(command)
		print(output)
