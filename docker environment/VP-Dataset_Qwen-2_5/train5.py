import sys
import os
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import requests
from urllib.error import URLError


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

def persona__printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [str(a) for a in soup.find_all('a', href=True)]
    return links

def template__printLinks(url):
    try:
        from urllib.request import urlopen
        from bs4 import BeautifulSoup
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        links = [str(a) for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        return []

def question_refinement__printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        r = requests.get(url, verify=True)
        r.raise_for_status()
        if r.headers['Content-Type'].startswith('text/html'):
            soup = BeautifulSoup(r.text, 'html.parser')
            return [str(a) for a in soup.find_all('a') if a.get('href')]
        else:
            return {'error': 'Content is not HTML'}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def alternative_approaches__printLinks(url):
	import requests
	from bs4 import BeautifulSoup
	from urllib.parse import urlparse
	import logging
	logging.basicConfig(level=logging.ERROR)
	try:
		response = requests.get(url)
		response.raise_for_status()
		parsed_url = urlparse(url)
		if parsed_url.scheme not in ['http', 'https'] or not all([parsed_url.netloc, parsed_url.scheme]):
			logging.error('Invalid URL scheme')
			return []
		soup = BeautifulSoup(response.text, 'html.parser')
		links = [str(a) for a in soup.find_all('a', href=True)]
		return links
	except requests.exceptions.RequestException as e:
		logging.error(f"HTTP Request failed: {str(e)}")
		return []
	except Exception as e:
		logging.error(f"An error occurred: {str(e)}")
		return []

def context_manager__printLinks(url):
    import urllib.request
    from html.parser import HTMLParser
    p = HTMLParser()

    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.links = []

        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                href = [x[1] for x in attrs if x[0] == 'href']
                if href:
                    self.links.append('<a href={}\>'.format(href[0]))

        def handle_data(self, data):
            if self.links:
                self.links[-1] += data

        def handle_endtag(self, tag):
            if tag == 'a':
                self.links[-1] += '</a>'

    h = urllib.request.urlopen(url)
    b = h.read().decode(encoding='utf-8')
    m = MyHTMLParser()
    m.feed(b)
    return m.links

def flipped_interaction_3__printLinks(url):
	try:
		r = requests.get(url, allow_redirects=True)
		r.raise_for_status()
		soup = BeautifulSoup(r.content, 'html.parser')
		a_tags = soup.find_all('a', href=True)
		a_tags_with_content = [str(tag) for tag in a_tags if tag['href'].strip()]
		return a_tags_with_content
	except requests.exceptions.RequestException as e:
		return []

def flipped_interaction_4__printLinks(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            a_tags = soup.find_all('a')
            full_a_tags = [str(tag) for tag in a_tags]
            return full_a_tags
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return []

def flipped_interaction_5__printLinks(url):
	import requests
	from bs4 import BeautifulSoup
	from urllib.parse import urlparse, urljoin
	try:
		soup = BeautifulSoup(requests.get(url, allow_redirects=True).text, 'html.parser')
		a_tags = soup.find_all('a', href=True)
		base_url = urlparse(url).netloc
		links = [str(a) for a in a_tags if urlparse(urljoin(url, a['href'])).netloc == base_url]
		return links
	except Exception:
		return []

def iterative_prompting_3__printLinks(url):
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        raise ValueError("URL must be a string starting with http:// or https://")
    try:
        response = requests.get(url, timeout=10, verify=True)
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching the URL: {{e}}")
    try:
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        raise RuntimeError(f"Error parsing the HTML: {{e}}")
    return [str(link) for link in soup.find_all("a, href=True")]

def iterative_prompting_4__printLinks(url):
    try:
        if not isinstance(url, str):
            raise ValueError('URL must be a string.')
        if not url.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL scheme.')
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'}, verify=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [str(a) for a in soup.find_all('a', href=True)]
        return links
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []

def iterative_prompting_5__printLinks(url):
    import requests
    from bs4 import BeautifulSoup
    import re
    if not isinstance(url, str) or not re.match(r'^https?://[\w.-]+(?:/[\w.-]*)*$', url):
        raise ValueError('Invalid URL format')
    try:
        r = requests.get(url, timeout=10, headers={{'User-Agent': 'Mozilla/5.0'}})
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f'An error occurred: {{e}}')
    soup = BeautifulSoup(r.content, 'html.parser')
    links = [str(a) for a in soup.find_all('a', href=True)]
    return links

def few_shots_prompting__printLinks(url):
	from bs4 import BeautifulSoup
	import requests
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	links = [str(a) for a in soup.find_all('a', href=True)]
	return links

def cot_prompting__printLinks(url):
	from bs4 import BeautifulSoup
	import requests
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	links = soup.find_all('a', href=True)
	return [str(link) for link in links]

def fact_check_list__printLinks(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            a_tags = soup.find_all('a', href=True)
            formatted_a_tags = [str(tag) for tag in a_tags]
            return formatted_a_tags
        else:
            return []
    except requests.exceptions.RequestException:
        return []

def not_interactive_mix__printLinks(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL")
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        a_tags_with_urls = soup.find_all('a', href=True)
        full_a_tags = []
        for tag in a_tags_with_urls:
            full_tag_str = str(tag)
            full_a_tags.append(full_tag_str)
        return full_a_tags
    except ValueError as ve:
        return [f"ValueError: {ve}"]
    except URLError as e:
        return [f"URLError: {e.reason}"]
    except HTTPException as e:
        return [f"HTTPException: {e}"]
    except Exception as e:
        return [f"An unexpected error occurred: {str(e)}"]

def interactive_mix__printLinks(url):
    import re
    import requests
    from urllib.parse import urlparse, urljoin
    from bs4 import BeautifulSoup
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ('http', 'https'):
        raise ValueError('URL must use http or https scheme.')
    if not re.match(r'^https?://[^]+$', url):
        raise ValueError('Invalid URL format.')
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
    except requests.RequestException as e:
        raise RuntimeError(f'HTTP request failed: {e}')
    try:
        soup = BeautifulSoup(html, 'html.parser')
        base_url = url
        links = []
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            links.append(str(link))
        return links
    except Exception as e:
        raise RuntimeError(f'HTML parsing failed: {e}')

def baseline__printLinks(url):
	from bs4 import BeautifulSoup
	import requests
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	links = [str(a) for a in soup.find_all('a', href=True)]
	return links

