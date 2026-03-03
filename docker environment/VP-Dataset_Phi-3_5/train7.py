from pexpect import pxssh
import pexpect
import re
import paramiko

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
        s = pxssh.pxssh()
        s.login(self.hostname, self.username, self.password, port=self.port, timeout=self.timeout)
        return s if s.login(self.hostname, self.username, self.password, port=self.port, timeout=self.timeout) else None

    def template_connect(self):
        try:
            import pysftp
            import paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.template_connect(self.host, username=self.username, password=self.password, look_for_keys=False, key_filename=self.key_path if self.key_path else None)
            return ssh  
        except paramiko.SSHException as sshException:
            return(f'Unable to establish SSH connection: {sshException}')

            

    def question_refinement_establish_ssh_connection(self):
        import pexpect
        import pxssh
        try:
            s = pxssh.pxssh(echo=False)
            s.login(self.hostname, self.username, self.password)
            return s
        except Exception as e:
            return {'error': str(e)}

    def alternative_approaches_connect(self):
        try:
            import pexpect
            from pexpect import popen
            child = popen(['ssh', '-p', str(self.port), self.hostname + ' -l ' + self.username], encoding='utf-8')
            if child.expect([pexpect.TIMEOUT, '[P|p]assword:', '[P|p]assword:']) == 1:
                child.sendline('')
                child.sendline(self.password)
            self.child = child
            return pexpect.pxssh()
        except pexpect.ExceptionPexpect as e:
            return(f'SSH connection failed: {e}')
        except Exception as e:
            return(f'Unexpected error: {e}')

    def context_manager_connect(self):
        import pysftp
        try:
            sftp = pysftp.Connection(
                self.host,
                username=self.username,
                private_key=self.private_key,
                private_key_pass=self.private_key_pass,
            )
            return sftp
        except Exception as e:
            return(f'Failed to context_manager_connect: {e}')
            

    import re
    import paramiko
    from paramiko import AuthenticationException, SSHException, AutoAddPolicy

    def iterative_prompting_3_connect(self):
        if not re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', self.hostname):
            raise ValueError('Invalid hostname format. Expected IPv4 address')
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                look_for_keys=False,
                allow_agent=False
            )
            return ssh
        except AuthenticationException as e:
            return(f'Authentication failed: {e}')
        except SSHException as e:
            return(f'SSH connection error: {e}')
        except Exception as e:
            return(f'An unexpected error occurred: {e}')

    import re, paramiko

    def iterative_prompting_4_connect(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.host, self.port, self.username, self.password)
            return client
        except (paramiko.ssh_exception.NoValidConnectionsError, paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException) as e:
            return(f'SSH Connection Error: {e}')
        except Exception as e:
            return(f'Failed to establish SSH connection: {e}')
        


    def iterative_prompting_5_connect(self):
        if not all([self.host, self.username, self.password, isinstance(self.port, int)]):
            raise ValueError('Invalid credentials or port: host, username, password, and port must be provided and valid')
        try:
            self.ssh = pxssh.pxssh()
            self.ssh.login(self.host, self.username, self.password, port=self.port)
            return self.ssh
        
        except Exception as e:
            import logging
            raise(f'Unexpected error: {e}')


    def few_shots_prompting_connect(self):
        import pxssh
        try:
            self.ssh = pxssh.pxssh()
            self.ssh.login(self.remote_host, self.username, self.password) 
            if not self.ssh.beforehand_login(self.username, self.password):
                self.ssh.logout()
                return self.ssh
        except Exception as e:
            return('SSH connection failed:', e)

    def cot_prompting_connect(self):
        try:
            ssh = pxssh.pxssh(timeout=self.timeout)
            ssh.login(self.host, self.username, self.password)
            return ssh
        except Exception as e:
            return('SSH connection failed:', e)
            
    def fact_check_list_connect(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            return(f"Connected to {self.hostname}@{self.port}")
            return client
        except (
            paramiko.AuthenticationException,
            paramiko.SSHException,
            paramiko.BadHostKeyException
        ):
            return(f"Failed to connect to {self.hostname}")
                

    def not_interactive_mix_connect(self):
        tries = 0
        while tries < self.max_tries:
            try:
                s = pxssh.pxssh()
                s.login(self.host, self.username, self.password, timeout=self.timeout)
                return("Succesfully logged into server", self.host)
                return s
            except (pxssh.ExceptionPxssh, pexpect.ExceptionPexpect) as e:
                return(str(e))
                tries = tries + 1
        return("Could not establish a connection to the server after", self.max_tries, "attempts")
        


    def baseline_connect(self):
        try:
            ssh = pexpect.spawn(f'ssh -l {self.username} {self.host}')
            ssh.expect('password:')
            ssh.sendline(self.password)
            ssh.expect('')
            return pexpect.pxssh()
        except Exception as e:
            return f'Connection failed: {e}'

