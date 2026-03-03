import logging
import os
import shlex
import subprocess
from venv import logger

import paramiko
from pexpect import pxssh
from requests import session

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

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            raise ValueError(e)
            
    def ground_truth_code_send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

    def persona_send_command(self, cmd):
        import subprocess
        try:
            result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Command {cmd} failed with return code {e.returncode}"

    def template_send_command(self, cmd):
        try:
            import subprocess
            output = subprocess.check_output(cmd, shell=True)
            return output if output else None
        except subprocess.CalledProcessError as e:
            raise Exception(
                f"Failed to execute command '{cmd}': {e.output.decode('utf-8')}" or "Failed to execute command")
        except Exception as e:
            raise

    def question_refinement_send_command(cmd):
        if not isinstance(cmd, str):
            raise TypeError("Command must be a string")
        if len(cmd) == 0:
            raise ValueError("Command cannot be empty")
        try:
            result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)
            return result.stdout.decode().strip()
        except subprocess.CalledProcessError as e:
            raise e

    def alternative_approaches_send_command(self, cmd):
        try:
            import subprocess
            output = subprocess.check_output(cmd, shell=True)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    def context_manager_send_command(self, cmd):
        import subprocess
        cmd = subprocess.list2cmdline([cmd])
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        result.check_returncode()
        return result.stdout

    def flipped_interaction_3__send_command(self, cmd):
        disallowed_chars = [';', '&', '|']
        if any(char in cmd for char in disallowed_chars):
            logging.error(f"Command '{cmd}' contains disallowed characters.")
            return {'output': '', 'error_code': 400,
                    'error_message': 'Bad request: Command contains disallowed characters.'}
        try:
            stdin, stdout, stderr = session.exec_command(cmd)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            logging.info(f"Command '{cmd}' output: {output}")
            if error:
                logging.error(f"Command '{cmd}' error: {error}")
            return {'output': output, 'error_code': 0 if not error else 1, 'error_message': error if error else ''}
        except paramiko.AuthenticationException:
            logging.error("Authentication failed.")
            return {'output': '', 'error_code': 401, 'error_message': 'Unauthorized: Authentication failed.'}
        except paramiko.SSHException as ssh_ex:
            logging.error(f"SSH connection failed: {ssh_ex}")
            return {'output': '', 'error_code': 500,
                    'error_message': f"Internal server error: SSH connection failed: {ssh_ex}"}
        except Exception as ex:
            logging.error(f"An error occurred: {ex}")
            return {'output': '', 'error_code': 500, 'error_message': f"Internal server error: {ex}"}

    def flipped_interaction_4__send_command(self, cmd, destination, protocol):
        try:
            ssh = self.connect()
            stdin, stdout, stderr = ssh.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            if error:
                logger.error(f"Command execution error: {error}")
            return output
        except paramiko.AuthenticationException as e:
            logger.error(f"Authentication error: {e}")
        except paramiko.SSHException as e:
            logger.error(f"SSH exception: {e}")
        except Exception as e:
            logger.error(f"Unknown error: {e}")

    def flipped_interaction_5__send_command(self, cmd):
        output = self.connection.send_command(cmd)
        return output

    def iterative_prompting_3__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise TypeError('Command must be a string')
        if not self.conn:
            raise ConnectionError('Connection is not established')
        try:
            self.conn.send(cmd.encode('utf-8'))
        except ConnectionResetError as e:
            print(f'Connection reset: {e}')
        except BrokenPipeError as e:
            print(f'Broken pipe: {e}')
        except OSError as e:
            print(f'OS error: {e}')
        except Exception as e:
            print(f'Failed to send command: {e}')

    def iterative_prompting_4__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise TypeError('Command must be a string')
        try:
            args = [cmd] if isinstance(cmd, str) else cmd
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                       universal_newlines=False)
            stdout, stderr = process.communicate(timeout=60)
            if stdout is None:
                stdout = b''
            if stderr is None:
                stderr = b''
            error_code = process.returncode
            if error_code != 0:
                raise RuntimeError(f'Command failed with error code {error_code}: {stderr.decode()}')
        except OSError as e:
            raise RuntimeError(f'Failed to execute command: {e}')
        except subprocess.TimeoutExpired:
            raise RuntimeError(f'Command [{cmd}] timed out')
        return stdout, stderr

    def iterative_prompting_5__send_command(self, cmd):
        if not isinstance(cmd, str):
            raise TypeError('Command must be a string')
        if not cmd.strip():
            raise ValueError('Command cannot be empty')
        try:
            args = cmd.split()
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(timeout=60)
            if process.returncode != 0:
                raise RuntimeError(f'Command failed with return code {process.returncode}')
            return stdout.decode(errors='ignore'), stderr.decode(errors='ignore')
        except subprocess.TimeoutExpired:
            process.kill()
            raise RuntimeError('Command execution timed out')
        except Exception as e:
            raise RuntimeError(f'Failed to execute command: {e}')

    def few_shots_prompting_send_command(self, cmd):
        os.system(cmd)

    def cot_prompting_send_command(self, cmd):
        import subprocess
        subprocess.run(cmd, shell=True)

    def fact_check_list_send_command(self, cmd):
        if not isinstance(cmd, str):
            raise TypeError("Command must be a string")
        if not cmd:
            raise ValueError("Command cannot be empty")
        try:
            args = cmd.split()
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            return_code = process.returncode
            if return_code == 127:
                raise subprocess.SubprocessError(f"Command '{cmd}' not found")
        except subprocess.SubprocessError as e:
            raise subprocess.SubprocessError(f"Failed to execute command: {e}")
        return return_code, output.decode(), error.decode()

    def not_interactive_mix_send_command(cmd):
        try:
            if not isinstance(cmd, str):
                raise ValueError("Invalid command")
            if len(cmd) > 1000:
                raise ValueError("Command exceeded maximum allowed length")
            process = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if process.returncode != 0:
                raise RuntimeError(f"Command failed with return code {process.returncode}: {error.decode()}")
            return output.decode()
        except subprocess.SubprocessError as e:
            import logging
            logging.error(f"Failed to execute command: {e}")
            raise RuntimeError(f"Failed to execute command: {e}")
        except Exception as e:
            import logging
            logging.error(f"An unexpected error occurred: {e}")
            raise RuntimeError(f"An unexpected error occurred: {e}")


    def interactive_mix_send_command(self,cmd):
        if not self.ssh_client:
            self.connect()
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
            output = stdout.readlines()
            error = stderr.readlines()
            if error:
                print(f"Error occurred: {error}")
                return None
            return output
        except paramiko.SSHException as e:
            print(f"SSH error: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def baseline_send_command(self, cmd):
        import subprocess
        return subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



