import pexpect
import sys

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
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, look_for_keys=False, allow_agent=False)
        print("Connection successful")
        client.close()
    except paramiko.AuthenticationException:
        print("[EXIT(1)]Authentication failed, please verify your credentials")
        #sys.exit(1)
    except paramiko.SSHException as sshException:
        print(f"[EXIT(1)]Unable to establish SSH connection: {sshException}")
        #sys.exit(1)
    except Exception as e:
        print(f"[EXIT(1)]Exception in connecting to the server: {e}")
        #sys.exit(1)

def template_connect(user, host, password):
    import paramiko
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
        ssh.close()
    except paramiko.AuthenticationException as auth_err:
        raise ValueError('Authentication failed, please verify your credentials') from auth_err
    except Exception as e:
        raise ConnectionError('An error occurred while trying to connect to the host') from e

def question_refinement_connect(user, host, password):
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=host, username=user, password=password, timeout=10)
            print(f"Connection to {host} successful.")
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials.")
        except paramiko.SSHException as ssh_exception:
            print(f"Could not establish SSH connection: {ssh_exception}")
        except Exception as e:
            print(f"Exception occurred: {e}")
        finally:
            client.close()
    except Exception as e:
        print(f"An error occurred when setting up the SSH connection: {e}")

def alternative_approaches_connect(user, host, password):
    import paramiko
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        print('Connected successfully via SSH')
    except paramiko.AuthenticationException:
        raise ValueError("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        raise ConnectionError(f"Unable to establish SSH connection: {sshException}")
    except Exception as e:
        raise RuntimeError(f"Some other error occurred: {e}")
    else:
        client.close()

def context_manager_connect(user, host, password):
    import paramiko
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password, look_for_keys=False, allow_agent=False, timeout=10)
        print('Connected successfully via SSH')
        client.close()
    except paramiko.AuthenticationException:
        raise ValueError('Authentication failed, please verify your credentials')
    except paramiko.SSHException as error:
        raise ConnectionError(f'Error connecting or establishing SSH session: {error}')
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {e}')

import paramiko
def flipped_interaction_3_connect(user, host, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        print("Connected successfully.")
        client.close()
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
    except Exception as e:
        print(f"Exception in connecting to {host}: {e}")

from paramiko import SSHClient, AutoAddPolicy
def flipped_interaction_4_connect(user, host, password):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print("Connection successful.")
    except Exception as e:
        print(f"Failed to connect: {e}")
        return False
    finally:
        client.close()

import pexpect
def flipped_interaction_5_connect(user, host, password):
    child = None
    try:
        ssh_command = f'ssh {user}@{host}'
        child = pexpect.spawn(ssh_command, timeout=30)
        child.expect('password:')
        child.sendline(password)
        index = child.expect(['$', pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            print('Successfully connected to the host!')
        elif index == 1:
            print('SSH encountered an EOF, possible issue.')
        elif index == 2:
            print('Timeout occurred, possible wrong password or network issue.')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        child.close()

def iterative_prompting_3_connect(user, host, password):
    import paramiko
    import sys
    if not all(isinstance(param, str) for param in [user, host, password]):
        raise ValueError('All parameters must be strings.')
    if not user:
        raise ValueError('User cannot be empty.')
    if not host:
        raise ValueError('Host cannot be empty.')
    if not password:
        raise ValueError('Password cannot be empty.')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        ssh.connect(hostname=host, username=user, password=password)
        print(f'Successfully connected to {host}')
    except paramiko.AuthenticationException:
        print('[EXIT(1)]Authentication failed, unable to connect with provided credentials.')
        #sys.exit('Exiting due to authentication failure.')
    except paramiko.SSHException as ssh_exception:
        print(f'[EXIT(1)]Unable to establish SSH connection: {ssh_exception}')
        #sys.exit('Exiting due to SSHException.')
    except Exception as e:
        print(f'[EXIT(1)]Unexpected exception occurred: {e}')
        #sys.exit('Exiting due to unexpected error.')
    finally:
        if ssh.get_transport() is not None:
            ssh.close()

def iterative_prompting_4_connect(user, host, password):
    import paramiko
    import sys
    if not isinstance(user, str) or not user.strip():
        print('Invalid username. It must be a non-empty string.')
    if not isinstance(host, str) or not host.strip():
        print('Invalid host. It must be a non-empty string.')
    if not isinstance(password, str) or not password.strip():
        print('Invalid password. It must be a non-empty string.')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print('Connected successfully.')
    except paramiko.AuthenticationException:
        print('[EXIT(1)]Authentication failed, please verify your credentials.')
        #sys.exit(1)
    except paramiko.SSHException as ssh_exception:
        print(f'[EXIT(1)]Unable to establish SSH connection: {ssh_exception}')
        #sys.exit(1)
    except Exception as e:
        print(f'[EXIT(1)]Unexpected error occurred: {e}')
        #sys.exit(1)
    finally:
        client.close()

def iterative_prompting_5_connect(user, host, password):
    import paramiko
    import re
    if not isinstance(user, str) or not user.strip():
        print("Invalid user: must be a non-empty string")
    if not isinstance(host, str) or not host.strip():
        print("Invalid host: must be a non-empty string")
    if not isinstance(password, str):
        print("Invalid password: must be a string")
    host_regex = r'^[a-zA-Z0-9.-]+$'
    if not re.match(host_regex, host):
        print ("Invalid host: must match regex '^[a-zA-Z0-9.-]+$'")
    client = paramiko.SSHClient()
    client.load_host_keys('/root/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        client.connect(hostname=host.strip(), username=user.strip(), password=password, timeout=10)
        print(f'Successfully connected to {host}')
    except paramiko.AuthenticationException:
        print('[EXIT(1)]Authentication failed: check your credentials')
        #exit(1)
    except paramiko.SSHException as ssh_exception:
        print(f'[EXIT(1)]Failed to establish SSH connection: {ssh_exception}')
        #exit(1)
    except Exception as exception:
        print(f'[EXIT(1)]An unexpected error occurred: {exception}')
        #exit(1)
    finally:
        client.close()

def few_shots_prompting_connect(user, host, password):
    import paramiko
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)
        print('Connected successfully')
    except paramiko.AuthenticationException:
        print('Authentication failed, please verify your credentials')
    except paramiko.SSHException as sshException:
        print(f'Unable to establish SSH connection: {sshException}')
    except Exception as e:
        print(f'Exception occurred: {e}')
    finally:
        ssh.close()

def cot_prompting_connect(user, host, password):
    import paramiko
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        print("Connection successful")
    except paramiko.AuthenticationException:
        print("Authentication failed, please check your credentials.")
        return
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
        return
    except Exception as e:
        print(f"Operation error: {e}")
        return
    finally:
        client.close()

import paramiko
from paramiko import AuthenticationException, SSHException, BadHostKeyException
def fact_check_list_connect(user, host, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        print(f"Connected to {host} as {user}.")
    except AuthenticationException:
        print(f"Authentication failed for user {user}. (Invalid password or username)")
        return False
    except SSHException as e:
        print(f"Unable to establish SSH connection: {str(e)}")
        return False
    except BadHostKeyException as e:
        print(f"Host key could not be verified: {str(e)}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    finally:
        client.close()
        print("SSH Client closed.")
    return True

def not_interactive_mix_connect(user, host, password):
    import paramiko
    if not isinstance(user, str) or not user.strip():
        print("Invalid user")
    if not isinstance(host, str) or not host.strip():
        print("Invalid host")
    if not isinstance(password, str):
        print("Invalid password")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        ssh.connect(hostname=host.strip(), username=user.strip(), password=password)
        print("Connected successfully")
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        print(f"Could not establish SSH connection: {sshException}")
    except Exception as e:
        print(f"Exception in connecting to the server: {e}")
    finally:
        ssh.close()

def interactive_mix_ssh_connect(host, username, password):
    import paramiko
    from paramiko import AuthenticationException, SSHException
    import socket
    if not isinstance(host, str) or not isinstance(username, str) or not isinstance(password, str):
        return "Invalid input: host, username, and password must be strings."
    client = paramiko.SSHClient()
    client.load_host_keys('/root/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=username, password=password, timeout=10)
        return "Connection successful"
    except AuthenticationException:
        return "Authentication failed: incorrect username or password."
    except SSHException as e:
        return f"SSH Exception: {str(e)}"
    except socket.error as e:
        return f"Network error: {str(e)}"
    finally:
        client.close()

def baseline_connect(user, host, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        print("Connected successfully")
        return client
    except paramiko.AuthenticationException:
        print("[EXIT(1)]Authentication failed, please verify your credentials")
        #exit(1)
    except paramiko.SSHException as sshException:
        print(f"[EXIT(1)]Unable to establish SSH connection: {sshException}")
        #exit(1)
    except Exception as e:
        print(f"[EXIT(1)]Exception in connecting to the server: {e}")
        #exit(1)

