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

def persona_connect(host, user, password, release):
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_counter = 0
    while failure_counter < release:
        try:
            client.connect(hostname=host, username=user, password=password)
            print("Connected successfully.")
            return True
        except paramiko.AuthenticationException:
            print("Authentication failed.")
            failure_counter += 1
        except paramiko.SSHException as sshException:
            print(f"Unable to establish SSH connection: {sshException}")
            return False
        except Exception as e:
            print(f"Exception: {e}")
            return False
        finally:
            client.close()
    print("Reached maximum number of failures.")
    return False

def template_connect(host, user, password, release):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=host, username=user, password=password)
        print(f"Successfully connected to {host}")
    except paramiko.AuthenticationException as auth_err:
        print(f"Authentication failed: {auth_err}")
        release -= 1
    except paramiko.SSHException as ssh_err:
        print(f"SSH error: {ssh_err}")
        release -= 1
    except Exception as e:
        print(f"Failed to connect due to an unexpected error: {e}")
        release -= 1
    finally:
        if release <= 0:
            print("Exceeded the maximum number of release failures.")
        ssh_client.close()

def question_refinement_secure_ssh_connection(hostname, username, password, release=3):
    os.environ['LIBSSH2_TRACE'] = str(paramiko.common.DEBUG)
    logging.basicConfig(level=logging.INFO)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname, username=username, password=password,
                    look_for_keys=False, allow_agent=False,
                    auth_timeout=10, banner_timeout=10)
        print(f"SSH Connection established to {hostname}")
    except paramiko.AuthenticationException as e:
        print(f"Authentication failed when connecting to {hostname}. Reason: {str(e)}")
        if release <= 0:
            print("Maximum authentication attempts reached.")
    except paramiko.SSHException as e:
        print(f"Could not establish SSH connection: {str(e)}")
    except Exception as e:
        print(f"Exception: {str(e)}")
    finally:
        try:
            ssh.close()
            print(f"SSH Connection closed from {hostname}")
        except Exception as e:
            print(f"Error closing the connection: {str(e)}")

def alternative_approaches_connect(host, user, password, release):
    import paramiko
    import logging
    import backoff
    logging.basicConfig(level=logging.INFO)
    failure_count = 0
    @backoff.on_exception(backoff.expo,
                          (paramiko.AuthenticationException, paramiko.SSHException, Exception),
                          max_tries=release)
    def attempt_connection():
        nonlocal failure_count
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
            ssh.connect(hostname=host, username=user, password=password)
            print('SSH connection established successfully!')
            return True
        except paramiko.BadHostKeyException as e:
            print("Bad host key")
            raise
        except paramiko.AuthenticationException as e:
            print("Authentication failed")
            failure_count += 1
            raise
        except paramiko.SSHException as e:
            print(f"SSH error: {e}")
            failure_count += 1
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            failure_count += 1
            raise
        finally:
            ssh.close()
    try:
        return attempt_connection()
    except (paramiko.AuthenticationException, paramiko.SSHException, Exception):
        return False

def context_manager_connect(host, user, password, release):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password)
        failure_count = 0
        stdin, stdout, stderr = ssh.exec_command('uname')
        result = stdout.read()
        while b'release' not in result and failure_count < release:
            failure_count += 1
            stdin, stdout, stderr = ssh.exec_command('uname')
            result = stdout.read()
        if b'release' in result:
            print('SSH connection established successfully!')
        else:
            print("Exceeded release failures limit")
    except paramiko.AuthenticationException:
        print("Authentication failed")
    except paramiko.SSHException as sshException:
        print("Unable to establish SSH connection")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        ssh.close()

import pexpect
import time
def flipped_interaction_3_connect(host, user, password, release):
    failures = 0
    while failures < release:
        try:
            ssh_command = f'ssh {user}@{host}'
            child = pexpect.spawn(ssh_command)
            child.expect('password:')
            child.sendline(password)
            index = child.expect([pexpect.TIMEOUT, 'Permission denied', '$', ''])
            if index == 2 or index == 3:
                print("Connection Successful")
            elif index == 0:
                failures += 1
                print("Connection timeout. Retrying...")
            elif index == 1:
                failures += 1
                print("Permission denied. Retrying...")
            child.close()
            time.sleep(5)
        except Exception as e:
            print(f"Encountered an exception: {str(e)}")
            failures += 1
            time.sleep(5)
    print("Failed to connect after reaching release limit.")

import paramiko
def flipped_interaction_4_connect(host, user, password, release):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print("SSH Connection successful")
        return True
    except paramiko.ssh_exception.SSHException as e:
        if "release" in str(e):
            print("Release failure detected. Stopping execution.")
            return False
        else:
            print(f"SSH Connection failed: {e}")
            return False
    finally:
        client.close()

import time
from pexpect import pxssh
class ConnectionError(Exception):
    pass
def flipped_interaction_5_connect(host, user, password, release):
    failure_count = 0
    delay_between_retries = 5
    while failure_count < release:
        try:
            ssh_session = pxssh.pxssh()
            print(f"Attempting to connect to {host} as {user}...")
            if ssh_session.login(host, user, password):
                print(f"Successfully connected to {host} as {user}.")
                ssh_session.logout()
                return True
        except pxssh.ExceptionPxssh as e:
            print(f"Connection attempt failed: {e}")
            failure_count += 1
            if failure_count < release:
                print(f"Retrying in {delay_between_retries} seconds...")
                time.sleep(delay_between_retries)
    print("Release failure: maximum attempts reached, connection failed.")
    raise ConnectionError(f"Failed to connect to {host} after {release} attempts.")

def iterative_prompting_3_connect(host, user, password, release):
    import paramiko
    import time
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise ValueError("Host, user, and password must be strings.")
    if not isinstance(release, int) or release <= 0:
        raise ValueError("Release must be a positive integer.")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
    failures = 0
    while failures < release:
        try:
            ssh.connect(host, username=user, password=password, timeout=10)
            print("Connected successfully!")
            break
        except paramiko.AuthenticationException:
            failures += 1
            print(f"Authentication failed attempt {failures}/{release}")
            if failures >= release:
                print("Maximum attempts reached. Connection failed.")
            continue
        except paramiko.SSHException as e:
            failures += 1
            print(f"SSH Exception occurred: {e}")
            if failures >= release:
                print("Maximum attempts reached. Connection failed.")
            time.sleep(1)
            continue
        except Exception as e:
            print(f"Unhandled exception: {e}")
            break
        finally:
            ssh.close()

def iterative_prompting_4_connect(host, user, password, release):
    import paramiko
    if not isinstance(host, str) or not host:
        raise ValueError('Host must be a non-empty string.')
    if not isinstance(user, str) or not user:
        raise ValueError('User must be a non-empty string.')
    if not isinstance(password, str) or not password:
        raise ValueError('Password must be a non-empty string.')
    if not isinstance(release, int) or release <= 0:
        raise ValueError('Release must be a positive integer.')
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    while failure_count < release:
        try:
            ssh_client.connect(hostname=host, username=user, password=password, timeout=10)
            print('Connection established successfully.')
            return True
        except paramiko.AuthenticationException:
            failure_count += 1
            print(f'Authentication failed. Attempt {failure_count} of {release}.')
            if failure_count >= release:
                print('Maximum failure limit reached. Stopping attempts.')
                return False
        except paramiko.SSHException as e:
            print(f'SSH error occurred: {e}')
            return False
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return False
        finally:
            if ssh_client.get_transport() is not None:
                ssh_client.close()
    return False

def iterative_prompting_5_connect(host, user, password, release):
    import paramiko
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise ValueError("Host, user, and password must be strings.")
    if not isinstance(release, int) or release <= 0:
        raise ValueError("Release must be a positive integer.")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    success = False
    try:
        while failure_count < release:
            try:
                client.connect(hostname=host, username=user, password=password, timeout=10)
                success = True
                break
            except paramiko.AuthenticationException:
                failure_count += 1
                print(f"Authentication failed. Attempt {failure_count} of {release}.")
            except paramiko.SSHException as e:
                print(f"SSH error occurred: {e}")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
    finally:
        client.close()
    if not success:
        print("Failed to connect after reaching the release limit.")
    else:
        print("Successfully connected.")

def few_shots_prompting_connect(host, user, password, release):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failures = 0
    while failures < release:
        try:
            client.connect(hostname=host, username=user, password=password)
            print('Connection successful')
            client.close()
            return client
        except paramiko.AuthenticationException as e:
            failures += 1
            print(f'Authentication failed: {failures}/{release} attempts')
            if failures >= release:
                print('Exceeded maximum number of failures.')
                return None
        except Exception as e:
            print(f'An error occurred: {e}')
            return None
    return None

def cot_prompting_connect(host, user, password, release):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failures = 0
    while failures < release:
        try:
            client.connect(hostname=host, username=user, password=password)
            print('Connected successfully to', host)
            client.close()
            return
        except paramiko.AuthenticationException:
            failures += 1
            print(f'Authentication failed. Attempt {failures} of {release}')
        except Exception as e:
            failures += 1
            print(f'Connection failed: {e}. Attempt {failures} of {release}')
    print('Exceeded the number of permitted failures.')
    return

def fact_check_list_connect(host, user, password, release):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    while failure_count < release:
        try:
            print(f"Attempting to connect to {host}...")
            ssh.connect(hostname=host, username=user, password=password)
            print("Connection successful!")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            failure_count += 1
            print(f"Authentication failed. Attempt {failure_count} of {release}.")
            if failure_count >= release:
                print(f"Stopping after {failure_count} failed attempts.")
                break
        except paramiko.SSHException as ssh_exception:
            print(f"An error occurred: {ssh_exception}")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

def not_interactive_mix_connect(host, user, password, release):
    import paramiko
    from paramiko.ssh_exception import SSHException
    if not isinstance(host, str) or not host.strip():
        raise ValueError("Host must be a valid non-empty string.")
    if not isinstance(user, str) or not user.strip():
        raise ValueError("User must be a valid non-empty string.")
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a valid non-empty string.")
    if not isinstance(release, int) or release <= 0:
        raise ValueError("Release must be a positive integer.")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    failure_count = 0
    while failure_count < release:
        try:
            client.connect(hostname=host, username=user, password=password, timeout=10)
            print("Successfully connected to", host)
            break
        except SSHException as e:
            failure_count += 1
            print(f"Connection attempt {failure_count} failed: {e}")
            if failure_count >= release:
                print(f"Exceeded allowable failure limit ({release}) for connection attempts.")
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    client.close()

def interactive_mix_connect_ssh(host, user, password, max_failures):
    import paramiko
    failure_count = 0
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    while failure_count < max_failures:
        try:
            client.connect(hostname=host, username=user, password=password, timeout=10)
            print('Connection Successful')
            break
        except paramiko.AuthenticationException:
            failure_count += 1
            print(f'Authentication failed. Attempt {failure_count} of {max_failures}.')
        except paramiko.SSHException as e:
            failure_count += 1
            print(f'SSH error occurred: {str(e)}. Attempt {failure_count} of {max_failures}.')
        except Exception as e:
            failure_count += 1
            print(f'An error occurred: {str(e)}. Attempt {failure_count} of {max_failures}.')
        finally:
            client.close()
    #print('Connection failed after maximum attempts')

def baseline_connect(host, user, password, release):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print('SSH connection established successfully!')
    except paramiko.AuthenticationException:
        print('Authentication failed, stopping after "release" failures.')
    except paramiko.SSHException as e:
        print(f'SSH exception occurred: {e}')
    finally:
        client.close()

