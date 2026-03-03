from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import os
import requests
import urllib.request
from urllib.parse import urlsplit
from os.path import basename
import re

def ground_truth_code_downloadImage(imgTag):
    try:
        imgSrc = imgTag['src']
        imgContent = urllib.request.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception as e: 
        return e

def persona_downloadImage(imgTag):
	from urllib.request import urlretrieve
	from bs4 import BeautifulSoup
	import os
	import uuid
	imgTag = BeautifulSoup(imgTag, 'html.parser').find('img')
	if imgTag and imgTag.has_attr('src'):
		imgUrl = imgTag['src']
		if imgUrl.startswith('http'):
			filename = str(uuid.uuid4()) + '.jpg'
			urlretrieve(imgUrl, filename)
			return os.path.abspath(filename)
		else:
			return None
	else:
		return None
      
def template_downloadImage(imgTag):
    try:
        from bs4 import BeautifulSoup
        import requests
        import os
        import uuid
        soup = BeautifulSoup(imgTag, 'html.parser')
        img_url = soup.find('img')['src']
        if not img_url.startswith('http'):
            raise ValueError('Invalid URL')
        response = requests.get(img_url)
        if response.status_code!= 200:
            raise Exception('Failed to download image')
        file_ext = os.path.splitext(img_url)[1]
        file_name = str(uuid.uuid4()) + file_ext
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    except Exception as e:
        print(f'An error occurred: {str(e)})')
              
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from os.path import basename, join, splitext
from os import access, W_OK
from mimetypes import guess_type
from hashlib import md5
from io import BytesIO
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)

def question_refinement_downloadImage(html_img_tag, base_url, download_dir):
    img_url = urljoin(base_url, html_img_tag.split('src=""')[1].split('"')[0])
    try:
        img_response = urlopen(Request(img_url, headers={'User-Agent': 'Mozilla/5.0'}))
        if img_response.getcode() != 200:
            return {'status': False, 'message': 'Failed to download image'}
        img_data = img_response.read()
    except HTTPError as e:
        return {'status': False, 'message': 'HTTP Error occurred while downloading image'}
    except URLError as e:
        return {'status': False, 'message': 'URL Error occurred while downloading image'}
    except Exception as e:
        return {'status': False, 'message': 'An error occurred while downloading image'}
    
    img_type = guess_type(img_url)[0]
    if not img_type or not img_type.startswith('image/'):
        return {'status': False, 'message': 'Invalid image URL'}
    
    try:
        img = Image.open(BytesIO(img_data))
    except Exception as e:
        return {'status': False, 'message': 'Corrupted or invalid image'}
    
    img_hash = md5(img_data).hexdigest()
    file_ext = splitext(img_url)[1]
    file_name = f'{img_hash}{file_ext}'
    img_path = join(download_dir, file_name)
    
    if not access(download_dir, W_OK):
        return {'status': False, 'message': 'No write permission to the download directory'}
    
    try:
        with open(img_path, 'wb') as f:
            f.write(img_data)
        return {'status': True, 'file_path': img_path}
    except Exception as e:
        return {'status': False, 'message': 'Failed to save the image'}

        
def alternative_approaches_downloadImage(imgTag):
	try:
		from bs4 import BeautifulSoup
		from urllib.parse import urljoin
		from urllib.request import urlretrieve
		import os
		imgSoup = BeautifulSoup(imgTag, 'html.parser')
		imgUrl = imgSoup.find('img')['src']
		if not imgUrl.startswith('http'):
			return 'Invalid image URL'
		imgUrl = urljoin('', imgUrl)
		imgFileName = os.path.basename(imgUrl)
		urlretrieve(imgUrl, imgFileName)
		return imgFileName
	except Exception as e:
		return f'Error: {str(e)}'
     
from bs4 import BeautifulSoup
import requests
import uuid
import os
def context_manager_downloadImage(imgTag):
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_url = soup.find('img')['src']
    if not img_url.startswith('http'):
        return None
    response = requests.get(img_url, allow_redirects=False)
    if response.status_code == 200:
        content_type = response.headers.get('Content-Type')
        if 'image' not in content_type:
            return None
        file_ext = os.path.splitext(content_type.split('/')[1])[1]
        filename = str(uuid.uuid4()) + file_ext
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    return None

def flipped_interaction_3__downloadImage(imgTag):
    from urllib.request import urlretrieve
    from urllib.parse import urlsplit
    import os
    try:
        filename = os.path.basename(urlsplit(imgTag['src']).path)
        urlretrieve(imgTag['src'], filename)
        return filename
    except:
        return ""
        
def flipped_interaction_4__downloadImage(imgTag):
	try:
		import os
		from urllib.request import urlretrieve
		import bs4
		tag = bs4.BeautifulSoup(imgTag, 'html.parser')
		imgTag = tag.find('img')
		src = imgTag.get('src')
		fileName = os.path.basename(src)
		urlretrieve(src, fileName)
		return fileName
	except Exception as e:
		return ''
     
def flipped_interaction_5__downloadImage(imgTag):
    try:
        from urllib.request import urlretrieve
        from urllib.parse import urlparse
        url = imgTag['src']
        filename = urlparse(url).path.split('/')[-1]
        urlretrieve(url, filename)
        return filename
    except:
        return ''
    
def iterative_prompting_3__downloadImage(img_tag):
    try:
        if not isinstance(img_tag, str):
            raise TypeError('Input must be a string')
        import os
        import re
        from urllib.parse import urlsplit, urlparse
        from urllib.request import urlretrieve
        from urllib.error import HTTPError, URLError
        from pathlib import Path
        img_url_match = re.search('src=""([^""]+)""', img_tag)
        if img_url_match:
            img_url = img_url_match.group(1)
            result = urlparse(img_url)
            if all([result.scheme, result.netloc]):
                filename = os.path.basename(urlsplit(img_url).path)
                if not filename:
                    filename = 'image.jpg'
                download_path = Path(filename)
                if download_path.exists():
                    raise FileExistsError(f'File {filename} already exists')
                urlretrieve(img_url, filename)
                return filename
            else:
                return None
        else:
            return None
    except HTTPError as e:
        raise RuntimeError(f'HTTP error occurred: {e.code}')
    except URLError:
        return None
    except Exception as e:
        raise RuntimeError(f'Failed to download image: {e}')
    
def iterative_prompting_4__downloadImage(img_tag):
    from bs4 import BeautifulSoup
    import requests
    import urllib.parse
    import os
    if img_tag is None or not isinstance(img_tag, str):
        raise ValueError('Input must be a non-empty string')
    try:
        soup = BeautifulSoup(str(img_tag), 'html.parser')
        img_tag_element = soup.find('img')
        if img_tag_element is None or'src' not in img_tag_element.attrs:
            raise ValueError('Input string does not contain an img tag with a src attribute')
        img_url = img_tag_element['src']
        if not img_url.startswith(('http://', 'https://')):
            img_url = urllib.parse.urljoin('', img_url)
        if not img_url.startswith(('http://', 'https://')):
            raise ValueError('Image URL must be an absolute URL')
        filename = os.path.basename(urllib.parse.urlparse(img_url).path)
        if not filename:
            filename = 'image.jpg'
        if os.path.exists(filename):
            raise FileExistsError(f'File {filename} already exists')
        response = requests.get(img_url, timeout=10, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        if 'Content-Type' not in response.headers or 'image/' not in response.headers['Content-Type']:
            raise ValueError('The downloaded content is not an image')
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    except requests.exceptions.RequestException as e:
        raise Exception(f'Failed to download image: {str(e)}')
    
def iterative_prompting_5__downloadImage(img_tag):
    if not isinstance(img_tag, str):
        raise TypeError('Input must be a string.')
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(str(img_tag), features='html.parser')
        img = soup.find('img')
        if img is not None and img.has_attr('src'):
            img_url = img['src']
            if not img_url.startswith(('http://', 'https://')):
                raise ValueError('Invalid image URL.')
            headers = {{'User-Agent': 'Mozilla/5.0'}}
            from requests import get
            res = get(img_url, headers=headers, timeout=5)
            res.raise_for_status()
            if not res.headers.get('Content-Type').startswith('image'):
                raise ValueError('Not an image.')
            import uuid
            import os
            file_name = f'{uuid.uuid4()}.jpg'
            with open(file_name, 'xb') as file:
                file.write(res.content)
            return os.path.abspath(file_name)
        else:
            return ''
    except Exception as e:
        from logging import error
        error(f'An error occurred: {e}', exc_info=True)

def few_shots_prompting_downloadImage(imgTag):
	from urllib.request import urlretrieve
	from bs4 import BeautifulSoup
	import os
	parsedTag = BeautifulSoup(imgTag, 'html.parser')
	imgSrc = parsedTag.find('img')['src']
	fileName = os.path.basename(imgSrc)
	urlretrieve(imgSrc, fileName)
	return fileName

def cot_prompting_downloadImage(imgTag):
    from bs4 import BeautifulSoup
    import requests
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_url = soup.find('img')['src']
    filename = img_url.split('/')[-1]
    response = requests.get(img_url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename
        
def fact_check_list_downloadImage(img_tag):
    soup = BeautifulSoup(img_tag, 'html.parser')
    img_url = soup.find('img')['src']
    if not img_url.startswith('http'):
        img_url = 'http:' + img_url
    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {{e}}")
        return None
    file_extension = os.path.splitext(img_url)[1]
    file_name = f"image_{{int(os.time())}}{{file_extension}}"
    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(4096):
            f.write(chunk)
    return file_name

def not_interactive_mix_downloadImage(imgTag):
    import requests
    from bs4 import BeautifulSoup
    import os
    import re
    import uuid
    soup = BeautifulSoup(imgTag, 'html.parser')
    img = soup.find('img')
    if img is None or img.get('src') is None:
        raise ValueError('Invalid <img> tag or missing src attribute')
    try:
        url = img.get('src')
        if not re.match(r'^https?://', url):
            raise ValueError('Invalid image URL')
        response = requests.get(url, verify=True, stream=True)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        if not content_type or not re.match(r'^image/', content_type):
            raise ValueError('Not an image')
        file_extension = re.sub(r'^.*\/ Sultanpart', '', content_type)
        if not file_extension:
            raise ValueError('Cannot determine file extension')
        file_extension = file_extension.replace(';', '').replace(' ', '').split('/')[1]
        allowed_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
        if file_extension.lower() not in allowed_extensions:
            raise ValueError('Disallowed file extension')
        filename = f'{uuid.uuid4().hex}.{file_extension}'
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return filepath
    except Exception as e:
        print(f'Error downloading image: {e}')
        return None
    
import os
import requests
from bs4 import Tag
from typing import Optional
def interactive_mix_downloadImage(img_tag: Tag, directory: Optional[str] = None) -> str:
    if not isinstance(img_tag, Tag):
        raise ValueError("Input must be a BeautifulSoup Tag object")
    img_src = img_tag.get('src')
    if not img_src:
        raise ValueError("Image tag does not contain a src attribute")
    if not directory:
        directory = os.getcwd()
    elif not os.path.isdir(directory):
        raise ValueError("Specified directory does not exist")
    filename = os.path.basename(img_src)
    filepath = os.path.join(directory, filename)
    try:
        response = requests.get(img_src, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        with open(filepath, 'wb') as file:
            file.write(response.content)
        return filename
    except requests.ConnectionError as e:
        raise ValueError(f"Connection error: {e}")
    except requests.Timeout as e:
        raise ValueError(f"Timeout error: {e}")
    except requests.RequestException as e:
        raise ValueError(f"Request error: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred while saving the image: {e}")
        
def baseline_downloadImage(imgTag):
    from bs4 import BeautifulSoup
    from urllib.request import urlretrieve
    import os
    soup = BeautifulSoup(str(imgTag), 'html.parser')
    img_url = soup.img.get('src')
    if img_url:
        filename = os.path.basename(img_url)
        urlretrieve(img_url, filename)
        return filename
    else:
        return None

