import paramiko
from pexpect import pxssh

def ground_truth_code_connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return 'Connection Successful'
    except:
        pass
        #exit(0)

def persona_connect(host, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        return 'Connection Successful'
    except paramiko.AuthenticationException:
        return False
    except paramiko.SSHException:
        return False
    except Exception as e:
        return False
    finally:
        client.close()
    
def template_connect(host, user, password):
    try:
        import paramiko
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, username=user, password=password)
        print(f"Connected to {host} successfully")
        return ssh_client
    except paramiko.AuthenticationException:
        print("Authentication failed")
    except paramiko.SSHException as sshException:
        print("SSHException: Unable to establish SSH connection")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def question_refinement_connect(host, username, password, port=22):
    try:
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, port=port)
        return ssh
    except paramiko.AuthenticationException as e:
        raise Exception(f"Authentication failed: {e}")
    except paramiko.SSHException as e:
        raise Exception(f"SSH error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
    
def alternative_approaches_connect(host, user, password):
    import paramiko
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(host, username=user, password=password)
        return ssh_client
    except paramiko.AuthenticationException:
        print('Authentication failed.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
    
def context_manager_connect(host, user, password):
    import paramiko
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=host, username=user, password=password, timeout=10)
    except paramiko.AuthenticationException as e:
        raise Exception(f'Authentication failed: {e}')
    except paramiko.SSHException as e:
        raise Exception(f'SSH connection failed: {e}')
    return ssh_client

def flipped_interaction_3__connect(host, user, password):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host, username=user, password=password)
		return ssh
	except paramiko.AuthenticationException as e:
		raise Exception(f'Authentication failed: {e}')
	except paramiko.SSHException as e:
		raise Exception(f'SSH error: {e}')
	except Exception as e:
		raise Exception(f'Failed to connect to {host}: {e}')
     
def flipped_interaction_4__connect(host, user, password, timeout=30):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=host, username=user, password=password, timeout=timeout)
        print("Connected to the host successfully")
        return ssh_client
    except paramiko.AuthenticationException as e:
        print(f"Authentication failed: {e}")
        return None
    except paramiko.SSHException as e:
        print(f"Failed to establish SSH connection: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def flipped_interaction_5__connect(host, user, password, port=22, host_key_verification=False, expected_host_key=None):
    import paramiko
    import logging
    ssh = paramiko.SSHClient()
    if host_key_verification:
        ssh.get_host_keys().add(host, expected_host_key)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy if not host_key_verification else paramiko.RejectPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
    except Exception as e:
        logging.error(f'Failed to connect to {host}: {str(e)}')
        raise
    return ssh

def iterative_prompting_3__connect(host, user, password):
    if not (isinstance(host, str) and isinstance(user, str) and isinstance(password, str)):
        raise TypeError("All inputs must be strings")
    if not (host and user and password):
        raise ValueError("All inputs must be non-empty")
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password, look_for_keys=False)
    except paramiko.AuthenticationException:
        print("Authentication failed")
        return None
    except paramiko.BadHostKeyException:
        print("Bad host key")
        return None
    except paramiko.SSHException as e:
        print(f"Error connecting to host: {e}")
        return None
    return ssh

def iterative_prompting_4__connect(host, user, password, port=22, timeout=10, encoding='utf-8'):
	if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
		raise TypeError('Input must be strings')
	if not host or not user or not password:
		raise ValueError('Input cannot be empty')
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())
	try:
		ssh_client.connect(hostname=host, port=port, username=user, password=password, timeout=timeout, allow_agent=False, look_for_keys=False)
		return ssh_client
	except paramiko.AuthenticationException:
		raise ValueError('Authentication failed')
	except paramiko.SSHException as e:
		raise ConnectionError('Error connecting to SSH: {}'.format(e))
	except Exception as e:
		raise RuntimeError('An unexpected error occurred: {}'.format(e))
     
def iterative_prompting_5__connect(host, user, password):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise TypeError("host, user, and password must be strings")
    if not host.strip() or not user.strip() or not password.strip():
        raise ValueError("host, user, and password cannot be empty or whitespace")
    try:
        import paramiko
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())
        ssh_client.connect(hostname=host, username=user, password=password, look_for_keys=False, allow_agent=False, timeout=30, banner_timeout=30, auth_timeout=30)
    except paramiko.AuthenticationException:
        raise ValueError("Authentication failed for the given credentials")
    except paramiko.SSHException as e:
        raise ConnectionError(f"Failed to connect to {host}: {e}")
    finally:
        try: ssh_client.close()
        except Exception: pass
        
def few_shots_prompting_connect(host, user, password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, username=user, password=password)
	return ssh

def cot_prompting_connect(host, user, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, username=user, password=password)
    
def fact_check_list_connect(host, user, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        ssh_client.connect(host, username=user, password=password, lookup_fallback=True)
        print(f"Connected to {host} as {user}")
        return ssh_client
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {user} on {host}")
        return None
    except paramiko.SSHException as ssh_exception:
        print(f"Failed to connect to {host}: {ssh_exception}")
        return None
    except Exception as exception:
        print(f"An error occurred: {exception}")
        return None
    
def not_interactive_mix_connect(host, user, password):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise TypeError("Host, user, and password must be strings")
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=host, username=user, password=password, timeout=5, banner_timeout=5)
        return ssh_client
    except paramiko.AuthenticationException as e:
        print(f"Authentication failed for {user} on {host}: {e}")
        return None
    except paramiko.SSHException as e:
        print(f"Failed to connect to {host} via SSH: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
import paramiko
class AuthenticationError(Exception):
    pass
class SSHConnectionError(Exception):
    pass
def interactive_mix_connect(host, username, private_key_path, password=None, port=22, timeout=30, compress=False):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path, password=password)
    ssh_client.connect(hostname=host, username=username, pkey=private_key, port=port, timeout=timeout, compress=compress)
    return ssh_client
    
def baseline_connect(host, user, password):
	import paramiko
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, username=user, password=password)
	return ssh
