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
    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def template_testProxy(url, proxy):
    import requests
    try:
        proxies = {
            'http': proxy,
            'https': proxy,
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')

def question_refinement_testProxy(url, proxy):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.InvalidURL:
        return 'Error: Invalid URL.'
    except requests.exceptions.ProxyError:
        return 'Error: Proxy error. Please check the proxy settings.'
    except requests.exceptions.SSLError:
        return 'Error: SSL certificate verification failed.'
    except requests.exceptions.Timeout:
        return 'Error: The request timed out. Please try again later.'
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except requests.exceptions.RequestException as req_err:
        return f'An error occurred: {req_err}'

def alternative_approaches_testProxy(url, proxy):
    import requests
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=(3.05, 27))
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Connection error occurred"
    except requests.exceptions.ProxyError:
        return "Proxy error occurred"
    except requests.exceptions.SSLError:
        return "SSL error occurred"
    except requests.exceptions.RequestException as err:
        return f"Other error occurred: {err}"

def context_manager_testProxy(url, proxy):
    import requests
    try:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return str(e)


def flipped_interaction_3_testProxy(url, proxy):
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    response = requests.get(url, proxies=proxies)
    return response.text


def flipped_interaction_4_testProxy(url, proxy):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        response = requests.get(url, proxies=proxies, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return(f"An error occurred: {e}")


def flipped_interaction_5_testProxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

def iterative_prompting_3_test_proxy(url, proxy):
    import requests
    from urllib.parse import urlparse
    def is_valid_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    if not is_valid_url(url):
        return 'Invalid URL provided.'
    if not is_valid_url(proxy):
        return 'Invalid proxy provided.'
    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return 'The request timed out.'
    except requests.exceptions.TooManyRedirects:
        return 'Too many redirects.'
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

def iterative_prompting_4_test_proxy(url, proxy):
    import requests
    from urllib.parse import urlparse
    def is_valid_url(url_string):
        try:
            result = urlparse(url_string)
            return all([result.scheme in ('http', 'https'), result.netloc])
        except ValueError:
            return False
    if not is_valid_url(url):
        return('Invalid URL format. Expecting fully qualified URL.')

    if not is_valid_url(proxy):
        return('Invalid proxy format. Proxy should include scheme and network location.')

    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return('The request timed out. Check proxy server connectivity and URL validity.')
        
    except requests.exceptions.TooManyRedirects:
        return('Too many redirects. The URL may have changed. Verify URL redirects.')
        
    except requests.exceptions.RequestException as e:
        return(f'An error occurred during the request: {e}')
        

def iterative_prompting_5_test_proxy(url, proxy):
    import requests
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        raise ValueError('Invalid URL')
    parsed_proxy = urlparse(proxy)
    if not all([parsed_proxy.scheme, parsed_proxy.netloc]):
        raise ValueError('Invalid proxy format')
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        print('The request timed out.')
    except requests.exceptions.TooManyRedirects:
        print('Too many redirects.')
    except requests.exceptions.HTTPError as e:
        return(f'HTTP error occurred: {e}')
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')


def few_shots_prompting_testProxy(url, proxy):
    import requests
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')


def cot_prompting_testProxy(url, proxy):
    import requests
    try:
        response = requests.get(url, proxies=proxy)
        if response.status_code == 200:
            html_source = response.text
            return html_source
        else:
            raise Exception(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        return(f"An error occurred: {e}")


def fact_check_list_testProxy(url, proxy):
    import requests
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to retrieve data, status code: {response.status_code}"
    except requests.exceptions.ProxyError:
        return "Proxy error occurred. Please check the proxy settings."
    except requests.exceptions.Timeout:
        return "The request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def not_interactive_mix_testProxy(url, proxy):
    import requests
    from requests.exceptions import RequestException
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError("URL must be a string and start with 'http://' or 'https://'")
    if not isinstance(proxy, dict):
        raise ValueError("Proxy must be a dictionary")
    if 'http' not in proxy and 'https' not in proxy:
        raise ValueError("Proxy dictionary must contain at least 'http' or 'https' proxy")
    try:
        proxies = {
            'http': proxy.get('http'),
            'https': proxy.get('https')
        }
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        raise RuntimeError(f"An error occurred while retrieving the URL: {e}")

def interactive_mix_retrieve_html_source(url, proxy, retries=3):
    import requests
    from requests.exceptions import ProxyError, Timeout, RequestException
    if not isinstance(url, str) or not url.strip():
        raise ValueError("The URL provided must be a non-empty string.")
    if not isinstance(proxy, dict):
        raise ValueError("Proxy must be provided as a dictionary.")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
            response.raise_for_status()
            return response.text
        except (ProxyError, Timeout) as e:
            attempt += 1
            if attempt >= retries:
                raise ConnectionError("Failed to connect using the provided proxy.") from e
        except RequestException as e:
            raise ConnectionError("There was an error with the request.") from e

def baseline_testProxy(url, proxy):
    import requests
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')

