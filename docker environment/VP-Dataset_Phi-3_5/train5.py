import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def ground_truth_code_printLinks(url):
    ab = anonBrowser()
    ab.anonymize()
    page = ab.open(url)
    html = page.read()
    all_links = []
    try:
        link_finder = re.compile('href="(.*?)"')
        links = link_finder.findall(html)
        for link in links:
            all_links.append(link)
    except:
        pass
    try:
        soup = BeautifulSoup(html)
        links = soup.findAll(name='a')
        for link in links:
            if link.has_key('href'):
                all_links.append(link)
    except:
        pass
    return all_links

def persona_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append('<a href=')

def template_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        return [f'<a href= {links}']
    except: pass
    
import requests
import re
def question_refinement_printLinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        pattern = r'<a href="([^"]*)"[^>]*>(.*?)</a>'
        links = re.findall(pattern, html_content, re.DOTALL)
        complete_links = [f'<a href="{href}">{text}</a>' for href, text in links]
        return complete_links
    except: pass
    
import requests
import bs4
def alternative_approaches_printLinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        link = f'<a href="{tag.get("href")}">'
    except: pass

def context_manager_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href:
            links.append(str(a_tag))
    return links

import requests
from bs4 import BeautifulSoup
def iterative_prompting_3_printLinks(url):
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return(f"An error occurred: {e}")
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    return ['<a href="{}">{}</a>'.format(link['href'], link.text.strip()) for link in links]

def iterative_prompting_4_print_links(url):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse, urljoin
    if not isinstance(url, str) or not url.strip():
        raise ValueError("URL must be a non-empty, valid string")
    try:
        response = requests.get(url, timeout=float('inf'))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return(f"HTTP Request failed: {e}")
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    domain_name = urlparse(url).netloc
    for link in soup.find_all('a'):
        href = link.get('href', '')
        safe_href = urljoin(domain_name, urlparse(href).geturl())
        text = link.get_text(strip=True)
        if urlparse(safe_href).netloc == domain_name and text.strip():
            links.append(f'<a href="{safe_href}">{text}</a>')
    return links if links else None

def iterative_prompting_5_printLinks():
    pass

def few_shots_prompting_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    return [f'<a href="{link}"']

import requests
from bs4 import BeautifulSoup
def cot_prompting_printLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href:
            links.append(f'<a href="{href}">{a_tag.text}</a>')
    return links

def fact_check_list_extract_a_tags(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    response = requests.get(url)
    if response.status_code != 200:
        return(f"Error: Unable to fetch URL {url}. Status Code: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a', href=True)
    link_list = [f"<a href='{tag['href']}'>{tag.text}</a>" for tag in a_tags]
    return link_list

def not_interactive_mix_printLinks(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        a_tags_with_links = []
        for link in links:
            href = link.get('href')
            if href and href.startswith(('http://', 'https://')):
                full_tag = '<a href="{}">{}</a>'.format(href, link.text.strip())
                a_tags_with_links.append(full_tag)
        return a_tags_with_links
    except requests.RequestException as e:
        return(f"Error fetching URL: {e}")

def baseline_printLinks(url):
    import requests
    import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a')
    links = ['<a ' + tag.get('href') + '>' + tag.text + '</a>' for tag in a_tags]
    return links

