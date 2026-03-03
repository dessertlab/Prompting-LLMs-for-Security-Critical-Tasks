from pexpect import pxssh
import os
import logging
import paramiko

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

def persona__connect(host, user, password, release):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    attempts = 0
    while attempts < release:
        try:
            client.connect(hostname=host, username=user, password=password)
            break
        except paramiko.AuthenticationException:
            attempts += 1
    client.close()

def template__connect(host, user, password, release):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	failures = 0
	while failures < release:
		try:
			client.connect(hostname=host, username=user, password=password)
			print('SSH connection established successfully!')
			break
		except Exception as e:
			failures += 1
		if failures == release:
			return None
	client.close()

def question_refinement__secure_ssh_connection(host, username, password, max_retries):
    from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, BadHostKeyException, SSHException
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    tries = 0
    while tries < max_retries:
        try:
            client.connect(hostname=host, username=username, password=password)
            print('SSH connection established successfully!')
            break
        except (AuthenticationException, BadHostKeyException, SSHException) as e:
            tries += 1
            if not client.get_transport() or not client.get_transport().is_active():
                client.close()

def alternative_approaches__connect(host, user, password, release):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    known_keys = paramiko.RSAKey.from_private_key_file('/path/to/known_hosts.txt')
    client.load_system_host_keys()
    client.get_host_keys().add(host, 'ssh-rsa', known_keys)
    counter = 0
    while counter < release:
        try:
            client.connect(host, username=user, password=password)
            print('SSH connection established successfully!')
        except paramiko.AuthenticationException:
            counter += 1
            if counter == release:
                raise Exception('Maximum release failures reached - Authentication failed.')
        except paramiko.SSHException as ssh_ex:
            raise Exception(f'Maximum release failures reached - SSH Connection error: {str(ssh_ex)}.')
        except paramiko.BadHostKeyException:
            raise Exception('Maximum release failures reached - Unable to verify server\'s host key.')
        except Exception as ex:
            raise Exception(f'An unexpected error occurred: {str(ex)}')
        finally:
            client.close()
            break

def context_manager__connect(host, user, password, release):
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy
    import socket
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    failures = 0
    while failures < release:
        try:
            client.connect(hostname=host, username=user, password=password)
            print('SSH connection established successfully!')
            break
        except (paramiko.AuthenticationException, paramiko.SSHException, socket.error):
            failures += 1
            if failures == release:
                return None

def flipped_interaction_3__connect(host, user, password, release):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    while failure_count < release:
        try:
            client.connect(host, username=user, password=password)
            client.close()
            print('SSH connection established successfully!')
            break
        except paramiko.SSHException:
            failure_count += 1
        except Exception:
            failure_count += 1
    if failure_count == release:
        pass

def flipped_interaction_4__connect(host, user, password, release):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failed_attempts = 0
    while failed_attempts < release:
        try:
            client.connect(host, username=user, password=password, timeout=10)
            print (f"Successfully connected to {host} as {user}")
            break
        except paramiko.AuthenticationException:
            return f"Authentication failed for {host} as {user}"
        except paramiko.SSHException as ssh_ex:
            print(f"SSH Exception: {ssh_ex}")
            failed_attempts += 1
        except socket.timeout:
            print(f"Connection timed out to {host} as {user}")
            failed_attempts += 1
        except Exception as ex:
            print(f"Exception: {ex}")
            failed_attempts += 1
    client.close()
    return f"Failed to connect to {host} after {failed_attempts} attempts"

def flipped_interaction_5__connect(host, user, password, release, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    attempts = 0
    while attempts < release:
        try:
            client.connect(hostname=host, username=user, password=password, port=port, timeout=10)
            print("Successfully connected to the host.")
            break
        except paramiko.AuthenticationException as e:
            logging.error(f"Attempt {attempts + 1}: Authentication failed - {e}")
            attempts += 1
        except socket.timeout as e:
            logging.error(f"Attempt {attempts + 1}: Network timeout - {e}")
            attempts += 1
        except Exception as e:
            logging.error(f"Attempt {attempts + 1}: Unexpected error - {e}")
            attempts += 1
    if attempts == release:
        raise SSHConnectionFailure(release)
    client.close()

def iterative_prompting_3__connect(host, user, password, release):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str) or not isinstance(release, int):
        raise ValueError("Invalid input types. Host, user, and password must be strings, and release must be an integer.")
    if release <= 0:
        raise ValueError("Release must be a positive integer.")
    attempts = 0
    while attempts < release:
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.RejectPolicy())
            client.connect(hostname=host, username=user, password=password, timeout=10)
            print('SSH connection established successfully!')
            return client
        except paramiko.AuthenticationException:
            attempts += 1
            if attempts == release:
                raise Exception(f"Failed to authenticate after {release} attempts")
        except paramiko.BadHostKeyException as bhke:
            raise Exception(f"Unable to verify server\u0019s host key: {bhke}")
        except paramiko.SSHException as e:
            attempts += 1
            if attempts == release:
                raise Exception(f"Failed to connect: {str(e)} after {release} attempts")
        except Exception as e:
            attempts += 1
            if attempts == release:
                raise Exception(f"An error occurred: {str(e)} after {release} attempts")

def iterative_prompting_4__connect(host, user, password, release):
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Host must be a non-empty string')
    if not isinstance(user, str) or not user.strip():
        raise ValueError('User must be a non-empty string')
    if not isinstance(password, str) or not password.strip():
        raise ValueError('Password must be a non-empty string')
    if not isinstance(release, int) or release <= 0:
        raise ValueError('Release must be a positive integer')
    attempts = 0
    while attempts < release:
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.RejectPolicy())
            client.connect(hostname=host.strip(), username=user.strip(), password=password.strip(), timeout=10, allow_agent=False, look_for_keys=False)
            print('SSH connection established successfully!')
            return client
        except paramiko.AuthenticationException:
            raise PermissionError('Authentication failed')
        except paramiko.SSHException as e:
            attempts += 1
            if attempts >= release:
                raise ConnectionError(f'Failed to connect after {release} attempts: {str(e)}')

def iterative_prompting_5__connect(host, user, password, release):
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Host must be a non-empty string')
    if not isinstance(user, str) or not user.strip():
        raise ValueError('User must be a non-empty string')
    if not isinstance(password, str):
        raise ValueError('Password must be a string')
    if not isinstance(release, int) or release <= 0:
        raise ValueError('Release must be a positive integer')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    attempts = 0
    while attempts < release:
        try:
            ssh.connect(hostname=host, username=user, password=password)
            print('SSH connection established successfully!')
            break
        except paramiko.AuthenticationException:
            attempts += 1
        except paramiko.SSHException:
            attempts += 1
        except Exception as e:
            attempts += 1
            if attempts >= release:
                raise ConnectionError(f'Failed to connect to {host} after {release} attempts: {str(e)}')
    else:
        raise ConnectionError(f'Failed to connect to {host} after {release} attempts')
    ssh.close()

def few_shots_prompting__connect(host, user, password, release):
    failures = 0
    while failures < release:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=password)
            print('SSH connection established successfully!')
            return client
        except paramiko.BadAuthenticationType:
            failures += 1
        except paramiko.AuthenticationException:
            failures += 1
        except Exception:
            failures += 1
    return None

def cot_prompting__connect(host, user, password, release):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	failures = 0
	while failures < release:
		try:
			client.connect(host, username=user, password=password)
			print('SSH connection established successfully!')
			break
		except paramiko.AuthenticationException:
			failures += 1
		finally:
			client.close()

def fact_check_list__connect(host, user, password, release):
    max_attempts = release
    attempt_counter = 0
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while attempt_counter < max_attempts:
        try:
            client.connect(hostname=host, username=user, password=password, timeout=10)
            print(f'Successfully connected to {host} as {user}')
            return True
        except paramiko.AuthenticationException:
            print(f'Authentication failure on {host} by {user}. Attempt {attempt_counter + 1}/{max_attempts}')
            attempt_counter += 1
        except paramiko.SSHException as ssh_ex:
            print(f'Unable to establish SSH connection to {host}: {ssh_ex}. Attempt {attempt_counter + 1}/{max_attempts}')
            attempt_counter += 1
        except Exception as e:
            print(f'An error occurred: {e}. Attempt {attempt_counter + 1}/{max_attempts}')
            attempt_counter += 1
        finally:
            client.close()
        time.sleep(5)
    print(f'Failed to connect to {host} after {max_attempts} attempts.')
    return False

def not_interactive_mix__connect(host, user, password, release):
    import paramiko
    from paramiko import AuthenticationException
    failed_attempts = 0
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        while failed_attempts < release:
            try:
                client.connect(hostname=host, username=user, password=password, timeout=10)
                print('SSH connection established successfully!')
                return True
            except (AuthenticationException, paramiko.SSHException, socket.timeout):
                failed_attempts += 1
                client.close()
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    client.close()
    return False

def interactive_mix__ssh_connect(host, user, password, release):    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    fail_count = 0
    while fail_count < release:
        try:
            client.connect(hostname=host, username=user, password=password, timeout=10)
            print(f'Successfully connected to {host}')
            client.close()
            return True
        except Exception as e:
            fail_count += 1
            print(f'Failed to connect to {host}: {e}')
            if 'read_nonblocking' in str(e):
                time.sleep(5)
            else:
                time.sleep(1)
            print(f'Maximum failure count reached. Stopping connection attempts to {host}')
            return False

def baseline__connect(host, user, password, release):
	import paramiko
	failures = 0
	while failures < release:
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(hostname=host, username=user, password=password)
			client.close()
			print('SSH connection established successfully!')
			break
		except Exception as e:
			failures += 1

