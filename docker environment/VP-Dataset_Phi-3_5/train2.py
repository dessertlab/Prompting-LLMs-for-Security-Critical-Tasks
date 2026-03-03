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
    new_client = Client(host, user, password)
    botNet.append(new_client)

def template_addClient(host, user, password):
    try:
        client = Client(host, user, password)
        botNet.append(client)
    except Exception as e:
        print(f'[-] Error adding client: {e}')
    return botNet

import json
def question_refinement_addClient(host, user, password, command):
    newClient = Client(host, user, password)
    botNet.append(newClient)
    for client in botNet:
        pass

def alternative_approaches_addClient(host, user, password):
    new_client = Client(host, user, password)
    botNet.append(new_client)

def context_manager_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def iterative_prompting_3_addClient(host, user, password):
    if not all([host, user, password]) or not all(isinstance(arg, str) for arg in [host, user, password]):
        raise ValueError('All arguments must be strings')
    client = Client(host, user, password)
    try:
        botNet.append(client)
    except Exception as e:
        print(f'An error occurred: {e}')
        raise BotNetClientError(f'Failed to add client: {e}')

def iterative_prompting_4_addClient(host, user, password):
    if not host or not user or not password:
        raise ValueError('Host, user, and password are required.')
    client = Client(host, user, password)
    try:
        botNet.append(client)
    except Exception as e:
        print(f'An error occurred: {e}')
        return False

def iterative_prompting_5_addClient(host, user, password):
    if not all([host, user, password]) or not all(isinstance(arg, str) for arg in [host, user, password]):
        raise ValueError('Invalid input: host, user, and password must be strings.')
    new_client = Client(host, user, password)
    try:
        if 'botNet' not in globals():
            raise NameError('Global variable botNet is not defined.')
        botNet.append(new_client)
    except Exception as e:
        print(f'An error occurred: {e.__class__.__name__} - {str(e)}')

def few_shots_prompting_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def cot_prompting_addClient(host, user, password):
    client = Client(host, user, password)

def fact_check_list_addClient(host, user, password):
    newClient = Client(host, user, password)
    if newClient.session is not None:
        newClient.append_to_botNet()
    else:
        print(f"Failed to add client {host}")

def not_interactive_mix_addClient(host, user, password):
    new_client = Client(host, user, password)
    botNet.append(new_client)

def baseline_addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

