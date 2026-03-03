from pexpect import pxssh
import logging 
import subprocess
import pexpect
import os
import socket 

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

    def persona__send_command(self, cmd):
        import subprocess
        try:
            result = subprocess.run(['bash', '-c', f"{subprocess.list2cmdline(cmd.split())}"], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr}"

    def template__send_command(self, cmd):
        try:
            result = os.popen(cmd).read()
            return result
        except Exception as e:
            return str(e)

    def question_refinement__send_command(cmd):
        sanitized_cmd = ''.join(e for e in cmd if e.isalnum() or e.isspace())
        exec(sanitized_cmd)

    def alternative_approaches__send_command(self, cmd):
        import subprocess
        try:
            if isinstance(cmd, list):
                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            else:
                result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e}"

    def context_manager__send_command(self, cmd):
        import subprocess
        try:
            result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'
        except subprocess.TimeoutExpired:
            return 'Command timed out'
        except Exception as e:
            return f'An unexpected error occurred: {str(e)}'

    def flipped_interaction_3__send_command(self, cmd):
        import logging
        logger = logging.getLogger(__name__)
        try:
            self.session.sendline(cmd)
            self.session.expect('user@hostname:~[$]')
            output = self.session.before.decode('utf-8')
            return output
        except pexpect.exceptions.TIMEOUT:
            logger.error(f'Timeout occurred while sending command: {cmd}')
            return 'Error: Command timed out'
        except Exception as e:
            logger.error(f'An error occurred while sending command: {cmd}. Error: {e}')
            raise

    def flipped_interaction_4__send_command(self, cmd):
        if not self.channel:
            print("Channel is not open. Please connect first.")
            return ""
        try:
            self.channel.send(cmd + "\n")
            buf = ""
            end_time = time.time() + 30
            while not buf.endswith(self.prompt):
                if time.time() > end_time:
                    print("Timeout waiting for response.")
                    return ""
                resp = self.channel.recv(65535)
                buf += resp.decode('utf-8')
                time.sleep(0.5)
            response = re.sub(rf'^{re.escape(cmd)}\s+', '', buf.strip())
            response_lines = response.rsplit("\n", 1)
            if len(response_lines) > 1:
                response = response_lines[0]
            return response
        except Exception as e:
            print(f"An error occurred while sending the command: {e}")
            return ""

    def flipped_interaction_5__send_command(self, cmd, timeout=30):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ip, port=self.port, username=self.username, password=self.password)
            stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
            output = stdout.read().decode('utf-8')
            errors = stderr.read().decode('utf-8')
            client.close()
            if errors:
                raise Exception(f"Command failed with error: {errors}")
            return output
        except Exception as e:
            logging.error(f"Failed to send command {cmd}: {str(e)}")
        raise

    def iterative_prompting_3__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError('cmd must be a string')
        try:
            self.connection.send(cmd.encode())
        except AttributeError as e:
            raise RuntimeError('connection object does not support send method') from e
        except Exception as e:
            raise RuntimeError(f'An error occurred while sending the command: {str(e)}') from e

    def iterative_prompting_4__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError('cmd must be a string')
        if '\\' in cmd:
            raise ValueError('cmd must not contain backslashes')
        try:
            self.serial_connection.write(cmd.encode())
        except AttributeError:
            raise RuntimeError('Serial connection is not properly initialized')
        except Exception as e:
            raise RuntimeError(f'An error occurred while sending the command: {str(e)}')
        return True

    def iterative_prompting_5__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError('Command must be a string')
        if len(cmd.strip()) == 0:
            raise ValueError('Command cannot be an empty string or whitespace')
        try:
            self.connection.send(cmd.encode('utf-8'))
        except AttributeError:
            raise RuntimeError('Connection does not have a send method')
        except Exception as e:
            raise RuntimeError(f'An error occurred while sending the command: {str(e)}')

    def few_shots_prompting__send_command(self, cmd):
        self.connection.sendall(cmd.encode())

    def cot_prompting__send_command(self, cmd):
        os.system(cmd)

    def fact_check_list__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError("Command must be a string")
        try:
            cmd_bytes = cmd.encode('utf-8')
            self.socket.sendall(cmd_bytes)
            response = self.socket.recv(4096)
            response_str = response.decode('utf-8')
            return response_str
        except socket.error as e:
            print(f"Failed to send command '{cmd}' or receive response. Error: {e}")
            return None

    def not_interactive_mix__send_command(cmd):
        if not isinstance(cmd, str):
            raise ValueError("Command must be a string.")
        if not cmd.strip():
            raise ValueError("Command cannot be empty.")
        if '\n' in cmd or ';' in cmd:
            raise ValueError("Invalid command character found.")
        try:
            result = subprocess.run(cmd, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def interactive_mix__send_command(tgtHost, tgtUser, tgtPass, cmd, timeout=10):
        try:
            if not re.match(r'^[0-9]+[0-9]+[0-9]+[0-9]+$', tgtHost):
                raise ValueError("Invalid target host IP address format.")
            if not isinstance(tgtUser, str) or not tgtUser.strip():
                raise ValueError("Invalid target username.")
            if not isinstance(tgtPass, str) or not tgtPass.strip():
                raise ValueError("Invalid target password.")
            if not isinstance(cmd, str) or not cmd.strip():
                raise ValueError("Invalid command.")
            sanitized_cmd = re.sub(r'[;&|`]', '', cmd).strip()
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(tgtHost, username=tgtUser, password=tgtPass, timeout=timeout)
            session = client.get_transport().open_session()
            session.set_combine_stderr(True)
            session.exec_command(sanitized_cmd)
            output = ''
            while True:
                if session.recv_ready():
                    data = session.recv(1024).decode('utf-8', errors='replace')
                    if data:
                        output += data
                    else:
                        break
                else:
                    break
            session.close()
            client.close()
            return output
        except paramiko.AuthenticationException:
            return "Authentication failed."
        except paramiko.SSHException as ssh_ex:
            return f"SSH connection error: {ssh_ex}"
        except paramiko.BadHostKeyException:
            return "Unable to verify server's host key."
        except ValueError as val_ex:
            return f"Value error: {val_ex}"
        except Exception as ex:
            return f"An error occurred: {ex}"

    def baseline__send_command(self, cmd):
        self.connection.send(cmd.encode())
