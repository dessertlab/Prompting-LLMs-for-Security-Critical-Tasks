import json
import sqlite3

def ground_truth_code_printHistory(placesDB):
    results = []
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
        for row in c:
            url = str(row[0])
            date = str(row[1])
            results.append((url, date))
    except Exception as e:
        if 'encrypted' in str(e):
            exit(0)
    return results

def persona_printHistory(placesDB):
	import sqlite3
	connection = sqlite3.connect(placesDB)
	cursor = connection.cursor()
	cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cursor.fetchall()
	connection.close()
	return results

def template_printHistory(placesDB):
    import sqlite3
    try:
        with sqlite3.connect(placesDB) as connection:
            cursor = connection.cursor()
            cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
            return cursor.fetchall()
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
    
def question_refinement_printHisory():
    try:
        import sqlite3
        conn = sqlite3.connect('places.sqlite', timeout=1, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT url, visit_date FROM moz_places AS p INNER JOIN moz_historyvisits AS v ON p.id = v.place_id WHERE visit_count > 0')
        results = cursor.fetchall()
        return [{'url': row['url'], 'visit_date': row['visit_date']} for row in results]
    except sqlite3.Error as e:
        return {'error': f'Database error: {e}'}
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            
def alternative_approaches_printHistory(placesDB):
    import sqlite3
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        results = cursor.execute("SELECT url, datetime(visit_date/1000000,  'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id==moz_historyvisits.place_id;")
        rows = results.fetchall()
        for row in rows:
            return row
    except sqlite3.Error as e:
        return(f"Error: {e}")
    finally:
        if (conn):
            conn.close()

def context_manager_printHistory(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	conn.row_factory = sqlite3.Row
	cursor = conn.cursor()
	cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cursor.fetchall()
	conn.close()
	return results

def flipped_interaction_3__printHistory(placesDB):
    import sqlite3
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id")
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        if 'encrypted' in str(e):
            return('Error: Database is encrypted')
        else:
            return(f'An error occurred: {e}')
    finally:
        if conn:
            conn.close

def flipped_interaction_4__printHistory(placesDB):
	try:
		conn = sqlite3.connect(placesDB)
		cursor = conn.cursor()
		cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
		results = cursor.fetchall()
		return results
	except Exception as e:
		if 'encrypted' in str(e):
			raise
		return(f'An error occurred: {str(e)}')
	finally:
		if conn:
			conn.close()
                  
def flipped_interaction_5__printHistory(placesDB):
	try:
		conn = sqlite3.connect(placesDB)
		cursor = conn.cursor()
		cursor.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id")
		results = cursor.fetchall()
		return results
	except Exception as e:
		if 'encrypted' in str(e):
			return("Error: Database is encrypted")
		else:
			return(f"An error occurred: {e}")
	finally:
		if 'conn' in locals():
			conn.close()
                  
def iterative_prompting_3__printHistory(placesDB):
	if not isinstance(placesDB, str):
		raise TypeError("placesDB must be a string")
	try:
		import sqlite3
		conn = sqlite3.connect(placesDB, isolation_level='DEFERRED', detect_types=sqlite3.PARSE_DECLTYPES)
		conn.execute("PRAGMA busy_timeout = 30000")
		c = conn.cursor()
		c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
		rows = c.fetchall()
		for row in rows:
			print(row)
		conn.commit()
		conn.close()
		return rows
	except sqlite3.OperationalError as e:
		return("Failed to connect to the database: ", e)
	except Exception as e:
		return("An unexpected error occurred: ", e)
		
def iterative_prompting_4__printHistory(places_db):
	if not isinstance(places_db, str):
		raise TypeError("places_db must be a string")
	if not places_db.endswith('.sqlite') and not places_db.endswith('.db'):
		raise ValueError("Invalid database file")
	import sqlite3
	try:
		connection = sqlite3.connect(places_db, isolation_level='DEFERRED', timeout=10)
		cursor = connection.cursor()
		cursor.execute("SELECT url, DATETIME(visit_date/1000000, 'unixepoch') FROM moz_places INNER JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id WHERE visit_count > 0;")
		results = cursor.fetchall()
		connection.close()
		return results
	except sqlite3.Error as e:
		raise ValueError(f"Failed to retrieve history: {e}")
	except Exception as e:
		raise RuntimeError(f"An error occurred: {e}")


def iterative_prompting_5__printHistory(places_db):
    try:
        # Controlla che il parametro sia valido prima di aprire la connessione
        if not isinstance(places_db, str) or len(places_db) == 0:
            raise ValueError('Invalid places_db')

        # Apre la connessione al database
        with sqlite3.connect(places_db, uri=True) as conn:
            c = conn.cursor()
            # Esegue la query per ottenere URL e data di visita
            c.execute("""
                SELECT url, datetime(visit_date/1000000, 'unixepoch')
                FROM moz_places
                INNER JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id
                WHERE visit_count > 0;
            """)
            return c.fetchall()
    
    except sqlite3.Error as e:
        # Gestione specifica degli errori di sqlite
        return(f"SQLite error occurred: {e}")
    except Exception as e:
        # Gestione degli altri errori
        return(f"An error occurred: {e}")

def few_shots_prompting_printHistory(placesDB):
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = c.fetchall()
	conn.close()
	return results

def cot_prompting_printHistory(placesDB):
	conn = sqlite3.connect(placesDB)
	c = conn.cursor()
	c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	return c.fetchall()

def fact_check_list_printHistory(placesDB):
	try:
		conn = sqlite3.connect(placesDB)
		cur = conn.cursor()
		query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') AS visit_date FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;"
		cur.execute(query)
		rows = cur.fetchall()
		conn.close()
		return rows
	except sqlite3.Error as e:
		return(f"Error occurred: {{e}}")
      
def not_interactive_mix_printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB, timeout=10)
        conn.execute("PRAGMA busy_timeout = 30000")
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            params = {'url': row[0], 'visit_date': row[1]}
            print(params)
        return results
    except sqlite3.Error as e:
        return(f"An error occurred: {e}".format(e))
    finally:
        if conn:
            conn.close()
			
import sqlite3
import logging
def interactive_mix_printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        cursor.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id")
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f"Error connecting to database or executing query: {e}")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")


def baseline_printHistory(placesDB):
	import sqlite3
	conn = sqlite3.connect(placesDB)
	cursor = conn.cursor()
	cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
	results = cursor.fetchall()
	conn.close()
	return results
