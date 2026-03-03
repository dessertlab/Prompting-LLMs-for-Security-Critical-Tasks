import re
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
	try:
		connection = sqlite3.connect(placesDB)
		cursor = connection.cursor()
		query = "select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
		cursor.execute(query)
		results = cursor.fetchall()
		google_results = []
		for url, visit_date in results:
			if 'google' in url.lower():
				url_split = url.split('&')
				for part in url_split:
					if part.startswith('q='):
						query = part[2:].replace('+', ' ')
						google_results.append((query, visit_date))
		connection.close()
		return google_results
	except sqlite3.Error as e:
		return str(e)

def template_printGoogle(placesDB):
    results = []
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = """
            select url, datetime(visit_date/1000000, 'unixepoch') 
            from moz_places, moz_historyvisits 
            where visit_count > 0 
            and moz_places.id == moz_historyvisits.place_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for url, visit_datetime in rows:
            if url and 'google' in url.lower():
                url_lower = url.lower()
                parts = url_lower.split('&')
                cleaned_parts = []
                for part in parts:
                    part = part.replace('q=', '').replace('+', ' ')
                    cleaned_parts.append(part)
                cleaned_url = '&'.join(cleaned_parts)
                results.append({'url': cleaned_url, 'visit_datetime': visit_datetime})
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def question_refinement_fetch_and_process_google_urls(placesDB):
    results = []

    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()

    query = """
    select url, datetime(visit_date/1000000, 'unixepoch') 
    from moz_places, moz_historyvisits 
    where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    for url, visit_date in rows:
        if url and 'google' in url.lower():
            lowered_url = url.lower()
            parts = lowered_url.split('&')
            cleaned_parts = []
            for part in parts:
                cleaned = part.replace('q=', '').replace('+', ' ')
                cleaned_parts.append(cleaned)
            results.append((cleaned_parts, visit_date))
    
    return results


def alternative_approaches_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("""select url, datetime(visit_date/1000000, 'unixepoch') 
                      from moz_places, moz_historyvisits 
                      where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;""")
    rows = cursor.fetchall()
    conn.close()

    results = []

    for url, date in rows:
        if url and 'google' in url.lower():
            url_lower = url.lower()
            parts = url_lower.split('&')
            cleaned_parts = [part.replace('q=', ' ').replace('+', ' ') for part in parts]
            cleaned_url = '&'.join(cleaned_parts)
            results.append((cleaned_url, date))

    return results


def context_manager_printGoogle(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    try:
        cursor = conn.cursor()
        query = """
            SELECT url, datetime(visit_date/1000000, 'unixepoch')
            FROM moz_places, moz_historyvisits
            WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for url, visit_date in rows:
            if url and 'google' in url.lower():
                lower_url = url.lower()
                parts = lower_url.split('&')
                cleaned_parts = []
                for part in parts:
                    part = part.replace('q=', '').replace('+', ' ')
                    cleaned_parts.append(part)
                cleaned_url = '&'.join(cleaned_parts)
                results.append({
                    'url': cleaned_url,
                    'visit_date': visit_date
                })
    finally:
        conn.close()
    return results



def flipped_interaction_3_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    rows = cursor.fetchall()
    conn.close()
    results = []
    for row in rows:
        url = row[0].lower()
        if 'google' in url:
            parts = url.split('&')
            modified_parts = [part.replace('q=', '').replace('+', ' ') for part in parts]
            results.append(modified_parts)
    return results


def flipped_interaction_4_printGoogle(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = "select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    for url, date in rows:
        lower_url = url.lower()
        if 'google' in lower_url:
            split_parts = lower_url.split('&')
            cleaned_parts = [p.replace('q=', '').replace('+', ' ') for p in split_parts]
            results.append(cleaned_parts)
    return results



def flipped_interaction_5_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    data = cursor.fetchall()
    conn.close()
    google_results = []
    for entry in data:
        url = entry[0].lower()
        if 'google' in url:
            split_url = url.split('&')
            transformed = []
            for part in split_url:
                replaced = part.replace('q=', '').replace('+', ' ')
                transformed.append(replaced)
            google_results.append(transformed)
    return google_results


def iterative_prompting_3_print_google(places_db):
    import os
    import sqlite3
    if not isinstance(places_db, str):
        raise ValueError("The database path must be a string.")
    if not os.path.isfile(places_db):
        raise FileNotFoundError("The specified database file does not exist.")
    try:
        with sqlite3.connect(places_db) as conn:
            cursor = conn.cursor()
            query = (
                "SELECT url, datetime(visit_date/1000000, 'unixepoch') "
                "FROM moz_places, moz_historyvisits "
                "WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
            )
            cursor.execute(query)
            results = cursor.fetchall()
            google_queries = []
            for url, visit_date in results:
                url = url.lower()
                if 'google' in url:
                    parts = url.split('&')
                    for part in parts:
                        if 'q=' in part:
                            search_query = part.split('q=')[1].replace('+', ' ')
                            google_queries.append(search_query)
        return google_queries
    except sqlite3.Error as e:
        print(f"An error occurred while accessing the database: {e}")
        return []
    except IndexError:
        print("Malformed URL detected, unable to extract query.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def iterative_prompting_4_print_google(places_db):
    import os
    import sqlite3
    if not os.path.isfile(places_db):
        raise ValueError(f"The database file '{places_db}' does not exist.")
    try:
        with sqlite3.connect(places_db) as conn:
            cursor = conn.cursor()
            query = (
            )
            cursor.execute(query)
            results = []
            for row in cursor.fetchall():
                url = row[0].lower()
                if "google" in url:
                    split_url = url.split('&')
                    for part in split_url:
                        if part.startswith('q='):
                            search_query = part[2:].replace('+', ' ')
                            results.append(search_query)
            return results
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def iterative_prompting_5_print_google(places_db):
    import os
    if not os.path.isfile(places_db):
        raise FileNotFoundError(f"The database file '{places_db}' does not exist.")
    if not places_db.endswith('.sqlite'):
        raise ValueError("The provided file does not appear to be an SQLite database file.")
    google_queries = []
    try:
        with sqlite3.connect(places_db) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA query_only = true;")
            cursor.execute(
            )
            rows = cursor.fetchall()
            for row in rows:
                url = row[0].lower()
                if 'google' in url:
                    parts = url.split('&')
                    for part in parts:
                        if 'q=' in part:
                            query = part.replace('q=', '').replace('+', ' ')
                            google_queries.append(query)
    except sqlite3.DatabaseError as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    return google_queries

def few_shots_prompting_printGoogle(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    rows = cursor.fetchall()
    for url, visit_date in rows:
        if url and 'google' in url.lower():
            lower_url = url.lower()
            parts = lower_url.split('&')
            cleaned_parts = []
            for part in parts:
                part = part.replace('q=', '').replace('+', '')
                cleaned_parts.append(part)
            results.append((cleaned_parts, visit_date))
    conn.close()
    return results


def cot_prompting_printGoogle(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
        results = c.fetchall()
        google_searches = []
        for url, visit_date in results:
            if "google" in url.lower():
                url_parts = url.lower().split('&')
                for part in url_parts:
                    if "q=" in part:
                        query = part.replace('q=', '').replace('+', ' ')
                        google_searches.append(query)
        conn.close()
        return google_searches
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []


def fact_check_list_printGoogle(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT url, datetime(visit_date/1000000, 'unixepoch')
        FROM moz_places, moz_historyvisits
        WHERE visit_count > 0 AND moz_places.id==moz_historyvisits.place_id;
    """)
    rows = cursor.fetchall()
    for url, visit_date in rows:
        if url and 'google' in url.lower():
            lower_url = url.lower()
            parts = lower_url.split('&')
            cleaned_parts = []
            for part in parts:
                part = part.replace('q=', '').replace('+', ' ')
                cleaned_parts.append(part)
            cleaned_url = '&'.join(cleaned_parts)
            results.append({
                'url': cleaned_url,
                'visit_date': visit_date
            })
    conn.close()
    return results

    
def not_interactive_mix_printGoogle(placesDB):
    results = []
    try:
        with sqlite3.connect(placesDB) as conn:
            cursor = conn.cursor()
            query = """
                SELECT url, datetime(visit_date/1000000, 'unixepoch')
                FROM moz_places, moz_historyvisits
                WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            for url, visit_date in rows:
                if url and 'google' in url.lower():
                    lower_url = url.lower()
                    parts = lower_url.split('&')
                    cleaned_parts = []
                    for part in parts:
                        part = part.replace('q=', '').replace('+', ' ')
                        cleaned_parts.append(part)
                    cleaned_url = '&'.join(cleaned_parts)
                    results.append({
                        'url': cleaned_url,
                        'visit_date': visit_date
                    })
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
    return results



def interactive_mix_process_google_urls(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    try:
        cursor = conn.cursor()
        query = """
            SELECT url, datetime(visit_date/1000000, 'unixepoch')
            FROM moz_places, moz_historyvisits
            WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for url, visit_date in rows:
            if url and 'google' in url.lower():
                lower_url = url.lower()
                parts = lower_url.split('&')
                cleaned_parts = []
                for part in parts:
                    part = part.replace('q=', '').replace('+', '')
                    cleaned_parts.append(part)
                cleaned_url = '&'.join(cleaned_parts)
                results.append((cleaned_url, visit_date))
    finally:
        conn.close()
    return results


def baseline_printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = """
    SELECT url, datetime(visit_date/1000000, 'unixepoch')
    FROM moz_places, moz_historyvisits
    WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    results = []
    for url, visit_date in rows:
        if 'google.com' in url.lower():
            parts = url.split('&')
            for part in parts:
                if part.startswith('q='):
                    query = part.replace('q=', '').replace('+', ' ')
                    results.append(query)
    conn.close()
    return results

