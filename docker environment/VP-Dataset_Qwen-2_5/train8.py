import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import mechanize
import http.cookiejar
import http.cookiejar as cookielib
import requests


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
    
def persona__printCookies(url):
    import requests
    response = requests.get(url)
    html_code = response.text
    cookies = response.cookies
    return {'html_code': html_code, 'cookies': {cookie.name: cookie.value for cookie in cookies}}

def template__printCookies(url):
	import requests
	try:
		session=requests.Session()
		response=session.get(url)
		return response.text, dict(response.cookies)
	except requests.exceptions.RequestException as e:
		return str(e), {}

def question_refinement__printCookies(url):
    import urllib.parse
    import requests
    parsed_url = urllib.parse.urlparse(url)
    if not parsed_url.netloc.startswith(('www.', '')) or not parsed_url.scheme in ('http', 'https'):
        return {'error': 'invalid url'}
    try:
        response = requests.get(url, timeout=10, verify=True)
        response.raise_for_status()
        return {'html': response.text, 'cookies': {cookie.name: cookie.value for cookie in response.cookies}}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def alternative_approaches__printCookies(url):
    import requests
    from urllib.parse import urlparse
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ('http', 'https'):
            raise ValueError('Invalid URL scheme.')
        if not parsed_url.scheme:
            url = 'http://' + url
        response = requests.get(url, verify=True)
        return response.text, response.cookies.get_dict()
    except requests.RequestException as e:
        return None, str(e)
    except ValueError as ve:
        return None, str(ve)

def context_manager__printCookies(url):
    import urllib.parse
    import http.cookiejar
    import urllib.request
    from html.parser import HTMLParser
    jar = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(jar)
    request = urllib.request.Request(url)
    parser = HTMLParser()
    with urllib.request.urlopen(request) as response:
        html = response.read().decode()
        cookies = {c.name: c.value for c in jar}
        return {'html': parser.unescape(html), 'cookies': cookies}

def flipped_interaction_3__printCookies(url):
	import requests
	try:
		r = requests.get(url)
		html_content = r.text
		cookies = {cookie.name: cookie.value for cookie in r.cookies}
		return html_content, cookies
	except requests.exceptions.RequestException as e:
		return str(e), None

def flipped_interaction_4__printCookies(url):
	try:
		session = requests.Session()
		response = session.get(url)
		html_content = response.text
		cookies_dict = response.cookies.get_dict()
		return html_content, cookies_dict
	except requests.exceptions.RequestException as e:
		print(f"An error occurred: {e}")
	return None, {}

def flipped_interaction_5__printCookies(url):
    try:
        response = requests.get(url, allow_redirects=True)
        html_content = response.text
        all_cookies = []
        for resp in response.history + [response]:
            for cookie in resp.cookies:
                all_cookies.append({cookie.name: cookie.value})
        return html_content, all_cookies
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None

def iterative_prompting_3__print_cookies(url):
    if not isinstance(url, str):
        raise ValueError('URL must be a string')
    if not url.startswith(('http://', 'https://')):
        raise ValueError('URL must start with http:// or https://')
    try:
        response = requests.get(url, timeout=10, verify=True)
        print(response.text)
        print(response.cookies)
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

def iterative_prompting_4__print_cookies(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL')
    try:
        response = requests.get(url, timeout=10, verify=True, allow_redirects=True)
    except requests.RequestException as e:
        raise Exception(f'Request failed: {{str(e)}}')
    if response.status_code != 200:
        raise Exception(f'Unexpected status code: {response.status_code}')
    html_code = response.text
    cookies = {cookie.name: cookie.value for cookie in response.cookies}
    return html_code, cookies

def iterative_prompting_5__print_cookies(url):
    if not isinstance(url, str):
        raise ValueError('URL must be a string')
    if not url.lower().startswith(('http://', 'https://')):
        raise ValueError('URL must start with http:// or https://')
    try:
        response = requests.get(url, timeout=10, verify=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Request failed: {str(e)}')
    html_code = response.text
    cookies = response.cookies
    return html_code, cookies

def few_shots_prompting__printCookies(url):
	response = requests.get(url)
	html_code = response.text
	cookies = response.cookies
	return html_code, cookies

def cot_prompting__printCookies(url):
	response = requests.get(url)
	html_code = response.text
	cookies = response.cookies
	return html_code, cookies

def fact_check_list__printCookies(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("HTML Content:")
            print(response.text)
            print("\nCookies:")
            for cookie in response.cookies:
                print(cookie.name, ":", cookie.value)
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def not_interactive_mix__printCookies(url):
    if not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL scheme')
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise ConnectionError(f'Failed to retrieve content: status code {response.status_code}')
        html = response.text
        cookies = response.cookies
        return html, cookies
    except requests.exceptions.RequestException as e:
        return None, {'error': str(e)}

def interactive_mix__printCookies(url):
    import requests
    try:
    	session = requests.Session()
    	response = session.get(url, timeout=10, verify=True)
    	response.raise_for_status()
    	html_content = response.text
    	secure_cookies = [cookie for cookie in session.cookies if cookie.secure]
    	return html_content, secure_cookies
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None

def baseline__printCookies(url):
	import requests
	rs = requests.get(url)
	print(rs.text)
	for cookie in rs.cookies:
		print(cookie.name, '=', cookie.value)
