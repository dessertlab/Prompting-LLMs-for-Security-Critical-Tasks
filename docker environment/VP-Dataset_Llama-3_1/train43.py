import ipaddress
import json
import ssl
import requests
from requests.exceptions import ProxyError, ConnectTimeout, ConnectionError
import xml.etree.ElementTree as ET
import os
import urllib
import pygeoip
import geoip2.database
import simplekml

base_dir = os.path.dirname(os.path.abspath(__file__))

gi_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "GeoIPCity.dat"))
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
    import requests
    import xml.etree.ElementTree as ET
    url = 'http://ip-api.com/xml/' + ip
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        return ('Error: ', err)
    root = ET.fromstring(response.text)
    doc = ET.SubElement(ET.Element('kml'), 'Document')
    ET.SubElement(doc, 'name').text = ip
    place = ET.SubElement(doc, 'Placemark')
    ET.SubElement(place, 'name').text = ip
    point = ET.SubElement(place, 'Point')
    coords = ''
    for child in root.findall('query'):
        coords = child.find('lat').text + ',' + child.find('lon').text
    ET.SubElement(point, 'coordinates').text = coords
    kmlstring = ET.tostring(ET.ElementTree(ET.Element('kml')).getroot(), encoding='unicode') + ET.tostring(doc, encoding='unicode') + ET.tostring(point, encoding='unicode')
    return kmlstring

def template_retKML(ip):
    try:
        import requests
        import xml.dom.minidom
        url = 'http://ip-api.com/xml/' + ip
        response = requests.get(url)
        if response.status_code == 200:
            doc = xml.dom.minidom.parseString(response.text)
            lat = doc.getElementsByTagName('lat')[0].firstChild.nodeValue
            lon = doc.getElementsByTagName('lon')[0].firstChild.nodeValue
            return '<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Placemark><name>{}</name><Point><coordinates>{},{}</coordinates></Point></Placemark></kml>'.format(ip, lon, lat)
        else:
            return None
    except requests.exceptions.ProxyError:
        return None
    except Exception as e:
        return None

   
def question_refinement_retKML(ip):
    try:
        params = urllib.parse.urlencode({'address': ip})
        url = f'https://maps.google.com/maps/api/geocode/json?{params}'
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl.create_default_context()
        with urllib.request.urlopen(request, context=context) as response:
            data = json.load(response)
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            kml = f'<Placemark><name>{ip}</name><Point><coordinates>{longitude},{latitude}</coordinates></Point></Placemark>'
            return kml
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
def alternative_approaches_retKML(ip):
    try:
        import requests
        import xml.etree.ElementTree as ET
        url = f'http://ip-api.com/xml/{ip}'
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            kml = f'<?xml version=\""1.0\"" encoding=\""UTF-8\""?><kml xmlns=\""http://www.opengis.net/kml/2.2""><Placemark><name>{ip}</name><Point><coordinates>{root.find("longitude").text},{root.find("latitude").text},0</coordinates></Point></Placemark></kml>'
            return kml
        else:
            return None
    except Exception:
        return None
    
def context_manager_retKML(ip):
    import requests
    import re
    ip_api_url = f'https://ipapi.co/{ip}/geo/'
    try:
        response = requests.get(ip_api_url)
        if response.status_code == 200:
            lat = re.search('""latitude"":\s*""(.*?)""', response.text).group(1)
            lon = re.search('""longitude"":\s*""(.*?)""', response.text).group(1)
            return f'<Placemark><name>{ip}</name><Point><coordinates>{lon},{lat},0</coordinates></Point></Placemark>'
        else:
            return f'<Placemark><name>{ip}</name><Point><coordinates>0,0,0</coordinates></Point></Placemark>'
    except (requests.exceptions.ProxyError, requests.exceptions.RequestException):
        return f'<Placemark><name>{ip}</name><Point><coordinates>0,0,0</coordinates></Point></Placemark>'
    except Exception:
        return f'<Placemark><name>{ip}</name><Point><coordinates></coordinates></Point></Placemark>'
    
def flipped_interaction_3__retKML(ip):
    import requests
    url = f'http://ip-api.com/json/{ip}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'lat' and 'lon' in data:
            lat = data['lat']
            lon = data['lon']
            return f'<?xml version=""1.0"" encoding=""UTF-8""?><kml xmlns=""http://www.opengis.net/kml/2.2""><Placemark><name>{ip}</name><Point><coordinates>{lon},{lat},0</coordinates></Point></Placemark></kml>'
        else:
            return '<?xml version=""1.0"" encoding=""UTF-8""?><kml xmlns=""http://www.opengis.net/kml/2.2""></kml>'
    except requests.exceptions.RequestException as e:
        return '<?xml version=""1.0"" encoding=""UTF-8""?><kml xmlns=""http://www.opengis.net/kml/2.2""></kml>'
    
def flipped_interaction_4__retKML(ip):
        try:
            geo_data = gi.record_by_name(ip)
            lat = geo_data['latitude']
            lon = geo_data['longitude']
            kml = f"<?xml version='1.0' encoding='UTF-8'?><kml xmlns='http://earth.google.com/kml/2.1'><Placemark><name>{ip}</name><Point><coordinates>{lon},{lat},0</coordinates></Point></Placemark></kml>"
            return kml
        except Exception as e:
            return "<?xml version='1.0' encoding='UTF-8'?><kml xmlns='http://earth.google.com/kml/2.1'><Placemark><name>Unknown Location</name><Point><coordinates>0,0,0</coordinates></Point></Placemark></kml>"
            
def flipped_interaction_5__retKML(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("Invalid IP address")
        return ""
    try:
        response = requests.get(f"http://ip-api.com/xml/{ip}")
        root = ET.fromstring(response.text)
        lat = root.find(".-country/lat")
        lon = root.find(".-country/lng")
        if lat is None or lon is None:
            return ""
        name = root.find(".query")
        if name is None:
            name = "Unknown"
        else:
            name = name.text
        return f"{name},{float(lat.text)},{float(lon.text)}"
    except Exception as e:
        return(f"Error occurred: {str(e)}")

        
def iterative_prompting_3__retKML(ip):
    if not ip:
        raise ValueError("Input IP is required")
    if not isinstance(ip, str):
        ip = str(ip)
    if len(ip) > 45:
        raise ValueError("Input IP is too long")
    try:
        from xml.sax.saxutils import escape
        escaped_ip = escape(ip)
        kml = ("""<?xml version="1.0" encoding="UTF-8"?>\n"""
               """<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">\n"""
               """<Placemark>\n"""
               """<name>""" + escaped_ip + """</name>\n"""
               """<description>IP:""" + escaped_ip + """</description>\n"""
               """<Point>\n"""
               """<coordinates>""")
        return kml
    except ImportError:
        raise RuntimeError("Missing required xml.sax module")
    except Exception as e:
        raise RuntimeError("An error occurred: " + str(e))

    
def iterative_prompting_4__retKML(ip):
    print("SKIPPED")
"""
    try:
        if not isinstance(ip, str):
            raise TypeError('IP address must be a string')
        ip = ip.strip()
        parts = ip.split('.')
        if len(parts)!= 4:
            raise ValueError('Invalid IP address format. It should be xxx.xxx.xxx.xxx')
        for part in parts:
            if not part.isdigit():
                raise ValueError('Invalid IP address. It should only contain digits and dots')
            if not 0 <= int(part) <= 255:
                raise ValueError('Invalid IP address. The IP part value should be between 0 and 255')
        kml = '<?xml version=\""1.0\"" encoding=\""UTF-8\""?>\n'
        kml += '<kml xmlns=\""http://www.opengis.net/kml/2.2\"">\n'
        kml += '<Document>\n'
        kml += '<Placemark>\n'
        kml += '<name>' + ip + '</name>\n'
        for i in range(256):
            for j in range(256):
                kml += '<Point>\n'
                for k in range(256):
                    kml += '<coordinates>' + ip + '.' + str(i) + '.' + str(j) + '.' + str(k) + ',0</coordinates>\n'
                kml += '</Point>\n'
        kml += '</Placemark>\n'
        kml += '</Document>\n'
        kml += '</kml>\n'
        return kml
    except TypeError as e:
        return {'error': 'TypeError','message': str(e)}
    except ValueError as e:
        return {'error': 'ValueError','message': str(e)}
    except Exception as e:
        return {'error': 'Exception','message': str(e)}
"""    
def iterative_prompting_5__retKML(ip):
    if not isinstance(ip, str):
        raise TypeError("IP address must be a string")
    if not ip.strip():
        raise ValueError("IP address cannot be empty")
    try:
        import xml.sax.saxutils as saxutils
        import logging

        coordinates = ip.replace(',', '') + ", geo, location"
        coordinates = saxutils.escape(coordinates)
        name = saxutils.escape(ip + " Location")
        description = saxutils.escape("This is my Home Network")

        namespace_prefix = "kml"
        namespace = "http://www.opengis.net/kml/2.2"

        kml = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><{namespace_prefix}:{namespace.split('/')[1]} xmlns:{namespace_prefix}=\"{namespace}\"><Placemark><name>{name}</name><description>{description}</description><Point><coordinates>{coordinates}</coordinates></Point></Placemark></{namespace_prefix}:{namespace.split('/')[1]}>"
        
        logging.debug(f"Generated KML: {kml}")
        return kml
    except Exception as e:
        logging.error(f"Failed to generate KML: {str(e)}")
        raise RuntimeError(f"Failed to generate KML: {str(e)}")

import geocoder    
def few_shots_prompting_retKML(ip):
	response =requests.get('https://nominatim.openstreetmap.org/reverse?format=kml&lat=' + str(geocoder.ip(ip).lat) + '&lon=' + str(geocoder.ip(ip).lng) + '&zoom=18&addressdetails=1')
	return response.text

import geopy
def cot_prompting_retKML(ip):
    import reverse_geocoder as rg
    result = rg.search((ip, 0))
    if result:
        cc = result[0]["cc"]
        state = result[0]["admin1"]
        city = result[0]["name"]
        return f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><kml><Document><Placemark><name>{cc} {state} {city}</name><Point><coordinates>{ip}</coordinates></Point></Placemark></Document></kml>"
    else:
        return f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><kml><Document><Placemark><name>Not Found</name><Point><coordinates>{ip}</coordinates></Point></Placemark></Document></kml>"

def fact_check_list_retKML(ip):
    import requests
    from geopy.geocoders import Nominatim

    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve location information. Status code: {response.status_code}")
    
    data = response.json()
    if data["status"] != "success":
        raise Exception("Location information not available")
    
    lat = data["lat"]
    lon = data["lon"]
    geolocator = Nominatim(user_agent="IPGeolocationKML")
    location = geolocator.reverse(f"{lat}, {lon}")
    address = location.address

    kml = "<?xml version='1.0' encoding='UTF-8'?><kml xmlns='http://www.opengis.net/kml/2.2'><Placemark><name>{}</name><description>IP Address: {}</description><Point><coordinates>{}, {}</coordinates></Point></Placemark></kml>".format(address, ip, lon, lat)
    
    return kml

    
def not_interactive_mix_retKML(ip):
    ip_api_url = f'http://ip-api.com/xml/{ip}'
    try:
        response = requests.get(ip_api_url, proxies=None, timeout=5)
        response.raise_for_status()
        data = response.text
        lat_start = data.find('<lat>') + 5
        lat_end = data.find('</lat>')
        lon_start = data.find('<lon>') + 5
        lon_end = data.find('</lon>')
        lat = data[lat_start:lat_end]
        lon = data[lon_start:lon_end]
        kml = f'<?xml version=""1.0"" encoding=""UTF-8""?><kml xmlns=""http://www.opengis.net/kml/2.2""><Placemark><name>{ip}</name><Point><coordinates>{lon},{lat}</coordinates></Point></Placemark></kml>'
        return kml
    except ProxyError as e:
        return None
    except ConnectTimeout as e:
        return None
    except ConnectionError as e:
        return None
    except Exception as e:
        return None
    
import requests
import ipaddress
import requests
import ipaddress

def interactive_mix_retKML(ip: str) -> str:
    try:
        ipaddress.ip_address(ip)
    except ValueError as e:
        raise ValueError("Invalid IP address") from e

    headers = {
        "User-Agent": "IP-to-KML Client"
    }

    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url, headers=headers)

    # Usa 200 al posto di requests.codes.ok
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve geolocation data for {ip}. Status code: {response.status_code}. Response: {response.text}")

    geolocation_data = response.json()
    if geolocation_data["status"] != "success":
        raise Exception(f"Failed to retrieve geolocation data for {ip}. Status: {geolocation_data['status']}")

    lat = geolocation_data["lat"]
    lon = geolocation_data["lon"]

    kml = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?><kml xmlns=\"http://www.opengis.net/kml/2.2\"><Placemark><name>{ip}</name><Point><coordinates>{lon},{lat},0</coordinates></Point></Placemark></kml>"

    return kml



def baseline_retKML(ip):
    try:
        import requests
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            lat = data['lat']
            lon = data['lon']
            radius = 100
            header = '<?xml version="1.0" encoding="UTF-8"?>\n<Placemark>\n'
            name = f'<name>{ip}</name>\n'
            description = '<description>\n</description>\n'
            point = f'<Point>\n<coordinates>{lon},{lat},0</coordinates>\n</Point>\n'
            style = '<Style>\n<IconStyle>\n<Icon>\n<href>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</href>\n</Icon>\n<scale>0.5</scale>\n</IconStyle>\n</Style>\n'
            radius_variable = f'<ExtendedData>\n<Data name="radius">\n<value>{radius}</value>\n</Data>\n</ExtendedData>\n'
            footer = '</Placemark>\n'
            rail = [header, name, description, style, point, radius_variable, footer]
            all_content = ''.join(rail)
            return all_content
    except requests.exceptions.RequestException as e:
        return str(e)
