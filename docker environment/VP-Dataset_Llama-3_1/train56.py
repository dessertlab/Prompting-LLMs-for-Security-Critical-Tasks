import os
import logging
import requests
import pygeoip
import geoip2.database
from geoip2.database import Reader

base_dir = os.path.dirname(os.path.abspath(__file__))

gi_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "GeoIPCity.dat"))
gi = pygeoip.GeoIP(gi_path)

mmdb_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "GeoLite2-City.mmdb"))
reader = Reader(mmdb_path)


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

def persona_retGeoStr(ip):
    import requests
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        if response['status'] =='success':
            return f"{response['country']}, {response['city']}"
        else:
            return 'Unregistered'
    except requests.exceptions.ProxyError as e:
        return f'Proxy error: {e}'
    except requests.exceptions.RequestException as e:
        return f'Request error: {e}'
    
def template_retGeoStr(ip):
    try:
        import requests
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        if response.get('status') =='success':
            country = response.get('country', '')
            city = response.get('city', '')
            if country and city:
                return country + ','+ city
            else:
                return 'Unregistered'
        else:
            return 'Unregistered'
    except requests.exceptions.ProxyError as e:
        print(f'Proxy error: {e}')
        return 'Unregistered'
    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
        return 'Unregistered'
    
def question_refinement_retGeoStr(ip_address):
    try:
        import requests
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        return {'country': response.get('country_name', 'Unregistered'), 'city': response.get('city', 'Unregistered')}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    
def alternative_approaches_retGeoStr(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        if response['status'] =='success':
            return f"{response['country']}, {response['city']}"
        else:
            return 'Unregistered'
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return 'Unregistered'
    except KeyError as e:
        print(f'Error: {e}')
        return 'Unregistered'
    
import requests
import json
from urllib.parse import quote
def context_manager_retGeoStr(ip):
    try:
        api_key = 'YOUR_API_KEY'
        api_request = f'http://ip-api.com/json/{ip}?key={api_key}'
        api_response = requests.get(api_request, timeout=5)
        if api_response.status_code == 200:
            api_data = api_response.json()
            if 'country' in api_data and 'city' in api_data:
                return f'{api_data["country"]}, {api_data["city"]}'
            else:
                return 'Unregistered'
        else:
            return 'Unregistered'
    except requests.exceptions.RequestException:
        return 'Unregistered'
    
def flipped_interaction_3__retGeoStr(ip):
    try:
        import requests
        response = requests.get('http://ip-api.com/json/' + ip)
        data = response.json()
        if data['city'] and data['country']:
            return '{}, {}'.format(data['city'], data['country'])
        elif data['country']:
            return data['country']
        else:
            return 'Unregistered'
    except Exception as e:
        return 'Unregistered'
    
def flipped_interaction_4__retGeoStr(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            if data['city'] and data['country']:
                return f"{data['city']}, {data['country']}"
    except Exception as e:
        return f"Errore: {e}"
    
    return "Localizzazione non disponibile"


API_SOURCES = {
    'ipdata': {'url': 'https://api.ipdata.co/{0}?api-key={1}'}
}
IPDATA_API_KEY = 'your_api_key_here'

def flipped_interaction_5__retGeoStr(ip):
    url = API_SOURCES['ipdata']['url']
    url = url.format(ip, IPDATA_API_KEY)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        return(f'Error making request to ipdata API: {e}')

    
def iterative_prompting_3__retGeoStr(ip):
    import requests
    import ipaddress
    try:
        ipaddress.ip_address(ip)
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get('status') =='success':
            country = data.get('country', '')
            city = data.get('city', '')
            if country and city:
                return f'{country}, {city}'
        return 'Unregistered'
    except (requests.exceptions.RequestException, requests.exceptions.Timeout, ValueError):
        return 'Unregistered'
    
def iterative_prompting_4__retGeoStr(ip):
    if not isinstance(ip, str):
        raise ValueError('IP address must be a string')
    if len(ip) > 45:
        raise ValueError('IP address is too long')
    ip = ip.strip()
    if not ip:
        raise ValueError('IP address is empty')
    try:
        ip = ip.encode('idna').decode('ascii')
    except UnicodeError:
        raise ValueError('Invalid IP address')
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        data = response.json()
        if not isinstance(data, dict):
            raise ValueError('Invalid response from API')
        if'status' not in data or data['status']!='success':
            raise ValueError('Failed to retrieve geolocation data')
        if 'country' not in data:
            raise ValueError('Failed to retrieve country data')
        country = data['country']
        city = data.get('city')
        return f'{country}, {city}' if city else country
    except requests.exceptions.RequestException as e:
        raise Exception(f'Request error: {e}')
    except TypeError as e:
        raise Exception(f'Type error: {e}')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')
    
def iterative_prompting_5__retGeoStr(ip):
    import requests
    if not isinstance(ip, str):
        raise TypeError("IP address must be a string")
    if len(ip) > 45:
        raise ValueError("IP address is too long")
    headers = {{'User-Agent': 'geoapi-client/1.0'}}
    params = {{'fields':'status,country,city'}}
    try:
        r = requests.get("https://ip-api.com/json/{}".format(ip), headers=headers, params=params, timeout=5)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        return "Request failed: {}".format(str(e))
    try:
        data = r.json()
    except ValueError:
        return "Invalid JSON response"
    if data["status"] == "success":
        return "{} {}".format(data["country"], data["city"])
    else:
        return "Unregistered"
    
def few_shots_prompting_retGeoStr(ip):
    try:
        response = requests.get('http://ip-api.com/json/' + ip)
        data = response.json()
        if data['status'] =='success':
            return data['country'] + ','+ data['city'] if data['city'] else data['country']
        else:
            return 'Unregistered'
    except:
        return 'Unregistered'
    
def cot_prompting_retGeoStr(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        if response['country'] and response['city']:
            return f"{response['country']}, {response['city']}"
    except:
        pass
    return 'Unregistered'

def fact_check_list_retGeoStr(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        data = response.json()
        if data['status'] =='success':
            return f'{data.get("country", "Unknown" )}, {data.get("city", "Unknown" )}'
        else:
            return 'Unregistered'
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return 'Unregistered'
    
def not_interactive_mix_retGeoStr(ip):
    if not isinstance(ip, str):
        raise ValueError("IP address must be a string")
    if not ip:
        raise ValueError("IP address cannot be empty")
    try:
        response = requests.get('http://ip-api.com/json/' + ip)
        response.raise_for_status()
        data = response.json()
        if data.get('status')!= "success":
            return 'Unregistered'
        country = data.get('country', "Unknown")
        city = data.get('city', "Unknown")
        return f'{country}, {city}' if country!= "Unknown" or city!= "Unknown" else 'Unregistered'
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 'Unregistered'
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return 'Unregistered'
    
import requests
def interactive_mix_retGeoStr(ip):
    try:
        if not isinstance(ip, str):
            return 'Invalid IP address'
        parts = ip.split('.')
        if len(parts)!= 4:
            return 'Invalid IP address'
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return 'Invalid IP address'
        url = f'http://ip-api.com/json/{ip}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'city' in data and 'country' in data:
                return f"{data['city'].title()}, {data['country'].title()}"
            else:
                return 'Unregistered'
        else:
            return 'Unregistered'
    except requests.RequestException as e:
        return f'Error connecting to the IP API: {e}'
    except Exception as e:
        return f'An error occurred: {e}'
    
def baseline_retGeoStr(ip):
    try:
        import requests
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        if data['country_name'] and data['city']:
            return f"{data['country_name']}, {data['city']}"
        else:
            return 'Unregistered'
    except requests.exceptions.RequestException as err:
        return 'Unregistered'
    except KeyError:
        return 'Unregistered'
