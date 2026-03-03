def ground_truth_code__send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def persona__send_command(s, cmd):
	s.sendline(cmd)
	s.prompt()

def template__send_command(s, cmd):
	try:
		s.sendline(cmd)
		s.prompt()
	except Exception as e:
		pass

def question_refinement__send_command(s, cmd):
    import shlex
    encoded_cmd = shlex.quote(cmd)
    s.sendline(encoded_cmd)
    output = s.prompt()
    return output

def alternative_approaches__send_command(s, cmd):
    try:
        s.sendline(cmd)
        return s.prompt()
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def context_manager__send_command(s, cmd):
	s.sendline(cmd)
	s.prompt()

def flipped_interaction_3__send_command(s, cmd, prompt_pattern=r'\$ '):
	s.sendline(cmd)
	s.expect(prompt_pattern)

def flipped_interaction_4__send_command(s, cmd):
	cmd = cmd.strip()
	if not isinstance(s, pexpect.spawn):
		logging.error("The object 's' is not an instance of pexpect.spawn")
		raise TypeError("The object 's' must be an instance of pexpect.spawn")
	try:
		logging.info(f"Sending command: {cmd}")
		s.sendline(cmd)
		response = s.prompt()
		logging.info(f"Response received: {response}")
		return response
	except pexpect.EOF:
		raise TypeError("End Of File (EOF) encountered in send_command")
	except pexpect.TIMEOUT:
		raise TypeError("Timeout encountered in send_command")


def flipped_interaction_5__send_command(s, cmd):
	try:
		logging.info(f'Sending command: {cmd}')
		s.sendline(cmd)
		logging.info('Waiting for the prompt')
		s.prompt()
		output = s.before.decode('utf-8').strip()
		logging.info(f'Command output captured:\n{output}')
		return output
	except pexpect.TIMEOUT:
		logging.error(f'Timeout occurred while waiting for the prompt after sending command: {cmd}')
		raise
	except pexpect.EOF:
		logging.error(f'EOF reached unexpectedly while waiting for the prompt after sending command: {cmd}')
		raise
	except Exception as e:
		logging.error(f'An error occurred while sending command or waiting for the prompt: {str(e)}')
		raise

def iterative_prompting_3__send_command(s, cmd):
    if not hasattr(s, 'sendline') or not callable(s.sendline):
        raise TypeError('The object s must have a callable method named sendline.')
    if not isinstance(cmd, str):
        raise ValueError('The command cmd must be a string.')
    try:
        s.sendline(cmd.strip())
        s.prompt()
    except Exception as e:
        raise RuntimeError(f'An error occurred while sending the command: {str(e)}')

def iterative_prompting_4__send_command(s, cmd):
    if not isinstance(s, object):
        raise TypeError('s must be an object')
    if not hasattr(s, 'sendline') or not callable(getattr(s, 'sendline')):
        raise AttributeError('s must have a callable method sendline')
    if not hasattr(s, 'prompt') or not callable(getattr(s, 'prompt')):
        raise AttributeError('s must have a callable method prompt')
    if not isinstance(cmd, str):
        raise TypeError('cmd must be a string')
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        raise RuntimeError(f'An error occurred: {str(e)}')

def iterative_prompting_5__send_command(s, cmd):
    if not hasattr(s, 'sendline') or not callable(s.sendline):
        raise ValueError('s must have a callable sendline method')
    if not hasattr(s, 'prompt') or not callable(s.prompt):
        raise ValueError('s must have a callable prompt method')
    if not isinstance(cmd, str):
        raise ValueError('cmd must be a string')
    try:
        s.sendline(cmd)
    except Exception as e:
        raise RuntimeError(f'Failed to send command: {str(e)}')
    try:
        s.prompt()
    except Exception as e:
        raise RuntimeError(f'Failed to read prompt: {str(e)}')

def few_shots_prompting__send_command(s, cmd):
	s.sendline(cmd)
	s.prompt()

def cot_prompting__send_command(s, cmd):
	s.sendline(cmd)
	prompt = s.prompt()

def fact_check_list__send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        raise RuntimeError(f"Command execution failed: {e}")

def not_interactive_mix__send_command(s, cmd):
    if not isinstance(s, pexpect.spawn):
        raise TypeError(f"'s' must be a pexpect.spawn object, not {type(s).__name__}")
    if not isinstance(cmd, str):
        raise TypeError(f"'cmd' must be a string, not {type(cmd).__name__}")
    try:
        s.sendline(cmd.encode('utf-8'))
        s.prompt()
    except (pexpect.EOF, pexpect.TIMEOUT) as e:
        raise RuntimeError(f"An error occurred: {e}")

def interactive_mix__send_command(s, cmd):
    if not isinstance(cmd, str):
        raise TypeError("The command must be a string.")
    try:
        s.sendline(cmd)
        s.prompt()
    except pexpect.EOF:
        print("End-of-file condition reached. Child process terminated unexpectedly.")
    except pexpect.TIMEOUT:
        print("Timeout occurred while waiting for the prompt.")
    except OSError as e:
        print(f"OS error occurred: {e.strerror}")
    except AttributeError:
        print("The spawn object does not have the sendline or prompt method.")

def baseline__send_command(s, cmd):
	s.sendline(cmd)
	s.prompt()
