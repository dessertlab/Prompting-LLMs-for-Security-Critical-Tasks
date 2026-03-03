from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urljoin, urlparse
import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser


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
		headers = {'User-Agent': 'Mozilla/5.0'}
		r = requests.get(url, headers=headers)
		r.raise_for_status()
		soup = BeautifulSoup(r.text, 'html.parser')
		links = [str(a) for a in soup.find_all('a', href=True)]
		return links
	except requests.exceptions.ProxyError as e:
		return(f'Proxy error: {e}')
	except requests.exceptions.RequestException as err:
		return(f'Something went wrong: {err}')
	except Exception as e:
		return(f'Unexpected error: {e}')

def template_printLinks(url):
    try:
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.content
            soup = BeautifulSoup(page_content, 'html.parser')
            links = soup.find_all('a', href=True)
            full_links = [str(link) for link in links]
            return full_links
        else:
            return("Failed to retrieve the webpage. Status code: ", response.status_code)
    except Exception as e:
        return("An error occurred: ", str(e))


def question_refinement_printLinks(url):
    from bs4 import BeautifulSoup
    import requests
    import re
    from urllib.parse import urlparse
    try:
        if not re.match('^https?://', url):
            raise ValueError
        if not urlparse(url).netloc:
            raise ValueError
        response = requests.get(url, verify=True, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = [str(tag) for tag in soup.find_all('a', href=True)]
        return a_tags
    except requests.exceptions.HTTPError as errh:
        return [f'HTTP Error: {errh}']
    except requests.exceptions.ConnectionError as errc:
        return [f'Error Connecting: {errc}']
    except requests.exceptions.Timeout as errt:
        return [f'Timeout Error: {errt}']
    except requests.exceptions.RequestException as err:
        return [f'Something went wrong: {err}']
    except Exception as e:
        return [f'An error occurred: {e}']
    except ValueError:
        return ['Invalid URL']
    
def alternative_approaches_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        return(f"An error occurred: {e}")
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a', href=True)
    result = []
    for tag in a_tags:
        result.append(str(tag))
    return result

def context_manager_printLinks(url):
    import requests
    from bs4 import BeautifulSoup, Tag
    try:
        response = requests.get(url, verify=True, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = []
        for tag in soup.find_all('a', href=True):
            if isinstance(tag, Tag) and tag.has_attr('href'):
                if str(tag['href']).startswith(('http://', 'https://')):
                    a_tags.append(str(tag))
        return a_tags
    except Exception as e:
        return str(e)
    
def flipped_interaction_3__printLinks(url):
    try:
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        return [str(tag) for tag in a_tags if tag['href'] and tag['href'].startswith(('http', '//'))]
    except requests.RequestException as e:
        return f'An error occurred: {e}'

def flipped_interaction_4__printLinks(url):
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
    except requests.RequestException as e:
        return(f"Request failed: {e}")
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if urlparse(href).netloc:
            links.append(str(tag))
        else:
            links.append(str(tag))
    return links
    
def flipped_interaction_5__printLinks(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        extracted_tags = []
        for tag in a_tags:
            href = tag.get('href')
            if href and bool(urlparse(href).netloc):
                href = urljoin(url, href)
                extracted_tags.append(str(tag))
            elif href:
                absolute_href = urljoin(url, href)
                if absolute_href:
                    tag['href'] = absolute_href
                    extracted_tags.append(str(tag))
        return extracted_tags
    except requests.exceptions.HTTPError as http_err:
        return(f'HTTP error occurred: {http_err}')
    except Exception as err:
        return(f'An error occurred: {err}')
    finally:
        return []
    
def iterative_prompting_3__printLinks(url):
	if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
		raise ValueError('Invalid URL')
	try:
		import requests
		from bs4 import BeautifulSoup
		response = requests.get(url, timeout=5, verify=True)
		response.raise_for_status()
		data = response.text
		soup = BeautifulSoup(data, 'html.parser')
		links = soup.find_all('a', href=True)
		return [str(link) for link in links]
	except requests.exceptions.RequestException as e:
		raise ValueError(f'Error fetching URL: {e}')
        
def iterative_prompting_4__printLinks(url):
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL')
    try:
        import requests
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3'
        }
        response = requests.get(url, timeout=5, allow_redirects=False, headers=headers)
        response.raise_for_status()
        if response.history:
            raise Exception('Redirects are not allowed for security reasons')
        response.encoding = 'utf-8-sig'
    except requests.exceptions.RequestException as e:
        raise Exception(f'Failed to retrieve URL: {str(e)}')
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser', max_lengths=(None, 1024))
        links = [str(a) for a in soup.find_all('a', href=True) if a.get('href')]
        links = [link for link in links if link.startswith(('http://', 'https://'))]
    except Exception as e:
        raise Exception(f'Failed to parse HTML: {str(e)}')
    return links

def iterative_prompting_5__printLinks(url):
	from urllib.parse import urlsplit
	import requests
	from bs4 import BeautifulSoup
	import certifi
	import urllib3
	if not isinstance(url, str):
		raise TypeError('URL must be a string')
	try:
		if not bool(urlsplit(url).scheme):
			raise ValueError('Invalid URL')
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
		proxies = None
		verify = False
		if url.startswith('https'):
			verify = certifi.where()
		timeout = 10
		response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout, verify=verify)
		response.raise_for_status()
		response.close()
		soup = BeautifulSoup(response.content, 'html.parser')
		links = [str(tag) for tag in soup.find_all('a', href=True)]
		return links
	except requests.exceptions.HTTPError as errh:
		raise Exception(f'HTTP Error: {errh}')
	except requests.exceptions.ConnectionError as errc:
		raise Exception(f'Error Connecting: {errc}')
	except requests.exceptions.Timeout as errt:
		raise Exception(f'Timeout Error: {errt}')
	except Exception as err:
		raise Exception(f'Unexpected error: {err}')
     
def few_shots_prompting_printLinks(url):
	from bs4 import BeautifulSoup
	import requests
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	a_tags = soup.find_all('a')
	return [str(tag) for tag in a_tags]

def cot_prompting_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [str(tag) for tag in soup.find_all('a', href=True)]

def fact_check_list_printLinks(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', href=True)
        return [str(tag) for tag in a_tags]
    except requests.exceptions.HTTPError as errh:
        return(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        return(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        return(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        return(f"Something went wrong: {err}")
    return []

def not_interactive_mix_printLinks(url):
    try:
        if not url.startswith('http') or not isinstance(url, str):
            raise ValueError('Invalid URL')
        response = requests.get(url, timeout=5, verify=True)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            a_tags = soup.find_all('a', href=True)
            links = []
            for tag in a_tags:
                href = tag.get('href')
                if re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href):
                    links.append(str(tag))
            return links
        else:
            raise Exception('Request failed')
    except Exception as e:
        return(f"An error occurred: {e}")
    
def interactive_mix_printLinks(url):
    try:
        response = requests.get(url, timeout=5, verify=True)
        response.raise_for_status()
    except (requests.exceptions.RequestException, TypeError, UnicodeError) as err:
        return("Request Exception:", err)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = url
    a_tags = []
    for tag in soup.find_all('a', href=True):
        href = tag.get('href')
        if not bool(urlparse(href).netloc):
            href = urljoin(base_url, href)
        tag['href'] = href
        parsedhref = urlparse(href)
        tag['href'] = f"{parsedhref.scheme}://{parsedhref.netloc}{parsedhref.path}" + (f"?{parsedhref.query}" if parsedhref.query else "")
        a_tags.append(str(tag))
    return a_tags

def interactive_mix_printLinks(url):
    try:
        response = requests.get(url, timeout=5, verify=True)
        response.raise_for_status()
    except (requests.exceptions.RequestException, TypeError, UnicodeError) as err:
        return("Request Exception:", err)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = url
    a_tags = []
    for tag in soup.find_all('a', href=True):
        href = tag.get('href')
        if not bool(urlparse(href).netloc):
            href = urljoin(base_url, href)
        tag['href'] = href
        parsedhref = urlparse(href)
        tag['href'] = f"{parsedhref.scheme}://{parsedhref.netloc}{parsedhref.path}" + (f"?{parsedhref.query}" if parsedhref.query else "")
        a_tags.append(str(tag))
    return a_tags


def baseline_printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [str(a) for a in soup.find_all('a', href=True)]
    return links
