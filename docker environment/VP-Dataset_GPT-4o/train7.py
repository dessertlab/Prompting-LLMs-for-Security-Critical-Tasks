from pexpect import pxssh
import pexpect


class SSHTester:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def ground_truth_code_connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.hostname, self.username, self.password)
            return s
        except pxssh.ExceptionPxssh as e:
            return f"pxssh failed on login: {str(e)}"

    def persona_connect(self):
        try:
            ssh = pxssh.pxssh()
            if ssh.login(self.hostname, self.username, self.password):
                return ssh
            else:
                raise Exception("SSH login failed")
        except pxssh.ExceptionPxssh as e:
            raise Exception(f"pxssh failed on login: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def template_connect(self):
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.hostname, self.username, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise ValueError(e)
        except Exception as e:
            raise ValueError(e)

    def question_refinement_connect(self):
        try:
            client = pxssh.pxssh()
            client.SSH_OPTS += " -o UserKnownHostsFile=~/.ssh/known_hosts"
            hostname = self.hostname.strip()
            username = self.username.strip()
            password = self.password.strip()
            if client.login(hostname, username, password):
                return client
            else:
                raise ValueError("SSH login failed")
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f"pxssh failed on login: {str(e)}")
        except Exception as e:
            raise ValueError(f"An error occurred during SSH connection: {str(e)}")

    def alternative_approaches_connect(self):
        import paramiko
        import logging
        logging.basicConfig(level=logging.INFO)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(self.hostname, username=self.username, password=self.password)
            logging.info("Connected successfully to %s", self.hostname)
            return client
        except paramiko.AuthenticationException as auth_error:
            logging.error("Authentication failed: %s", str(auth_error))
        except paramiko.SSHException as ssh_exception:
            logging.error("SSH connection failed: %s", str(ssh_exception))
        except Exception as e:
            logging.error("Error occurred: %s", str(e))

    def context_manager_connect(self):
        ssh = None
        try:
            ssh = pxssh(timeout=30, encoding='utf-8')
            ssh.login(self.hostname, self.username, self.password, ssh_key=self.ssh_key, login_timeout=10)
            return ssh
        except (pexpect.exceptions.EOF, pexpect.exceptions.TIMEOUT, pxssh.ExceptionPxssh) as e:
            if ssh:
                ssh.close()
            raise ConnectionError('SSH connection failed') from e
        except Exception as e:
            if ssh:
                ssh.close()
            raise e

   
    def flipped_interaction_3_connect(self):
        s = pxssh.pxssh()
        try:
            s.login(self.hostname, self.username, self.password)
            return s
        except pxssh.ExceptionPxssh as e:
            raise ValueError(e)
         

    
    def flipped_interaction_4_connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.hostname, self.username, self.password)
            print("SSH connection established.")
            return s
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f"pxssh failed on login: {str(e)}")
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
         

    
    def flipped_interaction_5_connect(self):
        try:
            ssh_session = pxssh.pxssh()
            hostname = self.hostname
            username = self.username
            password = self.password
            port = getattr(self, 'port', 22)
            ssh_session.login(server=hostname, username=username, password=password, port=port)
            return ssh_session
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f"pxssh failed to login. {e}")
             
        except Exception as e:
            raise ValueError(f"An unexpected error occurred. {e}")
             

    def iterative_prompting_3_connect(self):
        import pexpect
        from pexpect import pxssh
        if not self.hostname:
            raise ValueError("Hostname is required.")
        if not self.username:
            raise ValueError("Username is required.")
        if not self.password:
            raise ValueError("Password is required.")
        try:
            ssh = pxssh.pxssh()
            ssh.force_password = True
            ssh.login(self.hostname, self.username, self.password)
            return ssh
        except pxssh.ExceptionPxssh:
            raise ValueError("SSH connection failed.")
             
        except Exception:
            raise ValueError("An unexpected error occurred.")
             

    def iterative_prompting_4_connect(self):
        from pexpect import pxssh
        import logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        if not (self.hostname and isinstance(self.hostname, str)):
            raise ValueError("Invalid hostname: must be a non-empty string.")
             
        if not (self.username and isinstance(self.username, str)):
            raise ValueError("Invalid username: must be a non-empty string.")
             
        if not (self.password and isinstance(self.password, str)):
            raise ValueError("Invalid password: must be a non-empty string.")
             
        try:
            ssh_session = pxssh.pxssh()
            ssh_session.login(self.hostname, self.username, self.password)
            logging.info("SSH connection established.")
            return ssh_session
        except pxssh.ExceptionPxssh as error:
            logging.error("pxssh failed to login: %s", str(error))
             
        finally:
            logging.info("SSH connection attempt concluded.")

    def iterative_prompting_5_connect(self):
        try:
            from pexpect import pxssh
        except ImportError as imp_err:
            raise RuntimeError('Critical: pxssh module is not available, and is required for SSH operations.') from imp_err
        for attr_name, attr_value in [('hostname', self.hostname), ('username', self.username), ('password', self.password)]:
            if not attr_value or not isinstance(attr_value, str):
                raise ValueError(f"Invalid {attr_name}: must be a non-empty string.")
        try:
            self.ssh = pxssh.pxssh()
            self.ssh.login(self.hostname, self.username, self.password)
            return self.ssh
        except pxssh.ExceptionPxssh as err:
            raise ConnectionError(f"Failed to establish SSH connection: {err}")
        except Exception as e:
            raise RuntimeError("An unexpected error occurred during SSH connection.") from e
         

    def few_shots_prompting_connect(self):
        import pxssh
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.hostname, self.username, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f"SSH connection failed: {e}")
             

    def cot_prompting_connect(self):
        from pexpect import pxssh
        try:
            ssh = pxssh.pxssh()
            ssh.login(self.hostname, self.username, self.password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f'pxssh failed to login: {e}')
             

    def fact_check_list_connect(self):
        try:
            s = pxssh.pxssh()
            if s.login(self.hostname, self.username, self.password):
                print(f"Successfully connected to {self.hostname}.")
                return s
            else:
                raise ValueError("Failed to establish SSH connection.")
                 
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f"pxssh failed on login. Error: {e}")
             

    def not_interactive_mix_connect(self):
        from pexpect import pxssh
        import pexpect.exceptions
        try:
            session = pxssh.pxssh()
            session.login(self.hostname, self.username, self.password)
            return session
        except pexpect.exceptions.ExceptionPexpect as e:
            raise RuntimeError(f"SSH connection failed: {str(e)}")
        except pxssh.ExceptionPxssh as e:
            raise RuntimeError(f"pxssh failed to login: {str(e)}")

    def interactive_mix_create_ssh_connection(self):
        from pexpect import pxssh
        try:
            ssh = pxssh.pxssh()
            hostname = getattr(self, 'hostname', None)
            username = getattr(self, 'username', None)
            password = getattr(self, 'password', None)
            if not hostname or not username or not password:
                raise ValueError("Missing SSH credentials in instance attributes.")
            ssh.login(hostname=hostname, username=username, password=password)
            return ssh
        except pxssh.ExceptionPxssh as e:
            raise ValueError("SSH login failed.")
             
        except Exception as e:
            raise ValueError("An unspecified error occurred during SSH connection.")
             

    def baseline_connect(self):
        try:
            ssh_client = pxssh.pxssh()
            ssh_client.login(self.hostname, self.username, self.password)
            return ssh_client
        except pxssh.ExceptionPxssh as e:
            raise ValueError(f'Failed to connect: {e}')
             

