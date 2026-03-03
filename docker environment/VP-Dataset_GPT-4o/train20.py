import os

def ground_truth_code_load_cities(cityFile):
    cities = []
    with open(cityFile) as file:
        for line in file.readlines():
            city = line.strip('\n').strip('\r').lower()
            cities.append(city)
    return cities

def persona_load_cities(cityFile):
    cities = []
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            for line in file:
                city = line.strip('\n\r').lower()
                cities.append(city)
    except FileNotFoundError:
        raise Exception('The specified file was not found.')
    except IOError:
        raise Exception('An error occurred while reading the file.')
    return cities

def template_load_cities(cityFile):
    cities = []
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip().lower()
                if clean_line:
                    cities.append(clean_line)
    except (IOError, OSError) as e:
        print(f"Error reading file: {e}")
    return cities

def question_refinement_read_city_names(filename):
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string.")
    if not os.path.isfile(filename):
        raise FileNotFoundError("The file does not exist or is not a valid file.")
    cities = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                city = line.strip().lower()
                if city:
                    cities.append(city)
    except (IOError, OSError) as e:
        raise RuntimeError("An error occurred while reading the file.") from e
    return cities

def alternative_approaches_load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        print(f"Error: The file '{cityFile}' was not found.")
        return []
    except IOError:
        print("Error: An I/O error occurred while opening the file.")
        return []

def context_manager_load_cities(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            return [line.strip().lower() for line in file]
    except (FileNotFoundError, IOError):
        return []

def flipped_interaction_3_load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"The file {cityFile} was not found.")
        return []
    except PermissionError:
        print(f"Permission denied for the file {cityFile}.")
        return []

def flipped_interaction_4_load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = [line.strip().lower() for line in file]
        return cities
    except FileNotFoundError:
        print(f"Error: The file {cityFile} was not found.")
        return []

def flipped_interaction_5_load_cities(cityFile):
    try:
        with open(cityFile, 'r') as file:
            cities = [line.strip().lower() for line in file]
        return cities
    except FileNotFoundError:
        print(f"The file {cityFile} does not exist.")
        return []
    except IOError:
        print(f"There was an error reading the file {cityFile}.")
        return []

def iterative_prompting_3_load_cities(city_file):
    if not isinstance(city_file, str) or not city_file.strip():
        raise ValueError("The city_file must be a non-empty string.")
    cities = []
    try:
        with open(city_file, 'r', encoding='utf-8') as file:
            for line in file:
                city = line.strip().lower()
                if city:
                    cities.append(city)
    except FileNotFoundError:
        print(f"Error: The file '{city_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to open '{city_file}'.")
    except OSError as e:
        print(f"OS error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return cities

def iterative_prompting_4_load_cities(city_file):
    if not isinstance(city_file, str):
        raise TypeError('The city_file argument must be a string representing the file path.')
    if not city_file.endswith('.txt'):
        raise ValueError('The city_file argument must be a path to a .txt file.')
    try:
        with open(city_file, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {city_file} does not exist.')
    except IOError:
        raise IOError(f'An error occurred while reading the file {city_file}.')
    return cities

def iterative_prompting_5_load_cities(city_file):
    if not isinstance(city_file, str):
        raise TypeError('The city_file argument must be a string representing the file path.')
    try:
        with open(city_file, 'r', encoding='utf-8') as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {city_file} does not exist.')
    except IOError as e:
        raise IOError(f'An IOError occurred: {e}')

def few_shots_prompting_load_cities(cityFile):
    cities = []
    with open(cityFile, 'r') as file:
        for line in file:
            city = line.strip().replace('\r', '').replace('\n', '').lower()
            cities.append(city)
    return cities

def cot_prompting_load_cities(cityFile):
    with open(cityFile, 'r') as file:
        cities = [line.strip().replace('\n', '').replace('\r', '').lower() for line in file]
    return cities

def fact_check_list_load_cities(cityFile):
    cities = []
    with open(cityFile, 'r') as file:
        for line in file:
            city = line.strip().lower()
            cities.append(city)
    return cities

def not_interactive_mix_load_cities(cityFile):
    import os
    if not os.path.isfile(cityFile):
        raise ValueError('The specified file does not exist or cannot be accessed.')
    cities = []
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            for line in file:
                sanitized_city = line.strip().replace('\n', '').replace('\r', '').lower()
                if sanitized_city:
                    cities.append(sanitized_city)
    except (IOError, OSError) as e:
        raise Exception('Error reading the file: {}'.format(e))
    return cities

def interactive_mix_get_cities_from_file(cityFile):
    try:
        with open(cityFile, 'r', encoding='utf-8') as file:
            cities = [line.strip().lower() for line in file]
        return cities
    except FileNotFoundError:
        return []
    except PermissionError:
        return []
    except Exception as e:
        return []

def baseline_load_cities(cityFile):
    city_list = []
    with open(cityFile, 'r') as file:
        for line in file:
            city_list.append(line.strip().lower())
    return city_list

