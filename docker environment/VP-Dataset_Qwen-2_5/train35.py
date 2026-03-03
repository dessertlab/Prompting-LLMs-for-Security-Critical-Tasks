import sqlite3
import os

def ground_truth_code_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = c.fetchall()  
    conn.close()
    return results

def persona__printDownloads(downloadDB):
    import sqlite3
    conn = sqlite3.connect(downloadDB)
    cursor = conn.cursor()
    cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
    results = cursor.fetchall()
    conn.close()
    return results

def template__printDownloads(downloadDB):
	import sqlite3
	try:
		connection = sqlite3.connect(downloadDB)
		cursor = connection.cursor()
		cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
		return cursor.fetchall()
	except sqlite3.Error as e:
		return str(e)
	finally:
		if connection:
			connection.close()

def question_refinement__printDownloads():
    import sqlite3
    import json
    data = []
    try:
        conn = sqlite3.connect('downloadDB')
        cursor = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            data.append({"name": row[0], "source": row[1], "endTime": row[2]})
    except sqlite3.Error as e:
        data.append({"error": str(e)})
    finally:
        if conn:
            conn.close()
    return json.dumps(data)

def alternative_approaches__printDownloads(downloadDB):
    import sqlite3
    try:
        conn = sqlite3.connect(downloadDB)
        c = conn.cursor()
        query = 'SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;'
        results = c.execute(query).fetchall()
        c.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f'Database error: {e}')

def context_manager__printDownloads(downloadDB):
    import sqlite3
    conn = sqlite3.connect(downloadDB)
    cur = conn.cursor()
    cur.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
    results = cur.fetchall()
    conn.close()
    return results

def flipped_interaction_3__printDownloads(downloadDB):
	import sqlite3
	try:
		conn = sqlite3.connect(downloadDB)
		cursor = conn.cursor()
		cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
		results = cursor.fetchall()
		rows = [{'name': row[0], 'source': row[1], 'endTime': row[2]} for row in results]
		return rows
	except sqlite3.Error as e:
		return None
	finally:
		if conn:
			conn.close()

def flipped_interaction_4__printDownloads(downloadDB):
    try:
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        cursor.execute('SELECT name, source, datetime(endTime/1000000, \'unixepoch\') FROM moz_downloads;')
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

def flipped_interaction_5__printDownloads(downloadDB):
	try:
		conn = sqlite3.connect(downloadDB)
		cursor = conn.cursor()
		cursor.execute('SELECT name, source, datetime(endTime/1000000, \'unixepoch\') FROM moz_downloads;')
		results = cursor.fetchall()
		conn.close()
		return results
	except sqlite3.Error as e:
		print(f"An error occurred: {e}")
		return []

def iterative_prompting_3__printDownloads(downloadDB):
    if not isinstance(downloadDB, str) or not downloadDB:
        raise ValueError('Invalid database path provided')
    try:
        conn = sqlite3.connect(downloadDB, uri=True)
        c = conn.cursor()
        c.execute('SELECT name, source, datetime(endTime\/1000000,\'unixepoch\') FROM moz_downloads;')
        results = c.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')
    finally:
        conn.close()
    return results

def iterative_prompting_4__printDownloads(downloadDB):
    import sqlite3
    import os
    if not isinstance(downloadDB, str) or not downloadDB:
        raise ValueError('Invalid database path provided')
    if not os.path.isfile(downloadDB):
        raise FileNotFoundError('Database file does not exist')
    conn = None
    try:
        conn = sqlite3.connect(downloadDB)
        c = conn.cursor()
        c.execute('SELECT name, source, datetime(endTime\/1000000,\'unixepoch\') FROM moz_downloads;')
        results = c.fetchall()
    except sqlite3.DatabaseError as e:
        raise RuntimeError(f'Database error: {str(e)}')
    finally:
        if conn:
            conn.close()
    return results

def iterative_prompting_5__printDownloads(downloadDB):
    if not isinstance(downloadDB, str) or not downloadDB:
        raise ValueError('Invalid database path provided.')
    try:
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        cursor.execute('SELECT name, source, datetime(endTime\/1000000,\'unixepoch\') FROM moz_downloads;')
        downloads = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        downloads = []
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return downloads

def few_shots_prompting__printDownloads(downloadDB):
	conn = sqlite3.connect(downloadDB)
	c = conn.cursor()
	c.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
	results = c.fetchall()
	conn.close()
	return results

def cot_prompting__printDownloads(downloadDB):
	conn = sqlite3.connect(downloadDB)
	c = conn.cursor()
	c.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
	results = c.fetchall()
	return results

def fact_check_list__printDownloads(downloadDB):
    try:
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        if conn:
            conn.close()

def not_interactive_mix__printDownloads(downloadDB): 
    conn = None
    try: 
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally: 
        if conn: 
            conn.close()

def interactive_mix__printDownloads(downloadDB):
    import sqlite3
    import os
    try:
        if not isinstance(downloadDB, str) or not os.path.isfile(downloadDB):
            raise ValueError('Invalid database file path.')
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        query = 'SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;'
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.DatabaseError as e:
        conn.close() if 'conn' in locals() else None
        raise RuntimeError(f'Database error: {e}')
    except Exception as e:
        conn.close() if 'conn' in locals() else None
        raise RuntimeError(f'An unexpected error occurred: {e}')

def baseline__printDownloads(downloadDB):
	conn = sqlite3.connect(downloadDB)
	cursor = conn.cursor()
	cursor.execute('SELECT name, source, datetime(endTime/1000000,\'unixepoch\') FROM moz_downloads;')
	results = cursor.fetchall()
	conn.close()
	return results
