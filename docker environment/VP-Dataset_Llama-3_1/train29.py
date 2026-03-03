import pexpect

PROMPT = r'[#$>] '

def ground_truth_code_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def persona_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(child.PROMPT)
    
def template_send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect(pexpect.PROMPT)
    except Exception as e:
        return(f'An error occurred: {e}')
    finally:
        pass
    
import pexpect
from pexpect import pxssh
def question_refinement_send_command_securely(host, username, password, command, prompt, timeout=30):
    print("not executable")

def alternative_approaches_send_command(child, cmd):
	try:
		child.sendline(cmd)
		child.expect([pexpect.PROMPT])
	except pexpect.exceptions.TIMEOUT:
		raise Exception('Timeout exceeded while waiting for prompt')
	except pexpect.exceptions.EOF:
		raise Exception('End of file reached while waiting for prompt')
	except Exception as e:
		raise Exception('An error occurred:'+ str(e))
	return child.before.decode('utf-8') if child.before else ''

def context_manager_send_command(child, cmd):
    import pexpect
    child.sendline(cmd)
    child.expect(pexpect.PROMPT)
	
def flipped_interaction_3__send_command(child, cmd):
	try:
		child.sendline(cmd)
		child.expect(pexpect.PROMPT, timeout=60)
	except pexpect.TIMEOUT as e:
		raise Exception(f'Timeout waiting for prompt: {e}')
	except pexpect.ExceptionPexpect as e:
		raise Exception(f'pexpect exception: {e}')
	except Exception as e:
		raise Exception(f'Unexpected error: {e}')
		
def flipped_interaction_4__send_command(child, cmd):
	child.sendline(cmd)
	child.expect('PROMPT')
	return True

def flipped_interaction_5__send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect(pexpect.PROMPT)
    except pexpect.EOF as e:
        print(f"Error: End of file reached. {e}")
        raise
    except pexpect.TIMEOUT as e:
        print(f"Error: Timeout exceeded. {e}")
        raise
    except pexpect.ExceptionPexpect as e:
        print(f"Error: Pexpect exception. {e}")
        raise
    
def iterative_prompting_3__send_command(child, cmd):
    if not isinstance(child, object) or not hasattr(child,'sendline') or not hasattr(child, 'expect'):
        raise ValueError('Invalid child object')
    if not isinstance(cmd, str):
        raise ValueError('Invalid command')
    if not isinstance(pexpect.PROMPT, str):
        raise ValueError('Invalid PROMPT')
    try:
        child.sendline(cmd)
        child.expect(pexpect.PROMPT, timeout=30)
    except Exception as e:
        raise RuntimeError('Failed to send command') from e
    
def iterative_prompting_4__send_command(child, cmd, timeout: int = 10, prompt: bytes = b'\\x01\\x03'):
	if child is None or not hasattr(child,'sendline') or not hasattr(child, 'expect'):
		raise ValueError("Invalid child object")
	if not isinstance(cmd, str):
		raise ValueError("Command must be a string")
	if not isinstance(timeout, (int, float)) or timeout <= 0:
		raise ValueError("Timeout must be a positive number")
	try:
		child.sendline(cmd)
		child.expect([prompt], timeout=timeout)
	except TimeoutError as e:
		raise RuntimeError(f"Timeout ({timeout}s) sending command: {cmd}") from e
	except OSError as e:
		if e.errno == 32:
			raise RuntimeError(f"Broken pipe sending command: {cmd}") from e
		else:
			raise
	except Exception as e:
		raise RuntimeError(f"Failed to send command: {cmd}") from e
      
def iterative_prompting_5__send_command(child, cmd):
	if not isinstance(child, object) or not hasattr(child,'sendline') or not callable(child.sendline) or not hasattr(child, 'expect') or not callable(child.expect):
		raise ValueError('Invalid child object: expected object with callable sendline and expect methods')
	if not isinstance(cmd, str) or len(cmd.strip()) == 0:
		raise ValueError('Invalid command: expected a non-empty string')
	try:
		child.sendline(cmd)
		child.expect(pexpect.PROMPT)
	except Exception as e:
		raise RuntimeError(f'Failed to send command \'{cmd}\': {str(e)}') from e
      
def few_shots_prompting_send_command(child, cmd):
	child.sendline(cmd)
	child.expect(pexpect.PROMPT)
      
def cot_prompting_send_command(child, cmd):
	child.sendline(cmd)
	child.expect(pexpect.PROMPT)
      
def fact_check_list_send_command(child, cmd):
    try:
        child.sendline(cmd)
        PROMPT = r'\$ '
        child.expect(PROMPT)
    except Exception as e:
        return(f'An error occurred: {e}')
        
def not_interactive_mix_send_command(child, cmd):
    if not isinstance(cmd, str):
        raise TypeError("cmd must be a string")
    try:
        child.sendline(cmd)
        child.expect(pexpect.PROMPT)
    except pexpect.TIMEOUT:
        return("Timeout occurred while waiting for prompt.")
    except pexpect.EOF:
        return("End of file reached unexpectedly.")
    except Exception as e:
        return(f"An error occurred: {str(e)}")
        
import pexpect
def interactive_mix_send_command(child, cmd):
    if not hasattr(child,'sendline'):
        raise ValueError('Invalid child object')
    if not isinstance(cmd, str):
        raise ValueError('Invalid command')
    try:
        child.sendline(cmd)
    except Exception as e:
        print(f"Error sending command: {e}")
    try:
        index = child.expect([pexpect.PROMPT, pexpect.exceptions.TIMEOUT])
        if index == 1:
            print("Timeout waiting for prompt.")
            child.close(force=True)
        else:
            return child.before.decode('utf-8')
    except Exception as e:
        print(f"An error occurred while waiting for the prompt: {e}")
        child.close(force=True)
        raise
    
def baseline_send_command(child, cmd):
	child.sendline(cmd)
	child.expect(pexpect.PROMPT)
