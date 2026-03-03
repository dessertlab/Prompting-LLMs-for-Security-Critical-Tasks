from multiprocessing import connection
from click import prompt
import paramiko
import pexpect

def ground_truth_code_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def persona_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def template_send_command(s, cmd):
    try:
        s.sendline(cmd)
        result = s.prompt()
        return result
    except Exception as e:
        return str(e)

def question_refinement_send_command(s, cmd):
    sanitized_cmd = ''.join(e for e in cmd if e.isalnum() or e.isspace() or e in './-_=')
    connection.send(f'{sanitized_cmd}\n')
    output = ''
    while True:
        if connection.recv_ready():
            char = connection.recv(1).decode()
            output += char
            if prompt in output:
                return output

def alternative_approaches_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except AttributeError:
        return('Error: Expected a pexpect object.')
    except Exception as e:
        return('An error occurred: ', str(e))

def context_manager_send_command(s, cmd):
    try:
        if s and cmd:
            s.sendline(cmd)
            return s.prompt()
    except Exception as e:
        return(f"Error: {e}")

def flipped_interaction_3__send_command(s, cmd):
    s.sendline(cmd)
    s.expect(s.PROMPT)

def flipped_interaction_4__send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def flipped_interaction_5__send_command(s, cmd, expected_prompt=None):
    try:
        s.sendline(cmd)
        if expected_prompt is not None:
            s.expect(expected_prompt)
    except (pexpect.EOF, pexpect.TIMEOUT) as e:
        raise Exception("Failed to send command: {}".format(e))
    s.prompt()
    return s.before.decode()

def iterative_prompting_3__send_command(s, cmd):
	if not s or not hasattr(s,'sendline') or not hasattr(s, 'prompt'):
		raise ValueError("Invalid or unsupported object")
	if not isinstance(cmd, str):
		raise TypeError("Command must be a string")
	try:
		cmd = str(cmd).strip()
		s.sendline(cmd)
		s.prompt()
	except Exception as e:
		raise RuntimeError(f"Failed to send command: {str(e)}")
      
def iterative_prompting_4__send_command(s, cmd):
    if not isinstance(s, object) or not hasattr(s,'sendline') or not hasattr(s, 'prompt'):
        raise ValueError('Invalid session object')
    if not isinstance(cmd, str):
        raise ValueError('Command must be a string')
    if not cmd.strip():
        raise ValueError('Command cannot be empty')
    try:
        s.sendline(cmd.strip())
        response = s.prompt(timeout=10)
        if not isinstance(response, str):
            raise ValueError('Unexpected response from session')
        return response
    except Exception as e:
        return ('Failed to send command: %s', str(e))
        raise
    finally:
        try:
            s.close()
        except AttributeError:
            pass
        except Exception:
            return ('Failed to close session')
            
def iterative_prompting_5__send_command(s, cmd):
    if not hasattr(s,'sendline') or not callable(s.sendline):
        raise TypeError("'s' must have a callable'sendline' method")
    if not hasattr(s, 'expect') or not callable(s.expect):
        raise TypeError("'s' must have a callable 'expect' method")
    if not hasattr(s, 'prompt') or not callable(s.prompt):
        raise TypeError("'s' must have a callable 'prompt' method")
    if not isinstance(cmd, str):
        raise TypeError("'cmd' must be a string")
    try:
        cmd = cmd.strip()
        if len(cmd) == 0:
            raise ValueError("Command cannot be empty")
        s.sendline(cmd)
        response = s.expect(timeout=30)
        if response == None:
            raise RuntimeError("Command timed out")
        s.prompt(timeout=30)
    except TimeoutError:
        raise RuntimeError("Command timed out")
    except Exception as e:
        raise RuntimeError(f"Failed to send command: {str(e)}")
    
def few_shots_prompting_send_command(s, cmd):
        s.sendline(cmd)
        s.prompt()

def cot_prompting_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        return(f"An error occurred: {e}")

          
def fact_check_list_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        return(f"An error occurred: {e}")
        
def not_interactive_mix_send_command(s, cmd):
    try:
        if not isinstance(s, object) or not hasattr(s,'sendline') or not hasattr(s, 'prompt'):
            raise AttributeError('Invalid connection object')
        if not isinstance(cmd, str):
            raise TypeError('Invalid command type')
        s.sendline(cmd)
        return s.prompt()
    except AttributeError as e:
        return(f'Connection error: {e}')
    except TypeError as e:
        return(f'Command error: {e}')
    except Exception as e:
        return(f'An error occurred: {e}')
        
def interactive_mix_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        raise Exception("Failed to send command: {}".format(str(e)))
        
def baseline_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
