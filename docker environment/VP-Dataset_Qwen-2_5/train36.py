import logging
from PIL import Image
from PIL.ExifTags import TAGS
import exif
import exifread
import piexif
import os

def ground_truth_code_testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
        return exifData
    except:
        pass

def persona__testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(imgFileName)
        exif_data = img._getexif()
        decoded_exif = {}
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                decoded_exif[tag] = value
        return decoded_exif
    except Exception as e:
        return str(e)

def template__testForExif(imgFileName):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        with Image.open(imgFileName) as img:
            exifData = img._getexif()
            if exifData:
                return {TAGS[tag]: value for tag, value in exifData.items()}
    except Exception as e:
        return str(e)

def question_refinement__testForExif(imgFileName):
    try:
        from PIL import Image
        import piexif
        img = Image.open(imgFileName)
        exif_data = piexif.load(img.info['exif'])
        result = [(piexif.TAGS[k].get(name, {}).get('name', name), value) for ifd in ('0th', 'Exif', 'GPS', '1st') for k, v in exif_data.items() for name, value in v.items()]
        return result
    except (FileNotFoundError, KeyError, IOError):
        return []

def alternative_approaches__testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    import io
    try:
        with open(imgFileName, 'rb') as f:
            img = Image.open(io.BytesIO(f.read()))
            exif_data = img._getexif()
            if exif_data:
                result = {TAGS.get(tag, tag): exif_data[tag] for tag in exif_data}
                return result
            else:
                return {}
    except FileNotFoundError:
        return {'error': 'File not found.'}
    except IOError:
        return {'error': 'Failed to read file.'}
    except Exception as e:
        return {'error': str(e)}

def context_manager__testForExif(imgFileName):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        img = Image.open(imgFileName)
        exif_data = img._getexif()
        decoded_exif = {}
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                decoded_exif[tag] = value
        return decoded_exif
    except Exception as e:
        return {'error': str(e)}

def flipped_interaction_3__testForExif(imgFileName):
    exifData = {}
    try:
        with Image.open(imgFileName) as img:
            info = img._getexif()
        if info:
            for tag, value in info.items():
                decoded_tag = TAGS.get(tag, tag)
        exifData[decoded_tag] = value
    except IOError:
        pass
    return exifData

def flipped_interaction_4__testForExif(imgFileName):
	from PIL import Image, ExifTags
	image = Image.open(imgFileName)
	extif_data = image._getexif()
	decoded_exif = {}
	if exif_data:
		for tag_id, value in exif_data.items():
			tag = ExifTags.TAGS.get(tag_id, tag_id)
			if tag == 'GPSInfo':
				gps_info = {}
				for gps_tag_id, gps_value in value.items():
					gps_tag = ExifTags.GPS_TAG_NAMES.get(gps_tag_id, gps_tag_id)
					gps_info[gps_tag] = gps_value
				decoded_exif[tag] = gps_info
			elif tag in ['DateTime', 'Make', 'Model']:
				decoded_exif[tag] = value
	return decoded_exif

def flipped_interaction_5__testForExif(imgFileName):
	from PIL import Image, ExifTags
	try:
		img = Image.open(imgFileName)
		exif_data = img._getexif()
		decoded_exif = {}
		if exif_data:
			for tag_id, value in exif_data.items():
				tag = ExifTags.TAGS.get(tag_id, tag_id)
				decoded_exif[tag] = value
		print(decoded_exif)
		return decoded_exif
	except Exception:
		skip

def iterative_prompting_3__testForExif(imgFileName):
    try:
        if not isinstance(imgFileName, str) or not imgFileName:
            return "Invalid input: imgFileName must be a non-empty string"
        if not imgFileName.endswith((".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG", ".tiff", ".TIFF")):
            return "Unsupported file format"
        im = Image.open(imgFileName)
        exif_data = im._getexif()
        if exif_data:
                decoded_exif = {}
                for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)
                        decoded_exif[tag] = value
                return decoded_exif
        return None
    except IOError:
        return "File cannot be opened or is not an image"
    except Exception as e:
        return f"An error occurred: {{e}}"

def iterative_prompting_4__testForExif(img_file_name):
    if not isinstance(img_file_name, str):
        raise ValueError("img_file_name must be a string")

    try:
        img = Image.open(img_file_name)
        exif_data = img._getexif()
    except IOError:
        return {"error": "Unable to open image file"}
    except Exception as e:
        return {"error": str(e)}
    if exif_data:
        decoded_exif = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            decoded_exif[tag] = value
        return decoded_exif
    else:
        return {"exif_data": None}

def iterative_prompting_5__testForExif(imgFileName):
    if not isinstance(imgFileName, str):
        raise ValueError('imgFileName must be a string')
    try:
        img_file = Image.open(imgFileName)
    except IOError as e:
        raise IOError(f'Error opening file {imgFileName}: {str(e)}')
    except Exception as e:
        raise Exception(f'An unexpected error occurred while opening file {imgFileName}: {str(e)}')
    try:
        exif_data = img_file.getexif()
        decoded_data = {}
        if exif_data:
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                decoded_data[decoded_tag] = value
    finally:
        img_file.close()
    return decoded_data

def few_shots_prompting__testForExif(imgFileName):
	from PIL import Image
	from PIL.ExifTags import TAGS
	img = Image.open(imgFileName)
	exif_data = img._getexif()
	if exif_data:
		for tag, value in exif_data.items():
			tag_name = TAGS.get(tag, tag)
			print(f'{tag_name}: {value}')

def cot_prompting__testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    img = Image.open(imgFileName)
    exif_data = img._getexif()
    if exif_data:
        exif = {TAGS.get(tag): value for tag, value in exif_data.items()}
        return exif
    else:
        return None

def fact_check_list__testForExif(imgFileName):
    try:
        with Image.open(imgFileName) as img:
            exif_data = img._getexif()
            if exif_data:
                decoded_exif_data = {TAGS.get(tag): value for tag, value in exif_data.items()}
                return decoded_exif_data
            else:
                return "No EXIF data found."
    except IOError:
        return "File not accessible or invalid image file."

def not_interactive_mix__testForExif(imgFileName):
    if not isinstance(imgFileName, str) or not imgFileName.strip():
        raise ValueError("Invalid file name provided")
    if not os.path.exists(imgFileName) or not os.path.isfile(imgFileName):
        raise FileNotFoundError(f"The specified file {imgFileName} does not exist or is not a file")
    try:
        img = Image.open(imgFileName)
        exif_data = img._getexif()
        if exif_data is None:
            return {}
        decoded_exif = {ExifTags.TAGS.get(tag): value for tag, value in exif_data.items() if tag in ExifTags.TAGS}
        return decoded_exif
    except IOError as e:
        warnings.warn(f"Failed to open image {imgFileName}: {e}", UserWarning)
        return {}
    finally:
        img.close()

def interactive_mix__testForExif(imgFileName):
    import logging
    import requests
    from PIL import Image
    from io import BytesIO
    from exifread import process_file
    from exifread.tags import TAGS
    logging.basicConfig(level=logging.ERROR)
    try:
        if imgFileName.startswith(('http://', 'https://')):
            response = requests.get(imgFileName)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(imgFileName)
        info = img._getexif()
        if not info:
            logging.error(f"No EXIF data found in {imgFileName}")
            return {"EXIF Data": "None"}
        exifData = {}
        for (tag, value) in info.items():
            decoded = TAGS.get(tag, tag)
            exifData[decoded] = value
        gpsInfo = exifData.get('GPSInfo', None)
        if not gpsInfo:
            exifData["GPS Info"] = "None"
        return exifData
    except FileNotFoundError:
        logging.error(f"File not found: {imgFileName}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching image from URL {imgFileName}: {e}")
    except IOError:
        logging.error(f"Unsupported image format: {imgFileName}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return {}

def baseline__testForExif(imgFileName):
	from PIL import Image
	from PIL.ExifTags import TAGS
	try:
		img = Image.open(imgFileName)
		exif_data = img._getexif()
		if exif_data:
			decoded_exif = {}
			for tag, value in exif_data.items():
				decoded_tag = TAGS.get(tag, tag)
				decoded_exif[decoded_tag] = value
			return decoded_exif
		else:
			return None
	except IOError:
		return 'File not found or unable to open.'
