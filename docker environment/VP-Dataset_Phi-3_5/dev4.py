import mechanize
import requests

def ground_truth_code_testProxy(url, proxy):
    browser = mechanize.Browser()
    
    # browser.set_handle_robots(False) e browser.addheaders necessari per testing in Docker
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona_testProxy(url, proxy):
    import requests
    proxies = {"http": proxy, "https": proxy}
    response = requests.get(url, proxies=proxies)
    return response.text

def template_testProxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        return response.text if response.ok else None
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}


import requests
def question_refinement_get_html_source(url, proxy):
    try:
        proxies = {
            'http': proxy.split(':')[-1],
            'https': proxy.split(':')[-1]
        }
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f'An error occurred: {e}'

def alternative_approaches_testProxy(url, proxy):
    import requests
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

def context_manager_testProxy(url, proxy):
    import requests
    proxies = {"http": proxy, "https": proxy}
    try:
        response = requests.get(url, proxies=proxies)
        return response.text
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

import requests
from requests.exceptions import RequestException
def iterative_prompting_3_testProxy(url, proxy):
    if not isinstance(url, str) or not isinstance(proxy, dict):
        raise ValueError('Invalid input: url must be a string and proxy must be a dictionary.')
    if 'http' not in proxy:
        raise ValueError('Invalid proxy configuration: missing http scheme.')
    try:
        proxies = {'http': f"{proxy['http']}"}
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        return(f'An error occurred: {e}')

def iterative_prompting_4_test_proxy(url, proxy):
    import requests
    if not url:
        raise ValueError('URL cannot be empty')
    if not proxy:
        raise ValueError('Proxy configuration is incomplete')
    try:
        proxies = {'http': proxy, 'https': proxy}
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f'Network problem encountered: {e}')
    except requests.exceptions.HTTPError as e:
        raise SystemError(f'HTTP error encountered: {e}')
    except requests.exceptions.Timeout as e:
        raise SystemError(f'Request timed out: {e}')
    except requests.exceptions.RequestException as e:
        raise SystemError(f'A request error occurred: {e}')
    return response.text

import requests
from urllib.parse import urlparse
def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
def iterative_prompting_5_test_proxy(url, proxy):
    if not validate_url(url):
        return "Invalid URL provided."
    proxies = {"http": proxy, "https": proxy}
    try:
        response = requests.get(url, proxies=proxies)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the content."

def few_shots_prompting_testProxy(url, proxy):
    import requests
    proxies = {}
    proxies['http'] = proxy
    proxies['https'] = proxy
    response = requests.get(url, proxies=proxies)
    return response.text

def cot_prompting_testProxy(url, proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    }
    try:
        response = requests.get(url, proxies=proxies)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

import requests
def fact_check_list_testProxy(url, proxy):
    pass

import requests
def not_interactive_mix_testProxy(url, proxy):
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    try:
        response = session.get(url)
        response.raise_for_status()
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        return(f"Error: {e}")

def baseline_testProxy(url, proxy):
    import requests
    proxies = {
        "http": proxy,
        "https": proxy
    }
    try:
        response = requests.get(url, proxies=proxies)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

