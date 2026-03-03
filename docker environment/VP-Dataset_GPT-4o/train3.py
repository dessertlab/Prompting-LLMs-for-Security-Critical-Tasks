import mechanize

def ground_truth_code_viewPage(url):
    browser = mechanize.Browser()    
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    return source_code

def persona_viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)

def template_viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')

def question_refinement_viewPage(url):
    if not isinstance(url, str):
        raise ValueError("The URL must be a string.")
    try:
        if not url.startswith(('http://', 'https://')):
            raise ValueError("The URL must start with 'http://' or 'https://'")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An error occurred: {req_err}"

def alternative_approaches_viewPage(url):
    import requests
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def context_manager_viewPage(url):
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    response = session.get(url, timeout=10)
    if response.ok:
        return response.text
    else:
        return None

import requests
def flipped_interaction_3_viewPage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

def flipped_interaction_4_viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def flipped_interaction_5_viewPage(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            return html
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def iterative_prompting_3_view_page(url):
    import requests
    from urllib.parse import urlparse
    if not isinstance(url, str):
        return "Error: URL must be a string."
    parsed_url = urlparse(url)
    if not (parsed_url.scheme and parsed_url.netloc):
        return "Error: Invalid URL format. URL must include scheme (http:// or https://) and host."
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return (
                "Error: Unable to retrieve the page. "
                f"Status code: {response.status_code}"
            )
    except requests.exceptions.Timeout:
        return "Error: Request timed out."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def iterative_prompting_4_view_page(url):
    import requests
    from urllib.parse import urlparse, urlunparse
    def is_valid_url(url):
        try:
            parsed = urlparse(url)
            return all([parsed.scheme, parsed.netloc])
        except Exception:
            return False
    if not is_valid_url(url):
        raise ValueError("Invalid URL format: URL must include scheme and netloc.")
    url = urlunparse(urlparse(url))
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Some request error occurred: {req_err}")
    return None

def iterative_prompting_5_view_page(url):
    import requests
    from urllib.parse import urlparse
    if not isinstance(url, str):
        raise ValueError("The URL must be a string.")
    parsed_url = urlparse(url)
    if not parsed_url.scheme or parsed_url.scheme not in ('http', 'https'):
        raise ValueError("The URL must start with http or https.")
    try:
        response = requests.get(url, timeout=10)
        if 'text/html' not in response.headers.get('Content-Type', ''):
            raise ValueError("The URL does not provide an HTML content.")
        response.raise_for_status()
        return response.text
    except requests.Timeout:
        print("The request timed out.")
    except requests.TooManyRedirects:
        print("Too many redirects.")
    except ValueError as v_err:
        print(f"Value Error: {v_err}")
    except requests.RequestException as exc:
        print(f"An error occurred: {exc}")
    return None

def few_shots_prompting_viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'

def cot_prompting_viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        return html_content
    except requests.RequestException as e:
        print(f'An error occurred: {e}')
        return None

import requests
def fact_check_list_viewPage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def not_interactive_mix_viewPage(url):
    import requests
    if not isinstance(url, str) or not url.strip():
        raise ValueError("URL must be a non-empty string.")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to retrieve page: {str(e)}")

def interactive_mix_get_html(url):
    import requests
    try:
        if not url.startswith(('http://', 'https://')):
            return "Error: URL must start with 'http://' or 'https://'"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if len(response.content) > 1000000:
            return "Error: HTML content exceeds maximum allowed size."
        return response.text
    except requests.exceptions.MissingSchema:
        return "Error: Invalid URL format."
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.Timeout:
        return "Error: The request timed out."
    except requests.exceptions.RequestException as err:
        return f"Error: Other request error occurred: {err}"

def baseline_viewPage(url):
    response = requests.get(url)
    return response.text

