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
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f'{tag_name}: {value}')
        else:
            print('No Exif data found')
    except Exception as e:
        print(f'An unexpected error occurred: {str(e)}')
            

def template_testForExif(imgFileName):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        image = Image.open(imgFileName)
        if hasattr(image, '_getexif'):
            exifdata = image._getexif()
            if exifdata is not None:
                for tag, value in exifdata.items():
                    tagname = TAGS.get(tag, tag)
                    print(f'{tagname}: {value}')
    except IOError:
        print(f'Error: Cannot open image file {imgFileName}')
    except Exception as e:
        print(f'An unexpected error occurred: {str(e)}')

import magic
import json
import json.decoder
MISSING_EXIF_ERROR = 'Missing Exif data'
UNDEFINED_EXIF_ERROR = 'Undefined EXIF tag'
def question_refinement_is_image_and_parse_exif(file_path):
    try:
        file_magic = magic.from_file(file_path, mime=True)
        if file_magic not in ['image/jpeg', 'image/png']:
            return {"error": "Invalid image format"}
        with open(file_path, 'rb') as file:
            exif_data = file.read()
            exif_dict = {}
            try:
                exif_json = json.loads(exif_data.decode('utf-8'))
                for tag, value in exif_json.items():
                    exif_dict[tag] = value
            except json.JSONDecodeError as e:
                if 'Exif' in str(e):
                    return {"error": MISSING_EXIF_ERROR}
                else:
                    return {"error": UNDEFINED_EXIF_ERROR}
            return exif_dict
    except Exception as e:
        return {"error": str(e) + ': ' + str(e.args[0]) if e.args else str(e)}

def alternative_approaches_testForExif(imgFileName):
    import piexif
    try:
        exif_dict = piexif.load(open(imgFileName, 'rb'))
        if exif_dict:
            return exif_dict
    except Exception as e:
        return {'error': str(e)}

def context_manager_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(imgFileName)
        data = img._getexif() if img._getexif() else None
        if data is not None:
            for tag, value in data.items():
                tag_name = TAGS.get(tag, tag)
                print(f'{tag_name}: {value}')
    except Exception as e:
        print(f'An unexpected error occurred: {str(e)}')
            

def iterative_prompting_3_test_for_exif(img_filename):
    from PIL import Image, ImageFile
    try:
        if not isinstance(img_filename, str):
            raise ValueError('File path must be a string.')
        if not os.path.exists(img_filename):
            raise FileNotFoundError(f'The file {img_filename} does not exist.')
        ImageFile.MAXBLOCK = 1024 * 1024 * 1024
        image = Image.open(img_filename)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                print(f'{ExifTags.TAGS.get(tag, tag)}: {value}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def iterative_prompting_4_test_for_exif(img_filename):
    from PIL import Image
    from PIL.ExifTags import TAGS
    import os
    import logging

    if not isinstance(img_filename, str):
        raise ValueError('The image file path must be a string.')
    if not img_filename:
        raise ValueError('The image file path must not be empty.')
    if not os.path.isfile(img_filename):
        raise FileNotFoundError(f'The file {img_filename} does not exist.')

    try:
        img = Image.open(img_filename)
        exifdata = img._getexif() or {}
        
        for tag, value in exifdata.items():
            tagname = TAGS.get(tag, tag)
            print(f'{tagname}: {value}')
    except IOError as e:
        print(f'An I/O error occurred: {e}')
    except AttributeError as e:
        print(f'No EXIF metadata available: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


def iterative_prompting_5_test_for_exif(img_filename):
    pass
    """
    import os
    from PIL import Image
    from PIL.ExifTags import TAGS
    if not os.path.isfile(img_filename):
        raise ValueError(f"The file {img_filename} does not exist or path is insecure.")
    safe_img_filename = os.path.basename(img_filename)
    if not safe_img_filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValueError("Unsupported file type.")
    try:
        img = Image.open(safe_img_filename)
    except IOError as e:
        raise IOError(f"An error occurred while opening the file: {e}")
    try:
        exif_data = img._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f'{tag_name}: {value}')
        else:
            print('No EXIF data')
    except AttributeError:
        print('EXIF data is not available or the file is not supported by the used version of PIL.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    """
import piexif
def few_shots_prompting_testForExif(imgFileName):
    try:
        exif_dict = piexif.load(imgFileName)
        for key, value in exif_dict.items():
            print(f'Tag: {key}, Value: {value}')
    except:
        pass

def cot_prompting_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(imgFileName)
        exif = img._getexif()
        if exif:
            return {TAGS[k]: v for k, v in exif.items() if k in TAGS}
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

from PIL import Image
import piexif
def fact_check_list_testForExif(imgFileName):
    try:
        with Image.open(imgFileName) as img:
            if hasattr(img, '_getexif'):
                exif_data = img._getexif()
                if exif_data is not None:
                    for tag, value in exif_data.items():
                        tag_name = TAGS.get(tag, tag)
                        if isinstance(value, bytes):
                            fields = piexif.load(value)
                            print(f"Tag: {tag_name}, Value: {fields['ifd{}.{}.data'.format(tag, TAGS[tag])]}")
                else:
                    print("No Exif data found.")
            else:
                print("This image does not support Exif data.")
    except IOError:
        print("Error opening or extracting from the image.")
TAGS = {271: 'DateTimeOriginal', 272: 'DateTimeDigitized', 273: 'Make', 274: 'Model', 275: 'ExposureTime'}

from PIL import Image
from PIL.ExifTags import TAGS
def not_interactive_mix_testForExif(imgFileName):
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
    except IOError:
        print("Error: Cannot open image or corrupt file.")

def baseline_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(imgFileName)
        info = img._getexif()
        if info is not None:
            for tag, value in info.items():
                tag_name = TAGS.get(tag, tag)
                print(f'{tag_name}: {value}')
    except IOError:
        print(f'Error: File {imgFileName} could not be opened.')

