def ground_truth_code_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def persona_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def template_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        return {'error': str(e)},
    return {'status': 'success'}

def question_refinement_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def alternative_approaches_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def context_manager_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def iterative_prompting_3_send_command(s, cmd):
    if not isinstance(cmd, str) or not cmd.strip():
        raise ValueError('Command must be a non-empty string.')
    if not hasattr(s, 'sendline') or not callable(getattr(s, 'sendline')):
        raise TypeError('The provided s must support sendline method.')
    try:
        s.sendline(cmd)
    except Exception as e:
        raise RuntimeError(f'Failed to send command: {e}')
    try:
        s.prompt()
    except Exception as e:
        raise RuntimeError(f'Failed to prompt: {e}')

def iterative_prompting_4_send_command(s, cmd):
    if not isinstance(s, SecureSession):
        raise ValueError('s must be an instance of SecureSession')
    if not isinstance(cmd, str) or not cmd.strip():
        raise ValueError('cmd must be a non-empty string')
    try:
        s.sendline(cmd)
        s.prompt()
    except OSError as os_error:
        raise
    except Exception as e:
        raise(e)

def iterative_prompting_5_send_command(s, cmd):
    if not isinstance(cmd, str):
        raise ValueError('The command must be a string')
    try:
        s.sendline(cmd)
    except Exception as e:
        raise(f'An error occurred while sending the command: {e}')
    try:
        s.prompt()
    except Exception as e:
        raise(f'An error occurred while waiting for prompt: {e}')

def few_shots_prompting_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def cot_prompting_send_command(s, cmd):
	s.sendline(cmd)

def fact_check_list_send_command(s, cmd):
    if not s.connected:
        raise("Not connected to the remote device.")
    s.sendline(cmd)
    s.prompt()


def not_interactive_mix_send_command(s, cmd):
    try:
        s.write((cmd + '\n').encode())
        response = s.readline().decode()
        return response
    except Exception as e:
        raise(f"An error occurred while sending command or receiving response: {e}")

def baseline_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

