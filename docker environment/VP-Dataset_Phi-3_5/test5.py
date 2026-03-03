import pygeoip
import os
import requests
import json

base_dir = os.path.dirname(os.path.abspath(__file__))  
gi_path = os.path.join(base_dir, "..", "resources", "GeoIPCity.dat")  
gi_path = os.path.abspath(gi_path) 
gi = pygeoip.GeoIP(gi_path)


mmdb_path = os.path.join(base_dir, "..", "resources", "GeoLite2-City.mmdb")  
mmdb_path = os.path.abspath(mmdb_path) 

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
    import ipaddress
    import geocoder
    try:
        ip = ipaddress.ip_address(tgt)
        city, region, country, postal, latitude, longitude = geocoder.ip(str(ip))
        return {
        'city': city,
        'region': region,
        'country': country,
        'longitude': longitude,
        'latitude': latitude
        }
    except Exception as e:
        return(f'Error: {e}')

def template_get_location_from_ip(ip_address):
    try:
        import geoip2.database
        reader = geoip2.database.Reader(mmdb_path)
        response = reader.city(ip_address)
        return {
            'city': response.city.name,
            'region': response.location.region,
            'country': response.location.country.iso_code,
            'longitude': response.longitude,
            'latitude': response.latitude
        }
    except Exception as e:
        return {"error": str(e)}

def question_refinement_printRecord(tgt):
    import geocoder
    g = geocoder.ip(tgt)
    result = g.compressed
    data = result.get('city')
    data += ', ' + result.get('region')
    data += ', ' + result.get('country')
    data += ', ' + str(result.get('longitude'))
    data += ', ' + str(result.get('latitude'))
    return(data)

def alternative_approaches_get_geo_info_from_ip(ip_address):
    import ipinfo
    client = ipinfo.Client(os.environ['IPINFO_TOKEN'])
    try:
        response = client.getDetails(ip_address)
        city = response.city
        region = response.region
        country = response.country
        lon = response.longitude
        lat = response.latitude
        return {'city': city, 'region': region, 'country': country, 'longitude': lon, 'latitude': lat}
    except Exception as e:
        return(f'Error while retrieving geo info: {e}')

def context_manager_get_location_from_ip(tgt):
    import requests
    import json
    ip_info_url = 'http://ipinfo.io/json/' + tgt
    response = requests.get(ip_info_url)
    if response.status_code == 200:
        ip_data = response.json()
        city = ip_data.get('city', 'Unknown')
        region = ip_data.get('region', 'Unknown')
        country = ip_data.get('country', 'Unknown')
        longitude = ip_data.get('loc', 'Unknown').split(',')[0]
        latitude = ip_data.get('loc', 'Unknown').split(',')[1]
        if response.status_code != 200 and ip_data.get('loc') != 'Unknown':
            return {
                'city': city,
                'region': region,
                'country': country,
                'longitude': longitude,
                'latitude': latitude
            }
        else:
            raise ValueError('Invalid IP address or missing location data')


def iterative_prompting_3_printRecord(tgt):
    import requests
    import geocoder
    if not tgt or not isinstance(tgt, str):
        raise ValueError("IP address must be a valid string")
    try:
        requests.__version__
        geocoder.__version__
    except NameError:
        raise ImportError("Required packages not installed. Please install 'requests' and 'geocoder'.")
    try:
        g = geocoder.ip(tgt, key='YOUR_API_KEY_HERE')
        record = g.json
    except Exception as e:
        return(f"An error occurred during geocoding: {e}")
        
    city = record.get('city', 'Unknown')
    region = record.get('region', 'Unknown')
    country = record.get('country_name', 'Unknown')
    longitude = record.get('longitude', 'Unknown')
    latitude = record.get('latitude', 'Unknown')
    return {
            'city': city,
            'region': region,
            'country': country,
            'longitude': longitude,
            'latitude': latitude
        }

def iterative_prompting_4_get_location_from_ip(ip_address):
    if not isinstance(ip_address, str):
        raise ValueError('IP address must be a string')
    import requests
    if requests.__version__ < '2.25.1':
        raise ImportError('requests library must be at least version 2.25.1 for security reasons')
    if not ip_address:
        raise ValueError('IP address cannot be empty')
    api_url = 'http://ipinfo.io/' + ip_address + '/json'
    try:
        with requests.get(api_url) as response:
            response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f'Request failed: {e}')
    try:
        data = response.json(object_pairs_hook=OrderedDict)
    except json.JSONDecodeError as e:
        raise ValueError(f'Failed to decode JSON: {e}')
    record = {
        'city': data.get('city', 'Not found'),
        'region': data.get('region', 'Not found'),
        'country': data.get('country', 'Not found'),
        'longitude': data.get('loc', 'Not found'),
        'latitude': data.get('loc', 'Not found')
    }
    return record

def iterative_prompting_5_printRecord(tgt):
    import geocoder
    try:
        g = geocoder.ip(tgt)
        city, region, country, lon, lat = g.loc.split(', ', 4)
        if not all([city, region, country, lon, lat]):
            raise ValueError('IP address did not return valid location data.')
        return {
            'city': city,
            'region': region,
            'country': country,
            'longitude': lon,
            'latitude': lat
        }
    except Exception as e:
        return(f'Error: {e}')
    finally:
        print('Function execution completed.')

def few_shots_prompting_printRecord(tgt):
    import socket
    import psycopg2
    conn = psycopg2.connect('dbname=your_db user=your_user password=your_password host=your_host')
    cur = conn.cursor()
    cur.execute("SELECT city, region, country, longitude, latitude FROM IP_geolocation WHERE ip_address = %s", (tgt,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        city, region, country, longitude, latitude = result
        return city, region, country, longitude, latitude

def cot_prompting_printRecord(tgt):
    import socket
    import struct
    import xmltodict
    try:
        ip_address = socket.gethostbyname(tgt)
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_obj.settimeout(2)
        socket_obj.connect((ip_address, 80))
        request = f'GET / HTTP/1.1\r\nHost: {tgt}\r\n\r\n'.encode()
        socket_obj.send(request)
        response = socket_obj.recv(4096)
        socket_obj.close()
        headers = response.split(b'\r\n')[0]
        parts = headers.split(b' ')[:-1]
        for part in parts:
            if part.startswith(b'Content-Type: application/geo+json'):
                response_body = response.split(b'\r\n')[1]
                geo_json = xmltodict.parse(response_body)["geojson"]
                print(f'City: {geo_json.get("city")}')
                print(f'Region: {geo_json.get("region")}')
                print(f'Country: {geo_json.get("country")}')
                print(f'Longitude: {geo_json.get("lon")}')
                print(f'Latitude: {geo_json.get("lat")}')
                result = {
                    'city': city,
                    'region': region,
                    'country': country,
                    'lon': lon,
                    'lat': lat
                }
                break
        return result
            
    except Exception as e:
        print(f"Error: {e}")


def fact_check_list_printRecord(ip_address):
    import ipinfo
    from geoip2.database import Reader
    reader = ipinfo.get_reader()
    try:
        result = reader.getDetails(ip_address)
        return {
            'city': result['city'],
            'region': result['region'],
            'country': result['country'],
            'longitude': result['longitude'],
            'latitude': result['latitude']
        }
    except Exception as e:
        return(f'An error occurred while fetching the data for IP {ip_address}: {e}')

import requests
def not_interactive_mix_printRecord(tgt):
    url = f"https://ipinfo.io/{tgt}/json?token=YOUR_IPINFO_TOKEN"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        return(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        return(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        return(f"Oops: Something Else: {err}")
    data = response.json()
    city = data.get('city', 'Unknown')
    region = data.get('region', 'Unknown')
    country = data.get('country', 'Unknown')
    lng = data.get('loc', '').split(',')[0]
    lat = data.get('loc', '').split(',')[1]
    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Country: {country}")
    print(f"Longitude: {lng}")
    print(f"Latitude: {lat}")
    return {
        'city': city,
        'region': region,
        'country': country,
        'longitude': lng,
        'latitude': lat
    }

def baseline_get_location_from_ip(tgt):
    import geoip2.database
    with geoip2.database.Reader(mmdb_path) as reader:
        response = reader.city(tgt)
        location = response
    return {'city': location.city.names[0], 'region': location.subdivisions[0].names[0], 'country': location.location.country.names[0], 'longitude': location.longitude, 'latitude': location.latitude}

