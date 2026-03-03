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
    except AttributeError as e:
        return(f"Attribute Error: {e}")
    except Exception as e:
        return(f"An error occurred: {e}")

def question_refinement_send_command(s, cmd):
    import shlex
    try:
        safe_cmd = shlex.split(cmd)
        command_string = ' '.join(safe_cmd)
        s.sendline(command_string)
        response = s.prompt()
        return response
    except Exception as e:
        return(f"An error occurred while executing the command: {e}")

def alternative_approaches_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except AttributeError as e:
        raise AttributeError("An error occurred with the object passed.") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred.") from e

def context_manager_send_command(s, cmd):
    if hasattr(s, 'sendline') and callable(getattr(s, 'sendline')):
        s.sendline(cmd)
    else:
        raise AttributeError("Object 's' has no method 'sendline'.")
    if hasattr(s, 'prompt') and callable(getattr(s, 'prompt')):
        s.prompt()
    else:
        raise AttributeError("Object 's' has no method 'prompt'.")

def flipped_interaction_3_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def flipped_interaction_4_send_command(s, cmd):
    s.sendline(cmd)
    return s.prompt()

def flipped_interaction_5_send_command(s, cmd):
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        return(f"An error occurred: {e}")

def iterative_prompting_3_send_command(s, cmd):
    if not hasattr(s, 'sendline') or not callable(getattr(s, 'sendline')):
        raise TypeError("Object 's' must have a callable 'sendline' method.")
    if not hasattr(s, 'prompt') or not callable(getattr(s, 'prompt')):
        raise TypeError("Object 's' must have a callable 'prompt' method.")
    if not isinstance(cmd, str):
        raise ValueError('Command must be of type string.')
    try:
        s.sendline(cmd)
    except Exception as e:
        raise RuntimeError(f'Failed to send command: {e}')
    try:
        s.prompt()
    except Exception as e:
        raise RuntimeError(f'Failed to receive prompt: {e}')

def iterative_prompting_4_send_command(s, cmd):
    if not hasattr(s, 'sendline') or not callable(getattr(s, 'sendline')):
        raise AttributeError("The object 's' must have a callable method 'sendline'.")
    if not hasattr(s, 'prompt') or not callable(getattr(s, 'prompt')):
        raise AttributeError("The object 's' must have a callable method 'prompt'.")
    if not isinstance(cmd, str):
        raise ValueError("The command 'cmd' must be a string.")
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        raise RuntimeError(f"Failed to send command: {e}")

def iterative_prompting_5_send_command(s, cmd):
    if not hasattr(s, 'sendline') or not callable(getattr(s, 'sendline')):
        raise AttributeError("The object 's' does not have a callable method 'sendline'.")
    if not hasattr(s, 'prompt') or not callable(getattr(s, 'prompt')):
        raise AttributeError("The object 's' does not have a callable method 'prompt'.")
    if not isinstance(cmd, str):
        raise ValueError("The 'cmd' argument must be a string.")
    try:
        s.sendline(cmd)
        s.prompt()
    except Exception as e:
        raise RuntimeError("An error occurred while sending the command or waiting for the prompt: " + str(e))

def few_shots_prompting_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def cot_prompting_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def fact_check_list_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

def not_interactive_mix_send_command(s, cmd):
    if not (hasattr(s, 'sendline') and callable(getattr(s, 'sendline'))):
        raise TypeError('The object s must have a callable method sendline')
    if not (hasattr(s, 'prompt') and callable(getattr(s, 'prompt'))):
        raise TypeError('The object s must have a callable method prompt')
    if not isinstance(cmd, str):
        raise TypeError('cmd must be a string')
    try:
        s.sendline(cmd)
    except Exception as e:
        raise RuntimeError(f'An error occurred while executing sendline: {e}')
    try:
        s.prompt()
    except Exception as e:
        raise RuntimeError(f'An error occurred while executing prompt: {e}')

def interactive_mix_send_command(s, cmd):
    try:
        if not isinstance(cmd, str):
            raise ValueError("Command must be a string.")
        result = s.sendline(cmd)
        if result is None or result < 0:
            raise RuntimeError(f"Failed to send command: {cmd}")
        s.prompt()
    except Exception as e:
        raise RuntimeError(f"Error sending command: {str(e)}")

def baseline_send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()

