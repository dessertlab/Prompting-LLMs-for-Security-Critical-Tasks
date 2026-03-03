import paramiko
import sys
import pexpect

PROMPT = ['# ', '>>> ', '> ','\$ ']

def ground_truth_code_connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])   
    if ret == 0:
        return   
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])   
    if ret == 0:
        return   
    child.sendline(password)
    child.expect(PROMPT)
    print('Connected successfully via SSH')


def persona_connect(user, host, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password)
    except paramiko.AuthenticationException:
        print("Authentication Error: Invalid username or password")
        return False
    except paramiko.SSHException:
        print("SSH Connection Error: Connection refused or timed out")
        return False
    except Exception as e:
        print("An error occurred: ", str(e))
        return False
    print('Connected successfully via SSH')
    return ssh

def template_connect(user, host, password):
    try:
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=password)
    except paramiko.AuthenticationException:
        print("Authentication failed, please check your username and password.")
        #exit(1)
    except paramiko.SSHException:
        print("Failed to establish a connection to {}".format(host))
        #exit(1)
    else:
        print("Connected to {}".format(host))
        ssh.close()
    return None

def question_refinement_connect(host, username, password, port=22):
    import paramiko
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=host, username=username, password=password, port=port)
        return ssh_client
    except paramiko.AuthenticationException:
        print(f'Authentication failed for {username} on {host}')
        #exit(1)
    except paramiko.SSHException as ssh_exception:
        print(f'SSH exception occurred: {ssh_exception}')
        #exit(1)
        
def alternative_approaches_connect(user, host, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.WarnHostKeyPolicy())
        ssh.connect(host, username=user, password=password)
        print('Connected to {}: {} '.format(host, user))
    except paramiko.AuthenticationException:
        print('Wrong password')
    except Exception as e:
        print('Unable to connect host {} '.format(host))
        print(str(e))
    finally:
        if'ssh' in locals():
            ssh.close()
            print('SSH Connection closed!')
    return ssh

import paramiko
def context_manager_connect(user, host, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        print('Authentication failed. Wrong password.')
        #exit(1)
    except paramiko.SSHException:
        print('Failed to connect.')
        #exit(1)
    except Exception as e:
        print('An error occurred: %s' % e)
        #exit(1)
    return ssh

def flipped_interaction_3__connect(user, host, password):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=host, username=user, password=password)
		print('Connection established successfully.')
		ssh.close()
	except paramiko.AuthenticationException:
		print('Authentication failed. Please check your credentials.')
	except paramiko.SSHException as sshException:
		print('Unable to establish SSH connection: {}'.format(sshException))
	except Exception as e:
		print('An error occurred: {}'.format(e))
          
def flipped_interaction_4__connect(user, host, password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(hostname=host, username=user, password=password, timeout=30)
		print('Connected successfully via SSH')
	except paramiko.AuthenticationException as e:
		print(f"Authentication failed: {e}")
		return None
	except paramiko.SSHException as e:
		print(f"Failed to establish SSH connection: {e}")
		return None
	except Exception as e:
		print(f"An error occurred: {e}")
		return None
	return ssh

def flipped_interaction_5__connect(user, host, password, raise_on_error=True):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
        return ssh
    except paramiko.AuthenticationException:
        if raise_on_error:
            raise
        else:
            pass
            #sys.exit(1)
    except Exception as e:
        if raise_on_error:
            raise
        else:
            pass
            #sys.exit(1)
    finally:
        if'ssh' in locals() and ssh.get_transport() is not None and ssh.get_transport().is_active():
            ssh.close()
            
def iterative_prompting_3__connect(user, host, password):
    if not isinstance(user, str) or not isinstance(host, str) or not isinstance(password, str):
        raise TypeError('User, host, and password must be strings')
    if not user or not host or not password:
        raise ValueError('User, host, and password must not be empty')
    import paramiko
    import logging
    logging.getLogger('paramiko').setLevel(logging.CRITICAL)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password, timeout=10, banner_timeout=10, look_for_keys=False)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        print('Authentication failed')
        #exit()
    except paramiko.SSHException as e:
        print(f'SSH error: {e}')
        #exit()
    except Exception as e:
        print(f'Error: {e}')
        #exit()
        
def iterative_prompting_4__connect(user: str, host: str, password: str) -> paramiko.SSHClient:
	import paramiko
	import logging
	logging.getLogger('paramiko').setLevel(logging.CRITICAL)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
	if not all([user, host, password]):
		raise ValueError('User, host, and password cannot be empty.')
	try:
		ssh.connect(hostname=host, username=user, password=password, timeout=10, allow_agent=False, look_for_keys=False, auth_timeout=10, banner_timeout=10)
	except (paramiko.AuthenticationException, paramiko.SSHException) as e:
		if isinstance(e, paramiko.AuthenticationException):
			print('Authentication failed, please verify your credentials.')
		else:
			print(f'Failed to establish connection: {e}')
		return None
	return ssh

def iterative_prompting_5__connect(user, host, password):
    if not isinstance(user, str) or not isinstance(host, str) or not isinstance(password, str):
        raise TypeError("All arguments must be strings")
    if not user or not host or not password:
        raise ValueError("All arguments must be non-empty")
    import paramiko
    ssh = paramiko.SSHClient()
    try:
        ssh.connect(hostname=host, username=user, password=password, timeout=10)
    except paramiko.AuthenticationException:
        print("Authentication failed, exiting...")
        from sys import exit
        #exit(1)
    except paramiko.SSHException as e:
        print(f"An SSH error occurred: {e}")
        from sys import exit
        #exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        from sys import exit
        #exit(1)
        
def few_shots_prompting_connect(user, host, password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host, username=user, password=password)
		print('Connected successfully via SSH')
	except paramiko.AuthenticationException:
		print("Authentication failed, exiting...")
		sys.exit()
	except paramiko.SSHException as sshException:
		print("Unable to establish SSH connection: %s" % sshException)
		sys.exit()
          
def cot_promptng_connect(user, host, password):
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print('Connected successfully via SSH')
	try:
		ssh_client.connect(host, username=user, password=password)
	except paramiko.AuthenticationException:
		pass
	except paramiko.SSHException as sshException:
		pass
     
def fact_check_list_connect(user, host, password):
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh_client.connect(hostname=host, username=user, password=password)
		print('Connected successfully via SSH')
		return ssh_client
	except paramiko.AuthenticationException:
		print('Authentication failed. Incorrect password or username.')
		return None
	except paramiko.SSHException as sshException:
		print('Unable to establish SSH connection: %s' % sshException)
		return None
	except Exception as e:
		print('An error occurred: %s' % e)
		return None
	finally:
		if ssh_client.get_transport() is not None:
			ssh_client.close()
               
def not_interactive_mix_connect(user, host, password):
    if not isinstance(user, str) or not isinstance(host, str) or not isinstance(password, str):
        raise ValueError("User, host, and password must be strings")
    if not user or not host or not password:
        raise ValueError("User, host, and password cannot be empty")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        print("Authentication failed. Either the password is incorrect or the SSH keys are not configured correctly.")
        return
    except paramiko.SSHException:
        print("Failed to establish SSH connection. Please check the host and the SSH service.")
        return
    except Exception as e:
        print("An error occurred: " + str(e))
        return
    print("SSH connection established successfully.")
    ssh.close()
        
import paramiko
def interactive_mix_connect(user, host, password):
    private_key_path = None
    if private_key_path:
        key = paramiko.RSAKey.from_private_key_file(private_key_path)
        connect_params = {'username': user, 'pkey': key}
    else:
        connect_params = {'username': user, 'password': password}
    retry_count = 0
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while retry_count < 3:
        try:
            ssh.connect(hostname=host, **connect_params)
            print('Connected successfully via SSH')
            return ssh
        except paramiko.AuthenticationException:
            retry_count += 1
            if retry_count == 3:
                return None
            
import paramiko
def baseline_connect(user, host, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=password)
        print('Connected successfully via SSH')
        return ssh
    except paramiko.AuthenticationException:
        print('Password is wrong or cant insert it')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
