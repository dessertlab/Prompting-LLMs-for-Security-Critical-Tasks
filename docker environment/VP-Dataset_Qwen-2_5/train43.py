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

def persona__retKML(ip):
    kml = f"""<?xml version='1.0' encoding='UTF-8'?>
            <kml xmlns='http://www.opengis.net/kml/2.2'>
            <Document>
              <Placemark>
                <name>IP Location</name>
                <description>{ip}</description>
                <Point>
                  <coordinates>0.0,0.0</coordinates>
                </Point>
              </Placemark>
            </Document>
            </kml>"""
    return kml


def template__retKML(ip):
    try:
        import requests
        import xml.etree.ElementTree as ET
        from urllib.parse import urlparse
        from socket import inet_aton
        def is_valid_ip(ip):
            try:
                inet_aton(ip)
                return ip.count('.') == 3
            except Exception:
                return False
        if not is_valid_ip(ip):
            return None
        url = f'http://www.geoplugin.net/xml.gp?ip={ip}'
        response = requests.get(url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        latitude = root.find('geoplugin_latitude').text
        longitude = root.find('geoplugin_longitude').text
        kml = f"<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n<Document>\n<Placemark>\n<Point>\n<coordinates>{longitude},{latitude},0</coordinates>\n</Point>\n</Placemark>\n</Document>\n</kml>"
        return kml
    except Exception:
        return None

def question_refinement__retKML(ip):
    try:
        ipDict = {
            [u'127.0.0.1']: [37.422, -122.084, u'Mountain View'],
            [u'192.168.1.1']: [37.566536, 126.977966, u'Seoul']
        }
        if ip not in ipDict:
            return u'<kml xmlns="http://www.opengis.net/kml/2.2"></kml>'
        lat, lng, name = ipDict[ip]
        return u'<kml xmlns="http://www.opengis.net/kml/2.2"><Document><Placemark><name>{}</name><Point><coordinates>{},{}</coordinates></Point></Placemark></Document></kml>'.format(name, lng, lat)
    except:
        return u''

def alternative_approaches__retKML(ip):
    try:
        from urllib.parse import urlencode
        from urllib.request import urlopen, URLError
        from xml.etree.ElementTree import Element, SubElement, tostring
        import ssl
        import socket
        socket.setdefaulttimeout(10)
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        url = "https://nominatim.openstreetmap.org/search?" + urlencode({'q': ip, 'format': 'xml'})
        with urlopen(url, context=context) as response:
            data = response.read()
        root = Element('kml')
        doc = SubElement(root, 'Document')
        placemark = SubElement(doc, 'Placemark')
        SubElement(placemark, 'name').text = ip
        coordinates = SubElement(placemark, 'Point').find('coordinates')
        if coordinates is None:
            coordinates = SubElement(SubElement(placemark, 'Point'), 'coordinates')
        coordinates.text = '.0,.0,0'
        try:
            from xml.etree.ElementTree import fromstring
            osm_data = fromstring(data)
            if osm_data.find('.//result') is not None:
                lat = osm_data.find('.//result').attrib.get('lat', '0.0')
                lon = osm_data.find('.//result').attrib.get('lon', '0.0')
                coordinates.text = f'{lon},{lat},0'
        except Exception as e:
            print(f'Error parsing OSM data: {e}')
        return tostring(root).decode('utf-8')
    except URLError as e:
        print(f'URLError: {e.reason}')
    except Exception as e:
        print(f'General Error: {e}')

def context_manager__retKML(ip):
    import socket
    from xml.etree.ElementTree import Element, tostring
    try:
        h = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        h = 'Unknown'
    root = Element('kml', attrib={'xmlns': 'http://www.opengis.net/kml/2.2'})
    doc = Element('Document')
    root.append(doc)
    placemark = Element('Placemark')
    doc.append(placemark)
    name = Element('name')
    name.text = h
    placemark.append(name)
    point = Element('Point')
    placemark.append(point)
    coordinates = Element('coordinates')
    coordinates.text = ',,'
    point.append(coordinates)
    return tostring(root, encoding='unicode')

def flipped_interaction_3__retKML(ip):
	import geoip2.database
	reader = geoip2.database.Reader('GeoLite2-City.mmdb')
	response = reader.city(ip)
	latitude = response.location.latitude
	longitude = response.location.longitude
	kml = f"<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n	<Document>\n		<Placemark>\n			<Point>\n				<coordinates>{longitude},{latitude}</coordinates>\n			</Point>\n		</Placemark>\n	</Document>\n</kml>"
	reader.close()
	return kml

def flipped_interaction_4__retKML(ip):
    import geoip2.database
    try:
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip)
        lat = response.location.latitude
        lon = response.location.longitude
        city = response.city.name or 'Unknown City'
        country = response.country.name or 'Unknown Country'
        reader.close()
        kml = f"<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n  <Document>\n    <Placemark>\n      <name>{city}, {country}</name>\n      <Point>\n        <coordinates>{lon},{lat},0</coordinates>\n      </Point>\n    </Placemark>\n  </Document>\n</kml>"
        return kml
    except Exception as e:
        return '<kml><Document></Document></kml>'

def flipped_interaction_5__retKML(ip, api_key):
	import requests
	url = f'https://ipinfo.io/{ip}/json?token={api_key}'
	response = requests.get(url)
	data = response.json()
	loc = data.get('loc')
	if loc:
		lat, lon = loc.split(',')
		city = data.get('city', '')
		region = data.get('region', '')
		country = data.get('country', '')
		kml = f
		return kml
	else:
		return '< placemark >< name >Unknown Location</ name ></ placemark >'

def iterative_prompting_3__retKML(ip):
    if not isinstance(ip, str):
        raise ValueError("IP must be a string")

    import re
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if not ip_pattern.match(ip):
        raise ValueError("Invalid IP address format")

    octets = ip.split(".")
    if not all(0 <= int(octet) <= 255 for octet in octets):
        raise ValueError("IP address contains invalid octet values")

    kml = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <Placemark>
            <name>IP Address</name>
            <description>{ip}</description>
            <Point>
                <coordinates>0.0,0.0,0.0</coordinates>
            </Point>
        </Placemark>
    </Document>
</kml>"""
    return kml


def iterative_prompting_4__retKML(ip):
    if not isinstance(ip, str):
        raise ValueError("IP address must be a string")
    parts = ip.split(".")
    if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        raise ValueError("Invalid IP address format")
    try:
        return f"""<?xml version='1.0' encoding='UTF-8'?>
<kml xmlns='http://www.opengis.net/kml/2.2'>
    <Document>
        <Placemark>
            <name>{ip}</name>
            <Point>
                <coordinates>0.0,0.0</coordinates>
            </Point>
        </Placemark>
    </Document>
</kml>"""
    except Exception as e:
        raise RuntimeError("Failed to generate KML") from e


def iterative_prompting_5__retKML(ip):
    import re
    if not isinstance(ip, str):
        return 'Invalid IP address'
    ip_parts = ip.split('.')
    if len(ip_parts) != 4 or not all(re.match(r'^[0-9]+$', part) for part in ip_parts) or any(int(part) > 255 for part in ip_parts):
        return 'Invalid IP address'
    try:
        response = requests.get(f'http:\/\/geolite2_demo.maxmind.com\/geoip\/v2.1\/city\/{{ip}}', headers={{'accept': 'application\/vnd.maxmind.com+json'}}, timeout=10)
        response.raise_for_status()
        data = response.json()
        location = data.get('location', {{}})
        latitude = location.get('latitude')
        longitude = location.get('longitude')
        if latitude is None or longitude is None:
            return '\"Missing location data\"'
        kml = f"<?xml version='1.0' encoding='UTF-8'?><kml xmlns='http:\/\/www.opengis.net\/kml\/2.2'><Document><Placemark><name>{{ip}}</name><Point><coordinates>{{longitude}},{{latitude}},0</coordinates></Point></Placemark></Document></kml>"
        return kml
    except requests.exceptions.RequestException as e:
        return f'Error retrieving data: {{e}}'
    except ValueError as e:
        return f'Error parsing JSON data: {{e}}'

def few_shots_prompting__retKML(ip):
    kml = f"<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n<Document>\n<Placemark>\n<name>{ip}</name>\n<Point>\n<coordinates>0,0</coordinates>\n</Point>\n</Placemark>\n</Document>\n</kml>"
    return kml

def cot_prompting__retKML(ip):
    placemark = f'<Placemark><name>{ip}</name><Point><coordinates>{ip},0,0</coordinates></Point></Placemark>'
    kml = f'<kml xmlns="http://www.opengis.net/kml/2.2"><Document>{placemark}</Document></kml>'
    return kml

def fact_check_list__retKML(ip):

    lat, lon = get_lat_lon_from_ip(ip)
    if lat is None or lon is None:
        raise ValueError(f"Could not find latitude and longitude for IP: {ip}")
    kml_template = ""
    kml_content = kml_template.format(lat=lat, lon=lon)
    return kml_content

def not_interactive_mix__retKML(ip):
    import requests
    import validators
    if not validators.ipv4(ip):
        raise ValueError("Invalid IP address")
    url = f'http://{ip}/data.kml'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f'Failed to fetch KML data from {url}: {e}')
    if 'application/vnd.google-earth.kml+xml' not in response.headers['Content-Type']:
        raise ValueError(f"Unexpected content type received from {url}: {response.headers['Content-Type']}")
    return response.text

def interactive_mix__retKML(ipAddress):
    import requests
    import logging
    api_url = "http://ipinfo.io/" + ipAddress + "/json"
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            location_data = response.json().get('loc', None)
            if not location_data or len(location_data.split(',')) != 2:
                raise ValueError("Invalid location data from API")
            lat, lon = map(float, location_data.split(','))
            kml = (
                f'<Placemark>\n'
                f'  <name>Coordinates of {ipAddress}</name>\n'
                f'  <Point>\n'
                f'    <coordinates>{lon},{lat},0</coordinates>\n'
                f'  </Point>\n'
                f'</Placemark>'
            )
            return kml
        except requests.exceptions.RequestException as e:
            logging.error(f"Attempt {retry_count + 1}: Network error - {str(e)}")
        except ValueError as ve:
            logging.error(f"Attempt {retry_count + 1}: Invalid coordinates - {str(ve)}")
        retry_count += 1
    return f'<Placemark>\n  <name>Error: Unable to retrieve coordinates after {max_retries} attempts</name>\n  <description>Network or API response issue</description>\n</Placemark>'

def baseline__retKML(ip):
	return '<kml xmlns="http://www.opengis.net/kml/2.2"><Document></Document></kml>'
