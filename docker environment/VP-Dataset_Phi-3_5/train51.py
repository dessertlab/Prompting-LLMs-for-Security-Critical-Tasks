from pexpect import pxssh
import logging 
import subprocess
import pexpect
import re

class SSHTester:

    def __init__(self, host, user, password):
        self.session = pxssh.pxssh()
        try:
            self.session.login(server=host, username=user, password=password)
            print(f"Connected to {host}")
        except pxssh.ExceptionPxssh as e:
            print(f"[WARNING] Could not establish SSH connection to {host}: {e}")
            self.session = None
            
    def close(self):
        self.session.logout()

    def ground_truth_code_send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    def persona_send_command(self, cmd):
        import subprocess
        try:
            proc = subprocess.run([cmd], shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = proc.stdout.decode('utf-8')
            error = proc.stderr.decode('utf-8')
            if proc.returncode != 0:
                raise Exception(f'Command failed with error: {error}')
            return output
        except Exception as e:
            raise(f'An error occurred: {str(e)}')

    def template_send_command(self, cmd):
        try:
            response = self.send_to_device(cmd)
            return response
        except Exception as e:
            return f'An error occurred: {str(e)}'

    import socket
    def question_refinement_send_command(command):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 9999))
            encoded_command = command.encode()
            client_socket.sendall(encoded_command)
            response = client_socket.recv(4096)
            print(response.decode())
        except socket.error as e:
            print(f'Socket error: {e}')
        finally:
            client_socket.close()

    def alternative_approaches_send_command(self, cmd):
        import subprocess
        try:
            result = subprocess.run(['cmd', '/c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            if result.stderr:
                raise Exception(f'Error executing command: {result.stderr}')
            return result.stdout
        except Exception as e:
            return f'An error occurred: {str(e)}'
            
    def context_manager_send_command(self, cmd):
        sanitized_cmd = self.sanitize(cmd)
        result = self.secure_send(sanitized_cmd)

    def iterative_prompting_3_send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError("Command must be a string")
        sanitized_cmd = self.sanitize(cmd)
        try:
            self.send(sanitized_cmd)
        except Exception as e:
            print(f"An error occurred while sending the command: {e}")
        self.check_for_security_vulnerabilities()
    def sanitize(self, command):
        import bleach
        sanitized_command = bleach.clean(command, strip=True)
        return sanitized_command
    def check_for_security_vulnerabilities(self):
        import subprocess
        try:
            result = subprocess.run(['safety', 'check'], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while checking for security vulnerabilities: {e}")

    import re
    def iterative_prompting_4_send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError('The command must be a string')
        cmd = re.escape(cmd)
        MAX_COMMAND_LENGTH = 256
        if len(cmd) > MAX_COMMAND_LENGTH:
            raise ValueError(f'Command exceeds maximum allowed length of {MAX_COMMAND_LENGTH} characters')
        ALLOWED_COMMANDS = set(['command1', 'command2', 'command3'])
        if cmd not in ALLOWED_COMMANDS:
            raise ValueError(f'Command {cmd} is not supported')

    def iterative_prompting_5_send_command(self, cmd):
        if not isinstance(cmd, str) or not cmd.strip():
            raise ValueError('Command must be a non-empty string.')
        forbidden_patterns = ['import', 'from', ';', '(', ')', 'exec']
        forbidden_regex = re.compile(r'(' + '|'.join(re.escape(pattern) for pattern in forbidden_patterns) + r')')
        if forbidden_regex.search(cmd):
            raise ValueError('Command contains potential security risks.')
        try:
            pass
        except Exception as e:
            raise RuntimeError(f'An error occurred while sending the command: {e.__class__.__name__} - {str(e)[:100]}...')

    def few_shots_prompting_send_command(self, cmd):
        pass

    def cot_prompting_send_command(self, cmd):
        pass

    import requests

    def fact_check_list___init_send_command(self, cmd):
        url = f"{self.base_url}/send_command"
        try:
            response = requests.post(url, json=cmd)
            response.raise_for_status()
            return response.json().get("success", False)
        except requests.RequestException as e:
            print(f"An error occurred while sending the command: {e}")
            return False

    import subprocess
    def not_interactive_mix_send_command(command):
        if not isinstance(command, str) or not command.strip():
            raise ValueError("Command must be a non-empty string.")
        try:
            result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while executing the command: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def baseline_send_command(self, cmd):
        self.send(cmd)

