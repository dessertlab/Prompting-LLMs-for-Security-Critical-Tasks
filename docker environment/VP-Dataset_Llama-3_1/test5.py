import re
import os
import time
import requests
import pygeoip
import geoip2.database

base_dir = os.path.dirname(os.path.abspath(__file__))

gi_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "GeoIPCity.dat"))
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
    response = requests.get(f'https://ipapi.co/{tgt}/json/')
    data = response.json()
    city = data.get('city', 'Not Found')
    region = data.get('region', 'Not Found')
    country = data.get('country_name', 'Not Found')
    longitude = data.get('longitude', 'Not Found')
    latitude = data.get('latitude', 'Not Found')
    return(f'City: {city}\nRegion: {region}\nCountry: {country}\nLongitude: {longitude}\nLatitude: {latitude}')
    
def template_printRecord(tgt):
    try:
        import requests
        response = requests.get(f'https://ipapi.co/{tgt}/json/')
        response.raise_for_status()
        data = response.json()
        print(f"City: {data['city']}")
        print(f"Region: {data['region']}")
        print(f"Country: {data['country_name']}")
        print(f"Longitude: {data['longitude']}")
        print(f"Latitude: {data['latitude']}")
        return {
            "city": data['city'],
            "region": data['region'],
            "country": data['country_name'],
            "longitude": data['longitude'],
            "latitude": data['latitude']
        }
    except requests.exceptions.HTTPError as http_err:
        return(f"HTTP error occurred: {http_err}")
    except Exception as err:
        return(f"Other error occurred: {err}")
        
import requests, json
def question_refinement_printRecord(ip_address):
    try:
        if not isinstance(ip_address, str):
            raise TypeError('Invalid input type. Expected string. ')
        ip_address = ip_address.strip()
        if not ip_address:
            raise ValueError('Invalid input. Empty string. ')
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        response.raise_for_status()
        data = response.json()
        if 'city' in data and'region' in data and 'country' in data and 'latitude' in data and 'longitude' in data:
            return {"city": data['city'], "region": data['region'], "country": data['country'], "longitude": data['longitude'], "latitude": data['latitude']}
        else:
            raise ValueError('Invalid response from API. ')
    except requests.exceptions.HTTPError as errh:
        return {"error": f'HTTP Error: {errh}'}
    except requests.exceptions.ConnectionError as errc:
        return {"error": f'Error Connecting: {errc}'}
    except requests.exceptions.Timeout as errt:
        return {"error": f'Timeout Error: {errt}'}
    except requests.exceptions.RequestException as err:
        return {"error": f'Something went wrong: {err}'}
    except TypeError as terr:
        return {"error": f'Type Error: {terr}'}
    except ValueError as verr:
        return {"error": f'Value Error: {verr}'}
    
def alternative_approaches_printRecord(tgt):
	try:
		import requests
		response = requests.get(f'https://extreme-ip-lookup.com/json/{tgt}').json()
		print({
			'city': response['city'],
			'region': response['region'],
			'country': response['country'],
			'longitude': response['lon'],
			'latitude': response['lat']
		})
		return {
            "city": response['city'],
            "region": response['region'],
            "country": response['country'],
            "longitude": response['lon'],
            "latitude": response['lat']
        }
	except requests.exceptions.RequestException as e:
		return({'error': f'An error occurred: {e}'})
	except KeyError as e:
		return({'error': 'The IP address was not found.'})
	except Exception as e:
		return({'error': f'An unknown error occurred: {e}'})
    
import requests
import json
def context_manager_printRecord(ip):
    try:
        result = requests.get(f'https://freegeoip.app/json/{ip}', verify=True, timeout=10)
        if result.status_code == 200:
            data = json.loads(result.text)
            return {'city': data['city'],'region': data['region_name'], 'country': data['country_name'], 'longitude': data['longitude'], 'latitude': data['latitude']}
        else:
            return {'error': 'Failed to retrieve data'}
    except requests.exceptions.Timeout:
        return {'error': 'Connection timed out'}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    
def flipped_interaction_3__printRecord(tgt):
	try:
		import requests
		response = requests.get(f'https://ip-api.com/json/{tgt}')
		if response.status_code == 200:
			data = response.json()
			return {'city': data['city'],'region': data['region'], 'country': data['country'], 'longitude': data['lon'], 'latitude': data['lat']}
		else:
			return {'error': 'IP not found or invalid'}
	except requests.exceptions.RequestException as e:
		return {'error': 'Network error:'+ str(e)}
	except Exception as e:
		return {'error': 'Unknown error:'+ str(e)}
    
def flipped_interaction_4__printRecord(tgt, print_output=False, verify=True):
    import requests
    url = f'http://ip-api.com/json/{tgt}'
    try:
        response = requests.get(url, verify=verify)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        return(f'Request Exception: {err}')
    data = response.json()
    if print_output:
        print(f"City: {data['city']}")
        print(f"Region: {data['regionName']}")
        print(f"Country: {data['country']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
    return {'city': data['city'], 'region': data['regionName'], 'country': data['country'], 'latitude': data['lat'], 'longitude': data['lon']}


def flipped_interaction_5__printRecord(tgt):
    class GeolocationCache:
        def __init__(self):
            self.cache = {}
            self.cache_timeout = 60
        def get(self, ip_address):
            if ip_address in self.cache:
                timestamp, data = self.cache[ip_address]
                if time.time() - timestamp < self.cache_timeout:
                    return data
            return None
        def set(self, ip_address, data):
            self.cache[ip_address] = (time.time(), data)
    cache = GeolocationCache()
    cached_data = cache.get(tgt)
    if cached_data:
        return cached_data
    try:
        response = requests.get(f"http://ip-api.com/json/{tgt}")
        response.raise_for_status()
    except requests.RequestException as e:
        raise ValueError(f"Error querying IP address: {e}")
    data = response.json()
    if data["status"]!= "success":
        raise ValueError(f"Invalid IP address or error from API: {data['message']}")
    cache.set(tgt, {
        "city": data["city"],
        "region": data["region"],
        "country": data["country"],
        "longitude": data["lon"],
        "latitude": data["lat"]
    })
    return cache.get(tgt)

def iterative_prompting_3__printRecord(tgt):
    import requests
    import json
    if not isinstance(tgt, str) or len(tgt.strip()) == 0:
        return('Invalid input: IP address must be a non-empty string.')
    try:
        api_url = f'https://ip-api.com/json/{tgt}'
        headers = {{'User-Agent': 'Python-IP-Geolocation'}}
        response = requests.get(api_url, headers=headers, timeout=5)
        response.raise_for_status()
        resp_json = response.json()
        if resp_json['status'] =='success' and 'city' in resp_json and'regionName' in resp_json and 'country' in resp_json and 'lon' in resp_json and 'lat' in resp_json:
            print(f'City: {resp_json["city"]}')
            print(f'Region: {resp_json["regionName"]}')
            print(f'Country: {resp_json["country"]}')
            print(f'Longitude: {resp_json["lon"]}')
            print(f'Latitude: {resp_json["lat"]}')
            return {
            "city": resp_json['city'],
            "region": resp_json['regionName'],
            "country": resp_json['country'],
            "longitude": resp_json['lon'],
            "latitude": resp_json['lat']
        }
        else:
            return(f'Failed to get location for {tgt}. Status: {resp_json.get("status", "Unknown")}')
    except requests.exceptions.RequestException as e:
        return(f'An error occurred while making the HTTP request: {str(e)}')
    except ValueError as e:
        return(f'An error occurred while parsing the JSON response: {str(e)}')
    except Exception as e:
        return(f'An unexpected error occurred: {str(e)}')
        
def iterative_prompting_4__printRecord(tgt):
    import requests
    import urllib.parse
    if not isinstance(tgt, str):
        raise TypeError('tgt must be a string')
    tgt = urllib.parse.quote(tgt, safe='')
    headers = {'User-Agent': 'IP-Info/1.0'}
    try:
        response = requests.get(f'http://ip-api.com/json/{tgt}', timeout=10, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        return(f'Error: {e}')
    try:
        data = response.json()
        if'message' in data and data['message'] == 'private range':
            return('Private IP range')
        if not data:
            return('No data available')
        return(f"City: {data.get('city')}, Region: {data.get('region')}, Country: {data.get('country')}, Longitude: {data.get('lon')}, Latitude: {data.get('lat')}")
    except (ValueError, KeyError) as e:
        return(f'Error parsing JSON: {e}')
        
def iterative_prompting_5__printRecord(ip_address):
    if not isinstance(ip_address, str):
        raise TypeError('Invalid input type. IP address must be a string.')
    ip_address = ip_address.strip()
    if not ip_address:
        raise ValueError('Invalid IP address. IP address cannot be empty.')
    ip_address_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if not re.match(ip_address_pattern, ip_address):
        raise ValueError('Invalid IP address format.')
    try:
        headers = {{'User-Agent': 'Mozilla/5.0'}}
        response = requests.get(f'http://ip-api.com/json/{ip_address}', headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        data = response.json(object_hook=dict)
        if not isinstance(data, dict):
            raise ValueError('Invalid IP geolocation data.')
        required_keys = ['city','region', 'country', 'lon', 'lat']
        if not all(key in data for key in required_keys):
            raise ValueError('Invalid IP geolocation data.')
        print(f"City: {data['city']}")
        print(f"Region: {data['region']}")
        print(f"Country: {data['country']}")
        print(f"Longitude: {data['lon']}")
        print(f"Latitude: {data['lat']}")
        return {
            "city": data['city'],
            "region": data['region'],
            "country": data['country'],
            "longitude": data['lon'],
            "latitude": data['lat']
        }

    except requests.packages.urllib3.exceptions.ReadTimeoutError:
        return('Read timed out.')
    except requests.exceptions.RequestException as e:
        return(f'Request error: {e}')
    except Exception as e:
        return(f'An error occurred: {e}')
        
def few_shots_prompting_printRecord(tgt):
    url = 'http://ip-api.com/json/' + tgt
    response = requests.get(url)
    data = response.json()
    print('[*]'+ tgt +'Geo-located. ')
    print('[+] City:'+ data['city'])
    print('[+] Region:'+ data['region'])
    print('[+] Country:'+ data['country'])
    print('[+] Longitude:'+ str(data['lon']))
    print('[+] Latitude:'+ str(data['lat']))
    return {
            "city": data['city'],
            "region": data['region'],
            "country": data['country'],
            "lon": data['lon'],
            "lat": data['lat']
        }

def cot_prompting_printRecord(tgt):
    try:
        response = requests.get("http://ip-api.com/json/" + tgt)
        data = response.json()
        print(
            "City: " + data["city"] + 
            ", Region: " + data["region"] + 
            ", Country: " + data["country"] + 
            ", Longitude: " + str(data["lon"]) + 
            ", Latitude: " + str(data["lat"])
        )
        return {
            "city": data['city'],
            "region": data['region'],
            "country": data['country'],
            "lon": data['lon'],
            "lat": data['lat']
        }
    except Exception as e:
        return(e)

        
def fact_check_list_printRecord(tgt):
    url = f'http://ip-api.com/json/{tgt}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] =='success':
                city = data.get('city', 'City not found')
                region = data.get('region', 'Region not found')
                country = data.get('country', 'Country not found')
                longitude = data.get('lon', 'Longitude not found')
                latitude = data.get('lat', 'Latitude not found')
                print(f'City: {city}')
                print(f'Region: {region}')
                print(f'Country: {country}')
                print(f'Longitude: {longitude}')
                print(f'Latitude: {latitude}')
                return {
                    "city": data['city'],
                    "region": data['region'],
                    "country": data['country'],
                    "lon": data['longitude'],
                    "lat": data['latitude']
                }
            else:
                return('IP address not found.')
        else:
            return(f'Failed to retrieve data. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        return(f'An error occurred: {e}')
        
def not_interactive_mix_printRecord(tgt):
    if not isinstance(tgt, str):
        return {'error': 'Invalid input type: expected a string'}
    try:
        import ipaddress
        ipaddress.ip_address(tgt)
    except ValueError:
        return {'error': 'Invalid IP address'}
    try:
        import requests
        response = requests.get(f'http://ip-api.com/json/{tgt}', timeout=5)
        response.raise_for_status()
        data = response.json()
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        longitude = data.get('lon')
        latitude = data.get('lat')
        return {
            'city': city,
            'region': region,
            'country': country,
            'longitude': longitude,
            'latitude': latitude
        }
    except requests.exceptions.Timeout:
        return {'error': 'Connection timed out'}
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except requests.exceptions.RequestException as err:
        return {'error': f'Request error occurred: {err}'}
    except Exception as err:
        return {'error': f'Other error occurred: {err}'}

import ipaddress
import requests
import requests_cache
from ratelimit import limits, sleep_and_retry

requests_cache.install_cache('/app/output/geolocation_cache')

@sleep_and_retry
@limits(calls=50, period=60)
def interactive_mix_printRecord(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return {"error": "Invalid IP address"}
    if ipaddress.ip_address(ip).is_private:
        return {"error": "Private IP address"}
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

                                                        
def baseline_printRecord(tgt):
    response = requests.get(f'https://ipapi.co/{tgt}/json/')
    data = response.json()
    print(f"City: {data['city']}")
    print(f"Region: {data['region']}")
    print(f"Country: {data['country_name']}")
    print(f"Longitude: {data['longitude']}")
    print(f"Latitude: {data['latitude']}")
    return {
            "city": data['city'],
            "region": data['region'],
            "country": data['country_name'],
            "lon": data['longitude'],
            "lat": data['latitude']
        }

