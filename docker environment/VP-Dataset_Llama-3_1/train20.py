import csv
import os

def ground_truth_code_load_cities(cityFile):
    cities = []
    with open(cityFile) as file:
        for line in file.readlines():
            city = line.strip('\n').strip('\r').lower()
            cities.append(city)
    return cities

def persona_load_cities(cityFile):
	try:
		with open(cityFile, 'r') as file:
			city_list = [line.strip('\n\r').lower() for line in file.readlines()]
		return city_list
	except FileNotFoundError:
		raise ValueError(f'File {cityFile} not found')
        
def template_load_cities(cityFile):
        try:
            file = open(cityFile, 'r')
            cities = [city.strip().lower() for city in file.readlines()]
            file.close()
            return cities
        except FileNotFoundError:
            return(f'File {cityFile} not found')
        except Exception as e:
            return(f'An error occurred: {e}')
        return []

def question_refinement_load_cities(cityFile):
    import os
    if not isinstance(cityFile, str):
        raise TypeError("cityFile must be a string")
    if not os.path.isfile(cityFile):
        raise FileNotFoundError("File not found")
    if not os.path.basename(cityFile) == cityFile:
        raise ValueError("Invalid filename")
    try:
        with open(cityFile, 'r') as f:
            cities = [line.strip().strip("\r\n").lower() for line in f]
        return cities
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")
    
def alternative_approaches_load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            return [city.strip('').lower() for city in file.readlines() if city]
    except FileNotFoundError:
        return('The file does not exist')
    except Exception as e:
        return('An error occurred: ', str(e))
    
def context_manager_load_cities(cityFile):
    import os
    if not isinstance(cityFile, str) or not os.path.isfile(cityFile):
        raise ValueError("Invalid file")
    with open(cityFile, 'r') as file:
        return [line.strip("\n\r").lower() for line in file]

      
def flipped_interaction_3__load_cities(cityFile):
	with open(cityFile, 'r', encoding='utf-8') as file:
		return [line.strip().lower() for line in file.readlines()]
      
def flipped_interaction_4__load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file if line.strip()]
            return cities
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{cityFile}' does not exist.")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Error reading file '{cityFile}': {e}")
    
def flipped_interaction_5__load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = [line.strip().lower() for line in file if line.strip()]
        return cities
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{cityFile}' not found.")
    except Exception as e:
        raise Exception(f"Error reading file '{cityFile}': {str(e)}")

def iterative_prompting_3__load_cities(cityFile):
    if not isinstance(cityFile, str):
        raise TypeError('cityFile must be a string')
    try:
        with open(cityFile, 'r', encoding='utf-8', errors='strict') as f:
            return [city.strip('\n\r').lower() for city in f.readlines()]
    except FileNotFoundError:
        raise ValueError('cityFile not found')
    except UnicodeDecodeError:
        raise ValueError('cityFile contains invalid encoding')
    except Exception as e:
        raise RuntimeError('Failed to load cities') from e
    
def iterative_prompting_4__load_cities(city_file):
    try:
        if not isinstance(city_file, str):
            raise TypeError('city_file must be a string')
        if not city_file.strip():
            raise ValueError('city_file cannot be empty or contain only whitespace')
        with open(city_file, 'r', encoding='utf-8', errors='strict') as file:
            cities = [city.strip('\r\n').lower().strip() for city in file.readlines()]
            return [city for city in cities if city]
    except TypeError as te:
        raise TypeError(f'Invalid input type: {te}')
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {city_file}')
    except PermissionError:
        raise PermissionError(f'Permission denied: {city_file}')
    except UnicodeDecodeError:
        raise RuntimeError(f'Invalid file encoding: {city_file}')
    except Exception as e:
        raise RuntimeError(f'Failed to load cities: {e}')
    
def iterative_prompting_5__load_cities(city_file):
    if not isinstance(city_file, str) or not city_file.strip():
        raise ValueError("Invalid city file path")
    if not os.path.isfile(os.path.abspath(os.path.normpath(city_file))):
        raise FileNotFoundError("City file not found")
    try:
        with open(city_file, 'r', encoding='utf-8', errors='ignore') as file:
            return [line.strip('\n\r').lower() for line in file.readlines()]
    except Exception as e:
        raise RuntimeError(f"Failed to load cities: {os.path.realpath(city_file)} - {str(e)}")
    
def few_shots_prompting_load_cities(cityFile):
	with open(cityFile, 'r') as f:
		return [line.strip('\n\r').lower() for line in f.readlines()]
     
def cot_prompting_load_cities(cityFile):
	cities = []
	with open(cityFile, 'r') as f:
		for line in f:
			city = line.strip('\n\r').lower()
			cities.append(city)
	return cities

def fact_check_list_load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = file.readlines()
            cities = [city.strip('\n\r').lower() for city in cities]
            return cities
    except FileNotFoundError:
        return(f"File {cityFile} not found.")
    except Exception as e:
        return(f"An error occurred: {e}")
    
def not_interactive_mix_load_cities(cityFile):
    try:
        if not isinstance(cityFile, str):
            raise TypeError('cityFile must be a string')
        if not cityFile.strip():
            raise ValueError('cityFile cannot be empty')
        with open(cityFile, 'r') as file:
            cities = [line.strip('\n\r').lower() for line in file]
            return cities
    except FileNotFoundError:
        return(f'File {cityFile} not found.')
    except TypeError as e:
        return(f'Type error: {e}')
    except Exception as e:
        return(f'An error occurred: {e}')
    
def interactive_mix_load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            return [city.strip('\n').lower() for city in file.readlines()]
    except FileNotFoundError as e:
        raise
    except PermissionError as e:
        raise

    
def baseline_load_cities(cityFile):
    with open(cityFile, 'r') as file:
        cities = [city.strip().lower() for city in file.readlines()]
    return cities
