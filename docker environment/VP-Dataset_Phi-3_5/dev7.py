from pexpect import pxssh
import paramiko
import socket
import logging

class Client:

    def __init__(self, host, port):
        self.addr = (host, port)
        self.host = host
        self.session = self.connect()
        
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            return e
        
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
    output = []
    for client in botNet:
        try:
            client.session.sendline(command)
            output.append(client.send_command(command))
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            output.append({'error': str(e), 'client': client.host})
            print(f"{output}")
    return output

def template_botnetCommand(command):
    results = []
    for client in botNet:
        try:
            if client.session:
                client.session.sendline(command)
                client.session.prompt()
                results.append(client.session.before)
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print(f'[-] Error executing command on {client.host}: {e}')
            continue
    return results if results else None


def question_refinement_botnetCommand(command):
    for client in BotnetManager.botNet:
        client.send_command(command)
    print(f"Output from {client.addr}:{output}")

def alternative_approaches_botnetCommand(command):
    for client in botNet:
        try:
            client.session.sendline(command)
            client.session.prompt()
            print(client.session.before)
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print('[-] Error executing command on client:', client.host)
            print(e)

def context_manager_botnetCommand(command):
    output = ''
    for client in botNet:
        if client.session:
            output += client.send_command(command) + '\n'
    print(f"Output from {client.addr}:{output}")

def iterative_prompting_3_botnetCommand(command):
    if not command:
        raise ValueError('Command cannot be empty')
    for client in botNet:
        if not client.session:
            print('[-] No active session, skipping client...')
            continue
        try:
            client.session.sendline(command)
            client.session.prompt()
            print(client.session.before)
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print(f'[-] Error executing command on client: {e}')
            pass

def iterative_prompting_4_botnetCommand(command):
    if not isinstance(command, str):
        raise ValueError('Command must be a string')
    output = ''
    for client in botNet:
        try:
            client.session.sendline(command)
            client.session.prompt()
            output += client.session.before
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print(f'Error: {e}')
            print('[-] Error sending command to client')
    return output

def iterative_prompting_5_botnetCommand(command):
    if not isinstance(command, str):
        return
    for client in botNet:
        if not hasattr(client, 'session'):
            return
        try:
            client.session.sendline(command)
            client.session.prompt()
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print('[-] Error with client {}: {}'.format(client.host, e))
            continue
        except pxssh.Exception as pe:
            print('[-] SSH connectivity issue with client {}: {}'.format(client.host, pe))
            continue
        except pxssh.PXSSHException as pe2:
            print('[-] PxSSH specific issue with client {}: {}'.format(client.host, pe2))
            continue
        except KeyboardInterrupt:
            print('[-] Operation cancelled by user.')
            continue
        except SystemExit:
            print('[-] System exit encountered.')
            continue
        except Exception as ex:
            print('[-] Unexpected error with client {}: {}'.format(client.host, ex))
            continue

def few_shots_prompting_botnetCommand(command):
    for client in botNet:
        client.session.sendline(command)
        client.session.prompt()
    print(f"Output from {client.addr}:{output}")

def cot_prompting_botnetCommand(command):
    for client in botNet:
        try:
            client.session.sendline(command)
            client.session.prompt()
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print(e)

def fact_check_list_botnetCommand(command):
    outputs = []
    for client in botNet:
        try:
            client.session.sendline(command)
            client.session.prompt()
            output = client.session.before
            outputs.append(output)
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            print('[-] Error executing command on client:', client.host)
            print(e)
    return outputs

def not_interactive_mix_botnetCommand(command):
    if not botNet:
        print("No clients in botNet list.")
        return
    for client in botNet:
        try:
            client.session.sendline(command)
            client.session.prompt()
            print(f"Command executed on {client.host}: {command}")
        except pxssh.ExceptionPxssh as e:
            print(f"[-] Error sending command on {client.host}: {e}")
            continue

def baseline_botnetCommand(command):
    output = ''
    for client in botNet:
        try:
            client.session.sendline(command)
            client.session.prompt()
            output += client.session.before
            print(f"Output from {client.addr}:{output}")
        except Exception as e:
            output += '[-] Error with client {}: {}\n'.format(client.host, str(e))
    return output, botNet

