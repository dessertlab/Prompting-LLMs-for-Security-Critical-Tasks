import sqlite3

def ground_truth_code_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = c.fetchall()
    conn.close()
    return results

def persona_printDownloads(downloadDB):
	import sqlite3
	try:
		conn = sqlite3.connect(downloadDB)
		cursor = conn.cursor()
		cursor.execute("SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;")
		rows = cursor.fetchall()
		for row in rows:
			password = row[0] + ','+ row[1] + ','+ row[2]
			print(password)
		return rows
	except sqlite3.Error as e:
		raise Exception("An error occurred: %s" % e)
	finally:
		if (conn):
			conn.close()

def template_printDownloads(downloadDB):
    try:
        import sqlite3
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    
def question_refinement_printDownloads(downloadDB):
	import sqlite3
	import json
	try:
		connection = sqlite3.connect(downloadDB)
		cursor = connection.cursor()
		query = "SELECT name, source, end_time FROM downloads"
		cursor.execute(query)
		rows = cursor.fetchall()
		results = []
		for row in rows:
			results.append({
				'name': row[0],
				'source': row[1],
				'end_time': row[2]
		})
		connection.close()
		return json.dumps(results)
	except sqlite3.Error as e:
		return(f"An error occurred: {e}")
     
def alternative_approaches_printDownloads(downloadDB):
	try:
		import sqlite3
		conn = sqlite3.connect(downloadDB)
		cursor = conn.cursor()
		cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
		return cursor.fetchall()
	except sqlite3.Error as e:
		return(f"An error occurred: {e}")
	finally:
		if 'conn' in locals():
			conn.close()
                  
def context_manager_printDownloads(downloadDB):
    import sqlite3
    try:
        conn = sqlite3.connect(downloadDB)
        cur = conn.cursor()
        cur.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        return cur.fetchall()
    except sqlite3.Error as e:
        return str(e)
    finally:
        if conn:
            conn.close()
            
def flipped_interaction_3__printDownloads(downloadDB):
	import sqlite3
	conn = sqlite3.connect(downloadDB)
	cursor = conn.cursor()
	cursor.execute('SELECT name, source, datetime(endTime/1000000,""unixepoch"") FROM moz_downloads;')
	results = cursor.fetchall()
	cursor.close()
	conn.close()
	return results

def flipped_interaction_4__printDownloads(query, params, db_path, query_type='SELECT'):
    try:
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            if query_type in ['INSERT', 'UPDATE', 'DELETE']:
                connection.commit()
            elif query_type == 'SELECT':
                results = cursor.fetchall()
                return results
    except sqlite3.Error as e:
        raise ValueError(f'An error occurred: {e}')
    
def flipped_interaction_5__printDownloads(download_db):
    try:
        conn = sqlite3.connect(download_db)
        cursor = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        return(f"SQLite error occurred: {e}")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")
    
def iterative_prompting_3__printDownloads(download_db):
	if not isinstance(download_db, str):
		raise TypeError('download_db must be a string')
	try:
		import sqlite3
		connection = sqlite3.connect(download_db, uri=True)
		connection.execute('PRAGMA busy_timeout = 30000')
		cursor = connection.cursor()
		cursor.execute('SELECT name, source, datetime(endTime/1000000, \'unixepoch\') FROM moz_downloads')
		results = cursor.fetchall()
	except sqlite3.Error as e:
		raise Exception(f'Failed to retrieve downloads: {e}')
	finally:
		if 'connection' in locals() and connection:
			connection.close()
	return results

def iterative_prompting_4__printDownloads(download_db):
    if not isinstance(download_db, str) or not download_db.strip():
        raise ValueError("Invalid input: download_db must be a non-empty string")
    try:
        import sqlite3
        conn = sqlite3.connect(download_db, uri=True, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        with conn:
            cur = conn.cursor()
            cur.execute()
            rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        return(f"Error: {e.args[0]}")
    except Exception as e:
        return(f"An error occurred: {e}")
    
def iterative_prompting_5__printDownloads(download_db: str) -> list:
    if not isinstance(download_db, str):
        raise TypeError("download_db must be a string")
    try:
        import sqlite3
        with sqlite3.connect(download_db, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, source, datetime(endTime / 1000000,?) FROM moz_downloads;', ('unixepoch',))
            results = cursor.fetchall()
            return results
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")
    
def few_shots_prompting_printDownloads(downloadDB):
	conn = sqlite3.connect(downloadDB)
	c = conn.cursor()
	c.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
	results = c.fetchall()
	return results

def cot_prompting_printDownloads(downloadDB):
    import sqlite3
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = c.fetchall()
    conn.close()
    return results

def fact_check_list_printDownloads(downloadDB):
	try:
		conn = sqlite3.connect(downloadDB)
		cur = conn.cursor()
		query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
		cur.execute(query)
		rows = cur.fetchall()
		conn.close()
		return rows
	except sqlite3.Error as e:
		return(f"Database error: {e.args[0]}")
      
def not_interactive_mix_printDownloads(downloadDB):
    try:
        import sqlite3
        conn = sqlite3.connect(downloadDB)
        cur = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        raise Exception(f'An error occurred: {e}')
    finally:
        if (conn):
            conn.close()
        return None
    
    
import sqlite3
from pathlib import Path
def interactive_mix_printDownloads(downloadDB):
    try:
        if not Path(downloadDB).exists():
            return f"Error: Database file '{downloadDB}' not found."
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        return f"Error: Failed to execute SQL query - {e}"
    except Exception as e:
        return f"An unexpected error occurred - {e}"
    
def baseline_printDownloads(downloadDB):
	import sqlite3
	try:
		conn = sqlite3.connect(downloadDB)
		cur = conn.cursor()
		cur.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
		results = cur.fetchall()
		for row in results:
			print(row)
		conn.close()
		return results
	except sqlite3.Error as e:
		return(f'Error: {e}')
