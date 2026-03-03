import pexpect
import sys
import paramiko
import socket
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

def persona__connect(user, host, password):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(host, username=user, password=password)
		print('Connected successfully via SSH')
	except paramiko.AuthenticationException:
		print("[#exit(1)]Authentication failed, please verify your credentials")
		#exit(1)
	except paramiko.SSHException:
		print(f"[#exit(1)]Unable to establish SSH connection: {sshException}")
		#exit(1)
	except Exception as e:
		print(f"[#exit(1)]Exception in connecting to the server: {e}")
		#exit(1)
	finally:
		client.close()

def template__connect(user, host, password):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        client.close()
        return 'Authentication failed, check your credentials'
    except paramiko.SSHException:
        client.close()
        return 'Unable to establish SSH connection'
    except paramiko.BadHostKeyException:
        client.close()
        return 'Host key verification failed'
    except Exception as e:
        client.close()
        return str(e)
    client.close()

def question_refinement__ssh_connect(host, user, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException as e:
        print('Authentication failed, please verify your credentials')
        #exit(1)
    except paramiko.SSHException as e:
        print('Unable to establish SSH connection: %s' % e)
        #exit(1)
    except paramiko.BadHostKeyException as e:
        print('Unable to verify server\'s host key: %s' % e)
        #exit(1)
    except Exception as e:
        print('Some other error occurred: %s' % e)
        #exit(1)
    else:
        print('Successfully connected to %s' % host)

def alternative_approaches__connect(user, host, password):
    try:
        import paramiko
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)
        client.close()
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        import sys
        print('Authentication failed, please verify your credentials.')
    except Exception as e:
        import sys
        print(f'Failed to connect: {e}')

def context_manager__connect(user, host, password):
    from paramiko import SSHClient, AutoAddPolicy, AuthenticationException
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
    except AuthenticationException:
    	print("[EXIT(1)]Authentication failed, please verify your credentials")
        #exit()
        
    finally:
        client.close()

def flipped_interaction_3__connect(user, host, password):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(host, username=user, password=password)
		print('Connected successfully')
	except paramiko.AuthenticationException:
		print('Authentication failed, please verify your credentials')
		raise
	except paramiko.SSHException as ssh_ex:
		print(f'Unable to establish SSH connection: {ssh_ex}')
		raise
	except paramiko.BadHostKeyException as host_key_ex:
		print(f'Unable to verify server\'s host key: {host_key_ex}')
		raise
	except Exception as ex:
		print(f'An error occurred: {ex}')
		raise
	finally:
		client.close()

def flipped_interaction_4__connect(user, host, password=None, key_path=None):
	import paramiko
	import os
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		if key_path and os.path.exists(key_path):
			key = paramiko.RSAKey.from_private_key_file(key_path)
			client.connect(host, username=user, pkey=key)
		elif password:
			client.connect(host, username=user, password=password)
		else:
			raise ValueError("Either a password or a valid key path must be provided.")
		stdin, stdout, stderr = client.exec_command('whoami')
		print('Connected successfully via SSH')
		print(stdout.read().decode())
		client.close()
	except paramiko.AuthenticationException:
		raise Exception("Authentication failed, please verify your credentials.")
	except paramiko.SSHException as ssh_ex:
		raise Exception(f"Unable to establish SSH connection: {ssh_ex}")
	except Exception as e:
		raise Exception(f"An error occurred: {e}")

def flipped_interaction_5__connect(user, host, password, timeout=20):
	try:
		child = pexpect.spawn(f'ssh {user}@{host}')
		ret = child.expect(['Are you sure you want to continue connecting', 'password:', pexpect.EOF], timeout=timeout)
		if ret == 0:
			child.sendline('yes')
			child.expect('password:', timeout=timeout)
		child.sendline(password)
		prompt = f'.*{user}@{host}:.*'
		child.expect(prompt, timeout=timeout)
		print('Connected successfully via SSH')
		return child
	except pexpect.exceptions.TIMEOUT:
		child.close()
	except pexpect.exceptions.EOF:
		child.close()

def iterative_prompting_3__connect(user, host, password):
    if not isinstance(user, str) or not user.strip():
        raise ValueError('User must be a non-empty string')
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Host must be a non-empty string')
    if not isinstance(password, str):
        raise ValueError('Password must be a string')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        client.load_system_host_keys()
        client.connect(hostname=host, username=user, password=password, timeout=10)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        print('Authentication failed, please verify your credentials')
        #exit()
    except paramiko.SSHException as e:
        print(f'unable to establish SSH connection: {{e}}')
        #exit()
    except socket.timeout:
        print('Connection timed out')
        #exit()
    except Exception as e:
        print(f'An unexpected error occurred: {{e}}')
        #exit()

def iterative_prompting_4__connect(user, host, password):
    if not all(isinstance(i, str) for i in (user, host, password)):
        #exit()
        raise
    if not all(i.strip() for i in (user, host, password)):
        #exit()
        raise
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        client.connect(host, username=user, password=password, timeout=10)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        #exit()
        raise
    except socket.timeout as ste:
        #exit()
        raise
    except socket.error as se:
        #exit()
        raise
    except paramiko.SSHException as sse:
        #exit()
        raise
    except Exception as e:
        #exit()
        raise

def iterative_prompting_5__connect(user, host, password):
    if not isinstance(user, str) or not isinstance(host, str) or not isinstance(password, str):
        raise ValueError('User, host, and password must be strings.')
    if not user or not host or not password:
        raise ValueError('User, host, and password cannot be empty.')
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, timeout=10)
        client.close()
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        #exit(1)
        raise
    except paramiko.BadHostKeyException as e:
        print(f'Unable to verify server\'s host key: {e}')
        #exit(1)    
    except paramiko.SSHException as e:        
        print(f'SSH connection failed: {e}')       
        #exit(1)
    except Exception as e:
    	print(f'An unexpected error occurred: {e}')
    	#exit(1)

def few_shots_prompting__connect(user, host, password):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(hostname=host, username=user, password=password)
		client.close()
		print('Connected successfully via SSH')
	except paramiko.AuthenticationException:
		raise('Authentication failed, please verify your credentials')
	except paramiko.SSHException as ssh_ex:
		raise('Unable to establish SSH connection: {}'.format(ssh_ex))

def cot_prompting__connect(user, host, password):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(host, username=user, password=password)
		print('Connected successfully via SSH')
	except paramiko.AuthenticationException:
		print('Authentication failed, please verify your credentials')
		pass
	except Exception as e:
		print(f'Unable to establish SSH connection: {e}')
		pass
	else:
		client.close()

def fact_check_list__connect(user, host, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print(f"Successfully connected to {host} as {user}")
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
        #exit(1)
    except paramiko.SSHException as ssh_ex:
        print(f"Unable to establish SSH connection: {ssh_ex}")
        #exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        #exit(1)
    finally:
        if client.get_transport() and client.get_transport().is_active():
            client.close()

def not_interactive_mix__connect(user, host, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, timeout=10)
        client.close()
        print('Connected successfully via SSH')
        return True
    except paramiko.AuthenticationException:
        return False
    except paramiko.SSHException:
        return False
    except paramiko.BadHostKeyException:
        return False
    except Exception:
        return False

def interactive_mix__connect_ssh(host, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, timeout=10)
        print("Successfully connected to the host.")
        return client
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.SSHException as ssh_ex:
        print(f"Unable to establish SSH connection: {ssh_ex}")
    except socket.timeout:
        print("Connection timed out. Please check the target host availability.")
    except socket.error as sock_err:
        print(f"Socket error: {sock_err}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        client.close()

def baseline__connect(user, host, password):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(hostname=host, username=user, password=password)
		print('Connected successfully via SSH')
	except paramiko.AuthenticationException:
		#exit(1)
		raise
	except Exception as e:
		#exit(1)
		raise
