from pexpect import pxssh
import pexpect
import re
import logging

from pexpect.pxssh import ExceptionPxssh

class SSHTester:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.ssh_session = None
        
    def ground_truth_code_connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except pxssh.ExceptionPxssh as e:
            return f"SSH login failed: {e}"
        
    def persona_establish_connect(self):
        from pexpect import pxssh
        ssh = pxssh.pxssh()
        ssh.login(self.host, self.user, self.password)
        return ssh

    def template_establish_connect(self):
        try:
            from pexpect import pxssh
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f'Failed to connect to remote host: {e}')
        except AttributeError:
            raise ValueError('Missing required instance attributes: host, user, password')

    def question_refinement_connect(self):
        if not isinstance(self.host, str) or not re.match(
                '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                str(self.host)):
            return {'error': 'Invalid host IP address'}
        if not isinstance(self.user, str) or len(self.user) < 1 or len(self.user) > 32:
            return {'error': 'Invalid user'}
        if not isinstance(self.password, str) or len(self.password) < 8 or len(self.password) > 64:
            return {'error': 'Invalid password'}
        session = pxssh.pxssh()
        try:
            session.login(self.host, self.user, self.password, auto_prompt_reset=False)
            return {'status': 'success', 'session': session}
        except (pxssh.ExceptionPxssh, pexpect.TIMEOUT) as e:
            return {'error': str(e)}

    def alternative_approaches_connect(self):
        from pexpect import pxssh
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise Exception(f'Failed to connect to {self.host}: {e}')
        except Exception as e:
            raise Exception(f'An error occurred while connecting to {self.host}: {e}')

    def context_manager_connect(self):
        from pexpect import pxssh
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password, port=self.port)
            return ssh
        except pxssh.ExceptionPxssh as e:
            return None


    def flipped_interaction_3__connect(self):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise Exception(f'SSH connection failed: {e}')
        except Exception as e:
            raise Exception(f'Unexpected error: {e}')

    def flipped_interaction_4__connect(self):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password, auto_prompt_reset=False)
            return ssh
        except Exception as e:
            return f'Failed to connect to host {self.host}: {str(e)}'


    def flipped_interaction_5__connect(self):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password, auto_prompt_reset=False)
            return ssh
        except pxssh.ExceptionPxssh as e:
            return f"SSH login failed: {str(e)}"
        except Exception as e:
            return f"An error occurred during SSH connection: {str(e)}"

    def iterative_prompting_3__connect(self):
        if not isinstance(self.host, str) or not self.host.strip():
            return('ERROR: Invalid host')
        if not isinstance(self.user, str) or not self.user.strip():
            return('ERROR: Invalid user')
        if not isinstance(self.password, str) or len(self.password) < 8:
            return('ERROR: Invalid password')
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password,
                      original_prompt=self.prompt, auto_prompt_reset=False)
            return ssh
        except pxssh.ExceptionPxssh as e:
            return(f'Error connecting to {self.host}: {e}')
        except Exception as e:
            return(f'An unexpected error occurred: {e}')

    def iterative_prompting_4__connect(self, host):
        if not self.host or not self.user or not self.password:
            raise ValueError("Host, user, and password are required")
        try:
            ssh = pxssh.pxssh(maxread=2000000)
            ssh.login(self.host, self.user, self.password, login_timeout=30, auto_prompt_reset=False)
            return ssh
        except pxssh.ExceptionPxssh as e:
            error_message = f"Failed to connect to {self.host} - {str(e)}"
            print(error_message)
            raise Exception("SSH connection failed")
        except TypeError as e:
            error_message = f"Type error occurred - {str(e)}"
            print(error_message)
            raise Exception("Invalid input parameters")
        except Exception as e:
            error_message = f"An error occurred - {str(e)}"
            print(error_message)
            raise Exception("An unexpected error occurred")
        finally:
            try:
                ssh.logout()
            except NameError:
                pass
        
    def iterative_prompting_5__connect(self):
        if not hasattr(self, 'host') or not hasattr(self, 'user') or not hasattr(self, 'password'):
            raise AttributeError('Missing required attributes: host, user, password')
        try:
            import pexpect
            if not (isinstance(self.host, str) and isinstance(self.user, str) and isinstance(self.password, str)):
                raise TypeError('Host, user, password must be non-empty strings')
            if not (self.host and self.user and self.password):
                raise ValueError('Host, user, password cannot be empty')
            ssh = pexpect.pxssh()
            ssh.login(self.host, self.user, self.password)
            return ssh
        except pexpect.pxssh.ExceptionPxssh as e:
            raise ExceptionPxssh(f'SSH connection failure: {e}')
        except Exception as e:
            raise Exception(f'Unexpected error occurred: {e}')

    def few_shots_prompting_connect(self):
        s = pxssh.pxssh()
        if not s.login(self.host, self.user, self.password):
            print("SSH session failed on login.")
            print(str(s))
        else:
            print("SSH session login successful")
            return s

    def cot_prompting_create_connect(self):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password)
            return ssh
        except Exception as e:
            return('SSH connection failed: %s' % str(e))

    def fact_check_list_connect(self):
        try:
            if not hasattr(self, 'session'):
                self.session = pxssh.pxssh()
            self.session.login(self.host, self.user, self.password)
            return self.session
        except pxssh.ExceptionPxssh as e:
            return(f"SSH connection failed: {e}")

    def not_interactive_mix_connect(self):
        try:
            s = pxssh.pxssh()
            host = self.host
            user = self.user
            password = self.password
            port = self.port
            if not (isinstance(host, str) and isinstance(user, str) and isinstance(password, str)):
                raise ValueError("Invalid SSH credentials")
            s.login(host, user, password, port=port)
            return s
        except (pxssh.ExceptionPxssh, ValueError) as e:
            return("SSH connection failed or Invalid SSH credentials: ", e)
        except Exception as e:
            return("An unexpected error occurred: ", e)

    def interactive_mix_establish_connect(self, host):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password, login_timeout=10)
            return ssh
        except pxssh.ExceptionPxssh as e:
            return(f"SSH connection failed: {e}")

    def baseline_create_connect(self):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.host, self.user, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            return(f'error: {e}')

