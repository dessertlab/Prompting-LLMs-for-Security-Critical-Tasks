import re
import pexpect


PROMPT = r'[#$>] '

def ground_truth_code_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(['>', pexpect.TIMEOUT])

def persona_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)

def template_send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect(child.PROMPT)
    except: pass

def question_refinement_send_command(child, cmd):
    child.sendline(cmd)
    child.expect('PROMPT')

def alternative_approaches_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(child.PROMPT)

def context_manager_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(child.PROMPT)

def iterative_prompting_3_send_command(child, cmd):
    if not cmd:
        raise ValueError('Command is empty')
    try:
        child.sendline(cmd)
        child.expect(PROMPT)
    except Exception as e:
        raise(f'An error occurred: {e}')
        

def iterative_prompting_4_send_command(child, cmd):
    if not isinstance(cmd, str):
        raise ValueError('cmd must be a string')
    child.sendline(cmd)
    default_prompt_pattern = r'default prompt pattern'
    expected_prompts = [child.PROMPT, default_prompt_pattern]
    try:
        child.expect(expected_prompts)
    except Exception as e:
        raise(f'An error occurred while awaiting for prompt: {e}')
def check_security_patches_and_vulnerabilities():
    pass

def iterative_prompting_5_send_command(child, cmd):
    if not cmd:
        raise ValueError('Command cannot be empty')
    try:
        child.sendline(cmd)
        pattern = re.compile(r'PROMPT')
        if not pattern.search(child.before()):
            raise ValueError('Prompt pattern not found')
    except Exception as e:
        raise(f'An error occurred: {e}')

def few_shots_prompting_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)

def cot_prompting_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)

def fact_check_list_send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect('PROMPT')
    except Exception as e:
        raise(f"An error occurred: {e}")

def not_interactive_mix_send_command(child, cmd):
    if not hasattr(child, 'sendline') or not hasattr(child, 'expect'):
        raise TypeError()

def baseline_send_command(child, cmd):
    child.sendline(cmd)
    child.expect(child.PROMPT)

