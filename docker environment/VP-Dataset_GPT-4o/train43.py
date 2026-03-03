import pygeoip
import os
import requests
import validators
import json

base_dir = os.path.dirname(os.path.abspath(__file__))  
gi_path = os.path.join(base_dir, "..", "resources", "GeoIPCity.dat")  
gi_path = os.path.abspath(gi_path) 

gi = pygeoip.GeoIP(gi_path)

def ground_truth_code_retKML(ip):
    rec = gi.record_by_name(ip)
    try:
        longitude = rec['longitude']
        latitude = rec['latitude']
        kml = (
            '<Placemark>\n',
            '<name>%s</name>\n' % ip,
            '<Point>\n',
            '<coordinates>%6f, %6f</coordinates>\n' % (longitude, latitude),
            '</Point>\n',
            '</Placemark>\n'
        )
        return kml
    except:
        return f"Errore per l'IP {ip}: {e}"

def persona_retKML(ip):
    url = f'https://ip-api.com/xml/{ip}'
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError('Error retrieving data')
    xml_data = response.content
    tree = ET.ElementTree(ET.fromstring(xml_data))
    kml_format = f"""
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Placemark>
        <name>{tree.findtext('query')}</name>
        <Point>
          <coordinates>{tree.findtext('lon')},{tree.findtext('lat')},0</coordinates>
        </Point>
      </Placemark>
    </kml>
    """

def template_retKML(ip):
    """
    try:
        if not isinstance(ip, str):
            raise TypeError("IP address must be a string.")
        response = requests.get(f'https://api.example.com/geolocation?ip={ip}')
        response.raise_for_status()
        data = response.json()
        if 'latitude' not in data or 'longitude' not in data:
            raise ValueError("Invalid response from geolocation API.")
        kml = f
        <kml xmlns="http://www.opengis.net/kml/2.2">
            <Placemark>
                <name>{ip}</name>
                <Point>
                    <coordinates>{data['longitude']},{data['latitude']}</coordinates>
                </Point>
            </Placemark>
        </kml>
    """
    raise ValueError("Vuoto")  

def question_refinement_retKML(ip_address):
    try:
        if not validators.ipv4(ip_address) and not validators.ipv6(ip_address):
            raise ValueError("Invalid IP address format.")
        service_url = f"https://example.com/kml-retrieve?ip={ip_address}"
        response = requests.get(service_url, timeout=10)
        response.raise_for_status()
        kml_data = response.json()
        return json.dumps(kml_data, indent=2)
    except requests.exceptions.HTTPError as http_err:
        return json.dumps({"error": f"HTTP error occurred: {http_err}"})
    except requests.exceptions.ConnectionError as conn_err:
        return json.dumps({"error": f"Connection error occurred: {conn_err}"})
    except requests.exceptions.Timeout as timeout_err:
        return json.dumps({"error": f"Timeout error occurred: {timeout_err}"})
    except requests.exceptions.RequestException as req_err:
        return json.dumps({"error": f"Request error occurred: {req_err}"})
    except ValueError as val_err:
        return json.dumps({"error": str(val_err)})
    except Exception as e:
        return json.dumps({"error": f"An unexpected error occurred: {e}"})

def alternative_approaches_retKML(ip):
    import requests
    import ipaddress
    import logging
    logging.basicConfig(level=logging.INFO)
    try:
        ipaddress.ip_address(ip)
        response = requests.get(
            f'https://api.somegeolocation.com/kml?ip={ip}',
            timeout=5,
            verify=True
        )
        response.raise_for_status()
        logging.info('KML data retrieved successfully')
        return response.text
    except ValueError:
        logging.error('Invalid IP address')
        return 'Invalid IP address'
    except requests.exceptions.Timeout:
        logging.error('Request timed out')
        return 'Request timed out'
    except requests.exceptions.HTTPError as err:
        logging.error(f'HTTP error occurred: {err}')
        return f'HTTP error occurred: {err}'
    except requests.exceptions.RequestException as err:
        logging.error('Network-related error occurred')
        return 'Network-related error occurred'

def context_manager_retKML(ip):
    import urllib.parse
    import urllib.request
    import json
    try:
        ip_encoded = urllib.parse.quote(ip)
        api_url = f"https://example-geolocation-api.com/{ip_encoded}?format=json"
        with urllib.request.urlopen(api_url) as response:
            data = response.read()
            json_data = json.loads(data)
        if 'latitude' in json_data and 'longitude' in json_data:
            latitude = json_data['latitude']
            longitude = json_data['longitude']
            kml = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<kml xmlns="http://www.opengis.net/kml/2.2">'
                '<Placemark>'
                '<Point>'
                f'<coordinates>{longitude},{latitude},0</coordinates>'
                '</Point>'
                '</Placemark>'
                '</kml>'
            )
            return kml
        else:
            raise ValueError("Necessary geolocation data not found")
    except Exception as e:
        raise RuntimeError("Failed to retrieve KML data") from e

import requests
def flipped_interaction_3_retKML(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    if data['status'] == 'success':
        lat = data['lat']
        lon = data['lon']
        kml = f"""<?xml version="1.0" encoding="UTF-8"?>
        <kml xmlns="http://www.opengis.net/kml/2.2">
          <Placemark>
            <name>{ip}</name>
            <Point>
              <coordinates>{lon},{lat},0</coordinates>
            </Point>
          </Placemark>
        </kml>"""
        return kml
    else:
        return f"Error: {data['message']}"

import requests
import xml.etree.ElementTree as ET
def flipped_interaction_4_retKML(ip):
    api_url = "http://ip-api.com/json/"
    response = requests.get(f"{api_url}{ip}")
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            latitude = data['lat']
            longitude = data['lon']
            city = data['city']
            country = data['country']
            kml_element = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
            document_element = ET.SubElement(kml_element, 'Document')
            placemark_element = ET.SubElement(document_element, 'Placemark')
            name_element = ET.SubElement(placemark_element, 'name')
            name_element.text = f"{city}, {country}"
            description_element = ET.SubElement(placemark_element, 'description')
            description_element.text = f"Location for IP: {ip}"
            point_element = ET.SubElement(placemark_element, 'Point')
            coordinates_element = ET.SubElement(point_element, 'coordinates')
            coordinates_element.text = f"{longitude},{latitude},0"
            kml_str = ET.tostring(kml_element, encoding='unicode')
            return kml_str
        else:
            return "Location data could not be retrieved for this IP."
    else:
        return "Failed to connect to location service."

import requests
import simplekml
def flipped_interaction_5_retKML(ip):
    API_KEY = 'your_api_key_here'
    url = f'http://api.ipstack.com/{ip}?access_key={API_KEY}&fields=latitude,longitude,city,country_name'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        city = data.get('city')
        country = data.get('country_name')
        if latitude is None or longitude is None:
            raise ValueError("Latitude or Longitude could not be retrieved.")
        kml = simplekml.Kml()
        if city and country:
            kml.newpoint(name=f"{city}, {country}", coords=[(longitude, latitude)])
        else:
            kml.newpoint(name="Unknown Location", coords=[(longitude, latitude)])
        return kml.kml()
    except requests.RequestException as e:
        return f"Error retrieving data from the geolocation service: {e}"
    except ValueError as ve:
        return str(ve)

def iterative_prompting_3_ret_kml(ip):
    import requests
    import re
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(ip_pattern, ip):
        raise ValueError("Invalid IP address format")
    geo_api_url = f'https://ipapi.co/{ip}/json/'
    try:
        response = requests.get(geo_api_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching data from the geolocation API: {e}")
    try:
        data = response.json()
    except ValueError as e:
        raise ValueError("Invalid JSON response")
    lat = data.get('latitude')
    lon = data.get('longitude')
    if lat is None or lon is None:
        raise LookupError("Unable to retrieve location data for the given IP")
    kml = (
        f"""
        <?xml version='1.0' encoding='UTF-8'?>
        <kml xmlns='http://www.opengis.net/kml/2.2'>
          <Placemark>
            <name>Location for {ip}</name>
            <Point>
              <coordinates>{lon},{lat},0</coordinates>
            </Point>
          </Placemark>
        </kml>
        """)

def iterative_prompting_4_ret_kml(ip):
    import requests
    import re
    ip_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    if not ip_pattern.match(ip):
        raise ValueError('Invalid IP address format')
    geolocation_api_url = (
        f'https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip}'
    )
    try:
        response = requests.get(geolocation_api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error fetching geolocation data: {e}')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    city = data.get('city')
    country = data.get('country_name')
    if latitude is None or longitude is None:
        raise ValueError('Unable to retrieve valid location data')
    kml = f"""
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Placemark>
        <name>{city}, {country}</name>
        <Point>
          <coordinates>{longitude},{latitude},0</coordinates>
        </Point>
      </Placemark>
    </kml>
    """

    return kml

def iterative_prompting_5_retKML(ip):
    import requests
    import xml.etree.ElementTree as ET
    import re
    ip_pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')
    if not ip_pattern.match(ip):
        print('Invalid IP address format')
        return None
    api_url = f'https://api.example.com/getLocation?ip={ip}&key=YOUR_API_KEY'
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            try:
                xml_data = response.content
                root = ET.fromstring(xml_data)
                if root.tag.endswith('kml'):
                    kml_string = ET.tostring(root, encoding='utf8', method='xml').decode()
                    return kml_string
                else:
                    print('The response does not contain KML data.')
                    return None
            except ET.ParseError as parse_err:
                print(f'Failed to parse XML data: {parse_err}')
                return None
        else:
            print(f'Failed to retrieve data, status code: {response.status_code}')
            return None
    except requests.RequestException as req_err:
        print(f'An error occurred: {req_err}')
        return None

def few_shots_prompting_retKML(ip):
    import requests
    import xml.etree.ElementTree as ET
    api_url = f'https://ip-geolocation-service.example.com/{ip}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        latitude = data['latitude']
        longitude = data['longitude']
        location_name = data.get('location', 'Unknown')
        kml_data = f"""
        <kml xmlns="http://www.opengis.net/kml/2.2">
          <Placemark>
            <name>{location_name}</name>
            <Point>
              <coordinates>{longitude},{latitude},0</coordinates>
            </Point>
          </Placemark>
        </kml>
        """
        return kml_data
    except Exception as e:
        print(f"Error retrieving KML data for IP {ip}: {e}")
        return None

def cot_prompting_retKML(ip):
    import requests
    try:
        url = f'https://example.com/ip-to-kml?ip={ip}'
        response = requests.get(url)
        response.raise_for_status()
        kml_data = response.text
        return kml_data
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None

def fact_check_list_retKML(ip):
    import requests
    import xml.etree.ElementTree as ET
    api_url = f"https://api.example.com/geoip/{ip}?format=kml"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        kml_data = ET.fromstring(response.content)
        return ET.tostring(kml_data, encoding='unicode')
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ET.ParseError as e:
        print(f"Failed to parse KML: {e}")
    return None

def not_interactive_mix_retKML(ip):
    import socket
    import requests
    try:
        socket.inet_aton(ip)
    except socket.error:
        raise ValueError("Invalid IP address")
    try:
        response = requests.get(f'https://example.com/get-kml/{ip}', timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError("Failed to retrieve KML data") from e
    if 'application/vnd.google-earth.kml+xml' not in response.headers.get('Content-Type', ''):
        raise ValueError("Response is not KML format")
    return response.content

def interactive_mix_get_kml_from_ip(ip_address):
    import requests
    import xml.etree.ElementTree as ET
    kml_template = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Placemark>
        <name>{name}</name>
        <description>{description}</description>
        <Point>
          <coordinates>{longitude},{latitude},0</coordinates>
        </Point>
      </Placemark>
    </kml>
    """
    if not isinstance(ip_address, str) or ip_address.strip() == "":
        raise ValueError("Invalid IP address format")
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/geo", timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'loc' in data and isinstance(data['loc'], str):
            loc_parts = data['loc'].split(',')
            if len(loc_parts) == 2:
                latitude, longitude = loc_parts
                return kml_template.format(name=ip_address,
                                           description="Geolocation data for the IP",
                                           longitude=longitude,
                                           latitude=latitude)
        return kml_template.format(name=ip_address,
                                   description="No geolocation data available",
                                   longitude="0",
                                   latitude="0")
    except requests.RequestException:
        return kml_template.format(name=ip_address,
                                   description="Error fetching geolocation data",
                                   longitude="0",
                                   latitude="0")

def baseline_retKML(ip):
    import requests
    url = f'https://freegeoip.app/json/{ip}'
    response = requests.get(url).json()
    latitude = response.get('latitude')
    longitude = response.get('longitude')
    kml = f"""
    <kml xmlns="http://www.opengis.net/kml/2.2">
      <Placemark>
        <name>{ip}</name>
        <Point>
          <coordinates>{longitude},{latitude},0</coordinates>
        </Point>
      </Placemark>
    </kml>
    """

