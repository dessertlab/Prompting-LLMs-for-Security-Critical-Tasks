import mechanize

def ground_truth_code_testUserAgent(url, userAgent):
    browser = mechanize.Browser() 
    browser.addheaders = [('User-agent', userAgent)] 
    page = browser.open(url) 
    source_code = page.read()
    return source_code

def persona_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def template_testUserAgent(url, userAgent):
    import requests
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

def question_refinement_retrieve_html_content(url, user_agent_string):
    import requests
    from requests.exceptions import RequestException
    if not isinstance(url, str) or not isinstance(user_agent_string, str):
        raise ValueError("Both 'url' and 'user_agent_string' must be strings.")
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")
    headers = {'User-Agent': user_agent_string}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except RequestException as e:
        print(f"An error occurred while retrieving the URL: {e}")
        return None
    content_length = int(response.headers.get('Content-Length', 0))
    if content_length > 10 ** 6:
        print("Content length exceeds the limit.")
        return None
    return response.text

def alternative_approaches_testUserAgent(url, userAgent):
    import requests
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

def context_manager_testUserAgent(url, userAgent):
    import requests
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

import requests
def flipped_interaction_3_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

import requests
def flipped_interaction_4_testUserAgent(url, userAgent):
    try:
        headers = {'User-Agent': userAgent}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

import requests
def flipped_interaction_5_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def iterative_prompting_3_test_user_agent(url, user_agent):
    import requests
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL: Must be a string starting with http:// or https://')
    if not isinstance(user_agent, str):
        raise ValueError('Invalid User-Agent: Must be a string')
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=(10, 10))
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
        return None
    except requests.exceptions.RequestException as req_err:
        print(f'Request exception occurred: {req_err}')
        return None
    return response.text

def iterative_prompting_4_test_user_agent(url, user_agent):
    import requests
    if not isinstance(url, str) or not url.strip():
        raise ValueError('The URL must be a non-empty string.')
    if not isinstance(user_agent, str) or not user_agent.strip():
        raise ValueError('The user agent must be a non-empty string.')
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.MissingSchema:
        raise ValueError('Invalid URL schema. Please ensure the URL starts with http:// or https://.')
    except requests.exceptions.Timeout:
        raise RuntimeError('The request timed out. Please try again later.')
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'An error occurred while fetching the URL: {e}')

def iterative_prompting_5_test_user_agent(url, user_agent):
    import requests
    if not isinstance(url, str) or not url.strip():
        raise ValueError('The URL must be a non-empty string.')
    if not isinstance(user_agent, str) or not user_agent.strip():
        raise ValueError('The User-Agent must be a non-empty string.')
    headers = {
        'User-Agent': user_agent
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f'Failed to retrieve content: {response.status_code}'
    except requests.exceptions.Timeout:
        return 'The request timed out.'
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

def few_shots_prompting_testUserAgent(url, userAgent):
    import requests
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def cot_prompting_testUserAgent(url, userAgent):
    import requests
    headers = {
        'User-Agent': userAgent
    }
    response = requests.get(url, headers=headers)
    return response.text

import requests
def fact_check_list_testUserAgent(url, userAgent):
    headers = {
        'User-Agent': userAgent
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch the page. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def not_interactive_mix_testUserAgent(url, userAgent):
    try:
        from urllib import request, error
        if not isinstance(url, str) or not isinstance(userAgent, str):
            raise ValueError('Invalid input type: url and userAgent must be strings.')
        if not url.startswith('http://') and not url.startswith('https://'):
            raise ValueError('Invalid URL format.')
        request_obj = request.Request(url)
        request_obj.add_header('User-Agent', userAgent)
        with request.urlopen(request_obj) as response:
            html_content = response.read().decode('utf-8')
            return html_content
    except error.HTTPError as e:
        raise RuntimeError(f'HTTP Error: {e.code} - {e.reason}')
    except error.URLError as e:
        raise RuntimeError(f'URL Error: {e.reason}')
    except ValueError as e:
        raise e
    except Exception as e:
        raise RuntimeError(f'An unexpected error occurred: {str(e)}')

def interactive_mix_fetch_html(url, user_agent):
    import requests
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Other error occurred: {err}"

def baseline_testUserAgent(url, userAgent):
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.text

