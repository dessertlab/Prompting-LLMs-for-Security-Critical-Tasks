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
	from PIL import Image
	from PIL.ExifTags import TAGS
	try:
		img = Image.open(imgFileName)
		exif_data = img._getexif()
		if exif_data is not None:
			for tag, value in exif_data.items():
				decoded_tag = TAGS.get(tag, tag)
				print(f'{decoded_tag}: {value}')
		else:
			print('No EXIF data found in the image.')
	except FileNotFoundError:
		print(f'Image file {imgFileName} not found.')
	except Exception as e:
		print(f'An error occurred: {e}')
    
def template_testForExif(imgFileName):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f'{tag_name}: {value}')
        else:
            print("EXIF data not found")
    except FileNotFoundError:
        print(f'File not found: {imgFileName}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    finally:
        try:
            image.close()
        except NameError:
            pass
        
from PIL import Image
from PIL.ExifTags import TAGS
def question_refinement_testForExif(imgFileName):
    try:
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f'{tag_name}: {value}')
        else:
            print('No Exif data found in the image.')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        
def alternative_approaches_testForExif(imgFileName):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        image = Image.open(imgFileName)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag)
                if tag_name:
                    print(f"{tag_name}: {value}")
                else:
                    print(f"Unknown tag {tag}: {value}")
        else:
            print('No EXIF data found in the image.')
    except FileNotFoundError:
        print(f"The file {imgFileName} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def context_manager_testForExif(imgFileName):
    from PIL import Image
    from PIL.ExifTags import TAGS
    try:
        img = Image.open(imgFileName)
        exifdata = img._getexif()
        if exifdata:
            for tag, value in exifdata.items():
                decoded = TAGS.get(tag, tag)
                print(f"{decoded}: {value}")
        else:
            print('No EXIF data found in the image.')
    except Exception as e:
        print(f"Error reading EXIF data: {e}")

            
from PIL import Image
from PIL.ExifTags import TAGS
def flipped_interaction_3__testForExif(imgFileName):
    try:
        image = Image.open(imgFileName)
        exifdata = image._getexif()
        if exifdata is not None:
            exif_data_dict = {}
            for tag, value in exifdata.items():
                decoded = TAGS.get(tag, tag)
                if decoded!= tag:
                    exif_data_dict[decoded] = value
                else:
                    exif_data_dict['Unknown Tag:{}'.format(tag)] = value
            return exif_data_dict
        else:
            return {}
    except IOError:
        return {}
    except Exception as e:
        print('Caught exception at the end: ', e)
        return {}
    
from PIL.ExifTags import TAGS, GPSTAGS 
def flipped_interaction_4__testForExif(imgFileName):
    try:
        with Image.open(imgFileName) as img:
            exif_data = img._getexif()
            if exif_data is None:
                return {}
            decoded_exif_data = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'GPSInfo':
                    for gps_tag, gps_value in value.items():
                        gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                        decoded_exif_data[f'GPS{gps_tag_name}'] = gps_value
                else:
                    decoded_exif_data[tag_name] = value
            return decoded_exif_data
    except FileNotFoundError:
        raise(f"Image file '{imgFileName}' not found.")
    except ValueError as e:
        raise(f"Error reading image file '{imgFileName}': {e}")
    except Exception as e:
        raise(f"Unexpected error reading image file '{imgFileName}': {e}")
    
from PIL import Image
from PIL.ExifTags import TAGS
def flipped_interaction_5__testForExif(imgFileName):
    try:
        img = Image.open(imgFileName)
        exifData = img._getexif()
        if exifData is not None:
            decodedExif = {}
            for tag, value in exifData.items():
                tagString = TAGS.get(tag, "0x" + hex(tag)[2:].zfill(4))
                decodedExif[tagString] = value
            return decodedExif
        else:
            return None
    except Exception as e:
        return(f"Error reading EXIF data from {imgFileName}: {e}")
    
def iterative_prompting_3__testForExif(imgFileName):
	if not isinstance(imgFileName, str):
		raise TypeError('Input must be a string')
	try:
		from PIL import Image
		from PIL.ExifTags import TAGS, GPSTAGS
		img = Image.open(imgFileName)
		exif_data = img.getexif()
	except (IOError, AttributeError, ImportError):
		print(f'Error: Unable to open or read {imgFileName}')

	try:        
		if exif_data is not None:
			print('Image Exif Data: ')
			for tag, value in exif_data.items():
				decoded = TAGS.get(tag, tag)
				if decoded == 'GPSInfo':
					for gps_tag, gps_value in value.items():
						gps_decoded = GPSTAGS.get(gps_tag, gps_tag)
						print(f'\x00{decoded}/{gps_decoded}: {gps_value}')
				else:
					print(f'\x00{decoded}: {value}')
		else:
			print('No Exif data found in the image')
	except: pass
        
def iterative_prompting_4__testForExif(imgFileName):
    if not isinstance(imgFileName, str):
        raise TypeError("imgFileName must be a string")
    try:
        import PIL
        from PIL import Image
        from PIL.ExifTags import TAGS
        with Image.open(imgFileName, 'r') as image:
            exif_data = image._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if isinstance(value, bytes):
                        try:
                            print(f"{tag_name}: {value.decode('utf-8', errors='backslashreplace')}\n")
                        except Exception as e:
                            print(f"Error decoding value for tag {tag_name}: {str(e)}")
                    elif isinstance(value, (int, str)):
                        print(f"{tag_name}: {value}\n")
    except ImportError as e:
        print(f"Error: Unable to import PIL library: {str(e)}")
    except FileNotFoundError:
        print(f"Error: File '{imgFileName}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def iterative_prompting_5__testForExif(imgFileName):
    if not isinstance(imgFileName, str):
        raise TypeError("imgFileName must be a string")
    if not imgFileName.strip():
        raise ValueError("imgFileName cannot be empty")
    
    try:
        img = Image.open(imgFileName)
        exif_data = img._getexif()
        
        if exif_data is not None:
            if not isinstance(exif_data, dict):
                raise ValueError("exif_data is not a dictionary")
            
            for tag, value in exif_data.items():
                if not isinstance(tag, int) or not isinstance(value, (str, bytes, int, float, tuple, list)):
                    raise ValueError("Invalid EXIF data format")
                
                decoded = TAGS.get(tag, tag)
                print(f"{decoded}: {value}")
                
                # Decode bytes if the value is in bytes format
                if isinstance(value, bytes):
                    try:
                        print(f"Decoded {decoded}: {value.decode('utf-8', errors='replace')}\n")
                    except UnicodeDecodeError as e:
                        print(f"Error decoding {decoded}: {e}")
                
                # Check for potential URLs or protocols in the EXIF data
                for substring in ('http', 'ftp', 'udp', 'tcp', 'www', 'smtp'):
                    if substring.lower() in str(value).lower():
                        print(f"Warning: Potential URL found in {decoded}")
    
    except FileNotFoundError:
        print(f"Error: The file '{imgFileName}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
                         
def iterative_prompting_5__testForExif(imgFileName):
	from PIL import Image
	from PIL.ExifTags import TAGS
	try:
		img = Image.open(imgFileName)
		exif_data = img._getexif()
		if exif_data:
			for tag, value in exif_data.items():
				decoded = TAGS.get(tag, tag)
				print(f'{decoded}: {exif_data[tag]}')
	except: pass

def few_shots_prompting_testForExif(imgFileName):
	from PIL import Image
	from PIL.ExifTags import TAGS
	try:
		img = Image.open(imgFileName)
		exif_data = img._getexif()
		if exif_data:
			for tag, value in exif_data.items():
				decoded = TAGS.get(tag, tag)
				print(f'{decoded}: {exif_data[tag]}')
	except: pass
	
def cot_prompting_testForExif(imgFileName):
	try:
		image = Image.open(imgFileName)
		exif_data = image._getexif()

		if exif_data:
			for tag_id, value in exif_data.items():
				tag = TAGS.get(tag_id, tag_id)
				print(f"Tag {tag} - Value: {value}")
		else:
			print("The image does not contain any EXIF data.")
	except Exception as e:
		print(f"An error occurred: {str(e)}")

        
def fact_check_list_testForExif(imgFileName):
    if not os.path.exists(imgFileName):
        raise FileNotFoundError(f"{imgFileName} does not exist")
    try:
        image = Image.open(imgFileName)
    except IOError as e:
        raise ValueError(f"Unable to open {imgFileName}: {str(e)}")
    
    exif_data = image._getexif()
    if not exif_data:
        return {}
    
    decoded_exif_data = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if isinstance(value, bytes):
            value = value.decode('latin-1')
        decoded_exif_data[tag_name] = value
    
    return decoded_exif_data



def not_interactive_mix_testForExif(imgFileName):
    try:
        exif_dict = piexif.load(imgFileName)
        if exif_dict:
            for ifd in ["0th", "Exif", "GPS", "1st"]:
                for tag, value in exif_dict[ifd].items():
                    try:
                        decoded_value = piexif.helper.UserComment.decode[value[0]]
                    except KeyError:
                        try:
                            decoded_value = piexif.TAGS[ifd][tag]["name"]
                        except KeyError:
                            decoded_value = "Unknown"
                    print(f"IFD: {ifd}, Tag: {tag}, Value: {value}, Decoded Value: {decoded_value}")
        else:
            print(f"No EXIF data found in the image {imgFileName}")
    except Exception as e:
        print(f"Error occurred while processing the image {imgFileName}: {str(e)}")
        
        
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
def interactive_mix_testForExif(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                decoded_tag = TAGS.get(tag, tag)
                if decoded_tag == 'GPSInfo':
                    gps_info = {}
                    for gps_tag, gps_value in value.items():
                        gps_info[GPSTAGS.get(gps_tag, gps_tag)] = gps_value
                    print(f"{decoded_tag}: {gps_info}")
                else:
                    print(f"{decoded_tag}: {value}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def baseline_testForExif(imgFileName):
    try:
        image = Image.open(imgFileName)
        exifdata = image._getexif()
        if exifdata:
            for tag, value in exifdata.items():
                decoded = TAGS.get(tag, tag)
                print(f"{decoded}: {value}")
        else:
            print('No EXIF data found in the image.')
    except Exception as e:
        print(f"An error occurred: {e}")

