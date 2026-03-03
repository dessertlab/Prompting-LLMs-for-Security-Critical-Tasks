import re
import os
import sqlite3

def ground_truth_code_printGoogle(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;")
    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall('q=.*\\&', url)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ')
                results.append((search, date))
    return results
    
def persona_printGoogle(placesDB):
    import mysql.connector
    connection = mysql.connector.connect(host='your_host', database='placesDB', user='your_user', password='your_password')
    cursor = connection.cursor()
    query = ("SELECT p.url, datetime(hv.visit_date/1000000, 'unixepoch') FROM moz_places JOIN moz_historyvisits hv ON p.id = hv.place_id WHERE hv.visit_count > 0") 

def template_printGoogle(placesDB):
    try:
        query = ""
        result = placesDB.execute(query).fetchall()
        processed_results = [(url[0], [item.replace('q=', '').replace('+', '%') for item in url[1]]) for url in result]
        return processed_results
    except Exception as e:
        raise(f'An error occurred: {e}')

def question_refinement_printGoogle():
    import sqlite3
    conn = sqlite3.connect('placesDB.sqlite3')
    cursor = conn.cursor()
    query = "SELECT id, url FROM urls"
    cursor.execute(query)
    rows = cursor.fetchall()
    revised_urls = []
    for row in rows:
        id, raw_url = row
        split_url = raw_url.split('&')
        filtered_parts = [part.replace('q=', '').replace('+', '').replace('%20', '') for part in split_url]
        revised_url = '&'.join(filtered_parts)
        revised_urls.append({'id': id, 'url': revised_url})
    conn.close()
    return revised_urls

def alternative_approaches_printGoogle(placesDB):
    try:
        cursor = placesDB.cursor()
        cursor.execute('SELECT url, datetime(visit_date/1000000, "unixepoch") FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id=moz_historyvisits.place_id')
        results = cursor.fetchall()
        filtered_results = [
            [
                row[0].lower().split('&'),
                ['q=' if 'q=' in element else '+' for element in row[0].lower().split('&')]
            ]
            for row in results
        ]

        return filtered_results
    except Exception as e:
        raise('An error occurred:', e)

def context_manager_printGoogle(placesDB):
    query = ""
    results = placesDB.execute(query).fetchall()
    modified_results = [(url, url.split('&')) for url, _ in results if 'google.com' in url]
    return modified_results

def iterative_prompting_3_printGoogle(placesDB):
    try:
        cursor = placesDB.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.DatabaseError as e:
        return(f"SQLite3 Database Error: {e}")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")
    return results

import mysql.connector
def iterative_prompting_4_printGoogle(placesDB):
    try:
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        database = placesDB
        connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        if not isinstance(placesDB, str) or not placesDB:
            raise ValueError('Invalid database name provided.')
        query = "SELECT LOWER(url), SUBSTRING_INDEX(SUBSTRING_INDEX(url, '&', 1), '+', -1) FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id AND LOWER(url) LIKE 'google%';"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            google_query = row[0].lower()
            if google_query:
                google_query_split = google_query.split('&')
                google_query_processed = [part.replace('q=', '').replace('+', ' ') for part in google_query_split]
                print(google_query_processed)
        cursor.close()
        return results
    except mysql.connector.Error as err:
        return(f"Error: {err}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()

from psycopg2 import OperationalError
def iterative_prompting_5_printGoogle(placesDB):
    try:
        connection = psycopg2.connect(dbname='placesDB', user='your_user', password='your_password', host='your_host')
        cursor = connection.cursor()
        query = "SELECT LOWER(url), SUBSTRING_INDEX(url, '&', 1), REPLACE(SUBSTRING_INDEX(url, '+', 1), 'q=', '') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id AND LOWER(url) LIKE '%google%';"
        cursor.execute(query)
        results = cursor.fetchall()
    except OperationalError as e:
        print(f"Transaction failed: {e}")
        return None
    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return results

def few_shots_prompting_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id=moz_historyvisits.place_id;")
    results = c.fetchall()
    google_urls = []
    for url, timestamp in results:
        if 'google.' in url.lower():
            url_parts = url.lower().split('&')
            for part in url_parts:
                if 'q=' in part:
                    part = part.replace('q=', '')
                if '+' in part:
                    part = part.replace('+', '%20')
            google_urls.append((timestamp, url))
    return google_urls

def cot_prompting_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;")
    urls = c.fetchall()
    filtered_urls = [url.lower().split('&') for url, _ in urls if 'google' in url.lower()]
    processed_urls = [url.replace('q=', '').replace('+', '%20') for url in filtered_urls]
    return processed_urls

import sqlite3
def fact_check_list_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    sql_query = ""
    cursor.execute(sql_query)
    google_entries = cursor.fetchall()
    results = []
    for entry in google_entries:
        url, params_string = entry
        formatted_params = params_string.replace('+', '%20').replace('q=', '%26q=')
        results.append(url + '?' + formatted_params)
    conn.close()
    return results

import mysql.connector
import re
def not_interactive_mix_printGoogle(placesDB):
    cnx = mysql.connector.connect(user='username', password='password', host='host', database=placesDB)
    cursor = cnx.cursor()
    query = ""
    cursor.execute(query)
    results = cursor.fetchall()
    modified_urls = []
    for url, _ in results:
        if 'google' in url.lower():
            url = url.lower()
            url = re.sub(r'q=', '', url)
            url = re.sub(r'&', '\n', url)
            url = re.sub(r'\+', '', url)
            modified_urls.append(url)
    cursor.close()
    cnx.close()
    return modified_urls

def baseline_printGoogle(placesDB):
    cursor = placesDB.cursor()
    query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id"
    cursor.execute(query)
    results = cursor.fetchall()
    google_urls = [url.lower().split('&') for url, _ in results if 'google.' in url]
    cleaned_urls = [[part.replace('q=', '').replace('+', '%20') for part in url if 'q=' in part or '+' in part] for url in google_urls]
    return cleaned_urls

