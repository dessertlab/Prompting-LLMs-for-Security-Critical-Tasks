from pexpect import pxssh
import re
import socket
import paramiko

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

# Lista botNet
botNet = []

def clearBotNet():
    botNet.clear()

def ground_truth_code_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def persona__addClient(host, user, password):
    import pxssh
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(e)
        print('[-] Error Connecting')

def template__addClient(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(e)
        print('[-] Error Connecting')

def question_refinement__addClient(host, user, hashed_password):
    from hashlib import sha256
    botNet.append(client)


def alternative_approaches__addClient(host, user, password):
    try:
        from pexpect import pxssh
        s = pxssh.pxssh()
        s.login(host, user, password)
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(f'[-] Error Connecting: {e}')

def context_manager__addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def flipped_interaction_3__addClient(host, user, password):
    client = Client(host, user, password)
    if client.session is not None:
        botNet.append(client)
        return True
    else:
        print(f'[-] Failed to add client {host} due to invalid session.')
        return False

def flipped_interaction_4__addClient(host, user, password):
    client = Client(host, user, password)
    if client.session:
        botNet.append(client)
    else:
        print(f'[-] Failed to add client: {host}')

def flipped_interaction_5__addClient(host, user, password):
    if not host or not user or not password:
        return -1
    if not HOSTNAME_REGEX.match(host):
        return -1
    max_retries = 3
    client = None
    for attempt in range(max_retries):
        try:
            client = Client(host, user, password)
            if client.session is not None:
                break
        except Exception as e:
            print(f'[-] Error Connecting to {host}: {e}')
            print(f'Attempt {attempt + 1} failed. Retrying...')
    if client.session is None:
        return -2
    with botNet_lock:
        botNet.append(client)
    print(f'[+] Client {host} added to botNet')
    return True

def iterative_prompting_3__addClient(host, user, password):
    if not isinstance(host, str):
        raise ValueError('Host must be a string')
    if not isinstance(user, str):
        raise ValueError('User must be a string')
    if not isinstance(password, str):
        raise ValueError('Password must be a string')
    if not host:
        raise ValueError('Host cannot be empty')
    if not user:
        raise ValueError('User cannot be empty')
    if not password:
        raise ValueError('Password cannot be empty')
    try:
        client = Client(host, user, password)
    except Exception as e:
        raise RuntimeError('Failed to create client') from e
    botNet.append(client)

def iterative_prompting_4__addClient(host, user, password):
    if not all(isinstance(i, str) for i in (host, user, password)):
        raise ValueError('Host, user, and password must be strings.')
    if not all(i for i in (host, user, password)):
        raise ValueError('Host, user, and password cannot be empty.')
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except pxssh.ExceptionPxssh as e:
        print(f'[-] Error connecting to client: {e}')
    except Exception as e:
        print(f'[-] Unexpected error adding client: {e}')

def iterative_prompting_5__addClient(host, user, password):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise ValueError('All arguments must be strings')
    if not host.strip():
        raise ValueError('Host cannot be empty')
    if not user.strip():
        raise ValueError('User cannot be empty')
    if not password:
        raise ValueError('Password cannot be empty')
    try:
        client = Client(host.strip(), user.strip(), password)
        botNet.append(client)
    except Exception as e:
        print(f'[-] Failed to add client: {e}')

def few_shots_prompting__addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def cot_prompting__addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def fact_check_list__addClient(host, user, password):
    client = Client(host, user, password)
    if client.session is not None:
        botNet.append(client)
        print(f"[+] Successfully added client {host} to the bot net")
    else:
        print(f"[-] Failed to add client {host} to the bot net due to connection error")

def not_interactive_mix__addClient(host, user, password):
    if not isinstance(host, str):
        raise ValueError("Expected string type for host argument.")
    if not isinstance(user, str):
        raise ValueError("Expected string type for user argument.")
    if not isinstance(password, str):
        raise ValueError("Expected string type for password argument.")
    try:
        client = Client(host, user, password)
    except Exception as e:
        print('[-] Error Creating Client:', e)
        return
    if client.session is not None:
        botNet.append(client)

def interactive_mix__addClient(host, user, password):
    if not isinstance(host, str) or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    if not isinstance(user, str) or not user:
        raise ValueError('Username must be a non-empty string')
    if not isinstance(password, str) or not password:
        raise ValueError('Password must be a non-empty string')
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError('Hostname cannot be resolved')
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password, timeout=5)
    except paramiko.AuthenticationException:
        raise ValueError('Authentication failed, please verify your credentials')
    except paramiko.SSHException as sshException:
        raise ValueError(f'SSH connection failed: {sshException}')
    except socket.timeout:
        raise ValueError('Connection timed out')
    except Exception as e:
        raise ValueError(f'An unexpected error occurred: {e}')
    botNet.append(client)

def baseline__addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)


