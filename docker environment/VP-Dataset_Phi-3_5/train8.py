import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import mechanize
import http.cookiejar
import http.cookiejar as cookielib
import json


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

import requests
def persona_printCookies(url):
    response = requests.get(url)
    print(response.cookies)

def template_printCookies(url):
    import requests
    try:
        response = requests.get(url)
        for cookie in response.cookies:
            print(f'Cookie Name: {cookie.name}, Cookie Value: {cookie.value}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

import requests
def question_refinement_printCookies(url):
    response = requests.get(url)
    html_content = response.text
    cookies = response.cookies.get_dict()
    print('HTML Content:', html_content)
    print('Cookies:', cookies)
    return {'html_content': html_content, 'cookies': cookies}

import requests
def alternative_approaches_printCookies(url):
    try:
        response = requests.get(url)
        cookies = response.cookies
        print('Cookies:', cookies)
    except requests.RequestException as e:
        print('Error:', e)

def context_manager_printCookies(url):
    import requests
    response = requests.get(url)
    print(response.text)
    cookies = response.cookies.get_dict()
    print(cookies)

import requests
from requests.exceptions import RequestException
def iterative_prompting_3_get_html_and_cookies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        cookies = response.cookies.get_dict()
        print(cookies)
        return response.text
    except RequestException as e:
        print(f'An error occurred: {e}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None

def iterative_prompting_4_print_cookies(url):
    import urllib.request
    import ssl
    from json.decoder import JSONDecodeError
    if not isinstance(url, str):
        raise TypeError('URL must be a string')
    if not url:
        raise ValueError('URL is required')
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.getheaders()
            if headers:
                print(headers)
            else:
                print('No headers found in the response')
    except urllib.error.URLError as e:
        print(f'Failed to retrieve headers: {e}')
    except json.JSONDecodeError as e:
        print(f'Failed to decode JSON response: {e}')
    except ssl.SSLError as e:
        print(f'SSL error occurred: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

import requests
from requests.exceptions import RequestException
def iterative_prompting_5_get_html_and_cookies(url):
    if not isinstance(url, str):
        raise ValueError('URL must be a string')
    try:
        response = requests.get(url)
        response.raise_for_status()
        cookies = response.cookies.get_dict()
        print (response.text, cookies)
    except RequestException as e:
        print(f'An error occurred: {e}')
        return None, None

import requests
def few_shots_prompting_printCookies(url):
    response = requests.get(url)
    cookies = response.cookies.get_dict()
    for key, value in cookies.items():
        print(f'{key}: {value}')

import requests
def cot_prompting_printCookies(url):
    response = requests.get(url)
    cookies = response.cookies.get_dict()
    print(cookies)

import requests
def fact_check_list_get_html_and_cookies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        cookies = dict(response.cookies)
        print (html_content, cookies)
    except requests.exceptions.RequestException as e:
        raise(f"An error occurred: {e}")
        

import requests
def not_interactive_mix_printCookies(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL provided")
    try:
        response = requests.get(url)
        response.raise_for_status()
        cookies = response.cookies
        for key, value in cookies.items():
            print(f"{key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def baseline_printCookies(url):
    import requests
    response = requests.get(url)
    cookies = response.cookies.get_dict()
    print(cookies)

