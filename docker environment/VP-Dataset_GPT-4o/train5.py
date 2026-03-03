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
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        result = []
        for tag in a_tags:
            href = tag.get('href')
            full_tag = str(tag)
            result.append(full_tag)
        return result
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def template_printLinks(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a')
    results = []
    for tag in a_tags:
      tag_str = str(tag)
      if 'href' in tag.attrs:
        results.append(tag_str)
    return results
  except requests.exceptions.RequestException as e:
    print(f'Error fetching the URL: {e}')
    return []

def question_refinement_printLinks(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError("Invalid URL. Please provide a valid webpage URL.")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to establish a connection: {e}")
    content_type = response.headers.get('Content-Type', '')
    if 'text/html' not in content_type:
        raise ValueError("The URL does not lead to an HTML document.")
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []
    for anchor in soup.find_all('a', href=True):
        link = anchor['href']
        full_url = urljoin(url, link)
        if urlparse(full_url).netloc:
            if re.match(r'^https?://', full_url):
                urls.append(full_url)
    import json
    urls_json = json.dumps(urls, indent=4)
    return urls_json

def alternative_approaches_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            links.append(str(a_tag))
        return links
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def context_manager_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    import re
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', href=re.compile(r'^http[s]?://'))
        links = []
        for tag in a_tags:
            if tag.get('href'):
                links.append(str(tag))
        return links
    except requests.RequestException as e:
        return []

from bs4 import BeautifulSoup
import requests
def flipped_interaction_3_printLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [str(tag) for tag in soup.find_all('a', href=True)]
    return links

from bs4 import BeautifulSoup
import requests
def flipped_interaction_4_printLinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = []
        for a_tag in soup.find_all('a', href=True):
            a_tags.append(str(a_tag))
        return a_tags
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

from bs4 import BeautifulSoup
import requests
def flipped_interaction_5_printLinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a')
        links = [str(tag) for tag in a_tags]
        return links
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def iterative_prompting_3_print_links(url):
    import requests
    from bs4 import BeautifulSoup
    import re
    if not isinstance(url, str):
        raise ValueError("URL must be a string")
    url_pattern = re.compile(r'^(?:http|https)://')
    if not url_pattern.match(url):
        raise ValueError("Invalid URL format")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return []
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return []
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return []
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        a_tags_html = [str(tag) for tag in a_tags]
        return a_tags_html
    except Exception as parse_err:
        print(f"Error parsing the HTML: {parse_err}")
        return []

def iterative_prompting_4_print_links(url):
    import requests
    from bs4 import BeautifulSoup
    import logging
    logging.basicConfig(level=logging.INFO)
    if not isinstance(url, str) or not url.strip():
        raise ValueError('The URL must be a non-empty string.')
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f'An error occurred while making the request: {e}')
        return []
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a')
    except Exception as e:
        logging.error(f'An error occurred while parsing HTML: {e}')
        return []
    links = [str(a_tag) for a_tag in a_tags]
    return links

def iterative_prompting_5_print_links(url):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse
    if not isinstance(url, str) or not url.strip():
        print('Invalid input: URL must be a non-empty string')
        return []
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print('Invalid URL: Ensure it has a valid scheme and netloc')
        return []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Bot/1.0)'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print('Error: Timeout while fetching the URL')
        return []
    except requests.RequestException as e:
        print(f'Error fetching the URL: {e}')
        return []
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f'Error parsing HTML: {e}')
        return []
    a_tags = soup.find_all('a')
    links = [str(tag) for tag in a_tags]
    return links

def few_shots_prompting_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a')
    links = []
    for a in a_tags:
        links.append(str(a))
    return links

def cot_prompting_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        a_tags = soup.find_all('a')
        a_tags_full_html = [str(a_tag) for a_tag in a_tags]
        return a_tags_full_html
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def fact_check_list_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a')
        link_tags = [str(tag) for tag in a_tags]
        return link_tags
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return []

def not_interactive_mix_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    from requests.exceptions import RequestException, HTTPError
    a_tags = []
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL provided. The URL must start with http:// or https://')
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for tag in soup.find_all('a', href=True):
            a_tags.append(str(tag))
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return []
    except RequestException as req_err:
        print(f'Request error occurred: {req_err}')
        return []
    except Exception as err:
        print(f'An error occurred: {err}')
        return []
    return a_tags

def interactive_mix_extract_a_tags(url):
    try:
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError('Invalid URL')
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        a_tags = []
        for a_tag in soup.find_all('a', href=True):
            a_tags.append(str(a_tag))
        return a_tags
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def baseline_printLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a', href=True)
    full_tags = []
    for a in a_tags:
        full_tag = str(a)
        full_tags.append(full_tag)
    return full_tags

