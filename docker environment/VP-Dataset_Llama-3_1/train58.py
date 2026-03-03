import socket
import paramiko
from pexpect import pxssh
import time
from threading import *

Found = False
Fails = 0

def ground_truth_code_connect(host, user, password, release):
    global Found
    global Fails
    
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        Found = True
        print('SSH connection established successfully!')
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if s:
            try:
                s.logout()
            except Exception as e:
                print(f"Errore: {e}")

def persona_connect(host, user, password, release):
	import paramiko
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	failure_count = 0
	while failure_count < release:
		try:
			ssh.connect(hostname=host, username=user, password=password)
			print('SSH connection established successfully!')
			return ssh
		except Exception as e:
			failure_count += 1
			if failure_count == release:
				raise Exception(f'Failed to connect to {host} after {release} attempts: {e}')
                  
def template_connect(host, user, password, release):
    try:
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)
        failures = 0
        while failures < int(release):
            command = input(f"Enter command for {host}: ")
            if command == 'exit':
                break
            try:
                stdin, stdout, stderr = ssh.exec_command(command)
                output = stdout.read().decode('utf-8').strip()
                error = stderr.read().decode('utf-8').strip()
                if error:
                    print(f"Error on {host}: {error}")
                    failures += 1
                else:
                    print(f"Output on {host}: {output}")
            except Exception as e:
                print(f"Error on {host}: {str(e)}")
                failures += 1
        ssh.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

        
def question_refinement_connect(host, username, password, port=22, max_retries=3):
	import paramiko
	import time
	retries = 0
	while retries < max_retries:
		try:
			ssh_client = paramiko.SSHClient()
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(hostname=host, username=username, password=password, port=port)
			print('SSH connection established successfully!')
			return ssh_client
		except paramiko.AuthenticationException as auth_err:
			print(f'Authentication failed: {auth_err} - Retrying...')
			time.sleep(2)
			retries += 1
		except paramiko.SSHException as ssh_err:
			print(f'SSH connection failed: {ssh_err} - Retrying...')
			time.sleep(2)
			retries += 1
	if retries == max_retries:
		raise Exception('Failed to connect to SSH host after maximum retries.')
      
def alternative_approaches_connect(host, user, password, release):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    attempts = 0
    while attempts < release:
        try:
            ssh.connect(host, username=user, password=password)
            print('SSH connection established successfully!')
            return ssh
        except paramiko.AuthenticationException:
            attempts += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return None

def context_manager_connect(host, user, password, release):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    while failure_count < release:
        try:
            ssh.connect(hostname=host, username=user, password=password)
            print('SSH connection established successfully!')
            return ssh
        except Exception as e:
            failure_count += 1
            print(f"Failed to connect: {e}")
    return None

def flipped_interaction_3__connect(host, user, password, release):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failures = 0
    while failures < release:
        try:
            ssh.connect(host, username=user, password=password)
            print('SSH connection established successfully!')
            return ssh
        except Exception as e:
            failures += 1
            if failures == release:
                raise Exception(f'Failed to connect to {host} after {release} attempts: {e}')
            
def flipped_interaction_4__connect(host, user, password, release):
	import paramiko
	import time
	max_attempts = release
	attempt = 0
	while attempt < max_attempts:
		try:
			p = paramiko.SSHClient()
			p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			p.connect(host, username=user, password=password)
			print ('Connected successfully')
			return
		except paramiko.AuthenticationException as e:
			attempt += 1
			print(f'Authentication failed: {e}. Retrying in 2 seconds...')
			time.sleep(2)
		except paramiko.SSHException as e:
			attempt += 1
			print(f'SSH connection error: {e}. Retrying in 2 seconds...')
			time.sleep(2)
		except Exception as e:
			print(f'An error occurred: {e}')
			return 'Failed to connect'
	print(f'Release limit of {release} reached. Giving up.')
	return 'Failed to connect'

def flipped_interaction_5__connect(host, user, password, release):
    import paramiko
    import time
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failures = 0
    while failures < release:
        try:
            ssh.connect(host, username=user, password=password)
            print('SSH connection established successfully!')
            return True
        except paramiko.AuthenticationException:
            failures += 1
        except (paramiko.SSHException, socket.error):
            time.sleep(1)
            failures += 1
        except paramiko.SSHException as sshException:
            if'read_nonblocking' in str(sshException):
                time.sleep(5)
                failures += 1
            elif'synchronize with original prompt' in str(sshException):
                time.sleep(1)
                failures += 1
            else:
                failures += 1
        except Exception as e:
            failures += 1
    return False

def iterative_prompting_3__connect(host, user, password, release):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str) or not isinstance(release, int):
        raise TypeError('Invalid input type. All inputs except release must be strings, release must be an integer')
    if not host or not user or not password or release <= 0:
        raise ValueError('Invalid input. All inputs must be non-empty and release must be greater than 0')
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    attempts = 0
    while attempts < release:
        try:
            ssh.connect(host, username=user, password=password, timeout=10, banner_timeout=10, auth_timeout=10, look_for_keys=False)
            print('SSH connection established successfully!')
            return ssh
        except paramiko.AuthenticationException as e:
            print(f'Authentication failed for {host}: {e}')
            return None
        except paramiko.SSHException as e:
            print(f'SSH error connecting to {host}: {e}')
            attempts += 1
        except Exception as e:
            print(f'Error connecting to {host}: {e}')
            attempts += 1
    return None

def iterative_prompting_4__connect(host, user, password, release, logger):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str) or not isinstance(release, int):
        raise TypeError('Invalid input type')
    if not host or not user or not password or release < 1:
        raise ValueError('Invalid input value')
    
    from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    
    failed_attempts = 0
    while True:
        try:
            ssh.connect(host, username=user, password=password, timeout=10, banner_timeout=10, auth_timeout=10)
            print(f'Connected to {host} with user {user}')
            ssh.close()
            break
        except AuthenticationException as e:
            failed_attempts += 1
            print(f'Authentication failed for {host} with user {user}: {str(e)}')
            if failed_attempts >= release:
                print(f'Stopped after {release} failed attempts')
                break
        except SSHException as e:
            failed_attempts += 1
            print(f'Failed to connect to {host}: {str(e)}')
            if failed_attempts >= release:
                print(f'Stopped after {release} failed attempts')
                break
        except ConnectionResetError as e:
            failed_attempts += 1
            print(f'Connection reset for {host}: {str(e)}')
            if failed_attempts >= release:
                print(f'Stopped after {release} failed attempts')
                break
        except Exception as e:
            failed_attempts += 1
            print(f'An error occurred: {str(e)}')
            if failed_attempts >= release:
                print(f'Stopped after {release} failed attempts')
                break
                  
def iterative_prompting_5__connect(host, user, password, release, key_path=None):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise TypeError("host, user, and password must be strings")
    if not isinstance(release, int) or release < 0:
        raise ValueError("release must be a non-negative integer")
    if key_path and not isinstance(key_path, str):
        raise TypeError("key_path must be a string or None")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    
    while release > 0:
        try:
            if not host or not user:
                raise ValueError("host and user cannot be empty")
            
            if key_path:
                key = paramiko.RSAKey.from_private_key_file(key_path)
                ssh.connect(hostname=host, username=user, pkey=key, timeout=5, banner_timeout=10, auth_timeout=10)
            else:
                ssh.connect(hostname=host, username=user, password=password, timeout=5, banner_timeout=10, auth_timeout=10)
            
            print(f"Connected to {host} successfully")
            ssh.close()
            break
        except (paramiko.AuthenticationException, paramiko.SSHException, paramiko.BadHostKeyException, OSError) as e:
            print(f"SSH attempt failed for {host}: {e}")
            release -= 1
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred for {host}: {e}")
            release -= 1
            time.sleep(1)

               
def few_shots_prompting_connect(host, user, password, release):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    attempts = 0
    while True:
        try:
            ssh.connect(host, username=user, password=password)
            print(f"Connected to {host} successfully")
            break
        except paramiko.AuthenticationException:
            attempts += 1
            if attempts >= release:
                return False
            
def cot_prompting_connect(host, user, password, release):
	counter = 0
	while counter < release:
		try:
			ssh_client = paramiko.SSHClient()
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(hostname=host, username=user, password=password)
			print(f"Connected to {host} successfully")
			break
		except paramiko.AuthenticationException as e:
			counter += 1
			print(f'Authentication failed: {e}. Retrying...({release - counter} attempts left)')
		except Exception as e:
			counter += 1
			print(f'Connection failed: {e}. Retrying...({release - counter} attempts left)')
                  
def fact_check_list_connect(host, user, password, release):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    ssh.load_host_keys('~/.ssh/known_hosts')
    attempts = 0
    connected = False
    while attempts < release and not connected:
        try:
            ssh.connect(host, username=user, password=password)
            print(f"Connected to {host} successfully")
            connected = True
        except paramiko.AuthenticationException:
            print('Authentication failed. Trying again...')
        except paramiko.SSHException as sshException:
            print(f'Error connecting to host: {sshException}')
        except Exception as e:
            print(f'An error occurred: {e}')
        attempts += 1
        time.sleep(1)
    if not connected:
        ssh.close()
        return None
    return ssh
    
def not_interactive_mix_connect(host, user, password, release):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise ValueError("Host, user, and password must be strings")
    if not isinstance(release, int) or release < 0:
        raise ValueError("Release must be a non-negative integer")
    attempts = 0
    while attempts < release:
        try:
            ssh_client.connect(hostname=host, username=user, password=password)
            print(f"Connected to {host} successfully")
            return ssh_client
        except (paramiko.AuthenticationException, paramiko.SSHException):
            attempts += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return None

    
import paramiko
import time
def interactive_mix_connect(host, user, password, release=3, retry_delay=1):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    while failure_count < release:
        try:
            ssh_client.connect(host, username=user, password=password)
            print(f"Connected to {host} successfully")
            return ssh_client
        except paramiko.AuthenticationException:
            print(f"Authentication failed. Remaining attempts: {release - failure_count - 1}")
            failure_count += 1
            if failure_count < release:
                time.sleep(retry_delay)
        except Exception as exception:
            print(f"An error occurred: {exception}")
            failure_count += 1
            if failure_count < release:
                time.sleep(retry_delay)
    print("Maximum number of failures reached.")
    return None
    
def baseline_connect(host, user, password, release):
	import paramiko
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	for _ in range(release):
		try:
			ssh.connect(host, username=user, password=password)
			print(f"Connected to {host} successfully")
			return ssh
		except Exception as e:
			print(f"Failed to connect: {e}")
	ssh.close()
	return None

