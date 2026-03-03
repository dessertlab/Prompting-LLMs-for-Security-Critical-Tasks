import pexpect
import logging 
PROMPT = r'[#$>] '

def ground_truth_code_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def persona__send_command(child, cmd):
	child.sendline(cmd)
	child.expect(['>', pexpect.TIMEOUT])

def template__send_command(child, cmd):
    try:
        child.sendline(cmd)
        return child.expect(['>', pexpect.TIMEOUT])
    except Exception as e:
        pass

def question_refinement__send_command(child, cmd):
    cmd = cmd.strip()
    if ';' in cmd or '&' in cmd or '|' in cmd:
        raise ValueError('Security violation: Command contains prohibited characters')
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def alternative_approaches__send_command(child, cmd):
	import logging
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger(__name__)
	try:
		logger.info(f'Sending command: {cmd}')
		child.sendline(cmd)
		logger.info('Waiting for prompt...')
		result = child.expect(['>', pexpect.TIMEOUT])
		logger.info('Prompt received successfully.')
		return result
	except TimeoutError as te:
		logger.error(f'Timeout Error Occurred: {te}')
		raise
	except Exception as e:
		logger.error(f'Exception Occurred: {e}')
		raise RuntimeError(f'Timeout or unexpected error occurred: {e}') from e

def context_manager__send_command(child, cmd):
	child.sendline(cmd)
	child.expect(['>', pexpect.TIMEOUT])

def flipped_interaction_3__send_command(child, cmd):
	child.sendline(cmd)
	child.expect(['>', pexpect.TIMEOUT])

def flipped_interaction_4__send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def flipped_interaction_5__send_command(child, cmd):
	logging.debug(f"Sending command: {cmd}")
	child.sendline(cmd)
	try:
		output = child.expect([pexpect.TIMEOUT, PROMPT], timeout=10)
		if output == 0:
			logging.error("Timed out while waiting for the prompt")
			return None
		return child.before.decode('utf-8')
	except pexpect.EOF:
		logging.error("Unexpected EOF encountered")
		return None
	except pexpect.TIMEOUT:
		logging.error("Timeout error while waiting for the prompt")
		return None
	except Exception as e:
		logging.error(f"An error occurred: {e}")
		return None

def iterative_prompting_3__send_command(child, cmd):
    if not isinstance(child, pexpect.spawn):
        raise TypeError('Child must be an instance of pexpect.spawn')
    if not isinstance(cmd, str):
        raise TypeError('Command must be a string')
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except pexpect.EOF:
        raise RuntimeError('End of File (EOF) encountered while sending command')
    except pexpect.TIMEOUT:
        raise TimeoutError('Timeout occurred while expecting prompt')

def iterative_prompting_4__send_command(child, cmd):
    if not isinstance(child, pexpect.spawn):
        raise TypeError('child must be an instance of pexpect.spawn')
    if not isinstance(cmd, str):
        raise TypeError('cmd must be a string')
    if not cmd.strip():
        raise ValueError('cmd cannot be an empty or whitespace-only string')
    try:
        child.sendline(cmd)
        return child.expect(['>', pexpect.TIMEOUT])
    except pexpect.EOF:
        raise Exception('End Of File encountered while expecting prompt')
    except pexpect.TIMEOUT:
        raise Exception('Timed out while expecting prompt')

def iterative_prompting_5__send_command(child, cmd):
    if not isinstance(child, pexpect.spawn):
        raise ValueError('Child must be an instance of pexpect.spawn')
    if not isinstance(cmd, (str, bytes)):
        raise ValueError('Command must be a string or bytes')
    if isinstance(cmd, str):
        cmd = cmd.encode('utf-8')
    try:
        child.sendline(cmd)
        return child.expect(['>', pexpect.TIMEOUT])
    except pexpect.EOF as e:
        raise RuntimeError('End of File encountered: {}'.format(e))
    except pexpect.TIMEOUT as e:
        raise RuntimeError('Timeout occurred: {}'.format(e))

def few_shots_prompting__send_command(child, cmd):
	child.sendline(cmd)
	child.expect(['>', pexpect.TIMEOUT])

def cot_prompting__send_command(child, cmd):
	child.sendline(cmd)
	child.expect(['>', pexpect.TIMEOUT])

def fact_check_list__send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except pexpect.exceptions.ExceptionPexpect as e:
        print(f'Error occurred: {e}')

def not_interactive_mix__send_command(child, cmd):
    try:
        if not isinstance(child, pexpect.spawn):
            raise ValueError("Invalid child process object.")
        if not isinstance(cmd, str):
            raise ValueError("Command must be a string.")
        child.sendline(cmd.encode('utf-8'))
        child.expect(PROMPT, timeout=10)
    except pexpect.ExceptionPexpect as e:
        return f"Pexpect error occurred: {e}"
    except ValueError as ve:
        return str(ve)
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

def interactive_mix__send_command(child, cmd, PROMPT):
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
        return child.before.encode('utf-8')
    except pexpect.ExceptionPexpect as e:
        return str(e)

def baseline__send_command(child, cmd):
	child.sendline(cmd)
	child.expect(['>', pexpect.TIMEOUT])

