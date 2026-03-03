import pygeoip
import os
import requests
import re
import ipinfo
from geopy.geocoders import Nominatim
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

def persona__retGeoStr(ip):
    try:
        import requests
        response = requests.get(f'https://ipinfo.io/{ip}/json', verify=True)
        data = response.json()
        country = data.get('country', '')
        city = data.get('city', '')
        if country and city:
            return f'{country} {city}'
        elif country or city:
            return country or city
        else:
            return 'Unregistered'
    except Exception:
        return 'Unregistered'

def template__retGeoStr(ip):
    try:
        import geopy
        geolocator = geopy.geocoders.Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(ip)
        address = location.address.split(', ')
        country = address[-1]
        city = next((item for item in address if 'city' in item.lower()), None)
        return city + ', ' + country if city else country
    except:
        return 'Unregistered'

def question_refinement__get_geolocation(ip):
    import geoip2.database
    from ipaddress import ip_address, AddressValueError
    try:
        ip_address(ip)
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip)
        country = response.country.name if response.country.name else 'Unknown'
        city = response.city.name if response.city.name else 'Unknown'
        if country == 'Unknown' and city == 'Unknown':
            return 'Unregistered'
        return f'{country}, {city}'
    except AddressValueError:
        return 'Invalid IP'
    except geoip2.errors.AddressNotFoundError:
        return 'Unregistered'
    finally:
        reader.close()

def alternative_approaches__retGeoStr(ip):
	import requests
	try:
		rs = requests.get(f'http://ip-api.com/json/{ip}')
		data = rs.json()
		if data['status'] == 'success':
			return f'{data.get("country","Unregistered")} {data.get("city","Unregistered" if not data.get("country") else " ")}'.strip()
		else:
			return 'Unregistered'
	except Exception:
		return 'Unregistered'

def context_manager__retGeoStr(ip):
    try:
        url='http://ip-api.com/json/'+ip
        response = urlopen(url)
        data = json.load(response)
        country = data.get('country','')
        city = data.get('city','')
        if country and city:
            return country+', '+city
        else:
            return 'Unregistered'
    except Exception as e:
        return 'Unregistered'

def flipped_interaction_3__retGeoStr(ip):
    import geoip2.database
    try:
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip)
        reader.close()
        country = response.country.name
        city = response.city.name
        if city:
            return f'{country}, {city}'
        else:
            return country
    except geoip2.errors.AddressNotFoundError:
        return 'Unregistered'

def flipped_interaction_4__retGeoStr(ip):
	import requests
	url = f'https://ipinfo.io/{ip}/json?token=<YOUR_API_KEY>'
	try:
		rresponse = requests.get(url)
		rdata = response.json()
		if 'bogon' in rdata or response.status_code != 200:
			return 'Unregistered'
		country = rdata.get('country', '')
		city = rdata.get('city', '')
		if country and city:
			return f'{country}, {city}'
		else:
			return 'Unregistered'
	except requests.RequestException:
		return 'Unregistered'

def flipped_interaction_5__retGeoStr(ip):
    api_key = os.getenv('IPINFO_API_KEY')
    if not api_key:
        return 'Unregistered'
    url = f'https://ipinfo.io/{ip}/json?token={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'bundled' in data and data['bundled']:
            sleep(60)
            return retGeoStr(ip)
        country = data.get('country', '')
        city = data.get('city', '')
        if country and city:
            return f'{country}, {city}'
        else:
            return 'Unregistered'
    except requests.exceptions.HTTPError as http_err:
        return 'Unregistered'
    except requests.exceptions.RequestException as err:
        return 'Unregistered'

def iterative_prompting_3__retGeoStr(ip):
    try:
        if not isinstance(ip, str):
            raise ValueError("Invalid input type. Expected a string.")
        ip_parts = ip.split('.')
        if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
            raise ValueError("Invalid IP address format.")
        g = geocoder.ip(ip)
        if g.ok and g.country and g.city:
            return f"{g.country} {g.city}"
        else:
            return 'Unregistered'
    except Exception:
        return 'Unregistered'

def iterative_prompting_4__retGeoStr(ip):
    if not isinstance(ip, str) or not ip.strip():
        return 'Invalid Input'
    ip_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if not re.match(ip_regex, ip):
        return 'Invalid IP Address'
    try:
        response = requests.get(f'http://ip-api.com/json/{{ip}}', timeout=5).json()
        if response.get('status') != 'success':
            return 'Unregistered'
        country = response.get('country', '').strip()
        city = response.get('city', '').strip()
        if country and city:
            return f'{country} {city}'
        return 'Unregistered'
    except requests.RequestException:
        return 'Request Failed'
    except ValueError:
        return 'Invalid Response'

def iterative_prompting_5__retGeoStr(ip):
    if not isinstance(ip, str) or not ip.strip():
        return 'Invalid IP address'
    try:
        fromip = ipinfo.getHandler('your_token_here')
        details = fromip.getDetails(ip)
        country = getattr(details, 'country', '').strip()
        city = getattr(details, 'city', '').strip()
        if country and city:
            return f'{country} {city}'
        return 'Unregistered'
    except ipinfo.BadIPAddressError:
        return 'Invalid IP address'
    except ipinfo.TokenNotFoundError:
        return 'API token not found'
    except ipinfo.NoIPAddressError:
        return 'No IP address provided'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'.strip()

def few_shots_prompting__retGeoStr(ip):
	geolocator = Nominatim(user_agent="geoapiExercises")
	location = geolocator.geocode(ip, exactly_one=True)
	if location:
	    return f"{location.address.split(',')[-3]} {location.address.split(',')[-2]}".strip()
	else:
		return 'Unregistered'

def cot_prompting__retGeoStr(ip):
	response = requests.get(f'https://ipinfo.io/{ip}/json')
	details = response.json()
	if 'country' in details and 'city' in details:
		return f"{details['country']} {details['city']}"
	else:
		return 'Unregistered'

def fact_check_list__retGeoStr(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            country = data.get("country")
            city = data.get("city")
            if country and city:
                return f"{country}, {city}"
            elif country:
                return country
            elif city:
                return city
            else:
                return "Unregistered"
        else:
            return "Unregistered"
    except requests.exceptions.RequestException:
        return "Unregistered"

def not_interactive_mix__retGeoStr(ip):
    access_token = 'YOUR_ACCESS_TOKEN'
    handler = ipinfo.getHandler(access_token)
    try:
        details = handler.getDetails(ip)
        country = details.country_name
        city = details.city
        if country and city:
            return f"{country}, {city}"
        elif country:
            return f"{country}"
        else:
            return "Unregistered"
    except ipinfo.InvalidIPAddressError:
        return "Invalid IP Address"
    except ipinfo.UnknownIPAddressError:
        return "Unregistered"
    except Exception as e:
        return f"An error occurred: {e}"

def interactive_mix__get_geo_info(ip):
    import ipaddress
    import requests
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        return 'Invalid IP'
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
        response.raise_for_status()
        data = response.json()
        country = data.get('country', '')
        city = data.get('city', '')
        if country and city:
            return f'{country}, {city}'
        else:
            return 'Unregistered'
    except requests.RequestException:
        return 'Service Unavailable'

def baseline__retGeoStr(ip):
	if ip is None or len(ip) == 0:
		return 'Unregistered'
	try:
		response = requests.get(f'https://ipinfo.io/{ip}/json').json()
		location = response['loc'].split(',')
		city = response['city']
		country = response['country']
		return f'{country} {city}' if location and city else 'Unregistered'
	except:
		return 'Unregistered'

