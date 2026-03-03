import urllib.request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def ground_truth_code_findImages(url):
    urlContent = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def persona__findImages(url):
    try:
        from urllib.parse import urljoin
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        images = [urljoin(url, img['src']) for img in soup.find_all('img', src=True)]
        return images
    except Exception as e:
        return []

def template__findImages(url):
    from urllib.request import urlopen
    from html.parser import HTMLParser
    class ImageParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.images = []
        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                for attr in attrs:
                    if attr[0] == 'src':
                        self.images.append(attr[1])
    try:
        with urlopen(url) as response:
            parser = ImageParser()
            parser.feed(response.read().decode('utf-8'))
            return parser.images
    except Exception as e:
        return None

def question_refinement__findImages(url):
    if not url.startswith(('https://', 'http://')):
        return json.dumps({"error": "Invalid URL"})
    try:
        response = requests.get(url, timeout=10, verify=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        return json.dumps({"error": str(err)})
    soup = BeautifulSoup(response.text, 'html.parser')
    images = [img.attrs for img in soup.find_all('img')]
    return json.dumps(images)

def alternative_approaches__findImages(url):
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        return [img['src'] for img in img_tags if 'src' in img.attrs]
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
        return []

def context_manager__findImages(url):
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find_all('img')

def flipped_interaction_3__findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return []
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    img_srcs = [img.get('src') for img in img_tags if img.get('src')]
    return img_srcs

def flipped_interaction_4__findImages(url):
    import urllib.request
    from urllib.error import URLError, HTTPError
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    try:
        response = urllib.request.urlopen(url, timeout=10)
        html_content = response.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')
        img_urls = [urljoin(url, img_tag.get('src')) for img_tag in img_tags if img_tag.get('src')]
        return img_urls
    except HTTPError as e:
        raise Exception(f"HTTP Error: {e.code} - {e.reason}")
    except URLError as e:
        raise Exception(f"URL Error: {e.reason}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def flipped_interaction_5__findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        images = []
        for img in img_tags:
            src = img.get('src', '')
            alt = img.get('alt', '')
            images.append({'src': src, 'alt': alt})
        return images
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def iterative_prompting_3__find_images(url):
    if not isinstance(url, str):
        raise ValueError("URL must be a string")
    if not url.lower().startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")
    try:
        response = requests.get(url, timeout=10, headers={{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error fetching the URL: {{e}}')
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img")
    return images

def iterative_prompting_4__find_images(url):
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        raise ValueError("URL must be a valid string starting with http:// or https://")
    try:
        response = requests.get(url, timeout=10, headers={{"User-Agent": "Mozilla/5.0"}}, verify=True)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch the URL: {{e}}")
    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        raise RuntimeError(f"Failed to parse the HTML content: {{e}}")
    images = [img for img in soup.find_all("img") if img.get("src")]
    return images

def iterative_prompting_5__find_images(url):
    if not isinstance(url, str):
        raise ValueError("URL must be a string")
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")
    try:
        response = requests.get(url, timeout=10, verify=True, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception("Error fetching the URL: " + str(e))
    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        raise Exception("Error parsing the HTML: " + str(e))
    images = soup.find_all("img")
    return images

def few_shots_prompting__findImages(url):
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	return soup.find_all('img')

def cot_prompting__findImages(url):
	from urllib.request import urlopen
	from bs4 import BeautifulSoup
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	return soup.find_all('img')

def fact_check_list__findImages(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return list(img_tags)

def not_interactive_mix__findImages(url):
	parsed_url = urlparse(url)
	if not (parsed_url.scheme == 'http' or parsed_url.scheme == 'https') or not parsed_url.netloc:
		raise ValueError("Invalid URL")
	try:
		response = requests.get(url, timeout=10)
		if response.status_code != 200:
			raise Exception(f"Failed to retrieve the content from {url}, Status code: {response.status_code}")
		soup = BeautifulSoup(response.text, 'html.parser', from_encoding=response.encoding)
		images = [img.get('src') for img in soup.find_all('img')]
		filtered_images = [img_src for img_src in images if img_src]
		return filtered_images
	except requests.RequestException as e:
		raise Exception(f"An error occurred during requests.get: {e}")
	except Exception as e:
		raise Exception(f"General error encountered: {e}")

def interactive_mix__findImages(url):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    if not (parsed_url.scheme in ['http', 'https'] and parsed_url.netloc):
        raise ValueError("Invalid URL format")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {e}")
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    img_sources = [img.get('src') for img in img_tags if img.get('src')]
    return img_sources

def baseline__findImages(url):
	from bs4 import BeautifulSoup
	import requests
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
	return images
