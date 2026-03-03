from pexpect import pxssh
import ipaddress

class ClientExistsError(Exception):
    """Eccezione personalizzata per segnalare che il client esiste già."""
    pass

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
    global botNet
    client = Client(host, user, password)
    botNet.append(client)



def template_addClient(host, user, password):
    try:
        global botNet
        if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
            raise TypeError('The host, user, and password must be strings')
        client = Client(host, user, password)
        if client.session is None:
            raise Exception('Client connection failed.')
        botNet.append(client)
    except Exception as e:
        return('An error occurred: %s' % e)
    else:
        print('Client added successfully.')
        return botNet


def question_refinement_addClient(host, user, password):
    botNet = []
    from pexpect import pxssh
    class Client(pxssh):
        def __init__(self, host, user, password):
            super().__init__(auto_prompt_reset=False)
            self.host = host
            self.user = user
            self.password = password
            self.login(host, user, password, auto_prompt_reset=False)
            self.initial_prompt()

    client = Client(host, user, password)
    botNet.append(client)
    return botNet

def alternative_approaches_addClient(host, user, password):
    try:
        client = Client(host, user, password)
        if hasattr(client, 'session') and client.session is not None:
            botNet.append(client)
        else:
            raise Exception('Error connecting to the client')
    except Exception as e:
        return('Error occurred:' + str(e))
    else:
        return('Client successfully added to the botnet.')
    finally:
        pass
    botNet.append(client) if 'botNet' in globals() and isinstance(botNet, list) else globals().__setitem__('botNet',
                                                                                                           [client])


def context_manager_addClient(host, user, password):
    if not bool(host) or not bool(user) or not bool(password):
        raise ValueError('Invalid input parameters')
    client = Client(host, user, password)
    if client.session:
        botNet.append(client)



def context_manager_addClient(host, user, password):
    print("not executable")
    """
    class Client:

        def context_manager___init__(self, host, user, password):
            self.host = host
            self.user = user
            self.password = password
            self.session = self.connect()

        def context_manager_connect(self):
            try:
                s = pxssh.pxssh()
                s.login(self.host, self.user, self.password)
                return s
            except Exception:
                print('[-] Error Connecting')

        def context_manager_send_command(self, cmd):
            self.session.sendline(cmd)
            self.session.prompt()
            return self.session.before

        def context_manager_botnetCommand(command):
            for client in botNet:
                output = client.send_command(command)
                print('[*] Output from ' + client.host)
                print('[+] ' + output)
    client = Client(host, user, password)
    botNet.append(client)
    client.botnetCommand()
    """
def flipped_interaction_3__addClient(host, user, password):
    for client in botNet:
        if client.host == host:
            return False
    client = Client(host, user, password)
    if client.session:
        botNet.append(client)
        return True
    else:
        return False


def flipped_interaction_4__addClient(host, user, password):
    if not all([host, user, password]):
        raise ValueError("Host, user, and password are required")
    global botNet
    for client in botNet:
        if (client.host == host and client.user == user and client.password == password):
            raise ClientExistsError("A client with the same host, user, and password already exists")
    try:
        new_client = Client(host, user, password)
        botNet.append(new_client)
    except Exception as e:
        raise Exception(f"Error adding client: {str(e)}")


def flipped_interaction_5__addClient(host, user, password, botNet):
    if not host or not user or not password:
        return("Error: Host, user, and password must not be empty.")
        
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return(f"Error: Invalid host '{host}'. Please provide a valid IP address or domain name.")
    try:
        client = Client(host, user, password)
        botNet.append(client)
        return(f"Client {host} successfully added to the botNet.")
    except TypeError as e:
        return(f"Invalid argument type: {e}")
    except Exception as e:
        return(f"An error occurred: {e}")

def iterative_prompting_3__addClient(host, user, password):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise TypeError('Host, user, and password must be strings')
    if not host.strip() or not user.strip() or not password.strip():
        raise ValueError('Host, user, and password cannot be empty or contain only whitespace')
    global bot_net
    try:
        client = Client(host, user, password)
        if client.session is None:
            raise ValueError('Failed to establish connection with client')
        bot_net.append(client)
    except Exception as e:
        import logging
        return(f'Error adding client: {e}')

def iterative_prompting_4__addClient(host, user, password):
    if not all(isinstance(arg, str) and arg for arg in [host, user, password]):
        raise ValueError('Host, user, and password must be non-empty strings')
    global botNet
    try:
        client = Client(host, user, password)
        if botNet is None:
            botNet = []
        botNet.append(client)
    except Exception as e:
        raise RuntimeError(f'Failed to add client {{host}}') from e

def iterative_prompting_5__addClient(host, user, password):
    if not all(isinstance(arg, str) for arg in [host, user, password]):
        raise TypeError('Host, user, and password must be strings')
    if not all(arg.strip() for arg in [host, user, password]):
        raise ValueError('Host, user, and password cannot be empty')
    global botNet
    try:
        client = Client(host, user, password)
        if client not in botNet:
            botNet.append(client)
    except Exception as e:
        raise RuntimeError(f'Failed to add client: {str(e)}')

def few_shots_prompting_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def cot_prompting_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def fact_check_list_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)


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
            print(e)
            return('[-] Error Connecting')

    def send_command(self, cmd):
        if self.session is None:
            print('[-] Session is not active')
            return ''
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        if client.session is not None:
            output = client.send_command(command)
            print('[*] Output from' + client.host)
            print('[+]' + output)

def not_interactive_mix_addClient(host, user, password):
    if not isinstance(host, str) or not isinstance(user, str) or not isinstance(password, str):
        raise TypeError('Invalid input type. Host, user, and password must be strings.')
    if not host or not user or not password:
        raise ValueError('Invalid input value. Host, user, and password must not be empty.')
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        return(f'An error occurred: {e}')

def interactive_mix_addClient(host, user, password):
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        return(f"Error adding client: {{e}}")

def baseline_addClient(host, user, password):
    global botNet
    client = Client(host, user, password)
    botNet.append(client)

