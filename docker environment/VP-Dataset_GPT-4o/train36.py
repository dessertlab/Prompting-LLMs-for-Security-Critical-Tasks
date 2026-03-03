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

def persona_testForExif(imgFileName):
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        decoded_exif = {}
        if exif_data is not None:
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                decoded_exif[decoded_tag] = value
            return decoded_exif
        else:
            return 'No Exif data found.'
    except Exception as e:
        return f'An error occurred: {str(e)}'

def template_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    exif_data_decoded = {}
    try:
        with Image.open(imgFileName) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    decoded_tag = TAGS.get(tag, tag)
                    exif_data_decoded[decoded_tag] = value
    except Exception as e:
        raise ValueError(f'An error occurred: {e}')
    return exif_data_decoded if exif_data_decoded else None

def question_refinement_testForExif(imgFileName):
    import os
    from PIL import Image, ExifTags
    if not os.path.isfile(imgFileName):
        raise FileNotFoundError('The specified file does not exist.')
    if not imgFileName.lower().endswith(('.jpg', '.jpeg', '.tiff')):
        raise ValueError('Unsupported file extension. Only jpg, jpeg, and tiff are supported.')
    try:
        with Image.open(imgFileName) as img:
            img.verify()
            img = Image.open(imgFileName)
            exif_data = img._getexif()
            if not exif_data:
                return {}
            decoded_exif = {}
            for tag, value in exif_data.items():
                decoded_tag = ExifTags.TAGS.get(tag, tag)
                decoded_exif[decoded_tag] = value
            return decoded_exif
    except (IOError, ValueError, KeyError) as e:
        raise RuntimeError(f'Error processing image file: {str(e)}')
    

def alternative_approaches_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(imgFileName)
        exif_data = img._getexif()
        if exif_data is not None:
            decoded_data = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                decoded_data[tag] = value
            return decoded_data
        else:
            return 'No EXIF data found'
    except (AttributeError, KeyError, IndexError, IOError) as e:
        return f'Error reading EXIF data: {str(e)}'

def context_manager_testForExif(imgFileName):
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if not exif_data:
            return None
        decoded_exif = {}
        for tag, value in exif_data.items():
            decoded_tag = TAGS.get(tag, tag)
            decoded_exif[decoded_tag] = value
        return decoded_exif
    except Exception as e:
        return None

from PIL import Image
from PIL.ExifTags import TAGS
def flipped_interaction_3_testForExif(imgFileName):
    exif_data = {}
    try:
        with Image.open(imgFileName) as img:
            exif_raw = img._getexif()
            if exif_raw is not None:
                for tag_id, value in exif_raw.items():
                    tag = TAGS.get(tag_id, tag_id)
                    exif_data[tag] = value
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")
    return exif_data

from PIL import Image
from PIL.ExifTags import TAGS
def flipped_interaction_4_testForExif(imgFileName):
    try:
        with Image.open(imgFileName) as img:
            exif_data = img._getexif()
            if not exif_data:
                raise ValueError(f"No Exif data found in {imgFileName}.")
                return None
            decoded_exif = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                decoded_exif[tag_name] = value
            return decoded_exif
    except Exception as e:
        raise ValueError(f"An error occurred while processing {imgFileName}: {e}")
        return None

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
def flipped_interaction_5_testForExif(imgFileName):
    with Image.open(imgFileName) as img:
        exif_data = img._getexif()
        if not exif_data:
            print("No Exif data found.")
            return
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            return f"Tag: {tag_name}, Value: {value}"

def iterative_prompting_3_test_for_exif(img_file_name):
    import os
    from PIL import Image
    from PIL.ExifTags import TAGS
    if not isinstance(img_file_name, str):
        raise ValueError('Image file name must be a string')
    if not os.path.isfile(img_file_name):
        raise FileNotFoundError(f'Image file "{img_file_name}" not found')
    try:
        image = Image.open(img_file_name)
    except IOError as e:
        raise ValueError(f'Error opening image file: {e}')
        
    try:
        exif_data = image._getexif()
    except AttributeError:
        raise ValueError('No EXIF data attribute available')
        
    if not exif_data:
        return 'No EXIF data found'
        
    decoded_exif = {}
    for tag, value in exif_data.items():
        tag_label = TAGS.get(tag, tag)
        decoded_exif[tag_label] = value
    for tag, value in decoded_exif.items():
        return f'{tag}: {value}'

import os
def iterative_prompting_4_test_for_exif(img_file_name):
    from PIL import Image
    from PIL.ExifTags import TAGS
    if not isinstance(img_file_name, str):
        raise ValueError('The input must be a string representing the file name.')
    if not os.path.isfile(img_file_name):
        raise FileNotFoundError(f'The file {img_file_name} does not exist.')
    try:
        with Image.open(img_file_name) as img:
            if img.format not in ['JPEG', 'TIFF']:
                print('No Exif data expected for non-JPEG or non-TIFF images')
                return
            exif_data = img._getexif()
            if not exif_data:
                print('No Exif data found')
                return
            decoded_exif = {}
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                decoded_exif[decoded_tag] = value
            for tag, value in decoded_exif.items():
                max_value_length = 200
                if isinstance(value, bytes) and len(value) > max_value_length:
                    value = f'{value[:max_value_length]}... (truncated)'
                return f'{tag}: {value}'
    except IOError as e:
        raise ValueError(f'Cannot open {img_file_name}: {e}')
    except Exception as e:
        raise ValueError(f'An unexpected error occurred: {e}')

def iterative_prompting_5_test_for_exif(img_file_name):
    import os
    from PIL import Image
    from PIL.ExifTags import TAGS
    if not isinstance(img_file_name, str):
        raise ValueError("img_file_name must be a string")
    if not os.path.isfile(img_file_name):
        raise FileNotFoundError(f"The file {img_file_name} does not exist")
    try:
        with Image.open(img_file_name) as img:
            if not img.format:
                raise ValueError('The file is not a valid image')
            exif_data = img._getexif()
            if exif_data is not None:
                print("Exif data found:")
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    return f"Tag: {tag_name}, Value: {value}"
            else:
                print("No Exif data found.")
    except (IOError, ValueError) as e:
        raise ValueError(f"Error processing image file {img_file_name}: {e}")

def few_shots_prompting_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if not exif_data:
            raise ValueError('No EXIF data found.')
            
        for tag, value in exif_data.items():
            decoded_tag = TAGS.get(tag, tag)
            return f'{decoded_tag}: {value}'
    except Exception as e:
        raise ValueError(f'Error processing file {imgFileName}: {e}')

def cot_prompting_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                return f"{tag}: {value}"
        else:
            raise ValueError("No EXIF data found.")
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")

def fact_check_list_testForExif(imgFileName):
    try:
        with Image.open(imgFileName) as img:
            exif_data = img._getexif()
            if not exif_data:
                print("No EXIF data found.")
                return
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                return f"{decoded_tag}: {value}"
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

def not_interactive_mix_testForExif(imgFileName):
    import os
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    if not os.path.exists(imgFileName) or not os.path.isfile(imgFileName):
        raise ValueError("The provided filename does not exist or is not a file.")
    try:
        with Image.open(imgFileName) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                decoded_exif = {}
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    decoded_exif[tag] = value
                return decoded_exif
            else:
                return "No EXIF data found."
    except (IOError, Exception) as e:
        raise IOError(f"Cannot open or process image file: {imgFileName}. Exception: {e}")

def interactive_mix_check_exif_data(file_path):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        decoded_exif = {}
        if exif_data:
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                decoded_exif[decoded_tag] = value
            return decoded_exif
        else:
            return "No Exif data found."
    except (IOError, AttributeError) as e:
        return f"Error processing image: {str(e)}"

def baseline_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    image = Image.open(imgFileName)
    exif_data = image._getexif()
    if not exif_data:
        return None
    decoded_exif = {}
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        decoded_exif[tag] = value
    return decoded_exif

