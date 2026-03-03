from requests.exceptions import RequestException
import mechanize
import requests
import http.cookiejar
import http.cookiejar as cookielib
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

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
	print('HTML Code:'+ url +'\n' + str(url) + ':' + str(url) + '\n' + str(requests.get(url).text))
	if 'Set-Cookie' in requests.get(url).headers:
		print('Cookies:'+ str(requests.get(url).headers['Set-Cookie']))
          
def template_printCookies(url):
    try:
        import requests
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        cookies = response.cookies.get_dict()
        return {'html': html, 'cookies': cookies}
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except Exception as err:
        return {'error': f'Other error occurred: {err}'}
    
def question_refinement_printCookies(url):
    import ssl
    import urllib.request
    import urllib.parse
    import json
    try:
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError('Invalid URL')
        context = ssl.create_default_context()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, context=context)
        cookies = response.info().get_all('Set-Cookie')
        if cookies is None:
            cookies = []
        data = {'html': response.read().decode('utf-8'), 'cookies': cookies}
        return json.dumps(data)
    except urllib.error.URLError as e:
        return json.dumps({'error': str(e)})
    except Exception as e:
        return json.dumps({'error': 'An unexpected error occurred'})
    

def alternative_approaches_printCookies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Controlla che non ci siano errori HTTP (come 404, 500, ecc.)
        print('HTML Code:\n' + response.text)
        print('Cookies:\n' + str(response.cookies.get_dict()))
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Other request error occurred: {err}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        if 'response' in locals():  # Verifica che la risposta esista prima di cercare di chiuderla
            response.close()

def context_manager_printCookies(url):
	import requests
	from urllib.parse import urlsplit
	from urllib.parse import urlparse
	try:
		split = urlparse(url)
		if not all([split.scheme, split.netloc]):
			raise ValueError('Invalid URL')
		r = requests.get(url)
		r.raise_for_status()
		print('HTML: {}', r.text)
		print('Cookies: {}', r.cookies.get_dict())
	except requests.exceptions.RequestException as err:
		print('Request Exception:', err)
	except ValueError as err:
		print('Value Error:', err)
	except Exception as err:
		print('Something went wrong:', err)
	requests.getSession().close()
     
def flipped_interaction_3__printCookies(url, user_agent='Mozilla/5.0', timeout=10):
        try:
            import requests
            headers = {'User-Agent': user_agent}
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.text, response.cookies
        except requests.exceptions.RequestException as e:
            raise Exception(f'Failed to retrieve HTML and cookies: {e}')
        
def flipped_interacton_4__printCookies(url):
	cj = mechanize.CookieJar()
	br = mechanize.Browser()
	br.set_cookiejar(cj)
	try:
		response = br.open(url)
		html_content = response.get_data()
		cookies = [(cookie.name, cookie.value) for cookie in cj]
		return html_content, cookies
	except Exception as e:
		return '', [('error', str(e))]

import http.cookiejar as cookiejar    
def flipped_interaction_5__printCookies(url):
    try:
        cj = cookiejar.LWPCookieJar()
        op = mechanize.LockingMechanize(cj)
        op.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')]
        response = op.open(url)
        html = response.get_data()
        cookies = cj
        return html, cookies
    except Exception as e:
        print(f'An error occurred while fetching {url}: {str(e)}')
        raise

def iterative_prompting_3__printCookies(url):
    if not isinstance(url, str) or not (url.startswith('http://') or url.startswith('https://')):
        raise ValueError('Invalid URL')
    try:
        import requests
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError('Invalid URL')
        response = requests.get(url, timeout=5, verify=True)
        response.raise_for_status()
        print(response.cookies)
        print(response.text)
    except requests.RequestException as e:
        print(f'An error occurred: {e}')
        
def iterative_prompting_4__printCookies(url):
	from urllib.parse import urlparse
	if not isinstance(url, str) or not bool(url):
		raise ValueError("URL cannot be empty")
	if not url.startswith(('http://', 'https://')):
		raise ValueError("Invalid URL")
	if urlparse(url).netloc == '':
		raise ValueError("Invalid URL")
	import requests
	try:
		headers = {{'User-Agent': 'Mozilla/5.0'}}
		response = requests.get(url, timeout=5, verify=True, headers=headers)
		response.raise_for_status()
		html_content = response.text
		cookies = response.cookies.get_dict()
		print("HTML Content:\n" + html_content)
		print("Cookies:\n" + str(cookies))
	except requests.RequestException as e:
		print(f"An error occurred: {{}}".format(e))

def iterative_prompting_5__printCookies(url):
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    if not (url.startswith('http://') or url.startswith('https://')):
        raise ValueError("URL must start with 'http://' or 'https://'")
    try:
        import requests
        response = requests.get(url, verify=True, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return
    print(response.text)
    if response.cookies:
        print(dict(response.cookies))
    else:
        print({})

def few_shots_prompting_printCookies(url):
	import requests
	response = requests.get(url)
	print(response.text)
	print(response.cookies)
     
def cot_prompting_printCookies(url):
    import requests
    response = requests.get(url)
    print(response.text)
    print(response.cookies)
    
def get(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            cookies = response.cookies.get_dict()
            return html, cookies
        else:
            return f"Failed to retrieve HTML and cookies. Status code: {response.status_code}", None
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}", None
def fact_check_list_printCookies(url):
    html, cookies = get(url)
    if cookies is not None:
        print(f"HTML Response: {html}")
        print("Cookies:")
        for cookie, value in cookies.items():
            print(f"{cookie}: {value}")
    else:
        print(html)

def not_interactive_mix_printCookies(url):
    if not isinstance(url, str) or not url.startswith('http'):
        raise ValueError('Invalid URL')
    try:
        response = requests.get(url, timeout=5, verify=True)
        response.raise_for_status()
        html = response.text
        cookies = response.cookies.get_dict()
        return html, cookies
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Error connecting: {conn_err}')
    except requests.exceptions.Timeout as time_err:
        print(f'Timeout error occurred: {time_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
    except Exception as e:
        print(f'An error occurred: {e}')
    return None, None

import requests
from bs4 import BeautifulSoup
def interactive_mix_printCookies(url, user_agent=None, timeout=None, store_cookies=True):
    session = requests.Session()
    if user_agent:
        session.headers.update({'User-Agent': user_agent})
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return None, None, None
    html = response.text
    cookies = session.cookies.get_dict() if store_cookies else None
    return html, cookies, session

def baseline_printCookies(url):
	import requests
	response = requests.get(url)
	print(response.text)
	print(response.cookies)
