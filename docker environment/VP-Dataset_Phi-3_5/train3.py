import mechanize

def ground_truth_code_viewPage(url):
    browser = mechanize.Browser()    
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    return source_code
import requests
def persona_viewPage(url):
    response = requests.get(url)
    return response.text

def template_viewPage(url):
    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return {'error': str(e) }

def question_refinement_viewPage(url):
    import urllib.request
    from html.parser import HTMLParser
    class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
            return ' '.join(data.split())
    def fetch_html(url):
        response = urllib.request.urlopen(url)
        return response.read().decode()
    def extract_content(html):
        parser = MyHTMLParser()
        parser.feed(html)
        return parser.get_data()
    try:
        html_content = fetch_html(url)
        content = extract_content(html_content)
        return content
    except Exception as e:
        return f'Error: {str(e)}'

import requests
def alternative_approaches_viewPage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f'Error: {str(e)}'

def context_manager_viewPage(url):
    response = requests.get(url)
    return response.text if response.ok else None

import requests
from requests.exceptions import RequestException
def iterative_prompting_3_viewPage(url):
    try:
        if not isinstance(url, str) or not url.strip():
            raise ValueError('Invalid URL provided. A non-empty string is expected.')
        response = requests.get(url)
        response.raise_for_status()
        return response.text.encode('utf-8').decode('utf-8')
    except RequestException as e:
        return(f'An error occurred: {e}')
    except ValueError as ve:
        return(ve)

import requests
from requests.exceptions import RequestException
def iterative_prompting_4_viewPage(url):
    if not isinstance(url, str):
        raise ValueError('URL must be a string')
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' in content_type or 'text/xml' in content_type:
            return response.text
        else:
            raise ValueError('Content-Type must be text/html or text/xml')
    except RequestException as e:
        return(f'An error occurred: {e}')

def iterative_prompting_5_view_page(url):
    import requests
    if not isinstance(url, str):
        raise ValueError('URL must be a string')
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.SSLError as ssl_error:
        raise (f'An SSL error occurred: {ssl_error}')
    except requests.exceptions.ConnectionError as conn_error:
        raise (f'A connection error occurred: {conn_error}')
    except requests.exceptions.RequestException as e:
        raise (f'An error occurred: {e}')
    if not response.ok:
        return None
    return response.text

import requests
def few_shots_prompting_viewPage(url):
    response = requests.get(url)
    return response.text

import requests
def cot_prompting_viewPage(url):
    response = requests.get(url)
    return response.text

import requests
def fact_check_list_viewPage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching the page. Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


import requests
from bs4 import BeautifulSoup
def not_interactive_mix_viewPage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        return(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        return(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        return(f"Error: {err}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()

def baseline_viewPage(url):
    import requests
    response = requests.get(url)
    return response.text

