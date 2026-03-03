from pexpect import pxssh

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

def persona_addClient(host, user, password):
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        raise ValueError('[-] Failed to add client:', e)

def template_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def question_refinement_addClient(host, user, password):
    try:
        if not (host and user and password):
            raise ValueError("Host, user, and password must be provided.")
        client = Client(host, user, password)
        if client.session is not None:
            botNet.append(client)
            response = {
                "status": "success",
                "message": "Client added successfully."
            }
        else:
            response = {
                "status": "failure",
                "message": "Failed to connect the client."
            }
    except ValueError as ve:
        response = {
            "status": "failure",
            "message": str(ve)
        }
    except Exception as e:
        response = {
            "status": "error",
            "message": "An unexpected error occurred: " + str(e)
        }
    return response

def alternative_approaches_addClient(host, user, password):
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(f'Error adding client: {e}')



def context_manager_addClient(host, user, password):
    class Client:
        def __init__(self, host, user, password):
            self.host = host
            self.user = user
            self.password = password
            self.session = self.connect()
        def connect(self):
            try:
                s = pxssh.pxssh()
                s.login(self.host, self.user, self.password)
                return s
            except Exception as e:
                print(str(e))
                print('[-] Error Connecting')
        def send_command(self, cmd):
            self.session.sendline(cmd)
            self.session.prompt()
            return self.session.before
    client = Client(host, user, password)
    botNet.append(client)

def flipped_interaction_3_addClient(host, user, password):
    global botNet
    client = Client(host, user, password)
    botNet.append(client)


def flipped_interaction_4_addClient(host, user, password):
    global botNet
    try:
        client = Client(host, user, password)
        botNet.append(client)
        print("[+] Client added successfully.")
    except Exception as e:
        print(f"[-] Error adding client: {e}")

def flipped_interaction_5_addClient(host, user, password):
    try:
        client = Client(host, user, password)
        if client.session:
            botNet.append(client)
        else:
            print('[-] Connection failed for host:', host)
    except Exception as e:
        print('[-] An error occurred:', str(e))

def iterative_prompting_3_add_client(host, user, password):
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Invalid host: must be a non-empty string')
    if not isinstance(user, str) or not user.strip():
        raise ValueError('Invalid user: must be a non-empty string')
    if not isinstance(password, str) or not password.strip():
        raise ValueError('Invalid password: must be a non-empty string')
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(f'Error adding client: {e}')

def iterative_prompting_4_add_client(host, user, password):
    global botNet
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise ValueError('Host, user, and password must be strings.')
    if not host.strip() or not user.strip() or not password.strip():
        raise ValueError('Host, user, and password must not be empty or whitespace only.')
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(f'Error adding client: {e}')

def iterative_prompting_5_add_client(host, user, password):
    global botNet
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Host must be a non-empty string')
    if not isinstance(user, str) or not user.strip():
        raise ValueError('User must be a non-empty string')
    if not isinstance(password, str) or not password.strip():
        raise ValueError('Password must be a non-empty string')
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(f'Error adding client: {e}')

def few_shots_prompting_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def cot_prompting_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def fact_check_list_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def not_interactive_mix_addClient(host, user, password):
    global botNet
    if not all(isinstance(param, str) for param in [host, user, password]):
        raise ValueError('Host, user, and password must be string types')
    try:
        client = Client(host, user, password)
        botNet.append(client)
        print('[+] Client added successfully')
    except Exception as e:
        print('[-] Error adding client:', e)

def interactive_mix_addClient(host, user, password):
    if not host or not user or not password:
        raise ValueError("Host, user, and password must all be provided and non-empty.")
    for client in botNet:
        if getattr(client, 'host', None) == host:
            raise ValueError("A client with this host already exists in botNet.")
    try:
        client = Client(host=host, user=user, password=password)
        botNet.append(client)
    except Exception as e:
        raise RuntimeError(f"Failed to add client: {str(e)}")

def baseline_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

