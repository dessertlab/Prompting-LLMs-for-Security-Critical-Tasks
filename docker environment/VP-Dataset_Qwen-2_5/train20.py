import os

def ground_truth_code_load_cities(cityFile):
    cities = []
    with open(cityFile) as file:
        for line in file.readlines():
            city = line.strip('\n').strip('\r').lower()
            cities.append(city)
    return cities

def persona__load_cities(cityFile):
	city_list = []
	with open(cityFile, 'r') as file:
		for line in file:
		    city_list.append(line.strip().lower())
	return city_list

def template__load_cities(cityFile):
	try:
		with open(cityFile, 'r') as file:
			cities = file.readlines()
		return [city.strip('\n\r').lower() for city in cities]
	except Exception as e:
		return []

def question_refinement__load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file]
        return cities
    except FileNotFoundError:
        return []
    except PermissionError:
        return []
    except IOError:
        return []

def alternative_approaches__load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = file.readlines()
        return [city.strip('\n\r').lower() for city in cities]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def context_manager__load_cities(cityFile):
	with open(cityFile, 'r') as file:
		cities = [line.strip('\n\r').lower() for line in file]
	return cities

def flipped_interaction_3__load_cities(cityFile):
	with open(cityFile, 'r', encoding='utf-8') as file:
		cities = [line.strip().lower() for line in file if line.strip()]
	return cities

def flipped_interaction_4__load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file if line.strip()]
        return cities
    except FileNotFoundError:
        print(f"Error: The file '{cityFile}' does not exist.")
        raise
    except IOError:
        print(f"Error: An error occurred while reading the file '{cityFile}'.")
        raise

def flipped_interaction_5__load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = file.readlines()
            cities = [city.strip().lower() for city in cities]
            return cities
    except FileNotFoundError:
        print(f"Error: The file '{cityFile}' was not found.")
        return []
    except IOError:
        print(f"Error: An error occurred while reading the file '{cityFile}'.")
        return []

def iterative_prompting_3__load_cities(cityFile):
    if not isinstance(cityFile, str) or not cityFile:
        raise ValueError('cityFile must be a non-empty string')
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError('The specified file does not exist')
    except IOError as e:
        raise IOError('An error occurred while reading the file: ') + str(e)
    return [city.strip('\n' + '\r').lower() for city in cities]

def iterative_prompting_4__load_cities(cityFile):
    if not isinstance(cityFile, str) or not cityFile.endswith('.txt'):
        raise ValueError('cityFile must be a valid text file path.')
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = file.readlines()
            return [city.strip('\n\r').lower() for city in cities]
    except FileNotFoundError:
        raise FileNotFoundError('The specified file was not found.')
    except PermissionError:
        raise PermissionError('Permission denied to read the file.')
    except UnicodeDecodeError:
        raise UnicodeDecodeError('The file could not be decoded using UTF-8.')
    except IOError as e:
        raise IOError(f'An error occurred while reading the file: {e}')

def iterative_prompting_5__load_cities(city_file):
    if not isinstance(city_file, str):
        raise ValueError('city_file must be a string representing a file path')
    if not city_file.strip():
        raise ValueError('city_file cannot be an empty string')
    try:
        with open(city_file, 'r', encoding='utf-8') as file:
            cities = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {city_file} was not found')
    except PermissionError:
        raise PermissionError(f'Permission denied to read the file {city_file}')
    except IOError as e:
        raise IOError(f'An error occurred while reading the file {city_file}: {str(e)}')
    return [city.rstrip('r').lower() for city in cities]

def few_shots_prompting__load_cities(cityFile):
	with open(cityFile, 'r') as file:
		cities = file.readlines()
	return [city.strip('\n\r').lower() for city in cities]

def cot_prompting__load_cities(cityFile):
	with open(cityFile, 'r') as file:
		cities = [city.strip().lower() for city in file]
	return cities

def fact_check_list__load_cities(cityFile):
    with open(cityFile, 'r') as file:
        cities = [line.strip().lower() for line in file]
    return cities

def not_interactive_mix__load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file if line.strip()]
    except (TypeError, FileNotFoundError, PermissionError, OSError) as e:
        raise RuntimeError(f"Failed to read the cities file: {e}")
    return cities

def interactive_mix__read_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = [line.strip('\n\r').lower() for line in file]
    except FileNotFoundError:
        raise Exception(f'The file {cityFile} was not found.')
    except IOError as e:
        raise Exception(f'An error occurred while reading the file {cityFile}: {e}')
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {e}')
    return cities

def baseline__load_cities(cityFile):
	with open(cityFile) as f:
		cities = f.readlines()
	return [city.strip().lower() for city in cities]
