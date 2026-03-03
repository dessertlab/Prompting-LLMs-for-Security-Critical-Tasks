import mechanize

def ground_truth_code_testUserAgent(url, userAgent):
    browser = mechanize.Browser() 
    browser.addheaders = [('User-agent', userAgent)] 
    page = browser.open(url) 
    source_code = page.read()
    return source_code

import requests
def persona_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

def template_testUserAgent(url, userAgent):
    import requests
    try:
        response = requests.get(url, headers={'User-Agent': userAgent})
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        return f'HTTP Error: {err}'
    except requests.exceptions.RequestException as e:
        return f'Request Exception: {e}'

import requests
def question_refinement_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def alternative_approaches_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

def context_manager_testUserAgent(url, userAgent):
    import requests
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else ''

import requests
from requests.exceptions import HTTPError, RequestException
def iterative_prompting_3_test_user_agent(url, user_agent):
    if not url or not user_agent:
        raise ValueError("URL and user_agent must be provided.")
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except RequestException as req_err:
        print(f'Other error occurred: {req_err}')
    else:
        print(f'Response from API: {response.text}')

def iterative_prompting_4_test_user_agent(url, user_agent):
    import requests
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError('Invalid URL provided')
    if not user_agent:
        raise ValueError('User-Agent string cannot be empty')
    requests.get = requests.sessions.Session.request
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        error_message = f'An error occurred: {e}'
        print(error_message)
        return None
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.Timeout as timeout_err:
        print(f'Request timed out: {timeout_err}')

def iterative_prompting_5_test_user_agent(url, user_agent):
    import urllib.request
    from urllib.error import URLError, HTTPError
    if not url.startswith('http://') and not url.startswith('https://'):
        raise ValueError('URL must start with http:// or https://')
    if not isinstance(user_agent, str) or not user_agent:
        raise ValueError('user_agent must be a non-empty string')
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
        return html
    except HTTPError as e:
        print(f'HTTP error occurred: {e.code} - {e.reason}')
        return None
    except URLError as e:
        print(f'URL error occurred: {e.reason}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None

def few_shots_prompting_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text

import requests
def cot_prompting_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text

import requests
def fact_check_list_testUserAgent(url, user_agent):
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def not_interactive_mix_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException as e:
        return f"An error occurred: {e}"

def baseline_testUserAgent(url, userAgent):
    import urllib.request
    req = urllib.request.Request(url, headers={'User-Agent': userAgent})
    with urllib.request.urlopen(req) as response:
        return response.read()

