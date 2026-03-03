from pexpect import pxssh
import logging 
import subprocess
import pexpect


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
            result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {'status': 'success', 'output': result.stdout.strip()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error_message': e.stderr.strip(), 'returncode': e.returncode}

    def template_send_command(self, cmd):
        try:
            if not isinstance(cmd, str):
                raise ValueError('The command must be a string.')
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                return {'error': stderr.strip()}
            return {'output': stdout.strip()}
        except Exception as e:
            return f"exception: {str(e)}"

    def question_refinement_send_command(target, command):
        if not isinstance(target, str) or not target:
            logging.error("Invalid target provided.")
            return False
        if not isinstance(command, str) or not command:
            logging.error("Invalid command provided.")
            return False
        try:
            logging.info(f"Attempting to send command to target: {target}")
            sanitized_command = shlex.quote(command)
            full_command = f"ssh {shlex.quote(target)} {sanitized_command}"
            result = subprocess.run(shlex.split(full_command),
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            logging.info(f"Command executed successfully with output: {result.stdout}")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Command execution failed: {e.stderr}")
            return False
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return False

    def alternative_approaches_send_command(self, cmd):
        import subprocess
        try:
            result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed with error: {e}'
        except Exception as e:
            return f'Unexpected error: {e}'

    def context_manager_send_command(self, cmd):
        import subprocess
        from shlex import split
        try:
            command = split(cmd)
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr.strip()}"

    def flipped_interaction_3_send_command(self, cmd):
        import subprocess
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout.strip()
        except Exception as e:
            return str(e)

    import paramiko
    def flipped_interaction_4_send_command(self, cmd):
        if not hasattr(self, 'ssh_client'):
            raise AttributeError('SSH client not available')
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
        output = stdout.read().decode()
        errors = stderr.read().decode()
        if errors:
            raise Exception(f'Error executing command: {errors}')
        return output

    def flipped_interaction_5_send_command(self, cmd):
        child = pexpect.spawn(cmd, timeout=30)
        child.expect(pexpect.EOF)
        return child.before.decode('utf-8')

    def iterative_prompting_3_send_command(self, cmd):
        if not isinstance(cmd, str):
            raise ValueError("The command must be a string.")
        if not hasattr(self, 'device_connection') or not callable(getattr(self.device_connection, 'write', None)):
            raise RuntimeError("Device connection is not properly established.")
        response = ""
        try:
            self.device_connection.write(cmd + '\n')
            while True:
                part = self.device_connection.read(1024)
                if part:
                    response += part
                    if response.endswith('> '):
                        break
                else:
                    break
        except (IOError, OSError) as e:
            return f"I/O error occurred: {str(e)}"
        except Exception as e:
            return f"Unexpected error occurred: {str(e)}"
        return response

    def iterative_prompting_4_send_command(self, cmd):
        import subprocess
        if not isinstance(cmd, str):
            raise ValueError('Command must be a string.')
        unsafe_characters = ['&', ';', '|', '`', '>', '<']
        if any(char in cmd for char in unsafe_characters):
            raise ValueError('Command contains potentially unsafe characters.')
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Command execution failed with error: {e.stderr}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def iterative_prompting_5_send_command(self, cmd):
        import subprocess
        import shlex
        if not isinstance(cmd, str):
            return "Invalid command: Command must be a string."
        try:
            cmd_list = shlex.split(cmd)
        except ValueError as e:
            return f"Command parsing error: {e}"
        import logging
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(f'Executing command: {cmd_list}')
        try:
            result = subprocess.run(
                cmd_list,
                check=True,
                text=True,
                capture_output=True
            )
            logging.debug(f'Command output: {result.stdout}')
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f'Command failed with error: {e}')
            return f"An error occurred while executing the command: {e}"
        except FileNotFoundError:
            logging.error(f'Command not found: {cmd_list[0]}')
            return "Command not found, please check the command and try again."
        except Exception as e:
            logging.error(f'Unexpected error: {e}')
            return f"An unexpected error occurred: {e}"

    def few_shots_prompting_send_command(self, cmd):
        try:
            print(f"Sending command: {cmd}")
        except Exception as e:
            print(f"An error occurred while sending the command: {e}")

    def cot_prompting_send_command(self, cmd):
        try:
            if hasattr(self, 'connection'):
                self.connection.sendall(cmd.encode())
                response = self.connection.recv(1024).decode()
                return response
            else:
                raise ValueError('Error: No connection established.')
        except Exception as e:
            raise ValueError('An error occurred while sending the command:', str(e))

    def fact_check_list_send_command(self, cmd):
            try:
                completed_process = subprocess.run(
                    cmd,
                    shell=True,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                result = {
                    'output': completed_process.stdout,
                    'error': completed_process.stderr,
                    'exit_code': completed_process.returncode
                }
            except subprocess.CalledProcessError as e:
                result = {
                    'output': e.stdout,
                    'error': e.stderr if e.stderr else str(e),
                    'exit_code': e.returncode
                }
            return result

    def not_interactive_mix_send_command(self, cmd):
        import subprocess
        import shlex
        if not isinstance(cmd, str) or cmd.strip() == "":
            raise ValueError("Invalid command")
        command = shlex.split(cmd)
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command '{cmd}' failed with status {e.returncode}: {e.stderr.decode('utf-8')}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

    def interactive_mix_execute_local_command(cmd):
        import subprocess
        import shlex
        if not isinstance(cmd, str) or not cmd.strip():
            raise ValueError("Command must be a non-empty string.")
        try:
            sanitized_cmd = shlex.split(cmd)
            result = subprocess.run(sanitized_cmd, text=True, capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def baseline_send_command(self, cmd):
        import subprocess
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

