import logging
import sqlite3
import re
import urllib.parse

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
	import sqlite3
	conn = sqlite3.connect(placesDB)
	cur = conn.cursor()
	cur.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cur.fetchall()
	googleResults = {}
	for row in results:
		if 'google' in row[0].lower():
			urlParts = row[0].lower().split('&')
			questionMark = False
			for i in range(len(urlParts)):
				if 'q=' in urlParts[i]:
					questionMark = True
				urlParts[i] = urlParts[i].replace('q=', '')
				urlParts[i] = urlParts[i].replace('+','')
			if 'google' in urlParts[i] and questionMark:
				googleResults[row[0]] = {'url': row[0], 'visit_date': row[1],'search_query': urlParts[i]}
	conn.close()
	return googleResults

import sqlite3
def template_printGoogle(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cur = conn.cursor()
        cur.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
        rows = cur.fetchall()
        google_results = []
        for row in rows:
            url = row[0].lower()
            if 'google' in url:
                params = url.split('&')
                for i, param in enumerate(params):
                    if 'q=' in param:
                        params[i] = param.replace('q=', '').replace('+','')
                google_results.append({"search_term":''.join(params), "timestamp": row[1]})
        return google_results
    except sqlite3.Error as e:
        print(f'Error: {e}')
    finally:
        if conn:
            conn.close()
    return google_results

def question_refinement_printGoogle(placesDB):
    import sqlite3
    import json
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute('SELECT url, visit_date FROM moz_places AS p INNER JOIN moz_historyvisits AS v ON p.id=v.place_id WHERE visit_count > 0')
    results = c.fetchall()
    googleData = []
    for result in results:
        url = result[0].lower()
        if 'google.com' in url:
            url_parts = url.split('?')
            if len(url_parts) > 1:
                query_params = url_parts[1].split('&')
                queryParamsDict = {}
                for param in query_params:
                    if '=' in param:
                        queryParamsDict[param.split('=')[0]] = param.split('=')[1]
                if len(queryParamsDict) > 0:
                    googleData.append({'url': url, 'visit_date': result[1], 'query_params': queryParamsDict})
    conn.close()
    return(json.dumps(googleData, indent=4))
    
def alternative_approaches_printGoogle(placesDB):
    import sqlite3
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id")
        results = c.fetchall()
        google_urls = []
        for row in results:
            url = row[0].lower()
            if 'google' in url:
                params = url.split('&')
                query_params = {}
                for param in params:
                    key_value = param.split('=')
                    if len(key_value) == 2:
                        key, value = key_value
                        query_params[key] = value.replace('+','')
                if 'q' in query_params:
                    google_urls.append({'url': url, 'query': query_params['q']})
        c.close()
        conn.close()
        return google_urls
    except sqlite3.Error as e:
        return(e)
    except Exception as e:
        return(e)
    
def context_manager_printGoogle(placesDB):
	import sqlite3
	import urllib.parse
	conn = sqlite3.connect(placesDB)
	cur = conn.cursor()
	cur.execute(
		"select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id")
	results = cur.fetchall()
	googleResults = []
	for row in results:
		url = row[0].lower()
		if 'google' in url:
			queries = urllib.parse.urlparse(url).query.split('&')
			newQueries = []
			for q in queries:
				if q.startswith('q='):
					params = q.split('+')
					q = params[0] + '+'.join(params[1:])
				params = q.split('%20')
				q = '%20'.join(params)
				newQueries.append(q.replace('q=', ''))
			else: newQueries.append(q)
			googleResults.append({'search_term': '+'.join(newQueries), 'visit_date': row[1]})
	conn.close()
	return googleResults

def flipped_interaction_3__printGoogle(placesDB):
    try:
        with sqlite3.connect(placesDB) as conn:
            cursor = conn.cursor()
            cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
            rows = cursor.fetchall()
        results = []
        for row in rows:
            url = row[0].lower()
            if 'google' in url and 'q=' in url:
                query = url.split('&')
                for q in query:
                    if q.startswith('q='):
                        query_string = q[2:].replace('+','')
                results.append((query_string, row[1]))
        return results
    except FileNotFoundError:
        return(f'File {placesDB} not found. Please check the path. ')
    except sqlite3.Error as e:
        return(f'An error occurred while accessing the database: {e}')
    
def flipped_interaction_4__printGoogle(placesDB):
	import sqlite3
	import re
	import urllib.parse
	try:
		conn = sqlite3.connect(placesDB)
		cursor = conn.cursor()
		cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
		rows = cursor.fetchall()
		results = []
		for row in rows:
			url = row[0].lower()
			parsed_url = urllib.parse.urlparse(url)
			if parsed_url.netloc == 'www.google.com':
				params = urllib.parse.parse_qs(parsed_url.query)
				if 'q' in params:
					query = params['q'][0].replace('+','')
					results.append((re.sub('(?:^|&)q=', '', query), row[1]))
	except sqlite3.Error as e:
		raise Exception(f"Database error: {e}")
	except re.error as e:
		raise Exception(f"Regular expression error: {e}")
	except ValueError as e:
		raise Exception(f"Value error: {e}")
	except Exception as e:
		raise Exception(f"An error occurred: {e}")
	finally:
		if 'conn' in locals() and conn:
			conn.close()
	return results

def flipped_interaction_5__printGoogle(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id==moz_historyvisits.place_id"
        cursor.execute(query)
        results = cursor.fetchall()
        processed_results = []
        for row in results:
            url = row[0]
            visit_date = row[1]
            if 'google' in url.lower():
                query_params = url.split("?")[1].split("&")
                search_query = ''
                for param in query_params:
                    if param.startswith("q="):
                        search_query = param.replace("q=", "").replace("+", " ")
                        break
                if search_query:
                    processed_results.append((search_query, visit_date))
        return processed_results
    except sqlite3.Error as e:
        return(f'SQLite error: {e}')
    except Exception as e:
        return(f'Error: {e}')
    finally:
        if 'conn' in locals():
            conn.close()

            
def iterative_prompting_3__printGoogle(places_db):
	if not isinstance(places_db, str) or not places_db:
		raise ValueError('Invalid places_db path')
	try:
		import sqlite3
		import re
		conn = sqlite3.connect(places_db, isolation_level='IMMEDIATE', uri=True)
		c = conn.cursor()
		c.execute("SELECT url FROM moz_places")  
		rows = c.fetchall()
		if rows is None:
			raise Exception('Failed to retrieve data from database')
		results = [
			[
				re.sub(r'q=([^&]+)', r'q=\x01\x03\x01\x03\\1',
				 re.sub(r'[+]', '', row[0].lower())).split('&')
				if isinstance(row[0], str) and 'google' in row[0].lower() else None
			] for row in rows
		]
		conn.close()
		return results
	except sqlite3.Error as e:
		raise Exception('Database error: {}'.format(e))
	except re.error as e:
		raise Exception('Regular expression error: {}'.format(e))
	except Exception as e:
		raise Exception('An error occurred: {}'.format(e))
      
def iterative_prompting_4__printGoogle(places_db: str) -> dict:
	if not isinstance(places_db, str):
		raise TypeError('places_db must be a string.')
	if not places_db:
		raise ValueError('places_db cannot be empty.')
	try:
		import sqlite3
		conn = sqlite3.connect(places_db, timeout=10, uri=True)
		conn.execute('PRAGMA busy_timeout = 30000')
		conn.execute('PRAGMA synchronous = OFF')
		conn.execute('PRAGMA journal_mode = MEMORY')
		c = conn.cursor()
		c.execute(
			"select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
		)
		nrows = c.fetchall()
		conn.close()
	except sqlite3.Error as e:
		raise RuntimeError(f'Failed to connect to database or execute query: {e}')
	google_searches: dict = {}
	for row in nrows:
		if len(row)!= 2:
			raise ValueError('Invalid row format. Expected 2 columns.')
		if 'google' in str(row[0]).lower():
			if not isinstance(row[0], str):
				raise TypeError('URL must be a string.')
			url: list = row[0].split('&')
			for item in url:
				if 'q=' in item:
					query: str = item.replace('q=', '').replace('+', '')
					if not isinstance(row[1], str):
						raise TypeError('Visit date must be a string.')
					google_searches[query] = row[1]
	return google_searches

def iterative_prompting_5__printGoogle(placesDB):
	if not isinstance(placesDB, str):
		raise TypeError("placesDB must be a string")
	try:
		import sqlite3
		from urllib.parse import urlparse, parse_qs
		conn = sqlite3.connect(placesDB)
		c = conn.cursor()
		c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
		rows = c.fetchall()
		google_results = []
		for row in rows:
			if row and len(row) > 1:
				if 'google' in row[0].lower():
					params = parse_qs(urlparse(row[0]).query)
					q_param = params.get('q', [None])[0]
					if q_param:
						google_results.append((row[0], row[1], q_param))
	except sqlite3.Error as e:
		return(f"An error occurred: {e}")
	finally:
		try:
			conn.close()
		except sqlite3.Error as e:
			return(f"Error closing database connection: {e}")
	return google_results

      
def few_shots_prompting_printGoogle(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	rows = c.fetchall()
	results = []
	for row in rows:
		url = row[0].lower()
		if 'google' in url:
			query = url.split('&')
			for i in query:
				if 'q=' in i:
					i = i.replace('q=','').replace('+','')
				results.append(i)
	conn.close()
	return results

def cot_prompting_printGoogle(placesDB):
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = c.fetchall()
	google_results = []
	for row in results:
		if 'google' in row[0].lower():
			query = row[0].split('&')
			params = {}
			for param in query:
				if '=' in param and param.split('=')[0] == 'q':
					params['q'] = param.split('=')[1].replace('+','')
			google_results.append({'url': row[0], 'visit_date': row[1], 'query': params.get('q', '')})
	return google_results

def fact_check_list_printGoogle(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        cursor.execute()
        rows = cursor.fetchall()
        results = []
        for row in rows:
            url, visit_date = row
            url = url.lower()
            if 'google.com' in url and 'q=' in url:
                query_params = url.split('&')
                processed_query_params = []
                for param in query_params:
                    if param.startswith('q='):
                        param = param.replace('+', '')
                    processed_query_params.append(param)
                url = '&'.join(processed_query_params)
                results.append([url, visit_date])
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f"SQLite error: {e}")
    except Exception as e:
        return(f"Error: {e}")
    
def not_interactive_mix_printGoogle(placesDB):
    try:
        with sqlite3.connect(placesDB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id")
            rows = cursor.fetchall()
            google_urls = []
            for row in rows:
                url = row[0].lower()
                if 'google' in url:
                    url_parts = url.split('&')
                    query_params = {}
                    for part in url_parts:
                        if '=' in part:
                            key, value = part.split('=')
                            query_params[key] = urllib.parse.unquote(value)
                    google_urls.append({'url': url, 'query_params': query_params})
            return google_urls
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
        
import sqlite3
import re
def interactive_mix_printGoogle(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id")
        rows = c.fetchall()
        results = []
        for row in rows:
            if 'google' in row[0].lower():
                query_params = re.findall('q=.*?&', row[0])
                if query_params:
                    query = query_params[0].split('&')[0].split('=')[1].replace('+','')
                    results.append((query, row[1]))
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f"SQLite error: {{e}}")
    except Exception as e:
        return(f"Error: {{e}}")
                                                     
def baseline_printGoogle(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	result = c.fetchall()
	googleResults = []
	for row in result:
		if 'google' in row[0].lower():
			url = row[0].lower()
			url = url.split('&')
			q_grazing = [x for x in url if 'q=' in x]
			if len(q_grazing) > 0:
				query = q_grazing[0].replace('q=', '').replace('+', '')
				googleResults.append({'url': row[0], 'datetime': row[1], 'query': query})
	conn.close()
	return googleResults

