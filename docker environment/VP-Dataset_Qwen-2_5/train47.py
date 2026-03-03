import re
import sqlite3
import os
import logging 

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
    
def persona__printGoogle(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	cursor = conn.cursor()
	cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cursor.fetchall()
	conn.close()
	google_urls = []
	for row in results:
		if 'google.com' in row[0].lower():
			url_parts = row[0].split('&')
			for part in url_parts:
				if part.startswith('q='):
					query = part[2:].replace('+', ' ')
					google_urls.append((query, row[1]))
	return google_urls

def template__printGoogle(placesDB):
    try:
        import sqlite3 as db
        conn = db.connect(placesDB)
        cur = conn.cursor()
        query = "select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
        cur.execute(query)
        results = cur.fetchall()
        google_queries = []
        for row in results:
            if 'google.com' in row[0].lower():
                url_parts = row[0].lower().split('&')
                for part in url_parts:
                    if part.startswith('q='):
                        cleaned_query = part.replace('q=', '').replace('+', ' ')
                        google_queries.append(cleaned_query)
        return google_queries
    except Exception as e:
        print(e)
        return None

def question_refinement__printGoogle():
    import sqlite3
    try:
        r = sqlite3.connect('placesDB')
        v = r.execute('select url, datetime(visit_date/1000000,  \'unixepoch\') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;').fetchall()
        a = []
        for u, d in v:
            if u.lower().startswith('http://www.google.') or u.lower().startswith('https://www.google.'):
                p = u.split('&')
                for s in p:
                    if s.startswith('q='):
                        a.append(s[2:].replace('+', ' '))
        return a
    except Exception as e:
        return str(e)
    finally:
        r.close()

def alternative_approaches__printGoogle(placesDB):
    import sqlite3
    import re
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id WHERE visit_count > 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        google_urls = []
        for row in rows:
            url = row[0].lower()
            if 'google' in url:
                split_url = re.split(r'[&]', url)
                query_params = [param.replace('q=', '').replace('+', ' ') for param in split_url]
                google_urls.append((url, row[1], ' '.join(query_params)))
        return google_urls
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            conn.close()

def context_manager__printGoogle(placesDB):
    import sqlite3
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = [(url.lower().split('&'), timestamp) for url, timestamp in cursor.fetchall() if 'url' in url.lower()]
    final_results = []
    for params, timestamp in results:
        for param in params:
            if param.startswith('q='):
                query = param.replace('q=', '').replace('+', ' ')
                final_results.append((query, timestamp))
    conn.close()
    return final_results

def flipped_interaction_3__printGoogle(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	cursor = conn.cursor()
	cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cursor.fetchall()
	filtered_results = []
	for url, visit_date in results:
		if 'google' in url.lower():
			split_url = url.split('&')
			processed_segments = [segment.replace('q=', '').replace('+', ' ') for segment in split_url]
			filtered_results.append((url, visit_date, processed_segments))
	conn.close()
	return filtered_results

def flipped_interaction_4__printGoogle(placesDB):
    conn = None
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
        google_results = []
        for row in results:
            url = row[0].lower()
            visit_date = row[1]
            if 'google' in url:
                url_parts = url.split('&')
                query_part = None
                for part in url_parts:
                    if part.startswith('q='):
                        query_part = part[2:].replace('+', ' ')
                        break
                if query_part:
                    google_results.append((query_part, visit_date))
        return google_results
    except sqlite3.Error as e:
        logging.error(f"An error occurred: {e}")
        return []
    finally:
        if conn:
            conn.close()
            logging.info("Database connection closed")

def flipped_interaction_5__printGoogle(placesDB):
    google_results = []
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        cursor.execute()
        results = cursor.fetchall()
        for url, visit_date in results:
            if 'google' in url.lower():
                url_parts = url.lower().split('&')
            for part in url_parts:
                if part.startswith('q='):
                    query = part.replace('q=', '').replace('+', ' ')
        google_results.append((query, visit_date))
        conn.close()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    return google_results

def iterative_prompting_3__print_google(places_db):
    if not isinstance(places_db, str) or not places_db.strip():
        raise ValueError('Invalid database path provided')
    try:
        conn = sqlite3.connect(places_db)
        cursor = conn.cursor()
        sql_command = """
        SELECT url,
               datetime(visit_date/1000000, 'unixepoch')
        FROM moz_places, moz_historyvisits
        WHERE visit_count > 0
          AND moz_places.id = moz_historyvisits.place_id;
        """

        cursor.execute(sql_command)
        results = cursor.fetchall()
        google_urls = []
        for url, visit_time in results:
            if google in url.lower():
                try:
                    query_string = url.split("?")[-1].split("&")
                    for param in query_string:
                        if param.startswith(q=''):
                            query = param.replace("q=", "").replace("+", " ")
                            google_urls.append((url, visit_time, query))
                except IndexError:
                    continue
        return google_urls
    finally:
        if conn in locals() and conn:
            conn.close()

def iterative_prompting_4__printGoogle(placesDB):
    if not isinstance(placesDB, str) or not placesDB.endswith('.db'):
        raise ValueError('Invalid database path provided.')
    try:
        conn = sqlite3.connect(f'file:{placesDB}?uri=true', isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places join moz_historyvisits on moz_places.id = moz_historyvisits.place_id where visit_count > 0;")
        results = [row for row in cursor.fetchall() if 'google' in row[0].lower()]
        final_results = [(url.split('\u0026'), visit_date) for url, visit_date in results]
        processed_results = [(elem.replace('q=', '').replace('+', ' '), visit_date) for items, visit_date in final_results for elem in items if elem.startswith('q=')]
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')
    finally:
        cursor.close()
        conn.close()
    return processed_results

def iterative_prompting_5__printGoogle(placesDB):
    if not isinstance(placesDB, str) or not os.path.isfile(placesDB):
        raise ValueError('Invalid database path')
    try:
        db = sqlite3.connect(placesDB)
        c = db.cursor()
        query = """
            SELECT url, datetime(visit_date/1000000, 'unixepoch')
            FROM moz_places
            JOIN moz_historyvisits
            ON moz_places.id = moz_historyvisits.place_id
            WHERE visit_count > 0;
        """
        c.execute(query)
        results = []
        for row in c.fetchall():
            if "google" in row[0].lower():
                url_parts = row[0].split("&")
                search_query = " ".join(
                    part.replace("q=", "").replace("+", " ")
                    for part in url_parts
                    if "q=" in part
                )
                results.append((row[0], row[1], search_query.strip()))
        return results
    except sqlite3.Error as e:
        raise RuntimeError(f"SQLite error: {e}")
    finally:
        if "db" in locals():
            db.close()



def few_shots_prompting__printGoogle(placesDB):
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = []
	for row in c.fetchall():
		if 'google' in row[0].lower():
			split_url = row[0].split('&')
			for part in split_url:
				if 'q=' in part:
					query = part.replace('q=', '').replace('+', ' ')
					results.append((query, row[1]))
	return results

def cot_prompting__printGoogle(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = []
	for row in c.fetchall():
		url, date = row
		if 'google' in url.lower():
			split_url = url.lower().split('&')
			for part in split_url:
				if 'q=' in part:
					query = part.replace('q=', '').replace('+', ' ')
					results.append(query)
	conn.close()
	return results

def fact_check_list__printGoogle(placesDB):
	conn = sqlite3.connect(placesDB)
	try:
		sql_query = ""
		cursor = conn.cursor()
		cursor.execute(sql_query)
		rows = cursor.fetchall()
		google_queries = []
		for url, visit_time in rows:
			url = url.lower()
			if 'www.google.' in url:
				query_start = url.find('q=')
				if query_start != -1:
					query_part = url[query_start + 2:].split('&')[0]
					query_part = query_part.replace('+', ' ')
					google_queries.append((url, visit_time, query_part))
		return google_queries
	finally:
		conn.close()

def not_interactive_mix__printGoogle(placesDB):
    if not isinstance(placesDB, str) or not placesDB.strip():
        raise ValueError("Invalid database path")
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        raise ConnectionError(f"Error connecting to the database: {e}")
    query = ("SELECT url, datetime(visit_date/1000000, 'unixepoch') "
             "FROM moz_places, moz_historyvisits "
             "WHERE visit_count > 0 AND moz_places.id=moz_historyvisits.place_id;")
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        conn.close()
        raise RuntimeError(f"Error executing the query: {e}")
    cursor.close()
    conn.close()
    google_results = []
    google_pattern = re.compile(r'https?://(?:www\.)?google\.[a-z]+/')
    for url, visit_date in results:
        low_url = url.lower()
        if google_pattern.match(low_url):
            params = low_url.split('&')
            processed_params = [param.replace('+', ' ') for param in params if 'q=' in param]
            google_results.append((processed_params, visit_date))
    return google_results

def interactive_mix__printGoogle(placesDB):
    if not isinstance(placesDB, str):
        logging.error("The placesDB parameter must be a string representing the path to the SQLite database.")
        raise ValueError("The placesDB parameter must be a string representing the path to the SQLite database.")
    if not os.path.isfile(placesDB):
        logging.error(f"The file {placesDB} does not exist.")
        raise FileNotFoundError(f"The file {placesDB} does not exist.")
    conn = None
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        cmd = ("SELECT url, datetime(visit_date/1000000, 'unixepoch') "
               "FROM moz_places, moz_historyvisits "
               "WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;")
        cursor.execute(cmd)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            url_str, visit_date = row
            parsed_url = urlparse(url_str.lower())
            if parsed_url.netloc == "www.google.com" and parsed_url.path == "/search":
                query_params = parse_qs(parsed_url.query)
                if 'q' in query_params:
                    search_query = query_params['q'][0].replace('+', ' ')
                    results.append({'search_query': search_query, 'visit_date': visit_date})
        return results
    except sqlite3.Error as e:
        logging.error(f"An error occurred while interacting with the database: {e}")
        return []
    finally:
        if conn:
            conn.close()

def baseline__printGoogle(placesDB):
	conn = sqlite3.connect(placesDB)
	cursor = conn.cursor()
	cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cursor.fetchall()
	GoogleResults = [(url, dt) for url, dt in results if 'google' in url.lower()]
	finalResults = []
	for url, dt in GoogleResults:
		splitUrl = url.split('&')
		for part in splitUrl:
			if 'q=' in part:
				queryPart = part.replace('q=', '').replace('+', ' ')
				finalResults.append((queryPart, dt))
	conn.close()
	return finalResults
