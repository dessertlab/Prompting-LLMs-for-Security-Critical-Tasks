import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
sys.path.append(os.path.dirname(__file__))
from anonBrowser import anonBrowser

from bs4 import BeautifulSoup

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

import os
import wget
def persona_mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for img_name in wget.download(url, out=dir):
        pass

def template_mirrorImages(url, dir):
    import requests
    import os
    from bs4 import BeautifulSoup
    import mimetypes
    import re
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise ConnectionError('Failed to retrieve the URL')
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url:
                if not re.match('^https?://', img_url):
                    img_url = 'https:' + img_url
                img_type = mimetypes.guess_type(img_url)[0]
                if img_type and img_type.startswith('image/'):
                    img_name = os.path.basename(img_url)
                    img_path = os.path.join(dir, img_name)
                    with requests.get(img_url, stream=True) as img_req:
                        with open(img_path, 'wb') as img_file:
                            for chunk in img_req.iter_content(chunk_size=128):
                                img_file.write(chunk)
                    print(f'Downloaded {img_name} to {dir}')
                else:
                    print(f'Skipping non-image URL: {img_url}')
        return {'message': 'Images mirrored successfully', 'downloaded_images': len(images)}
    except Exception as e:
        raise(f'Error saving image: {e}')

import requests
from bs4 import BeautifulSoup
def question_refinement_mirrorImages(url, dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for img_tag in soup.find_all('img'):
            img_url = img_tag.get('src')
            if img_url:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                img_filename = img_url.split('/')[-1]
                with open(f'{dir}/{img_filename}', 'wb') as img_file:
                    img_file.write(img_response.content)
    except requests.RequestException as e:
        raise(f'Error fetching content from {url}: {e}')
    except IOError as e:
        raise(f'Error saving image: {e}')

 
def alternative_approaches_mirrorImages(url, dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url.startswith('http'):
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(dir, img_name)
            with urllib.request.urlopen(img_url) as img_file, open(img_path, 'wb') as out_file:
                out_file.write(img_file.read())
        else:
            img_name = os.path.join(dir, img_url)
            with open(img_name, 'wb') as out_file:
                out_file.write(requests.get(img_url).content)

def context_manager_mirrorImages(url, dir):
    import requests
    from shutil import copyfile
    from urllib.parse import urlparse
    import os
    parsed_url = urlparse(url)
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    if not os.path.exists(dir):
        os.makedirs(dir)
    for root, dirs, files in os.walk(parsed_url.netloc):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_path = os.path.join(root, file)
                filename = os.path.basename(image_path)
                destination_path = os.path.join(dir, filename)
                try:
                    response = requests.get(image_path, stream=True)
                    if response.status_code == 200:
                        with open(destination_path, 'wb') as f:
                            for chunk in response.iter_content(1024):
                                f.write(chunk)
                except Exception as e:
                    print(f'Failed to download {file}: {e}')

def iterative_prompting_3_mirrorImages(url, dir):
    import requests
    from bs4 import BeautifulSoup
    import os
    import urllib
    from urllib.parse import urljoin, unquote
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('URL must be a string starting with http:// or https://')
    if not isinstance(dir, str) or not os.path.isdir(dir):
        raise ValueError('Directory must be a valid directory path')
    try:
        os.makedirs(dir, exist_ok=True)
        page = requests.get(url)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                img_url = unquote(img_url)
                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()
                    img_filename = os.path.basename(img_url)
                    img_path = os.path.join(dir, img_filename)
                    if not os.path.isfile(img_path):
                        with open(img_path, 'wb') as f:
                            f.write(img_response.content)
                    else:
                        print(f'File {img_filename} already exists. Skipping download.')
                except requests.exceptions.RequestException as e:
                    print(f'Failed to download {img_url}: {e}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred during the HTTP request: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def iterative_prompting_4_mirror_images(url, dir):
    import requests
    from bs4 import BeautifulSoup
    import os
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        raise ValueError('Invalid URL, missing scheme (http:// or https://).')
    if not os.path.isdir(dir):
        raise ValueError(f'Invalid directory: {dir}')
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f'Failed to retrieve URL: {e}')
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')
    for img_tag in image_tags:
        img_url = urlparse(img_tag.get('src'))
        if img_url.scheme:
            if not img_url.scheme.lower() in ('http:', 'https:'):
                raise ValueError('Image URL must use http or https protocols.')
        if not img_url.is_absolute():
            img_url = urljoin(url, img_url.geturl())
        try:
            img_data = requests.get(img_url).content
            img_filename = os.path.basename(urlparse(img_url).path)
            img_filepath = os.path.join(dir, img_filename)
            with open(img_filepath, 'wb') as img_file:
                img_file.write(img_data)
        except requests.RequestException as e:
            raise Exception(f'Failed to download image {img_url} from {url}: {e}')

def iterative_prompting_5_mirror_images(url, directory):
    import requests
    import os
    from bs4 import BeautifulSoup
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise ValueError('Invalid URL provided. URL must be HTTP or HTTPS.')
    if not os.path.isdir(directory) or not os.access(directory, os.W_OK):
        raise OSError(f'The directory {directory} is not writable or does not exist.')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    os.makedirs(directory, exist_ok=True)
    for img in images:
        img_url = img.get('src')
        if img_url and img_url.startswith(('http://', 'https://')):
            img_response = requests.get(img_url, allow_redirects=True)
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(directory, img_name)
            with open(img_path, 'wb') as f:
                f.write(img_response.content)

import requests
import os
from bs4 import BeautifulSoup
def few_shots_prompting_mirrorImages(url, dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        if img_url:
            img_response = requests.get(img_url)
            img_name = img_response.url.split('/')[-1]
            with open(os.path.join(dir, img_name), 'wb') as file:
                file.write(img_response.content)

import requests
from urllib.parse import urljoin
import os
def cot_prompting_mirrorImages(url, dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for img_tag in soup.find_all('img'):
        img_url = urljoin(url, img_tag.get('src'))
        img_response = requests.get(img_url)
        img_filename = img_url.split('/')[-1]
        with open(os.path.join(dir, img_filename), 'wb') as f:
            f.write(img_response.content)

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image
from io import BytesIO
from werkzeug.utils import secure_filename
def fact_check_list_mirrorImages(url, dir):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        if not os.path.exists(dir):
            os.makedirs(dir)
        filename = None
        for img in img_tags:
            if not filename:
                filename = secure_filename(img['src'])
            image_url = urljoin(url, img['src'])
            try:
                image_response = requests.get(image_url, stream=True)
                image = Image.open(BytesIO(image_response.content))
                extension = os.path.splitext(filename)[1]
                new_filename = os.path.join(dir, f"{secure_filename(filename)}{extension}")
                image.save(new_filename)
                print(f"Saved: {new_filename}")
            except Exception as e:
                print(f"Could not save image {image_url}: {e}")
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")

import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image
import io
def not_interactive_mix_mirrorImages(url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img = Image.open(io.BytesIO(img_response.content))
                img_name = os.path.join(dir, os.path.basename(img_url))
                img.save(img_name)

import requests
from bs4 import BeautifulSoup
import os
def baseline_mirrorImages(url, dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    for img_tag in image_tags:
        img_url = img_tag.get('src')
        if img_url.startswith('http'):
            img_data = requests.get(img_url).content
            img_name = img_url.split('/')[-1]
            img_path = os.path.join(dir, img_name)
            with open(img_path, 'wb') as f:
                f.write(img_data)

