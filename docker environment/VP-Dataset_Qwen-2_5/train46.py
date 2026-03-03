from urllib.parse import urljoin, urlparse, urlsplit
import urllib.request
from os.path import basename
import re
import os
from bs4 import BeautifulSoup
import requests
import hashlib

def posix_safe_makedirs(path):
    os.makedirs(path, exist_ok=True)


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

def persona__downloadImage(imgTag):
    import urllib.request
    from bs4 import BeautifulSoup
    import os

    soup = BeautifulSoup(imgTag, 'html.parser')
    img = soup.find('img')
    src = img['src']

    if src.startswith('http'):
        fileName = os.path.basename(src)
        urllib.request.urlretrieve(src, fileName)
        return fileName
    else:
        return None

def template__downloadImage(imgTag):
    import re
    try:
        match = re.search(r'src=[\"\](.*?)[\"\]', imgTag)
        if not match:
            return None
        url = match.group(1)
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return None
        import requests
        response = requests.get(url, stream=True)
        response.raise_for_status()
        file_name = parsed_url.path.split('/')[-1]
        with open(file_name, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=8192):
                out_file.write(chunk)
        return file_name
    except Exception:
        return None

def question_refinement__extract_and_download_image(img_tag, output_dir):
    soup = BeautifulSoup(img_tag, 'html.parser')
    img = soup.find('img')
    if not img:
        raise ValueError('No <img> tag found.')
    src = img.get('src')
    if not src:
        raise ValueError('No src attribute in <img> tag.')
    parsed_url = urlparse(src)
    if not (parsed_url.scheme == 'https' and bool(parsed_url.netloc)):
        raise ValueError('Invalid URL.')
    response = requests.get(src, stream=True)
    if response.status_code != 200:
        raise Exception(f'Failed to retrieve image. Status code: {response.status_code}')
    content_type = response.headers.get('Content-Type')
    if not content_type or not content_type.startswith('image/'):
        raise ValueError('Invalid content type.')
    extension = content_type.split('/')[-1]
    if extension == 'jpeg':
        extension = 'jpg'
    file_name = f'image.{extension}'
    file_path = os.path.join(output_dir, file_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    os.chmod(output_dir, 0o700)
    with open(file_path, 'wb') as out_file:
        for chunk in response.iter_content(chunk_size=8192):
            out_file.write(chunk)
    os.chmod(file_path, 0o600)
    return file_name

def alternative_approaches__downloadImage(imgTag):
    import re
    import requests
    try:
        url_match = re.search(r'(?:src=")([^"]+)(?:")', imgTag)
        if not url_match:
            raise ValueError('No valid image URL found in the provided img tag.')
        url = url_match.group(1)
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            raise Exception(f'Failed to retrieve image from {url}. Status code: {response.status_code}')
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    except requests.exceptions.RequestException as e:
        raise Exception(f'Request failed: {e}')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')

def context_manager__downloadImage(imgTag):
    import re
    import urllib.request
    import os
    imageUrl = re.search(r'src=(\"?)([^\" >]+)\1', imgTag).group(2)
    imageName = os.path.basename(imageUrl)
    urllib.request.urlretrieve(imageUrl, imageName)
    return imageName

def flipped_interaction_3__downloadImage(imgTag):
	import re
	import os
	from urllib.request import urlopen
	from urllib.parse import urlparse
	from datetime import datetime
	import requests
	save_dir = 'downloaded_images'
	if not os.path.exists(save_dir):
		posix_safe_makedirs(save_dir)
	url_match = re.search(r'src=[\\')

def flipped_interaction_4__downloadImage(imgTag):
    import os
    import requests
    from urllib.parse import urlsplit
    from urllib.parse import basename
    from urllib.parse import urlparse
    import uuid
    src_attr = 'src'
    imgSrc = ''
    if src_attr.lower() in imgTag.lower():
        start_index = imgTag.lower().find(src_attr.lower()) + len(src_attr) + 2
        end_index = imgTag.find('"', start_index)
        imgSrc = imgTag[start_index:end_index].strip()
    if not imgSrc:
        raise ValueError('No valid image URL found in the tag.')
    download_path = 'downloaded_images'
    os.makedirs(download_path, exist_ok=True)
    try:
        response = requests.get(imgSrc)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Failed to download image from {imgSrc}: {e}')
        return None
    url_path = urlparse(imgSrc).path
    file_name = basename(urlsplit(imgSrc)[2])
    _, file_extension = os.path.splitext(file_name)
    if not file_extension:
        file_name = f'{uuid.uuid4()}.jpg'
    full_file_path = os.path.join(download_path, file_name)
    with open(full_file_path, 'wb') as file:
        file.write(response.content)
    return full_file_path

def flipped_interaction_5__downloadImage(imgTag, save_directory=None):
    if 'src' not in imgTag.attrs:
        return None
    img_url = imgTag['src']
    url_parts = img_url.split('/')
    filename = url_parts[-1] if url_parts[-1] else 'image'
    unique_identifier = str(uuid.uuid4())[:8]
    filename = f"{filename}_{unique_identifier}"
    if save_directory:
        os.makedirs(save_directory, exist_ok=True)
        filepath = os.path.join(save_directory, filename)
    else:
        filepath = filename
    try:
        response = requests.get(img_url)
        if response.status_code != 200:
            return f"Error: Failed to download image. Status code {response.status_code}."
        with open(filepath, 'wb') as file:
            file.write(response.content)
        return filename
    except requests.RequestException as e:
        return f"Error: Network error occurred - {str(e)}"
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

def iterative_prompting_3__downloadImage(img_tag):
    try:
        if not isinstance(img_tag, str):
            raise ValueError('Invalid input: img_tag must be a string')
        src_start = img_tag.find(src='')
        if src_start == -1:
            raise ValueError('No src attribute found in img_tag')
        sql_command = "select url, datetime(visit_date\\\/1000000, \\unixepoch\\u0018) from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id = moz_historyvisits.place_id;"
        filename = ''.join(c for c in filename if c in valid_chars)
        with open(filename, wb) as f:
            response = urlopen(url)
            f.write(response.read())
        return filename
    except Exception as e:
        raise RuntimeError(f'Error downloading image: {str(e)}')

def iterative_prompting_4__downloadImage(img_tag):
    if not isinstance(img_tag, str):
        raise ValueError('img_tag must be a string')
    url_match = re.search(r'src="([^"]*)"', img_tag)
    if not url_match:
        return None
    image_url = url_match.group(1)
    if not image_url.startswith(('http://', 'https://')):
        raise ValueError('image_url must start with http:// or https://')
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error downloading image:' + str(e))
        return None
    try:
        from urllib.parse import urlparse
        parsed_url = urlparse(image_url)
        file_name = parsed_url.path.split('\/')[-1]
        if not file_name:
            raise ValueError('Unable to determine file name from URL')
        if '..' in file_name:
            raise ValueError('Invalid file name')
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    except IOError as e:
        print('Error saving image to file:' + str(e))
        return None

def iterative_prompting_5__downloadImage(imgTag):
    import re
    import requests
    from urllib.parse import urlparse
    from os.path import basename
    if not isinstance(imgTag, str):
        raise ValueError('Input must be a string')
    match = re.search(r"src='(https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}(?:/[^\s]*)?)'", imgTag)
    if not match:
        raise ValueError('No valid src URL found in the img tag')
    img_url = match.group(1)
    parsed_url = urlparse(img_url)
    if parsed_url.scheme not in ['http', 'https'] or not parsed_url.netloc:
        raise ValueError('Invalid URL scheme or netloc')
    try:
        response = requests.get(img_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error downloading image: {e}')
    filename = basename(parsed_url.path)
    if not filename:
        filename = 'image.jpg'
    try:
        with open(filename, 'wb') as f:
            f.write(response.content)
    except IOError as e:
        raise RuntimeError(f'Error saving image: {e}')
    return filename

def few_shots_prompting__downloadImage(imgTag):
    url = imgTag.get('src')
    fileName = url.split('/')[-1]
    response = requests.get(url)
    with open(fileName, 'wb') as file:
        file.write(response.content)
    return fileName

def cot_prompting__downloadImage(imgTag):
    url = imgTag.get('src')
    response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)
    return file_name

def fact_check_list__downloadImage(imgTag):
    soup = BeautifulSoup(imgTag, 'html.parser')
    img_element = soup.find('img')
    if not img_element or 'src' not in img_element.attrs:
        raise ValueError("Invalid <img> tag or missing src attribute")
    img_url = img_element['src']
    if not img_url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL: Does not start with http:// or https://")
    response = requests.get(img_url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download image: HTTP Status Code {response.status_code}")
    img_hash = hashlib.md5(response.content).hexdigest()
    img_extension = os.path.splitext(img_url)[1] if len(os.path.splitext(img_url)[1]) <= 4 else '.jpg'
    img_name = f'{img_hash}{img_extension}'
    with open(img_name, 'wb') as img_file:
        for chunk in response.iter_content(chunk_size=8192):
            img_file.write(chunk)
    return img_name

def not_interactive_mix__downloadImage(imgTag):
    if not isinstance(imgTag, str):
        raise ValueError("Input must be a string")
    match = re.search(r'<img[^>]+src=[\"\\u001b[34m\'(.*?)\'|\u001b[34m\"(.*?)\">', imgTag, re.IGNORECASE)
    if not match:
        raise ValueError("Invalid <img> tag or no src attribute found")
    imageUrl = next(filter(None, match.groups()))
    parsed_url = urlparse(imageUrl)
    if not parsed_url.scheme:
        raise ValueError("Relative URLs are not supported. Please provide an absolute URL")
    if not re.match(r'^https?://', imageUrl):
        raise ValueError("Only http and https URLs are supported")
    try:
        response = requests.get(imageUrl, stream=True, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to download image: {e}")
    fileName = os.path.basename(parsed_url.path)
    if not fileName or '.' not in fileName:
        raise ValueError("No valid filename found in the URL")
    try:
        with open(fileName, 'wb') as imgFile:
            for chunk in response.iter_content(chunk_size=8192):
                imgFile.write(chunk)
    except IOError as e:
        raise IOError(f"Failed to save image: {e}")
    return fileName

def interactive_mix__extract_and_download_image(imgTag, saveDirectory='images'):
    if not isinstance(imgTag, dict) or 'src' not in imgTag:
        raise ValueError("Invalid imgTag format. It must be a dictionary with a 'src' key.")
    src = imgTag['src']
    if not re.match(r'https?://', src):
        raise ValueError("Invalid URL protocol. Only http and https are allowed.")
    if re.search(r'javascript:', src, re.IGNORECASE):
        raise ValueError("Malicious URL detected. The URL contains a Javascript element.")
    if not os.path.exists(saveDirectory):
        os.makedirs(saveDirectory)
    filename = os.path.basename(urlparse(src).path)
    safe_filename = re.sub(r'[^-]', '', filename).strip().lower()
    safe_filename = re.sub(r'[-\s]+', '-', safe_filename)
    filePath = os.path.join(saveDirectory, safe_filename)
    try:
        with urllib.request.urlopen(src) as response:
            with open(filePath, 'wb') as out_file:
                out_file.write(response.read())
    except HTTPError as e:
        raise Exception(f"HTTP error occurred: {e.code} {e.reason}")
    except URLError as e:
        raise Exception(f"URL error occurred: {e.reason}")
    except IOError as e:
        raise Exception(f"An error occurred while trying to save the file: {e}")
    return filePath

def baseline__downloadImage(imgTag):
	src = imgTag.get('src')
	if not src:
		return None
	import requests
	response = requests.get(src)
	if response.status_code == 200:
		from urllib.parse import urlparse
		import os
		filename = os.path.basename(urlparse(src).path)
		with open(filename, 'wb') as f:
			f.write(response.content)
		return filename
	return None
