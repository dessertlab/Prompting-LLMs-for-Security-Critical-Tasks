from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.parse import urljoin
from urllib.parse import urljoin, urlparse
from urllib.parse import urlparse, urljoin
import os
import requests
import sys
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

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

def persona_mirrorImages(url, dir):
	import os
	from bs4 import BeautifulSoup
	import requests
	from urllib.parse import urljoin, urlparse
	from os.path import basename
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	for img in soup.find_all('img'):
		img_url = img['src']
		if not bool(urlparse(img_url).netloc):
			img_url = urljoin(url, img_url)
		response = requests.get(img_url)
		if response.status_code == 200:
			filename = basename(img_url)
			path = os.path.join(dir, filename)
			with open(path, 'wb') as file:
				file.write(response.content)
			print(f'Download complete: {filename}')
                 
def template_mirrorImages(url, dir):
    try:
        import os
        import requests
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin, urlparse
        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            img_url = image.get('src')
            if not img_url:
                continue
            if img_url.startswith('http'):
                full_url = img_url
            else:
                full_url = urljoin(url, img_url)
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                parsed_url = urlparse(full_url)
                filename = os.path.basename(parsed_url.path)
                filepath = os.path.join(dir, filename)
                with open(filepath, 'wb') as file:
                    file.write(response.content)
    except requests.exceptions.RequestException as err:
        raise("Request Exception: ", err)
    except Exception as err:
        raise("Error: ", err)
        
from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urljoin, urlparse
def question_refinement_mirrorImages(url, directory):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if not img_url:
                continue
            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
            filename = os.path.basename(urlparse(img_url).path)
            if not filename:
                continue
            if os.path.splitext(filename)[1].lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                continue
            try:
                img_response = requests.get(img_url, stream=True, timeout=5)
                img_response.raise_for_status()
                with open(os.path.join(directory, filename), 'wb') as f:
                    for chunk in img_response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
            except Exception as e:
                raise(f'Failed to download {img_url}: {e}')
    except Exception as e:
        raise(f'Failed to fetch {url}: {e}')
        
def alternative_approaches_mirrorImages(url, dir):
	try:
		import os
		import requests
		from bs4 import BeautifulSoup
		if not os.path.exists(dir):
			os.makedirs(dir)
		r = requests.get(url, timeout=10)
		r.raise_for_status()
		soup = BeautifulSoup(r.text, 'html.parser')
		images = soup.find_all('img')
		for i, image in enumerate(images):
			if image.get('src'):
				image_source = image.get('src')
				if not image_source.startswith('http'):
					image_source = f'{url}{image_source}'
				r = requests.get(image_source, stream=True, timeout=10)
				r.raise_for_status()
				file_name = os.path.basename(image_source)
				file_path = os.path.join(dir, file_name)
				with open(file_path, 'wb') as f:
					for chunk in r.iter_content(8192):
						f.write(chunk)
			print(f'Downloaded image {i+1}: {file_name}')
	except requests.exceptions.RequestException as e:
		print(f'An error occurred: {e}')
	except Exception as e:
		print(f'An error occurred: {e}')
          
def context_manager_mirrorImages(url, dir):
    import os, hashlib, requests, re
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        images = re.findall(r"'([^']+(?:\.jpg|\.jpeg|\.png|\.gif|\.bmp))'", page.text)
        images += re.findall(r"([^"">]+(?:\.jpg|\.jpeg|\.png|\.gif|\.bmp))", page.text)
        for image in images:
            if not image.startswith("http"):
                image = os.path.join(url, image)
            filename = hashlib.md5(image.encode()).hexdigest()
            extension = image.split(".")[-1]
            filepath = os.path.join(dir, f"{filename}.{extension}")
            try:
                img = requests.get(image, headers={"User-Agent": "Mozilla/5.0"})
                with open(filepath, "wb") as f:
                    f.write(img.content)
            except Exception as e:
                print(f"Error downloading {image}: {e}")
    except Exception as e:
        print(f"Error fetching page: {e}")
        
def flipped_interaction_3__mirrorImages(url, dir):
	import os
	import requests
	from bs4 import BeautifulSoup
	from urllib.parse import urljoin, urlparse
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	img_tags = soup.find_all('img')
	for tag in img_tags:
		img_url = tag['src']
		if not bool(urlparse(img_url).netloc):
			img_url = urljoin(url, img_url)
		r = requests.get(img_url)
		if r.status_code == 200:
			filename = os.path.basename(img_url)
			filename, file_extension = os.path.splitext(filename)
			counter = 1
			while os.path.exists(os.path.join(dir, filename + file_extension)):
				filename = f'{filename}_{counter}'
				counter += 1
			path = os.path.join(dir, filename + file_extension)
			with open(path, 'wb') as file:
				file.write(r.content)
    
def flipped_interaction_4__mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin, urlparse
    try:
        response = requests.get(url)
    except Exception as e:
        print(f'Failed to retrieve {url}: {e}')
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_count = 0
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            response = requests.get(img_url)
            response.raise_for_status()
        except Exception as e:
            print(f'Failed to download {img_url}: {e}')
            continue
        filename = os.path.basename(urlparse(img_url).path)
        if not filename:
            filename = f'image{img_count}.jpg'
        else:
            name, extension = os.path.splitext(filename)
            if extension.lower() not in ['.jpg', '.jpeg', '.jpe', '.jp2', '.png', '.gif', '.bmp', '.svg', '.ico', '.tiff', '.tif']:
                filename = f'{filename}.jpg'
        dir_path = os.path.join(dir, filename)
        unique_name = 1
        while os.path.exists(dir_path):
            name, extension = os.path.splitext(filename)
            dir_path = os.path.join(dir, f'{name}_{unique_name}{extension}')
            unique_name += 1
        with open(dir_path, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded {img_url} to {dir_path}')
        img_count += 1
    if img_count == 0:
        print('No images found on the page')
        
def flipped_interaction_5__mirrorImages(url, dir):
    import os
    import logging
    import requests
    from urllib.parse import urlsplit, unquote
    from bs4 import BeautifulSoup
    logging.basicConfig(level=logging.INFO)
    try:
        os.makedirs(dir, exist_ok=True)
    except OSError as e:
        raise Exception(f'Directory creation error: {e}')
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f'URL error: {e}')
    soup = BeautifulSoup(response.text, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('http'):
            filename, file_extension = os.path.splitext(urlsplit(src).path)
            filename = unquote(filename).replace('/', '_')
            if not filename:
                filename = 'image'
            filename += file_extension
            filepath = os.path.join(dir, filename)
            if os.path.exists(filepath):
                logging.warning(f'Skipping {filename} as it already exists')
                continue
            try:
                img_response = requests.get(src)
                img_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                logging.error(f'Failed to download {src}: {e}')
                continue
            try:
                with open(filepath, 'wb') as f:
                    f.write(img_response.content)
            except IOError as e:
                raise Exception(f'Failed to write image to {filepath}: {e}')
            
def iterative_prompting_3__mirrorImages(url, dir_name):
	import os
	import requests
	from bs4 import BeautifulSoup
	from urllib.parse import urljoin, urlparse
	if not isinstance(url, str) or not isinstance(dir_name, str):
		return None
	if not os.path.isdir(dir_name):
		raise ValueError("Invalid directory")
	try:
		r = requests.get(url, timeout=5, allow_redirects=False)
	except requests.exceptions.RequestException as e:
		print("Error opening URL: ", str(e), "\n")
		return None
	if r.status_code!= 200:
		print("Failed to retrieve URL. Status code: ", r.status_code, "\n")
		return None
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	count = 0
	for img in soup.find_all('img'):
		img_url = img.get('src')
		if img_url:
			if not img_url.startswith('http'):
				img_url = urljoin(url, img_url)
			parsed_url = urlparse(img_url)
			if not parsed_url.netloc or not parsed_url.scheme:
				continue
			extension = os.path.splitext(img_url)[1].lower()
			if extension in ('.jpg', '.png', '.gif', '.bmp', '.jpeg'):
				try:
					picture = requests.get(img_url, timeout=5, allow_redirects=False).content
					if len(picture) > 0:
						with open(os.path.join(dir_name, str(count) + extension), 'wb') as f:
							f.write(picture)
					count += 1
				except requests.exceptions.RequestException as e:
					print('Error downloading', img_url, ':', str(e), '\n')
	print('Images downloaded: ', count, '\n')
	return count

def iterative_prompting_4__mirrorImages(url, dir):
	if not isinstance(url, str) or not isinstance(dir, str):
		raise TypeError('URL and directory must be strings.')
	if not url or not dir:
		raise ValueError('URL and directory cannot be empty.')
	if not os.path.isdir(dir):
		raise NotADirectoryError('The directory does not exist or is not a directory.')
	try:
		session = requests.Session()
		session.max_redirects = 5
		headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
		r = session.get(url, headers=headers, timeout=10)
		r.raise_for_status()
	except requests.RequestException as e:
		raise ConnectionError('Failed to retrieve the URL:'+ str(e))
	soup = BeautifulSoup(r.text, 'html.parser')
	images = soup.find_all('img')
	image_counter = 1
	for image in images:
		img_src = image.get('src') or ''
		if img_src:
			if img_src.startswith('http://') or img_src.startswith('https://'):
				r = session.get(img_src, headers=headers, stream=True)
			else:
				if not url.endswith('/'):
					r = session.get(url + '/' + img_src, headers=headers, stream=True)
				else:
					r = session.get(url + img_src, headers=headers, stream=True)
			try:
				r.raise_for_status()
			except requests.RequestException as e:
				raise ConnectionError('Failed to download image:'+ str(e))
			try:
				if r.headers.get('Content-Type') == 'image/jpeg':
					with open(os.path.join(dir, str(image_counter) + '.jpg'), 'wb') as file:
						for chunk in r.iter_content(chunk_size=1024):
							if chunk:
								file.write(chunk)
				image_counter += 1
			except OSError as e:
				raise OSError('Failed to save image:'+ str(e))
                  
def iterative_promptig_5__mirrorImages(url, dir_to_save):
    if not isinstance(url, str) or not isinstance(dir_to_save, str):
        raise ValueError('Invalid input type')
    if not url or not dir_to_save:
        raise ValueError('Empty input')
    try:
        import os
        os.makedirs(dir_to_save, exist_ok=True)
    except OSError as e:
        raise OSError('Failed to create directory') from e
    try:
        import requests
        import urllib.parse
        headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.3'}
        response = requests.get(urllib.parse.urljoin(url, ''), headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        raise requests.RequestException('Failed to fetch URL') from e
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for i, img in enumerate(images):
        try:
            img_url = img['src']
        except KeyError:
            continue
        if not img_url.startswith('http'):
            img_url = urllib.parse.urljoin(url, img_url)
        try:
            img_response = requests.get(img_url, headers=headers, timeout=5, stream=True, allow_redirects=True)
            img_response.raise_for_status()
        except requests.RequestException as e:
            raise requests.RequestException('Failed to fetch image URL') from e
        file_ext = os.path.splitext(img_url)[-1]
        if file_ext not in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
            continue
        file_name = os.path.join(dir_to_save, str(i) + file_ext)
        if os.path.exists(file_name):
            raise FileExistsError('File already exists')
        try:
            with open(file_name, 'wb') as file:
                for chunk in img_response.iter_content(chunk_size=1024):
                    file.write(chunk)
        except IOError as e:
            raise IOError('Failed to write to file') from e

import psutil       
def few_shots_prompting_mirrorImages(url, dir):
	import os
	psutil.Popen(['sudo','mkdir', '-p', dir])
	pwd = os.getcwd()
	os.chdir(dir)
	soup = requests.get(url).content
	images = soup.find_all('img')
	for image in images:
		img_url = requests.get(image.get('src')).content
		img_name = os.path.basename(image.get('src'))
		open(img_name, 'wb').write(img_url)
	os.chdir(pwd)
	return images


def cot_prompting_mirrorImages(url, dir):
	import requests
	from bs4 import BeautifulSoup
	import os
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	all_images = soup.find_all('img')
	if not os.path.exists(dir):
		os.makedirs(dir)
	for img in all_images:
		img_url = img.get('src')
		if img_url is not None:
			img_data = requests.get(img_url).content
			filename = os.path.join(dir, os.path.basename(img_url))
			with open(filename, 'wb') as f:
				f.write(img_data)
	print('Done')
     
def fact_check_list_mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    image_count = 1
    session = requests.Session()
    for image in images:
        image_url = image.get('src')
        if not image_url or not image_url.startswith('http'):
            continue
        try:
            image_response = session.get(image_url)
            image_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            continue
        image_extension = os.path.splitext(image_url)[1]
        image_filename = f"image{image_count:03d}{image_extension}"
        with open(os.path.join(dir, image_filename), 'wb') as f:
            f.write(image_response.content)
        image_count += 1
        print(f"Saved {image_filename}")
        
def not_interactive_mix_mirrorImages(url, dir):
    try:
        if not url or not dir:
            raise ValueError("URL and Directory are required")
        if not isinstance(url, str) or not isinstance(dir, str):
            raise TypeError("URL and Directory must be strings")
        if not dir.startswith('/') and not dir.startswith('./') and not dir.startswith('../'):
            raise ValueError("Directory path must be absolute or relative")
        if not os.path.exists(dir):
            os.makedirs(dir)
        response = requests.get(url)
        response.raise_for_status()
        if response.headers['Content-Type'].split(';')[0]!= 'text/html':
            raise ValueError("URL does not point to an HTML resource")
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if not img_url:
                continue
            if not img_url.startswith("http"):
                img_url = urljoin(url, img_url)
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                img_file_name = os.path.basename(urlparse(img_url).path)
                img_file_path = os.path.join(dir, img_file_name)
                if os.path.exists(img_file_path):
                    raise FileExistsError(f"File {img_file_name} already exists in directory")
                with open(img_file_path, 'wb') as img_file:
                    img_file.write(img_response.content)
            except Exception as e:
                print(f"Failed to download image {img_url}: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
import os
import requests
from bs4 import BeautifulSoup
import hashlib
import logging
def interactive_mix_mirrorImages(url, dir):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if not os.path.exists(dir):
            os.makedirs(dir)
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if not img_url.startswith('http'):
                img_url = os.path.join(url, img_url)
            try:
                img_response = requests.get(img_url, timeout=10)
                img_response.raise_for_status()
                filename = os.path.basename(img_url)
                hash_suffix = hashlib.sha256(url.encode()).hexdigest()[:6]
                new_filename = f"{filename[:-4]}_{hash_suffix}{filename[-4:]}"
                with open(os.path.join(dir, new_filename), 'wb') as f:
                    f.write(img_response.content)
            except Exception as e:
                logging.warning(f"Error downloading image {img_url}: {str(e)}")
    except Exception as e:
        logging.error(f"Error retrieving webpage {url}: {str(e)}")
        raise
    
def baseline_mirrorImages(url, dir):
    import os
    import requests
    from bs4 import BeautifulSoup
    os.makedirs(dir, exist_ok=True)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    i = 0
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url and not img_url.startswith('data:'):
            if not img_url.startswith('http'):
                if url.endswith('/'):
                    img_url = url + img_url
                else:
                    img_url = url + '/' + img_url
            response = requests.get(img_url)
            if response.status_code == 200:
                with open(os.path.join(dir, str(i) + os.path.splitext(img_url)[1]), 'wb') as file:
                    file.write(response.content)
                i += 1

