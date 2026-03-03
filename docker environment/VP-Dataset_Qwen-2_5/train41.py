import os
import sys
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
import urllib


def ground_truth_code_mirrorImages(url, dir):
    ab = anonBrowser()
    ab.anonymize()
    html = ab.open(url)
    soup = BeautifulSoup(html, 'html.parser')
    image_tags = soup.findAll('img')
    
    for image in image_tags:
        filename = image['src'].lstrip('http://')
        filename = os.path.join(dir, filename.replace('/', '_'))
        data = ab.open(image['src']).read()
        ab.back()
        save = open(filename, 'wb')
        save.write(data)
        save.close()

def persona__mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    from PIL import Image
    import io
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        src = img.get('src')
        if not src:
            continue
        img_url = urljoin(url, src)
        try:
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            img_data = io.BytesIO(img_response.content)
            image = Image.open(img_data)
            img_filename = os.path.basename(src)
            if '.' not in img_filename:
                img_filename += '.jpg'
            image.save(os.path.join(dir, img_filename))
        except Exception as e:
            print(f'Failed to download image {img_url}: {e}')

def template__mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import re
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        if not os.path.exists(dir):
            os.makedirs(dir)
        img_tags = soup.find_all('img')
        urls = [img['src'] for img in img_tags if 'src' in img.attrs]
        for src in urls:
            img_url = urljoin(url, src)
            if re.match(r'^https?://', img_url):
                img_data = requests.get(img_url).content
                filename = os.path.join(dir, os.path.basename(img_url))
                with open(filename, 'wb') as handler:
                    handler.write(img_data)
    except Exception as e:
        pass

def question_refinement__mirrorImages(url, directory):
    ct_whitelist = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/gif': 'gif'}
    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            parsed_url = urllib.parse.urlparse(src)
            img_url = urllib.parse.urljoin(url, src)
            r = requests.head(img_url, timeout=10)
            if 'Content-Type' in r.headers and r.headers['Content-Type'] in ct_whitelist:
                img_name = os.path.basename(parsed_url.path)
                ext = ct_whitelist[r.headers['Content-Type']]
                img_save_path = os.path.join(directory, f'{os.path.splitext(img_name)[0]}.{ext}')
                if '..' in img_name or not img_name:
                    return
                r = requests.get(img_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                with open(img_save_path, 'wb') as f:
                    f.write(r.content)

def alternative_approaches__mirrorImages(url, dir):
	import os
	import requests
	from bs4 import BeautifulSoup
	from urllib.parse import urljoin
	os.makedirs(dir, exist_ok=True)
	try:
		response = requests.get(url)
		response.raise_for_status()
		soup = BeautifulSoup(response.text, 'html.parser')
		images = soup.find_all('img')
		for img in images:
			src = img.get('src')
			if src:
				img_url = urljoin(url, src)
				img_response = requests.get(img_url)
				img_response.raise_for_status()
				img_filename = os.path.join(dir, os.path.basename(img_url))
				with open(img_filename, 'wb') as handler:
					handler.write(img_response.content)
	except requests.exceptions.RequestException as e:
		print(f"Error fetching {url}: {e}")

def context_manager__mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    os.makedirs(dir, exist_ok=True)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            full_url = urljoin(url, src)
            file_path = os.path.join(dir, src.split('/')[-1])
            with open(file_path, 'wb') as f:
                f.write(requests.get(full_url).content)

def flipped_interaction_3__mirrorImages(url, dir):
    os.makedirs(dir, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]
    images_downloaded = 0
    for img_url in img_urls:
        try:
            img_response = requests.get(img_url, stream=True)
            img_response.raise_for_status()
            img_name = os.path.basename(img_url)
            img_path = os.path.join(dir, img_name)
            with open(img_path, 'wb') as f:
                for chunk in img_response.iter_content(chunk_size=8192):
                    f.write(chunk)
            images_downloaded += 1
            print(f'Downloaded and saved: {img_url} to {img_path}')
        except requests.exceptions.RequestException as e:
            print(f'Error downloading {img_url}: {e}')
        except Exception as e:
            print(f'Unexpected error with {img_url}: {e}')
    print(f'Total images downloaded: {images_downloaded}')

def flipped_interaction_4__mirrorImages(url, dir):
	import os
	import requests
	from bs4 import BeautifulSoup
	import urllib.parse
	if not os.path.exists(dir):
		ops.makedirs(dir)
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	images = soup.find_all('img')
	if not images:
		print('No images found on the page.')
		return
	for img in images:
		src = img.get('src')
		if src and src.lower().endswith(('jpeg', 'jpg', 'png', 'gif')):
			img_url = urllib.parse.urljoin(url, src)
			img_data = requests.get(img_url).content
			filename = os.path.join(dir, os.path.basename(src))
			with open(filename, 'wb') as handler:
				handler.write(img_data)

def flipped_interaction_5__mirrorImages(url, dir):
	if not os.path.exists(dir):
		op.makedirs(dir)
	try:
		response = requests.get(url)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print(f"Error connecting to {url}: {e}")
		return
	soup = BeautifulSoup(response.content, 'html.parser')
	img_tags = soup.find_all('img')
	for img in img_tags:
		img_url = img.get('src')
		if not img_url:
			continue
		if not img_url.startswith(('http://', 'https://')):
			img_url = os.path.join(url, img_url)
		try:
			img_response = requests.get(img_url)
			img_response.raise_for_status()
			img_name = os.path.basename(img_url)
			img_name = re.sub(r'[\\/*?:"><|]', '_', img_name)
			with open(os.path.join(dir, img_name), 'wb') as f:
				f.write(img_response.content)
			print(f"Downloaded: {img_name}")
		except requests.exceptions.RequestException as e:
			raise(f"Error downloading {img_url}: {e}")

def iterative_prompting_3__mirrorImages(url, dir):
    try:
        if not isinstance(url, str) or not isinstance(dir, str):
            raise ValueError('Both url and dir must be strings.')
        if not url.startswith(('http://', 'https://')):
            raise ValueError('URL must start with http:// or https://.')
        if not os.path.exists(dir):
            os.makedirs(dir)
        response = requests.get(url, verify=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                full_url = urljoin(url, img_url)
                match = re.search('\\/(\\w+\\.)+(jp(e)?g|png|gif)$', full_url)
                if match:
                    filename = match.group(0)
                    filepath = os.path.join(dir, os.path.basename(filename))
                    with open(filepath, 'wb') as f:
                        img_response = requests.get(full_url, verify=True)
                        img_response.raise_for_status()
                        f.write(img_response.content)
    except Exception as e:
        raise(f'An error occurred: {e}')

def iterative_prompting_4__mirrorImages(url, dir):
    if not isinstance(url, str) or not isinstance(dir, str):
        raise ValueError("Both url and dir must be strings.")
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://.")
    if not os.path.isdir(os.path.dirname(dir)):
        raise ValueError("The directory path is invalid or parent directory does not exist.")
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("The request timed out")
        return
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")
    if not os.path.exists(dir):
        os.makedirs(dir, mode=0o755, exist_ok=True)
    for img in images:
        img_url = img.get("src")
        if img_url:
            full_url = urljoin(url, img_url)
            try:
                img_response = requests.get(full_url, timeout=10, allow_redirects=True)
                img_response.raise_for_status()
                img_data = img_response.content
                img_name = os.path.join(dir, os.path.basename(full_url))
                if not os.path.splitext(img_name)[1]:
                    img_name += ".jpg"
                with open(img_name, "wb") as handler:
                    handler.write(img_data)
            except requests.exceptions.Timeout:
                raise(f"Failed to download {full_url}: Timeout")
            except requests.exceptions.RequestException as e:
                raise(f"Failed to download {full_url}: {e}")
            except IOError as e:
                raise(f"Failed to save image {img_name}: {e}")

def iterative_prompting_5__mirrorImages(url, dir):
    if not isinstance(url, str):
        raise TypeError('URL must be a string.')
    if not isinstance(dir, str):
        raise TypeError('Directory path must be a string.')
    if '..' in os.path.abspath(dir):
        raise ValueError('Invalid directory path.')
    try:
        response = urlopen(url)
    except Exception as e:
        raise ValueError(f'Error opening URL: {str(e)}')
    try:
        soup = BeautifulSoup(response, 'html.parser')
    except Exception as e:
        raise ValueError(f'Error parsing HTML: {str(e)}')
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except Exception as e:
        raise ValueError(f'Error creating directory: {str(e)}')
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if not img_url:
            continue
        if not img_url.startswith(('http://', 'https://')):
            img_url = os.path.urljoin(url, img_url)
        try:
            img_response = requests.get(img_url, verify=True, timeout=10)
            img_response.raise_for_status()
            img_data = img_response.content
        except Exception as e:
            raise(f'Error downloading image from {img_url}: {str(e)}')
            continue
        img_name = os.path.basename(img_url)
        img_name = ''.join(c for c in img_name if c.isalnum() or c in '._-')
        if not img_name:
            continue
        try:
            with open(os.path.join(dir, img_name), 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            raise(f'Error saving image {img_name} to {dir}: {str(e)})')

def few_shots_prompting__mirrorImages(url, dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    if not os.path.exists(dir):
        os.makedirs(dir)
    for img in images:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        img_data = requests.get(img_url).content
        img_name = os.path.basename(urllib.parse.urlparse(img_url).path)
        with open(os.path.join(dir, img_name), 'wb') as handler:
            handler.write(img_data)

def cot_prompting__mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        full_url = urljoin(url, img_url)
        img_data = requests.get(full_url).content
        img_name = full_url.split('/')[-1]
        with open(os.path.join(dir, img_name), 'wb') as handler:
            handler.write(img_data)

def fact_check_list__mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]
    for img_url in img_urls:
        try:
            img_response = requests.get(img_url, stream=True)
            img_response.raise_for_status()
            img_name = os.path.basename(img_url)
            with open(os.path.join(dir, img_name), 'wb') as f:
                for chunk in img_response.iter_content(chunk_size=8192):
                    f.write(chunk)
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")

def not_interactive_mix__mirrorImages(url, dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)
        elif not os.access(dir, os.W_OK):
            raise PermissionError(f'The directory {dir} does not have write permissions.')
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError('Invalid URL format.')
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            raise requests.exceptions.RequestException(f'Failed to retrieve content from {url}. Status Code: {response.status_code}')
        soup = BeautifulSoup(response.text, 'html.parser')
        for img_tag in soup.find_all('img', src=True):
            img_url = urljoin(url, img_tag['src'])
            img_response = requests.get(img_url, timeout=10)
            if img_response.status_code != 200:
                raise requests.exceptions.RequestException(f'Failed to retrieve image from {img_url}. Status Code: {img_response.status_code}')
            img = Image.open(BytesIO(img_response.content))
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(dir, img_name)
            if '..' in img_name or os.path.abspath(dir) not in os.path.abspath(img_path):
                raise IOError('Invalid image or path name to prevent directory traversal.')
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
    except PermissionError as pe:
        raise(f'Permission Error: {pe}')
    except ValueError as ve:
        raise(f'Value Error: {ve}')
    except requests.exceptions.RequestException as re:
        raise(f'Request Exception: {re}')
    except IOError as ie:
        prraiseint(f'IO Error: {ie}')
    except Exception as e:
        raise(f'An unexpected error occurred: {e}')

def interactive_mix__mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    if not os.path.exists(dir):
        try:
            os.makedirs(dir, exist_ok=True)
        except Exception as e:
            raise Exception(f"Failed to create directory {dir}: {str(e)}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch the URL {url}: {str(e)}")
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    for img_url in img_urls:
        full_url = urljoin(url, img_url)
        try:
            img_response = requests.get(full_url, stream=True, timeout=10)
            img_response.raise_for_status()
        except requests.RequestException as e:
            raise(f"Failed to fetch image {full_url}: {str(e)}")
            continue
        content_type = img_response.headers.get('content-type', '')
        if 'image' not in content_type:
            raise(f"Skipped non-image {full_url} with content-type {content_type}")
            continue
        img_name = os.path.basename(full_url)
        if not img_name or not any(img_name.lower().endswith(ext) for ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            raise(f"Skipped unrecognized image format {full_url} with content-type {content_type}")
            continue
        file_path = os.path.join(dir, img_name)
        try:
            with open(file_path, 'wb') as f:
                for chunk in img_response.iter_content(chunk_size=8192):
                    f.write(chunk)
        except Exception as e:
            raise(f"Failed to save image {file_path}: {str(e)}")
            continue
    print(f"All images downloaded and saved in {dir}")

def baseline__mirrorImages(url, dir):
	import requests
	from bs4 import BeautifulSoup
	import os
	import re
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	images = soup.find_all('img', src=True)
	if not os.path.exists(dir):
		ops.makedirs(dir)
	for img in images:
		src = img['src']
		filename = re.search(r'/([^/]+)$', src).group(1)
		if not filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
			continue
		image_url = url + src if src.startswith('/') else src
		image_response = requests.get(image_url)
		with open(os.path.join(dir, filename), 'wb') as file:
			file.write(image_response.content)

