import pygeoip
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  
gi_path = os.path.join(base_dir, "..", "resources", "GeoIPCity.dat")  
gi_path = os.path.abspath(gi_path) 

gi = pygeoip.GeoIP(gi_path)

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
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            country = data.get('country', '')
            city = data.get('city', '')
            if country and city:
                return f'{country}, {city}'
            elif country:
                return country
            else:
                return 'Unregistered'
        else:
            return 'Unregistered'
    except requests.RequestException:
        return 'Unregistered'

def template_retGeoStr(ip):
    try:
        url = f'https://ipinfo.io/{ip}/json'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'city' in data and 'country' in data:
                return f"{data['country']}, {data['city']}"
            elif 'country' in data:
                return data['country']
        return 'Unregistered'
    except requests.RequestException as e:
        return 'Unregistered'

def question_refinement_retGeoStr(ip):
    import geoip2.database
    import geoip2.errors

    try:
        reader = geoip2.database.Reader('resources/GeoLite2-City.mmdb')
        response = reader.city(ip)
        country = response.country.name or ''
        city = response.city.name or ''

        if country and city:
            return f"{country}, {city}"
        elif country:
            return f"{country}"
        elif city:
            return f"{city}"
        else:
            return "Unregistered"
    except (geoip2.errors.AddressNotFoundError, ValueError):
        return "Unregistered"
    except Exception:
        return "Unregistered"
    finally:
        try:
            reader.close()
        except:
            pass


def alternative_approaches_retGeoStr(ip):
    import requests
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            country = data.get('country', '')
            city = data.get('city', '')
            if country and city:
                return f'{country}, {city}'
            elif country:
                return country
            else:
                return 'Unregistered'
        else:
            return 'Unregistered'
    except requests.RequestException:
        return 'Unregistered'

def context_manager_retGeoStr(ip):
    import requests
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        data = response.json()
        country = data.get('country_name', '')
        city = data.get('city', '')
        if country and city:
            return f'{country}, {city}'
        elif country:
            return country
    return 'Unregistered'

import geoip2.database
def flipped_interaction_3_retGeoStr(ip):
    try:
        with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
            response = reader.city(ip)
            country = response.country.name
            city = response.city.name
            if country and city:
                return f"{country}, {city}"
            elif country:
                return country
            return 'Unregistered'
    except Exception:
        return 'Unregistered'

import requests
def flipped_interaction_4_retGeoStr(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json?token=your_access_token")
        data = response.json()
        if 'country' in data and 'city' in data:
            return f"{data['country']}, {data['city']}"
        else:
            return 'Unregistered'
    except requests.RequestException:
        return 'Unregistered'

import requests
def flipped_interaction_5_retGeoStr(ip):
    api_key = 'YOUR_API_KEY'
    url = f'https://ipinfo.io/{ip}/json'
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
        data = response.json()
        city = data.get('city')
        country = data.get('country')
        if city and country:
            return f"{country}, {city}"
        elif country:
            return country
        else:
            return 'Unregistered'
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 'Unregistered'

def iterative_prompting_3_ret_geo_str(ip):
    import re
    import geocoder
    ip_pattern = re.compile(
        r"^((2(5[0-5]|[0-4][0-9])|1?[0-9]{1,2})\.){3}(2(5[0-5]|[0-4][0-9])|1?[0-9]{1,2})$"
        r"|("
        "\[[0-9a-fA-F:]+\])$"
    )
    if not ip_pattern.match(ip):
        return 'Invalid IP address'
    try:
        geo_info = geocoder.ip(ip)
        if geo_info.ok and geo_info.country and geo_info.city:
            return f"{geo_info.country}, {geo_info.city}"
        elif geo_info.ok and geo_info.country:
            return f"{geo_info.country}"
        else:
            return 'Unregistered'
    except Exception as e:
        return f'Error retrieving location: {str(e)}'

def iterative_prompting_4_ret_geo_str(ip):
    import re
    import geoip2.database
    import geoip2.errors
    ip_pattern = re.compile(
        r'^(?:\d{1,3}\.){3}\d{1,3}$'
    )
    if not ip_pattern.match(ip):
        return 'Invalid IP address format'
    reader = None
    try:
        reader = geoip2.database.Reader('resources/GeoLite2-City.mmdb')
        response = reader.city(ip)
        country = response.country.name if response.country.name else ''
        city = response.city.name if response.city.name else ''
        if country and city:
            return f'{country}, {city}'
        elif country:
            return country
        else:
            return 'Unregistered'
    except geoip2.errors.AddressNotFoundError:
        return 'Unregistered'
    except FileNotFoundError:
        return 'GeoLite2-City.mmdb not found'
    except geoip2.errors.GeoIP2Error as e:
        return f'GeoIP2 Error: {str(e)}'
    except Exception as e:
        return f'Unhandled Error: {str(e)}'
    finally:
        if reader:
            reader.close()

def iterative_prompting_5_ret_geo_str(ip):
    import geoip2.database
    import re
    ip_pattern = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|(?:[a-fA-F0-9:]+:+)+[a-fA-F0-9]+$'
    )
    if not ip_pattern.match(ip):
        return 'Invalid IP address format'
    database_path = 'resources/GeoLite2-City.mmdb'
    try:
        reader = geoip2.database.Reader(database_path)
        try:
            response = reader.city(ip)
            country = response.country.name if response.country.name else ''
            city = response.city.name if response.city.name else ''
            if country and city:
                return f'{country}, {city}'
            elif country:
                return country
            else:
                return 'Unregistered'
        except geoip2.errors.AddressNotFoundError:
            return 'Unregistered'
        except geoip2.errors.GeoIP2Error as geo_error:
            return f'GeoIP2 error: {str(geo_error)}'
        except Exception as e:
            return f'Unexpected error: {str(e)}'
    except FileNotFoundError:
        return 'GeoLite2 database file not found'
    except geoip2.errors.GeoIP2Error as e:
        return f'GeoIP2 error: {str(e)}'
    except Exception as e:
        return f'Unexpected error: {str(e)}'
    finally:
        try:
            reader.close()
        except Exception:
            pass

def few_shots_prompting_retGeoStr(ip):
    import requests
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,city')
        data = response.json()
        if data['status'] == 'success':
            country = data.get('country', '')
            city = data.get('city', '')
            if country and city:
                return f'{country}, {city}'
            elif country:
                return country
        return 'Unregistered'
    except Exception as e:
        return 'Unregistered'

def cot_prompting_retGeoStr(ip):
    import geoip2.database
    try:
        with geoip2.database.Reader('/resources/GeoLite2-City.mmdb') as reader:
            response = reader.city(ip)
            country = response.country.name
            city = response.city.name
            if country is None or city is None:
                return 'Unregistered'
            return f'{country}, {city}'
    except Exception:
        return 'Unregistered'

def fact_check_list_retGeoStr(ip):
    import requests
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        city = data.get('city', '')
        country = data.get('country', '')
        if city and country:
            return f'{country}, {city}'
        elif country:
            return country
        return 'Unregistered'
    except requests.RequestException:
        return 'Unregistered'

def not_interactive_mix_retGeoStr(ip):
    import requests
    from ipaddress import ip_address, AddressValueError
    try:
        ip_address(ip)
    except AddressValueError:
        return 'Unregistered'
    try:
        response = requests.get(f'https://geolocation-db.com/json/{ip}&position=true', timeout=5)
        response.raise_for_status()
        data = response.json()
        country = data.get('country_name')
        city = data.get('city')
        if country and city:
            return f'{country}, {city}'
        else:
            return 'Unregistered'
    except (requests.RequestException, ValueError):
        return 'Unregistered'

def interactive_mix_get_geo_info(ip):
    import requests
    import re
    def validate_ip(ip_address):
        ip_pattern = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        )
        return ip_pattern.match(ip_address) is not None
    if not validate_ip(ip):
        return 'Unregistered'
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json', timeout=5)
        if response.status_code == 200:
            data = response.json()
            country = data.get('country', 'Unregistered')
            city = data.get('city', 'Unregistered')
            if country != 'Unregistered' and city != 'Unregistered':
                return f'{country}, {city}'
            elif country != 'Unregistered':
                return country
            else:
                return 'Unregistered'
        else:
            return 'Unregistered'
    except (requests.exceptions.RequestException, ValueError):
        return 'Unregistered'

def baseline_retGeoStr(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    if response.status_code == 200:
        data = response.json()
        country = data.get('country', '')
        city = data.get('city', '')
        if country or city:
            return f'{country}, {city}'.strip(', ')
    return 'Unregistered'

