import pexpect

PROMPT = r'[#$>] '

def ground_truth_code_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def persona_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def template_send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except Exception as e:
        print(f"An error occurred: {e}")

def question_refinement_send_command(child, cmd):
    try:
        if '\n' in cmd or '\r' in cmd:
            raise ValueError("Command contains newline characters which are not allowed.")
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except pexpect.ExceptionPexpect as e:
        print(f"An error occurred while interacting with the subprocess: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def alternative_approaches_send_command(child, cmd):
    import logging
    logging.basicConfig(level=logging.INFO)
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as e:
        logging.error(f"A pexpect specific error occurred: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

def context_manager_send_command(child, cmd):
    if hasattr(child, 'sendline') and callable(getattr(child, 'sendline')):
        child.sendline(cmd)
    if hasattr(child, 'expect') and callable(getattr(child, 'expect')) and 'PROMPT' in globals():
        child.expect(['>', pexpect.TIMEOUT])

def flipped_interaction_3_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def flipped_interaction_4_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

import pexpect
def flipped_interaction_5_send_command(child, cmd, prompt, timeout=30):
    try:
        child.sendline(cmd)
        child.expect(prompt, timeout=timeout)
        output = child.before.decode('utf-8')
        return output
    except pexpect.EOF:
        return "Unexpected end of file encountered."
    except pexpect.TIMEOUT:
        return "Command timed out."
    except Exception as e:
        return f"An error occurred: {e}"

def iterative_prompting_3_send_command(child, cmd):
    if not hasattr(child, 'sendline') or not callable(getattr(child, 'sendline')):
        raise AttributeError("The child object must have a callable 'sendline' method.")
    if not hasattr(child, 'expect') or not callable(getattr(child, 'expect')):
        raise AttributeError("The child object must have a callable 'expect' method.")
    if not isinstance(cmd, str):
        raise TypeError("The cmd argument must be a string.")
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except Exception as e:
        raise RuntimeError(f"An error occurred while sending the command: {e}")

def iterative_prompting_4_send_command(child, cmd):
    if not hasattr(child, 'sendline') or not hasattr(child, 'expect'):
        raise AttributeError("The child object must have 'sendline' and 'expect' methods.")
    if not isinstance(cmd, str):
        raise TypeError("The command must be a string.")
    if 'PROMPT' not in globals():
        raise NameError("The global 'PROMPT' variable must be defined.")
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def iterative_prompting_5_send_command(child, cmd):
    if not isinstance(child, object):
        raise TypeError("Expected 'child' to be an object with sendline and expect methods.")
    if not isinstance(cmd, str):
        raise TypeError("Expected 'cmd' to be a string.")
    if not callable(getattr(child, 'sendline', None)):
        raise AttributeError("The 'child' object does not have a callable 'sendline' method.")
    if not callable(getattr(child, 'expect', None)):
        raise AttributeError("The 'child' object does not have a callable 'expect' method.")
    try:
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except Exception as e:
        raise RuntimeError(f"An error occurred while sending the command: {e}")

def few_shots_prompting_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def cot_prompting_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def fact_check_list_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def not_interactive_mix_send_command(child, cmd):
    import pexpect
    try:
        PROMPT = pexpect.EOF
        if not isinstance(cmd, str) or not cmd.strip():
            raise ValueError("Command must be a non-empty string.")
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except Exception as e:
        print(f"An error occurred during command execution: {e}")

def interactive_mix_send_command(child, cmd, PROMPT):
    import pexpect
    try:
        if not isinstance(cmd, str):
            raise ValueError("Command must be a string.")
        child.sendline(cmd)
        child.expect(['>', pexpect.TIMEOUT])
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except pexpect.exceptions.EOF:
        print("Unexpected EOF occurred. The command may not have been executed properly.")
    except pexpect.exceptions.TIMEOUT:
        print("Timeout reached. The expected prompt did not appear.")
    except Exception as e:
        print(f"An unexpected exception occurred: {e}")

def baseline_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

