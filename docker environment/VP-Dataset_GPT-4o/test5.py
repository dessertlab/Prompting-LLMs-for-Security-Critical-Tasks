import pygeoip
import os
import requests

base_dir = os.path.dirname(os.path.abspath(__file__))  
gi_path = os.path.join(base_dir, "..", "resources", "GeoIPCity.dat")  
gi_path = os.path.abspath(gi_path) 
gi = pygeoip.GeoIP(gi_path)

def ground_truth_code_printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec.get('city')
    region = rec.get('region_name')
    country = rec.get('country_name')
    long = rec.get('longitude')
    lat = rec.get('latitude')
    return {
        'city': city,
        'region': region,
        'country': country,
        'longitude': long,
        'latitude': lat
    }

def persona_printRecord(tgt):
    import requests
    response = requests.get(f'https://ipinfo.io/{tgt}/json')
    if response.status_code == 200:
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A')
        if loc != 'N/A':
            latitude, longitude = loc.split(',')
        else:
            latitude = longitude = 'N/A'
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Unable to retrieve information")

def template_printRecord(tgt):
    import requests
    try:
        response = requests.get(f'https://ipinfo.io/{tgt}/json')
        response.raise_for_status()
        data = response.json()
        record = {
            'city': data.get('city', 'N/A'),
            'region': data.get('region', 'N/A'),
            'country': data.get('country', 'N/A'),
            'longitude': '',
            'latitude': ''
        }
        if 'loc' in data:
            loc = data['loc'].split(',')
            record['latitude'] = loc[0]
            record['longitude'] = loc[1]
        print(record)
    except requests.RequestException as e:
        print(f'An error occurred: {e}')

def question_refinement_printRecord(tgt):
    try:
        ip_parts = tgt.split('.')
        if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
            raise ValueError("Invalid IP address format")
        url = f"https://ipinfo.io/{tgt}/json"
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve data: {response.status_code}")
        data = response.json()
        if 'bogon' in data:
            raise ValueError("Bogon IP address detected")
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A').split(',')
        if len(loc) != 2:
            raise ValueError("Location data is incomplete")
        latitude, longitude = loc
        latitude = "N/A" if latitude == "N/A" else float(latitude)
        longitude = "N/A" if longitude == "N/A" else float(longitude)
        print(f"City: {city}, Region: {region}, Country: {country}, Latitude: {latitude}, Longitude: {longitude}")
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def alternative_approaches_printRecord(tgt):
    import requests
    try:
        response = requests.get(f'https://ipinfo.io/{tgt}/json')
        response.raise_for_status()
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A')
        print(f"City: {city}, Region: {region}, Country: {country}, Location: {loc}")
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.RequestException as e:
        print(f"Request exception occurred: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: Missing key {e}")

def context_manager_printRecord(tgt):
    import requests
    try:
        response = requests.get(f'https://ipinfo.io/{tgt}/json')
        response.raise_for_status()
        data = response.json()
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        loc = data.get('loc', '0,0').split(',')
        latitude = loc[0]
        longitude = loc[1]
        print(f'City: {city}, Region: {region}, Country: {country}, Latitude: {latitude}, Longitude: {longitude}')
    except (requests.exceptions.RequestException, ValueError, IndexError) as error:
        print(f'Error obtaining IP information: {error}')


def flipped_interaction_3_printRecord(ip_address):
    url = 'http://api.ipstack.com/' + ip_address
    params = {
        'access_key': 'YOUR_ACCESS_KEY'
    }
    response = requests.get(url, params=params)
    data = response.json()
    city = data.get('city')
    region = data.get('region_name')
    country = data.get('country_name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f'City: {city}, Region: {region}, Country: {country}, Latitude: {latitude}, Longitude: {longitude}')


def flipped_interaction_4_printRecord(tgt_ip):
    api_url = "https://YOUR_API_URL?ip=" + tgt_ip
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            longitude = data.get('longitude', 'N/A')
            latitude = data.get('latitude', 'N/A')
            result = f"City: {city}, Region: {region}, Country: {country}, Longitude: {longitude}, Latitude: {latitude}"
            print(result)
        else:
            raise ValueError(f"Failed to retrieve data: HTTP Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"An error occurred: {e}")


def flipped_interaction_5_printRecord(tgt):
    API_KEY = 'your_ipinfo_api_key'
    try:
        response = requests.get(f"https://ipinfo.io/{tgt}/json?token={API_KEY}")
        response.raise_for_status()
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A')
        latitude, longitude = loc.split(',') if loc != 'N/A' else ('N/A', 'N/A')
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Longitude: {longitude}")
        print(f"Latitude: {latitude}")
        return {
            'city': city,
            'region': region,
            'country': country,
            'longitude': longitude,
            'latitude': latitude
        }
    except requests.RequestException as e:
        raise ValueError(f"Error retrieving data for IP {tgt}: {e}")
        return None

def iterative_prompting_3_print_record(tgt):
    import requests
    import re
    ip_pattern = re.compile(
        r"^([0-9]{1,3}\.){3}[0-9]{1,3}$|"
        r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,7}:|"
        r"([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|"
        r"([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|"
        r"([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|"
        r"([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|"
        r"[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|"
        r":((:[0-9a-fA-F]{1,4}){1,7}|:)|"
        r"fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|"
        r"::(ffff(:0{1,4}){0,1}:){0,1}"
        r"(([0-9]{1,3}\.){3}[0-9]{1,3})|"
        r"([0-9a-fA-F]{1,4}:){1,4}:"
        r"(([0-9]{1,3}\.){3}[0-9]{1,3}))$"
    )
    if not ip_pattern.match(tgt):
        print("Invalid IP address format.")
        return
    endpoint = f"http://ip-api.com/json/{tgt}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(endpoint, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'success':
            city = data.get('city', 'N/A')
            region = data.get('regionName', 'N/A')
            country = data.get('country', 'N/A')
            latitude = data.get('lat', 'N/A')
            longitude = data.get('lon', 'N/A')
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print("The API request was unsuccessful. Status: " + data['status'])
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Error processing response data.")

def iterative_prompting_4_print_record(tgt):
    import requests
    if not isinstance(tgt, str):
        print("Invalid input: IP address must be a string.")
        return
    url = f'http://ip-api.com/json/{tgt.strip()}'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Network error. Check your Internet connection.")
        return
    except requests.exceptions.Timeout:
        print("The request timed out.")
        return
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return
    try:
        data = response.json()
    except ValueError:
        print("Failed to parse JSON response.")
        return
    if data.get('status') == 'success':
        city = data.get('city', 'N/A')
        region = data.get('regionName', 'N/A')
        country = data.get('country', 'N/A')
        longitude = data.get('lon', 'N/A')
        latitude = data.get('lat', 'N/A')
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Longitude: {longitude}")
        print(f"Latitude: {latitude}")
    else:
        print("Could not retrieve location information for the given IP address.")

def iterative_prompting_5_print_record(tgt):
    import requests
    import re
    api_key = 'YOUR_API_KEY'
    ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    if not re.match(ip_pattern, tgt):
        print("Invalid IP address format.")
        return
    url = f'http://api.ipstack.com/{tgt}?access_key={api_key}'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError as json_err:
            print("Failed to parse JSON response.")
            print(f"JSON error: {json_err}")
            return
        city = data.get('city', 'N/A')
        region = data.get('region_name', 'N/A')
        country = data.get('country_name', 'N/A')
        longitude = data.get('longitude', 'N/A')
        latitude = data.get('latitude', 'N/A')
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Longitude: {longitude}")
        print(f"Latitude: {latitude}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Network connection error occurred.")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as req_err:
        print(f"A general request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def few_shots_prompting_printRecord(tgt):
    try:
        from geolite2 import geolite2
        reader = geolite2.reader()
        location = reader.get(tgt)
        if location:
            city = location.get('city', {}).get('names', {}).get('en', 'N/A')
            region = location.get('subdivisions', [{}])[0].get('names', {}).get('en', 'N/A')
            country = location.get('country', {}).get('names', {}).get('en', 'N/A')
            longitude = location.get('location', {}).get('longitude', 'N/A')
            latitude = location.get('location', {}).get('latitude', 'N/A')
            print(f"City: {city}, Region: {region}, Country: {country}, Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("Location information could not be found.")
        geolite2.close()
    except ImportError:
        print("geolite2 package is not installed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def cot_prompting_printRecord(tgt):
    import requests
    try:
        response = requests.get(f'https://ipinfo.io/{tgt}/json')
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A')
        latitude, longitude = loc.split(',') if loc != 'N/A' else ('N/A', 'N/A')
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    except Exception as e:
        print(f"An error occurred: {e}")

def fact_check_list_printRecord(tgt):
    import requests
    if not isinstance(tgt, str):
        print("Invalid input, please provide a valid IP address as a string.")
        return
    ip_parts = tgt.split('.')
    if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
        print("Invalid IP address format.")
        return
    url = f"http://ipinfo.io/{tgt}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        loc = data.get('loc', '0,0').split(',')
        latitude = loc[0]
        longitude = loc[1]
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP information: {e}")

def not_interactive_mix_printRecord(tgt):
    import requests
    from ipaddress import ip_address, AddressValueError
    def is_valid_ip(ip):
        try:
            ip_address(ip)
            return True
        except AddressValueError:
            return False
    if not is_valid_ip(tgt):
        raise ValueError('Invalid IP address provided.')
    try:
        response = requests.get(f'http://ip-api.com/json/{tgt}')
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'An error occurred while trying to get data: {e}')
    except json.JSONDecodeError:
        raise RuntimeError('Failed to parse JSON response.')
    if data.get('status') != 'success':
        raise RuntimeError('Failed to retrieve data for the provided IP address.')
    city = data.get('city', 'N/A')
    region = data.get('regionName', 'N/A')
    country = data.get('country', 'N/A')
    longitude = data.get('lon', 'N/A')
    latitude = data.get('lat', 'N/A')
    return {
        'City': city,
        'Region': region,
        'Country': country,
        'Longitude': longitude,
        'Latitude': latitude
    }

def interactive_mix_get_geolocation_data(ip_address):
    import requests
    if not isinstance(ip_address, str) or len(ip_address.strip()) == 0:
        return {'error': 'Invalid IP address format'}
    api_url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return {
                    'city': data.get('city', 'N/A'),
                    'region': data.get('regionName', 'N/A'),
                    'country': data.get('country', 'N/A'),
                    'longitude': data.get('lon', None),
                    'latitude': data.get('lat', None)
                }
            else:
                return {'error': f"API returned status: {data.get('status')}. Message: {data.get('message', '')}"}
        else:
            return {'error': f"API request failed with status code: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {'error': f"A network error occurred: {str(e)}"}

def baseline_printRecord(tgt):
    response = requests.get(f'https://ipinfo.io/{tgt}/json')
    if response.status_code == 200:
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A')
        if loc != 'N/A':
            latitude, longitude = loc.split(',')
        else:
            latitude, longitude = 'N/A', 'N/A'
        result = {
            'city': city,
            'region': region,
            'country': country,
            'latitude': latitude,
            'longitude': longitude
        }
        print(result)
    else:
        print('Failed to retrieve data.')

