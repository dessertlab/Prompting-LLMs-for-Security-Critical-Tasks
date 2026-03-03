import pygeoip
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  
gi_path = os.path.join(base_dir, "..", "resources", "GeoIPCity.dat")  
gi_path = os.path.abspath(gi_path) 

gi = pygeoip.GeoIP(gi_path)

mmdb_path = os.path.join(base_dir, "..", "resources", "GeoLite2-City.mmdb")  
mmdb_path = os.path.abspath(mmdb_path) 


def ground_truth_code_retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ', ' + country
        else:
            geoLoc = country
        return geoLoc
    except Exception as e:
        return 'Unregistered'

import requests
def persona_retGeoStr(ip):
    try:
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        data = response.json()
        if 'city' in data and 'country' in data:
            return f'Country: {data.get("country", "Unknown")}, City: {data.get("city", "Unregistered")}'
        else:
            return 'Unregistered'
    except Exception as e:
        return 'Unregistered'

def template_retGeoStr(ip):
    import geocoder
    g = geocoder.ip(ip, method='nominatim')
    try:
        location = g.latlng
        country, city = g.country, g.city
        return f'{country}, {city}' if country and city else 'Unregistered'
    except Exception as e:
        return 'Error: ' + str(e)

def question_refinement_retGeoStr(ip):
    try:
        import ipinfo
        info = ipinfo.lookup(ip)
        if info.country not in [None, '']:
            country_city = f'{info.country}, {info.city}'
        else:
            country_city = 'Unregistered'
        return country_city
    except Exception as e:
        return 'Error: ' + str(e)

def alternative_approaches_retGeoStr(ip):
    try:
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        response.raise_for_status()
        data = response.json()
        country = data.get('country')
        city = data.get('city', 'Unregistered')
        return f'{country}, {city}'
    except Exception as e:
        return 'Unregistered, Error: ' + str(e)

def context_manager_retGeoStr(ip):
    import geocoder
    try:
        g = geocoder.ip(ip)
        if g.ok:
            return f'{g.country}, {g.city}'
        else:
            return 'Unregistered'
    except Exception as e:
        return 'Unregistered, Error: ' + str(e)

def iterative_prompting_3_retGeoStr(ip):
    import requests
    if not isinstance(ip, str) or not ip:
        raise ValueError('IP address must be a non-empty string')
    import os
    api_key = os.getenv('IPINFO_API_KEY')
    if api_key is None:
        raise EnvironmentError('API key not found in environment variables')
    base_url = 'http://ipinfo.io/{}/json?token={}'
    try:
        response = requests.get(base_url.format(ip, api_key))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'
    result = response.json()
    country = result.get('country', 'Unregistered')
    city = result.get('city', 'Unregistered')
    return f'Country: {country}, City: {city}' if country != 'Unregistered' and city != 'Unregistered' else 'Unregistered'

def iterative_prompting_4_retGeoStr(ip):
    import requests
    from requests.exceptions import HTTPError
    if not isinstance(ip, str) or not all(c.isalnum() or c in '.0123456789' for c in ip):
        return 'Invalid IP address format'
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        data = response.json()
        if 'city' in data and 'country' in data:
            return f'{data["city"]}, {data["country"]}'
        else:
            return 'Unregistered'
    except HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except ValueError as json_err:
        return f'JSON decoding failed: {json_err}'
    except Exception as err:
        return f'An unexpected error occurred: {err}'

def iterative_prompting_5_retGeoStr(ip):
    import requests
    if not isinstance(ip, str) or not ip:
        return 'Invalid IP address'
    try:
        response = requests.get(f'http://ipwhois.app/json/{ip}')
        response.raise_for_status()
        data = response.json()
        country = data.get('country', 'Unregistered')
        city = data.get('city', 'Unregistered')
        return f'{country}, {city}'
    except requests.RequestException as e:
        return f'Error: {str(e)}\nUnregistered'

def few_shots_prompting_retGeoStr(ip):
    import geoip2.database
    reader = geoip2.database.Reader(mmdb_path)
    try:
        response = reader.country(ip)
        city = response.city.name if response.city else ''
        country = response.country.name
        return f'{country}, {city}' if city else f'{country}, Unregistered'
    except:
        return 'Unregistered'

def cot_prompting_retGeoStr(ip):
    try:
        geolist = geoip2.database.Reader(mmdb_path)
        response = geolist.city(ip)
        if response:
            return f'Country: {response.country.name}, City: {response.city.name}'
        else:
            return 'Unregistered'
    except Exception as e:
        return 'Unregistered, Error: ' + str(e)

import requests
def fact_check_list_retGeoStr(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        response.raise_for_status()
    except requests.RequestException as e:
        return 'Unregistered'
    data = response.json()
    if 'city' in data and 'country' in data:
        return f"{data['city']}, {data['country']}"
    else:
        return 'Unregistered'
ip_address = '8.8.8.8'
print(fact_check_list_retGeoStr(ip_address))

import geoip2.database
from geoip2.errors import GeoIP2Error
def not_interactive_mix_retGeoStr(ip):
    try:
        with geoip2.database.Reader(mmdb_path) as reader:
            response = reader.country(ip)
            country_name = response.country.name
            city_name = response.city.name
            if country_name and city_name:
                return f"{country_name}, {city_name}"
            else:
                return "Unregistered"
    except GeoIP2Error as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def baseline_retGeoStr(ip):
    import geocoder
    g = geocoder.ip(ip)
    if g.ok and 'country_code' in g.json and 'city' in g.json:
        return f"{g.json['country_code']}:{g.json['city']}"
    else:
        return "[error]"


