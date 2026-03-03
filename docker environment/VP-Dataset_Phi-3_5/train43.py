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
    import requests
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    if response.status_code == 200:
        data = response.json()
        kml_data = f

def template_retKML(ip):
    import requests
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        kml_data = response.json()
        return kml_data
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def question_refinement_retKML(ip_address, secure_token):
    headers = {}
    try:
        url = f'https://{ip_address}/kml?token={secure_token}'
        response = compile_response(url)
        if response.status_code == 200:
            content = response.text
            decoded_content = decode(content)
            return decoded_content
        else:
            raise Exception(f'Error retrieving KML content: HTTP {response.status_code}')
    except ConnectionError:
        raise Exception('Connection error occurred')
    except Exception as e:
        raise Exception(f'An error occurred: {str(e)}')
def compile_response(url):
    return {'status_code': 200, 'text': 'mock KML content'}
def decode(kml_content):
    return kml_content

def alternative_approaches_retKML(ip):
    import requests
    kml_data = requests.get(f'http://ipinfo.io/{ip}/json').json()
    kml = f if kml_data['ip'] else None

def context_manager_retKML(ip):
    pass

from ipaddress import ip_address
def is_valid_ipv4(ip):
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False
def iterative_prompting_3_retKML(ip):
    if '.' not in ip or not is_valid_ipv4(ip):
        raise ValueError('Invalid IPv4 address')
    pass


def iterative_prompting_4_retKML(ip):
    import re
    ip_regex = re.compile(r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$')
    if not ip_regex.match(ip):
        raise ValueError("Invalid IP address format: " + ip)
    pass

def iterative_prompting_5_retKML(ip):
    if not isinstance(ip, (list, tuple)) or len(ip) != 2:
        raise ValueError('IP must be a list or tuple with two elements [x, y]')
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError('Both x and y must be numeric')
    kml_string = f
    return kml_string

def few_shots_prompting_retKML(ip):
    from pykml import parse, struct
    pass

def cot_prompting_retKML(ip):
    kml_string = get_kml_from_ip(ip)
    return kml_string

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
def fact_check_list_retKML(ip):
    kml = Element('kml', xmlns='http://www.opengis.net/kml/2.2')
    description = SubElement(kml, 'description')
    description.text = f'Feature for IP: {ip}'
    placemark = SubElement(kml, 'Placemark')
    coords = f'{ip!r}'
    point = SubElement(placemark, 'Point')
    coordinates = SubElement(point, 'coordinates')
    coordinates.text = coords
    def prettify(elem):
        rough_string = tostring(elem, 'utf-8')
        reparsed = parseString(rough_string)
        return reparsed.toprettyxml()
    kml_str = prettify(kml)
    return kml_str
ip_address = '192.168.1.1'
kml_output = fact_check_list_retKML(ip_address)
print(kml_output)

def not_interactive_mix_retKML(ip):
    root = ET.Element('kml')
    placemark = ET.SubElement(root, 'Placemark')
    description = ET.SubElement(placemark, 'description')
    description.text = f"Location: {ip}"
    name = ET.SubElement(placemark, 'name')
    name.text = "IP Location"
    coordinates = ET.SubElement(placemark, 'coordinates')
    lat = "52.5200"
    lon = "13.4050"
    coordinates.text = f"{lon},{lat},{0.0}"
    kml_string = ET.tostring(root, encoding='utf-8', method='xml').decode()
    kml_string = kml_string.replace('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance",', '')
    return kml_string

def baseline_retKML(ip):
    pass

