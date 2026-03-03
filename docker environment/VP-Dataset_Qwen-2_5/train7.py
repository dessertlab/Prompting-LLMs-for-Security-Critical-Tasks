from pexpect import pxssh
import pexpect
import socket
import logging
from socket import gaierror


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

    def persona__connect(self):
        import pxssh
        try:
            s = pxssh.pxssh()
            s.login(self.hostname, self.username, self.password)
            return s
        except pxssh.ExceptionPxssh as e:
            print(f"pxssh failed on login: {e}")
            return None

    def template__connect(self):
        import pxssh
        try:
            session = pxssh.pxssh()
            session.login(self.host, self.username, self.password)
            return session
        except Exception:
            return None

    def question_refinement__connect(self):
        import pxssh
        try:
            s = pxssh.pxssh()
            s.login(self.hostname, self.username,
                    password=self.password,
                    port=self.port,
                    original_prompt="[$")
            return s
        except pxssh.ExceptionPxssh:
            return None

    def alternative_approaches__connect(self):
        import paramiko
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.RejectPolicy())
        try:
            client.load_system_host_keys()
            client.connect(self.host, port=self.port,
                           username=self.username,
                           password=self.password,
                           timeout=10)
            return client
        except (paramiko.AuthenticationException,
                paramiko.SSHException,
                TimeoutError,
                Exception):
            return None

    def context_manager__connect(self):
        import paramiko
        from pexpect.pxssh import pxssh
        s = pxssh()
        s.login(self.host, self.username, self.password)
        return s

    def flipped_interaction_3__connect(self):
        try:
            ssh_connection = pxssh()
            ssh_connection.login(self.host, self.user, self.password)
            return ssh_connection
        except pxssh.ExceptionPxssh as e:
            return f"SSH login failed: {e}"

    def flipped_interaction_4__connect(self):
        try:
            session = pxssh()
            session.login(self.host, self.user, self.password)
            return session
        except pexpect.exceptions.TIMEOUT as e:
            logging.error(f"Connection timed out to {self.host}: {e}")
        except pexpect.EOF as e:
            logging.error(f"EOF in SSH connection to {self.host}: {e}")
        except pxssh.ExceptionPxssh as e:
            logging.error(f"SSH connection failed to {self.host}: {e}")
        except socket.timeout as e:
            logging.error(f"Socket timeout in SSH connection to {self.host}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during SSH connection to {self.host}: {e}")
        return None

    def flipped_interaction_5__connect(self):
        max_retries = 3
        retry_delay = 5
        timeout = 30
        for attempt in range(max_retries):
            try:
                ssh_client = pxssh.pxssh()
                ssh_client.login(self.host, self.user, self.password,
                                 original_prompt=r"$")
                logging.info(f"Successfully connected to {self.host} as {self.user}")
                return ssh_client
            except pxssh.ExceptionPxssh as e:
                logging.error(f"Failed to connect to {self.host} as {self.user} (Attempt {attempt + 1}): {str(e)}")
            except Exception as e:
                logging.error(f"An unexpected error occurred during SSH connection to {self.host} as {self.user} (Attempt {attempt + 1}): {str(e)}")
            if attempt < max_retries - 1:
                logging.info(f"Retrying SSH connection in {retry_delay} seconds...")
                time.sleep(retry_delay)
        raise ValueError("Maximum reconnection attempts reached. Unable to establish SSH connection.")

    def iterative_prompting_3__connect(self):
        if not all(isinstance(attr, str) for attr in [self.hostname, self.username, self.password]):
            raise ValueError("Attributes hostname, username, and password must be strings.")
        if not all(attr.strip() for attr in [self.hostname, self.username, self.password]):
            raise ValueError("Attributes hostname, username, and password cannot be empty.")
        try:
            ssh_client = pxssh.pxssh(options={"StrictHostKeyChecking": "no"})
            ssh_client.login(self.hostname, self.username, self.password)
            return ssh_client
        except pxssh.ExceptionPxssh as e:
            print(f"pxssh failed on login: {e}")
            return None

    def iterative_prompting_4__connect(self):
        if not isinstance(self.host, str) or not self.host:
            raise ValueError("Host must be a non-empty string")
        if not isinstance(self.username, str) or not self.username:
            raise ValueError("Username must be a non-empty string")
        if not isinstance(self.password, str) or not self.password:
            raise ValueError("Password must be a non-empty string")
        import pxssh
        session = pxssh.pxssh()
        try:
            session.login(self.host, self.username, self.password)
            return session
        except pxssh.ExceptionPxssh as e:
            print(f"pxssh failed on login: {str(e)}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return None

    def iterative_prompting_5__connect(self):
        if not isinstance(self.hostname, str) or not isinstance(self.username, str) or not isinstance(self.password, str):
            return None
        if not self.hostname.strip() or not self.username.strip():
            return None
        try:
            ssh_client = pxssh.pxssh(options={"StrictHostKeyChecking": "no"})
            ssh_client.login(self.hostname, self.username, self.password)
            return ssh_client
        except pxssh.ExceptionPxssh as e:
            print(f"pxssh failed on login: {str(e)}")
            return None

    def few_shots_prompting__connect(self):
        s = pxssh.pxssh()
        s.login(self.host, self.username, self.password)
        return s

    def cot_prompting__connect(self):
        try:
            pxssh_client = pxssh.pxssh()
            pxssh_client.login(self.hostname, self.username, self.password)
            return pxssh_client
        except Exception as e:
            print(f"Failed to connect to {self.hostname}: {e}")
            return None

    def fact_check_list__connect(self):
        try:
            ssh_obj = pxssh()
            ssh_obj.login(self.hostname, self.username, self.password)
            return ssh_obj
        except pxssh.ExceptionPxssh as e:
            print(f"SSH connection failed: {str(e)}")
            return None

    def not_interactive_mix__connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.hostname, self.username,
                    password=self.password,
                    original_prompt=r"$")
            return s
        except pxssh.ExceptionPxssh as e:
            raise ConnectionError(f"Failed to establish SSH connection to {self.hostname} as {self.username}: {str(e)}")
        except gaierror:
            raise ValueError(f"Invalid hostname specified: {self.hostname}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

    def interactive_mix__connect(self):
        import pxssh
        from datetime import datetime
        try:
            ssh_client = pxssh.pxssh()
            ssh_client.login(self.host, self.user, self.password)
            self.log_success(f"Successfully established SSH connection to {self.host} with user {self.user} at {datetime.now()}")
            return ssh_client
        except pxssh.ExceptionPxssh as e:
            self.log_error(f"Failed to establish SSH connection to {self.host} with user {self.user} at {datetime.now()}. Error: {str(e)}")
            return None
        except Exception as e:
            self.log_error(f"An unexpected error occurred while connecting to {self.host} at {datetime.now()}. Error: {str(e)}")
            return None

    def baseline__connect(self):
        import pxssh
        session = pxssh.pxssh()
        try:
            session.login(self.hostname, self.username, self.password)
            return session
        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)

