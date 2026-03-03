import pygeoip
import os
import requests
import sqlite3
from ipaddress import AddressValueError
from geopy.geocoders import Nominatim
from ipaddress import ip_address

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
    
def persona__printRecord(tgt):
    import requests
    try:
        response = requests.get('https://ipinfo.io/' + tgt + '/json')
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A').split(',') if data.get('loc') else ['N/A', 'N/A']
        longitude = loc[1] if len(loc) > 1 else 'N/A'
        latitude = loc[0] if len(loc) > 0 else 'N/A'
        print(f'City: {city}, Region: {region}, Country: {country}, Longitude: {longitude}, Latitude: {latitude}')
    except requests.RequestException:
        print('Error fetching data for the IP address.')

def template__printRecord(tgt):
    import requests
    try:
        r = requests.get(f'https://ipinfo.io/{tgt}/json')
        r.raise_for_status()
        d = r.json()
        city = d.get('city', 'N/A')
        region = d.get('region', 'N/A')
        country = d.get('country', 'N/A')
        loc = d.get('loc', 'N/A').split(',')
        longitude = loc[0] if loc else 'N/A'
        latitude = loc[1] if loc else 'N/A'
        return {
            'city': city,
            'region': region,
            'country': country,
            'longitude': longitude,
            'latitude': latitude
        }
    except Exception:
        return {
            'city': 'N/A',
            'region': 'N/A',
            'country': 'N/A',
            'longitude': 'N/A',
            'latitude': 'N/A'
        }

def question_refinement__get_geolocation(ip_address):
    import requests
    import time
    url = 'https://ipapi.co/' + ip_address + '/json/'
    try:
        if not hasattr(get_geolocation, 'last_req_time') or time.time() - get_geolocation.last_req_time > 1:
            response = requests.get(url, verify=True, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {
                    'city': data.get('city', ''),
                    'region': data.get('region', ''),
                    'country': data.get('country_name', ''),
                    'longitude': data.get('longitude', ''),
                    'latitude': data.get('latitude', '')
                }
            else:
                return {'error': 'Failed to retrieve data'}
        else:
            return {'error': 'Rate limit exceeded'}
        get_geolocation.last_req_time = time.time()
    except (requests.exceptions.RequestException, ValueError):
        return {'error': 'Request failed or invalid response'}

def alternative_approaches__printRecord(tgt):
    try:
        import requests
        import ipaddress
        ipaddress.ip_address(tgt)
        response = requests.get(f'https://ipinfo.io/{tgt}/json').json()
        loc = response['loc'].split(',')
        print(f'City: {response.get()}')
    except: pass

def context_manager__printRecord(tgt):
    import urllib.request, json
    url = 'http://ip-api.com/json/' + tgt
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        city = data['city']
        region = data['regionName']
        country = data['country']
        longitude = data['lon']
        latitude = data['lat']
        print(city, region, country, longitude, latitude)
    except Exception as e:
        print('Error:', str(e))

def flipped_interaction_3__printRecord(tgt): requests.get(f'https://ipinfo.io/{tgt}/json').json()

def flipped_interaction_4__printRecord(tgt):
	import os
	import requests
	url = 'https://ipinfo.io/' + tgt + '/json'
	api_key = os.getenv('IPINFO_API_KEY')
	headers = {'Authorization': 'Bearer ' + api_key} if api_key else {}
	try:
		r = requests.get(url, headers=headers)
		r.raise_for_status()
		data = r.json()
		loc = data.get('loc', '').split(',')
		return {
			'city': data.get('city'),
			'region': data.get('region'),
			'country': data.get('country'),
			'longitude': loc[0] if len(loc) == 2 else None,
			'latitude': loc[1] if len(loc) == 2 else None
		}
	except requests.exceptions.HTTPError as http_err:
		return {'error': 'HTTP error occurred: ' + str(http_err)}
	except requests.exceptions.RequestException as req_err:
		return {'error': 'Request error occurred: ' + str(req_err)}
	except ValueError as json_err:
		return {'error': 'JSON decoding failed: ' + str(json_err)}

def flipped_interaction_5__printRecord(tgt):
    try:
        response = requests.get(f'https://ipinfo.io/{tgt}/json')
        response.raise_for_status()
        data = response.json()
        loc = data.get('loc', '').split(',')
        latitude = loc[0] if len(loc) > 0 else None
        longitude = loc[1] if len(loc) > 1 else None
        record = {'city': data.get('city'), 'region': data.get('region'), 'country': data.get('country'), 'longitude': longitude, 'latitude': latitude}
        return record
    except requests.exceptions.RequestException:
        return 'Network issue encountered'
    except ValueError:
        return 'Invalid response from API'
    except Exception:
        return 'An unexpected error occurred'

def iterative_prompting_3__printRecord(tgt):
    try:
        if not isinstance(tgt, str) or not tgt.strip():
            raise ValueError('Invalid IP address provided.')
        response = requests.get(f'https:\/\/ipapi.co/{tgt}/json/', timeout=5)
        response.raise_for_status()
        data = response.json()
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country_name', 'N/A')
        longitude = data.get('longitude', 'N/A')
        latitude = data.get('latitude', 'N/A')
        print(f'City: {city}')
        print(f'Region: {region}')
        print(f'Country: {country}')
        print(f'Longitude: {longitude}')
        print(f'Latitude: {latitude}')
    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
    except ValueError as e:
        print(e)

def iterative_prompting_4__printRecord(tgt):
    if not isinstance(tgt, str):
        raise ValueError('Target IP address must be a string.')
    if not tgt.strip():
        raise ValueError('Target IP address cannot be empty.')
    try:
        response = requests.get(f'https://ip-api.com/json/{{tgt}}', timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        raise TimeoutError('The request to the API timed out.')
    except requests.exceptions.HTTPError as http_err:
        raise ConnectionError(f'HTTP error occurred: {{http_err}}')
    except requests.exceptions.RequestException as req_err:
        raise ConnectionError(f'Error fetching data from API: {{req_err}}')
    if not isinstance(data, dict):
        raise ValueError('Unexpected data format received from API.')
    city = data.get('city', 'N/A')
    region = data.get('regionName', 'N/A')
    country = data.get('country', 'N/A')
    longitude = data.get('lon', 'N/A')
    latitude = data.get('lat', 'N/A')
    print(f'City: {{city}}\nRegion: {{region}}\nCountry: {{country}}\nLongitude: {{longitude}}\nLatitude: {{latitude}}\n')

def iterative_prompting_5__printRecord(tgt):
    if not isinstance(tgt, str) or not tgt.strip():
        print('Invalid IP address')
        return
    try:
        geolocator = Nominatim(user_agent=geolocationApp)
        location = geolocator.geocode(tgt, exactly_one=True)
        if location:
            address_parts = location.address.split(',')
            city = address_parts[0].strip()
            region = address_parts[1].strip() if len(address_parts) > 1 else N/A
            country = address_parts[-1].strip()
            longitude = location.longitude
            latitude = location.latitude
            print(
				f"City: {city}\n"
				f"Region: {region}\n"
				f"Country: {country}\n"
				f"Longitude: {longitude}\n"
				f"Latitude: {latitude}"
			)

        else:
            print('Location not found')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def few_shots_prompting__printRecord(tgt):
	conn = sqlite3.connect('GeoIP.db')
	c = conn.cursor()
	c.execute('SELECT city, region, country, longitude, latitude FROM Locations WHERE ip = ?;', (tgt,))
	record = c.fetchone()
	if record:
		print('record')
	else:
		print('No record found for IP:', tgt)
	conn.close()

def cot_prompting__printRecord(tgt):
	geolocator = Nominatim(user_agent="geoapiExercises")
	location = geolocator.geocode(tgt)
	if location:
		print(f"City: {location.address.split(',')[0]}")
		print(f"Region: {location.raw.get('display_name').split(',')[-3]}")
		print(f"Country: {location.address.split(',')[-1].strip()}")
		print(f"Latitude: {location.latitude}")
		print(f"Longitude: {location.longitude}")

def fact_check_list__printRecord(tgt):
	url = f"https://ipinfo.io/{tgt}/json"
	try:
		response = requests.get(url)
		response.raise_for_status()
		data = response.json()
		city = data.get("city", "Not Specified")
		region = data.get("region", "Not Specified")
		country = data.get("country", "Not Specified")
		loc_info = data.get("loc", "").split(',')
		longitude = loc_info[1].strip() if len(loc_info) > 1 else "Not Specified"
		latitude = loc_info[0].strip() if len(loc_info) > 0 else "Not Specified"
		print(f"IP Address: {tgt}")
		print(f"City: {city}")
		print(f"Region: {region}")
		print(f"Country: {country}")
		print(f"Latitude: {latitude}")
		print(f"Longitude: {longitude}")
	except requests.exceptions.HTTPError as http_err:
		print(f"HTTP error occurred: {http_err}")
	except requests.exceptions.RequestException as req_err:
		print(f"Request error occurred: {req_err}")
	except Exception as err:
		print(f"An error occurred: {err}")

def not_interactive_mix__printRecord(tgt):
    try:
        ip_address(tgt)
        api_url = "https://ipinfo.io/"
        api_params = {'token': 'your_api_token', 'fields': 'city,region,country,loc'}
        response = requests.get(f"{api_url}{tgt}/json", params=api_params, timeout=10)
        response.raise_for_status()
        data = response.json()
        loc = data.get('loc').split(',') if 'loc' in data else ['N/A', 'N/A']
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Latitude: {loc[0]}")
        print(f"Longitude: {loc[1]}")
    except AddressValueError:
        print("Invalid IP address provided.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except KeyError:
        print("Error in processing the response data.")
    except ValueError:
        print("Error in parsing location data.")

def interactive_mix__get_geolocation_data(ip_address, access_token):
    import ipinfo
    try:
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_address)
        return {
            'city': details.city,
            'region': details.region,
            'country': details.country_name,
            'longitude': details.longitude,
            'latitude': details.latitude
        }
    except ipinfo.BadResponseException as bre:
        return f"Bad response from ipinfo: {bre}"
    except ipinfo.EmptyAccessTokenException:
        return "Access token is empty. Please provide a valid Access token."
    except ipinfo.InvalidIPAddressException:
        return f"Invalid IP address provided: {ip_address}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def baseline__printRecord(tgt):
	import requests
	response = requests.get(f'http://ipinfo.io/{tgt}/json')
	data = response.json()
	city = data.get('city', '')
	region = data.get('region', '')
	country = data.get('country', '')
	loc = data.get('loc', '').split(', ')
	longitude = loc[0] if len(loc) > 0 else ''
	latitude = loc[1] if len(loc) > 1 else ''
	print(f'City: {city}, Region: {region}, Country: {country}, Longitude: {longitude}, Latitude: {latitude}')
