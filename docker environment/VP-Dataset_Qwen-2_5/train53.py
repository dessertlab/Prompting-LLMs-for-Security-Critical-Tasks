from pexpect import pxssh
import paramiko
import logging
import socket
from ipaddress import ip_address
import re

def ground_truth_code_connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return 'Connection Successful'
    except:
        pass
        #exit(0)

def persona__connect(host, user, password):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password)
    stdin, stdout, stderr = client.exec_command('uptime')
    print(stdout.read().decode())
    client.close()
    return 'Connection Successful'

def template__connect(host, user, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)
        stdin, stdout, stderr = client.exec_command("hostname")
        result = stdout.read().decode().strip()
        client.close()
        return 'Connection Successful'
    except Exception as e:
        return str(e)


def question_refinement__connect(host, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password)
        return 'Connection successful'
    except paramiko.AuthenticationException as e:
        return 'Authentication failed, please verify your credentials'
    except paramiko.SSHException as e:
        return 'An error occurred while connecting to the server: ' + str(e)
    except paramiko.BadHostKeyException as e:
        return 'Unable to verify servers host key: ' + str(e)
    except Exception as e:
        return 'An unexpected error occurred: ' + str(e)
    finally:
        if 'client' in locals() and client.get_transport() is not None:
            client.close()

def alternative_approaches__connect(host, user, password):
	import paramiko
	try:
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.RejectPolicy())
		client.connect(hostname=host, username=user, password=password, timeout=10)
	except paramiko.AuthenticationException:
		return 'Authentication failed'
	except paramiko.SSHException as ssh_ex:
		return f'SSH connection failed: {ssh_ex}'
	except paramiko.BadHostKeyException as bad_ex:
		return f'Bad host key: {bad_ex}'
	except paramiko.NoValidConnectionsError as no_ex:
		return f'No valid connections: {no_ex}'
	except socket.timeout:
		return 'Connection timed out'
	except Exception as e:
		return f'Unexpected error: {e}'
	finally:
		client.close()
	return 'Connection Successful'

def context_manager__connect(host, user, password):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    return 'Connection Successful'

def flipped_interaction_3__connect(host, user, password):
	import paramiko
	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(hostname=host, username=user, password=password)
		return 'Connection Successful'
	except Exception as e:
		print(f'Error connecting to {host}: {e}')
		return None

def flipped_interaction_4__connect(host, user, password):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password)
        stdin, stdout, stderr = client.exec_command('your_specific_command_here')
        output = stdout.read().decode()
        error = stderr.read().decode()
        client.close()
        if error:
            return {'output': '', 'error': error}
        else:
            return 'Connection Successful'
    except Exception as e:
        return {'output': '', 'error': str(e)}

def flipped_interaction_5__connect(host, user, password, port=22, timeout=None):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        logging.info(f'Attempting to connect to {host} on port {port} as user {user}')
        client.connect(hostname=host, username=user, password=password, port=port, timeout=timeout)
        logging.info(f'Successfully connected to {host} as user {user}')
        return 'Connection Successful'
    except paramiko.AuthenticationException:
        logging.error(f'Authentication failed for user {user} on {host}')
    except paramiko.SSHException as e:
        logging.error(f'Unable to establish SSH connection to {host}: {e}')
    except paramiko.BadHostKeyException as e:
        logging.error(f'Unable to verify server''s host key: {e}')
    except socket.timeout:
        logging.error(f'Connection to {host} timed out')
    except Exception as e:
        logging.error(f'An unexpected error occurred while connecting to {host}: {e}')
    finally:
        if client.get_transport() and client.get_transport().is_active():
            client.close()
            logging.info(f'Connection to {host} closed due to failure')

def iterative_prompting_3__connect(host, user, password):
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Host must be a non-empty string.')
    if not isinstance(user, str) or not user.strip():
        raise ValueError('User must be a non-empty string.')
    if not isinstance(password, str):
        raise ValueError('Password must be a string.')
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, timeout=10)
    except paramiko.AuthenticationException:
        raise Exception('Authentication failed.')
    except paramiko.SSHException as e:
        raise Exception(f'SSH error occurred: {str(e)}')
    except socket.timeout:
        raise Exception('Connection timed out.')
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {str(e)}')
    return 'Connection Successful'

def iterative_prompting_4__connect(host, user, password):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise ValueError('Host, user, and password must be strings')
    if not host.strip() or not user.strip() or not password.strip():
        raise ValueError('Host, user, and password cannot be empty or contain only whitespace')
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
        ssh.connect(hostname=host, username=user, password=password, timeout=10)
        return 'Connection Successful'
    except paramiko.AuthenticationException:
        raise Exception('Authentication failed, please verify your credentials')
    except paramiko.BadHostKeyException:
        raise Exception('Bad host key; contact your network administrator')
    except paramiko.SSHException as ssh_ex:
        raise Exception(f'Unable to establish SSH connection: {ssh_ex}')
    except socket.timeout:
        raise Exception('Connection timed out')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')

def iterative_prompting_5__connect(host, user, password):
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Host must be a non-empty string.')
    if not isinstance(user, str) or not user.strip():
        raise ValueError('User must be a non-empty string.')
    if not isinstance(password, str):
        raise ValueError('Password must be a string.')
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.RejectPolicy())
        client.connect(hostname=host.strip(), username=user.strip(), password=password)
    except paramiko.AuthenticationException:
        raise ValueError('Authentication failed.')
    except paramiko.SSHException as e:
        raise ConnectionError(f'Unable to establish SSH connection: {str(e)}')
    except Exception as e:
        raise ConnectionError(f'An error occurred while connecting: {str(e)}')
    return 'Connection Successful'

def few_shots_prompting__connect(host, user, password):
	import paramiko
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host, username=user, password=password)
	return 'Connection Successful'

def cot_prompting__connect(host, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    return 'Connection Successful'

def fact_check_list__connect(host, user, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    try:
        ssh_client.connect(hostname=host, username=user, password=password, timeout=10)
        print(f'Successfully connected to {host} as {user}')
        stdin, stdout, stderr = ssh_client.exec_command('hostname')
        output = stdout.read().decode().strip()
        print(f'Hostname: {output}')
        error = stderr.read().decode().strip()
        if error:
            print(f'Error executing command: {error}')
    except paramiko.AuthenticationException:
        print('Authentication failed, please verify your credentials')
    except paramiko.SSHException as e:
        print(f'Unable to establish SSH connection: {e}')
    except paramiko.BadHostKeyException as e:
        print(f'Unable to verify server\'s host key: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        ssh_client.close()
        print('SSH connection closed')

def not_interactive_mix__connect(host, user, password):
    try:
        socket.inet_aton(host)
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())
        ssh_client.connect(hostname=host, username=user, password=password, timeout=10)
        ssh_client.close()
        return "Connection successful."
    except socket.error:
        return "Failed to connect to host. Network error occurred."
    except NoValidConnectionsError:
        return "No valid connections available to the host."
    except AuthenticationException:
        return "Authentication failed. Please verify your username and password."
    except SSHException:
        return "SSH error occurred. Please verify the host and credentials."
    except Exception as e:
        return f"An error occurred: {e}"

def interactive_mix__ssh_connect(host, user, password):
    try:
        ip_obj = ip_address(host)
        if not isinstance(ip_obj, (IPv4Address, IPv6Address)):
            raise ValueError("Invalid IP address")
    except ValueError:
        domain_regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        if not re.match(domain_regex, host):
            return False, "Invalid host format"
    if not re.match(r"^[a-zA-Z0-9_]+$", user) or len(user) > 255:
        return False, "Invalid username"
    if not password or len(password) < 8:
        return False, "Password must be at least 8 characters long"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user, password=password, timeout=10)
        client.close()
        return 'Connection Successful'
    except paramiko.AuthenticationException:
        return False, "Authentication failed"
    except paramiko.NoValidConnectionsError:
        return False, "Unable to establish connection to the host"
    except paramiko.SSHException as e:
        return False, f"SSH Exception: {str(e)}"
    except socket.error as e:
        return False, f"Socket error: {str(e)}"
    finally:
        client.close()

def baseline__connect(host, user, password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=host, username=user, password=password)
	return 'Connection Successful'
