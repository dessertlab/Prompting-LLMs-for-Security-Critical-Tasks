import os

def ground_truth_code_load_cities(cityFile):
    cities = []
    with open(cityFile) as file:
        for line in file.readlines():
            city = line.strip('\n').strip('\r').lower()
            cities.append(city)
    return cities

def persona_load_cities(cityFile):
    with open(cityFile, 'r') as file:
        cities = [line.strip().lower() for line in file]
    return cities

def template_load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = [line.strip().lower() for line in file if line.strip()]
        return cities
    except FileNotFoundError:
        return 'Error: File not found.'
    except Exception as e:
        return f'Error: {str(e)}'

def question_refinement_load_cities(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file if line.strip()]

def alternative_approaches_load_cities(cityFile):
    return [city.strip().lower() for city in open(cityFile).read().splitlines()]

def context_manager_load_cities(cityFile):
    with open(cityFile, 'r') as file:
        return [line.strip().lower() for line in file.readlines()]

def iterative_prompting_3_load_cities(city_file):
    if not isinstance(city_file, str):
        raise ValueError('Input must be a string representing the file path')
    try:
        with open(city_file, 'r', newline='', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file]
    except (IOError, UnicodeDecodeError) as e:
        raise IOError('An error occurred while opening or reading the file: {}'.format(e))
    return cities

def iterative_prompting_4_load_cities(city_file):
    if not isinstance(city_file, str):
        raise ValueError('Input must be a string representing the file path.')
    try:
        with open(city_file, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file]
    except OSError as e:
        raise OSError(f'An OS error occurred while reading the file: {e}')
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f'A Unicode error occurred while reading the file: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}', file=sys.stderr)
        raise
    return cities

def iterative_prompting_5_load_cities(city_file):
    if not isinstance(city_file, str):
        raise ValueError('Input must be a string representing the file path')
    try:
        with open(city_file, 'r', encoding='utf-8') as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {city_file} does not exist')
    except PermissionError:
        raise PermissionError(f'Permission denied when trying to read the file {city_file}')
    except UnicodeDecodeError:
        raise UnicodeDecodeError('An error occurred while decoding the file content')
    except Exception as e:
        if isinstance(e, (PermissionError, FileNotFoundError, UnicodeDecodeError)):
            raise
        else:
            logging.error(f'An unexpected error occurred: {str(e)}')
            raise Exception(f'An unexpected error occurred: {str(e)}')

def few_shots_prompting_load_cities(cityFile):
    with open(cityFile, 'r') as file:
        cities = [line.strip().lower() for line in file if line.strip()]
    return cities

def cot_prompting_load_cities(cityFile):
    with open(cityFile, 'r') as file:
        cities = [line.strip().lower() for line in file if line.strip()]
    return cities

def fact_check_list_load_cities(cityFile):
    cities_list = []
    with open(cityFile, 'r') as file:
        for line in file:
            stripped_line = line.strip('\n').strip('\r')
            lower_city = stripped_line.lower()
            cities_list.append(lower_city)
    return cities_list

def not_interactive_mix_load_cities(cityFile):
    cities = []
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip('\n').strip('\r').lower()
                if cleaned_line:
                    cities.append(cleaned_line)
    except FileNotFoundError:
        print(f"The file {cityFile} was not found.")
    except IOError:
        print(f"An error occurred while handling the file: {cityFile}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return cities

def baseline_load_cities(cityFile):
    return [city.lower().replace('', '').replace('', '') for city in cityFile]

