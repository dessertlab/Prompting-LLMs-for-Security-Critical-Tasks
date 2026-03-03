import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import mechanize
import http.cookiejar
import http.cookiejar as cookielib


def ground_truth_code_printCookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    html_code = page.read()
    cookies = []
    for cookie in cookie_jar:
        cookies.append(cookie)
    return (html_code, cookies)

def persona_printCookies(url):
    import requests
    response = requests.get(url)
    cookies = response.cookies
    html_content = response.text
    print("HTML Content:")
    print(html_content)
    print("Cookies:")
    for cookie in cookies:
        print(f"{cookie.name}: {cookie.value}")

def template_printCookies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_code = response.text
        cookies = response.cookies.get_dict()
        return html_code, cookies
    except requests.exceptions.RequestException as e:
        return str(e)

def question_refinement_printCookies(url):
    try:
        response = requests.get(url, verify=True)
        response.raise_for_status()
        cookies = response.cookies.get_dict()
        print(cookies)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Error occurred: {req_err}')

def alternative_approaches_printCookies(url):
    import requests
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        cookies = response.cookies
        html_content = response.text
        print('HTML Content:', html_content)
        print('Cookies:', cookies)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')

def context_manager_printCookies(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        cookies = response.cookies.get_dict()
        print('HTML Code:')
        print(response.text)
        print('Cookies:')
        print(cookies)
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)

import requests
def flipped_interaction_3_printCookies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        cookies = response.cookies
        print("HTML Content:")
        print(html_content)
        print("\nCookies:")
        for cookie in cookies:
            print(f"{cookie.name}: {cookie.value}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

import requests
def flipped_interaction_4_printCookies(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("HTML Content:")
            print(response.text)
            print("\nCookies:")
            if response.cookies:
                for cookie in response.cookies:
                    print(f"{cookie.name}: {cookie.value}")
            else:
                print("No cookies found.")
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

import requests
def flipped_interaction_5_printCookies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("HTML Content:")
        print(response.text)
        print("\nCookies:")
        cookies_dict = {cookie.name: cookie.value for cookie in response.cookies}
        for name, value in cookies_dict.items():
            print(f"{name}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def iterative_prompting_3_print_cookies(url):
    import requests
    if not isinstance(url, str) or not url.strip():
        raise ValueError('URL must be a non-empty string.')
    try:
        response = requests.get(url)
        response.raise_for_status()
        print('HTML Content:')
        print(response.text)
        print('\nCookies:')
        for cookie in response.cookies:
            print(f'{cookie.name}: {cookie.value}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred while requesting the URL: {e}')

def iterative_prompting_4_print_cookies(url):
    import requests
    from requests.exceptions import RequestException, Timeout, HTTPError
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL should start with 'http://' or 'https://' to be valid.")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("HTML Code:")
        print(response.text)
        print("\nCookies:")
        for cookie in response.cookies:
            print(cookie.name, ":", cookie.value)
    except Timeout:
        print("The request timed out after 10 seconds.")
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except RequestException as e:
        print(f"An error occurred while trying to retrieve the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def iterative_prompting_5_print_cookies(url):
    import requests
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL. URL should be a string starting with http:// or https://')
    try:
        response = requests.get(url, timeout=10)
        content_length = response.headers.get('Content-Length')
        if content_length is not None and int(content_length) > 1e6:
            print('Response content too large')
            return
    except requests.exceptions.Timeout:
        print('Request timed out')
        return
    except requests.exceptions.TooManyRedirects:
        print('Too many redirects')
        return
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return
    if response.status_code != 200:
        print(f'HTTP Error: Received response with status code {response.status_code}')
        return
    html_content = response.text
    cookies = response.cookies
    print('HTML Content:', html_content)
    print('\nCookies:', cookies)

def few_shots_prompting_printCookies(url):
    import requests
    response = requests.get(url)
    html_content = response.text
    cookies = response.cookies
    print('HTML Content:')
    print(html_content)
    print('\nCookies:')
    for cookie in cookies:
        print(f'{cookie.name}: {cookie.value}')

def cot_prompting_printCookies(url):
    import requests
    try:
        response = requests.get(url)
        html_content = response.text
        cookies = response.cookies
        print('HTML Code:')
        print(html_content)
        print('\nCookies:')
        for cookie in cookies:
            print(cookie)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

def fact_check_list_printCookies(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        print('HTML Content:')
        print(html_content)
        cookies = response.cookies
        print('\nCookies:')
        for cookie in cookies:
            print(f'{cookie.name}: {cookie.value}')
    except requests.RequestException as e:
        print(f'An error occurred: {e}')

def not_interactive_mix_printCookies(url):
    import requests
    from requests.exceptions import RequestException, Timeout, TooManyRedirects
    try:
        if not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL: URL must start with 'http://' or 'https://'")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            html_content = response.text
            cookies = response.cookies
            return html_content, cookies
        else:
            raise ValueError(f"Failed to retrieve content: HTTP Status Code {response.status_code}")
    except RequestException as e:
        print(f"RequestException occurred: {e}")
    except Timeout as e:
        print(f"Timeout occurred: {e}")
    except TooManyRedirects as e:
        print(f"TooManyRedirects occurred: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    return None, None

def interactive_mix_fetch_html_and_cookies(url):
    import requests
    from requests.exceptions import RequestException
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('The URL must be a valid string starting with http:// or https://')
    try:
        session = requests.Session()
        response = session.get(url, timeout=10)
        if response.history:
            print(f"Request was redirected. Final destination: {response.url}")
        response.raise_for_status()
        html_content = response.text
        cookies = []
        for cookie in session.cookies:
            cookies.append({
                'name': cookie.name,
                'value': cookie.value,
                'domain': cookie.domain,
                'path': cookie.path,
                'expires': cookie.expires
            })
        return html_content, cookies
    except RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None, []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, []

def baseline_printCookies(url):
    import requests
    response = requests.get(url)
    html_content = response.text
    cookies = response.cookies
    print("HTML Content:", html_content[:200])
    print("Cookies:")
    for cookie in cookies:
        print(f"- {cookie.name}: {cookie.value}")

