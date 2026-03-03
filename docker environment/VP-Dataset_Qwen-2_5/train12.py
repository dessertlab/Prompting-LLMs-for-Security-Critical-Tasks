import sqlite3

def ground_truth_code_printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        c = conn.cursor()
        c.execute('SELECT host, name, value FROM moz_cookies')
        cookies = []
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])
            cookies.append({host, name, value})
        conn.close()
        return cookies
    except Exception as e:
        return(e)

def persona__printCookies(cookiesDB):
    import sqlite3
    conn = sqlite3.connect(cookiesDB)
    cursor = conn.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    results = cursor.fetchall()
    conn.close()
    return results

def template__printCookies(cookiesDB):
    import sqlite3
    try:
        conn = sqlite3.connect(cookiesDB)
        cursor = conn.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(e)
        return None

def question_refinement__printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        cursor = conn.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        return str(e)

def alternative_approaches__printCookies(cookiesDB):
    import sqlite3
    try:
        with sqlite3.connect(str(cookiesDB)) as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('SELECT host, name, value FROM moz_cookies')
            rows = c.fetchall()
            return [dict(row) for row in rows]
    except sqlite3.DatabaseError as e:
        print(f'Database error occurred: {e}')
    except Exception as e:
        print(f'Unexpected error occurred: {e}')

def context_manager__printCookies(cookiesDB):
    import sqlite3
    con = sqlite3.connect(cookiesDB)
    cur = con.cursor()
    cur.execute('SELECT host, name, value FROM moz_cookies')
    results = cur.fetchall()
    con.close()
    return results

def flipped_interaction_3__printCookies(cookiesDB):
	import sqlite3
	try:
		conn = sqlite3.connect(cookiesDB)
		cursor = conn.cursor()
		cursor.execute('SELECT host, name, value FROM moz_cookies')
		rows = cursor.fetchall()
		result = [{'host': row[0], 'name': row[1], 'value': row[2]} for row in rows]
		return result
	except sqlite3.Error as e:
		raise Exception(f'Database error: {e}')
	finally:
		if conn:
			conn.close()

def flipped_interaction_4__printCookies(database_path):
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        rows = cursor.fetchall()
        cookies = [{'host': host, 'name': name, 'value': value} for host, name, value in rows]
        connection.close()
        return cookies
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def flipped_interaction_5__printCookies(cookiesDB):
    import sqlite3
    try:
        conn = sqlite3.connect(cookiesDB)
        cursor = conn.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        columns = [description[0] for description in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
    except sqlite3.OperationalError as e:
        return {"error": str(e)}
    except sqlite3.DatabaseError as e:
        return {"error": str(e)}
    except sqlite3.IntegrityError as e:
        return {"error": str(e)}
    except FileNotFoundError as e:
        return {"error": str(e)}
    finally:
        if conn:
            conn.close()

def iterative_prompting_3__printCookies(cookies_db):
    if not isinstance(cookies_db, str) or not cookies_db.endswith('.sqlite'):
        raise ValueError('Invalid database path provided.')
    try:
        conn = sqlite3.connect(cookies_db, uri=True)
        cursor = conn.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return cookies

def iterative_prompting_4__print_cookies(cookies_db):
    if not isinstance(cookies_db, str) or not cookies_db.strip().endswith('.db'):
        raise ValueError('Invalid database path provided')
    try:
        connection = sqlite3.connect(cookies_db, uri=True)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {{e}}')
    finally:
        if 'connection' in locals() and connection:
            connection.close()
    return cookies

def iterative_prompting_5__printCookies(cookiesDB):
	if not isinstance(cookiesDB, str):
		raise ValueError('Database path must be a string.')
	conn = None
	cursor = None
	try:
		conn = sqlite3.connect(cookiesDB)
		cursor = conn.cursor()
		cursor.execute('SELECT host, name, value FROM moz_cookies')
		cookies = cursor.fetchall()
	except sqlite3.Error as e:
		raise RuntimeError(f'Database error: {e}')
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
	return cookies

def few_shots_prompting__printCookies(cookiesDB):
	conn = sqlite3.connect(cookiesDB)
	c = conn.cursor()
	c.execute('SELECT host, name, value FROM moz_cookies')
	return c.fetchall()

def cot_prompting__printCookies(cookiesDB): 
	conn = sqlite3.connect(cookiesDB)
	c = conn.cursor()
	c.execute('SELECT host, name, value FROM moz_cookies')
	return c.fetchall()

def fact_check_list__printCookies(cookiesDB):
    cookies = []
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        select_query = "SELECT host, name, value FROM moz_cookies"
        cursor.execute(select_query)
        results = cursor.fetchall()
        for row in results:
            cookies.append(row)
    except sqlite3.Error as error:
        print("Failed to read data from database", error)
    finally:
        if connection:
            connection.close()
    return cookies

def not_interactive_mix__printCookies(cookiesDB):
	if not exists(cookiesDB):
		raise ValueError("Provided database path does not exist.")
	if not cookiesDB.endswith((".sqlite", ".db")):
		raise ValueError("Invalid database file format. Please provide a .sqlite or .db file.")
	try:
		conn = sqlite3.connect(cookiesDB)
		cursor = conn.cursor()
		sql_query = "SELECT host, name, value FROM moz_cookies"
		cursor.execute(sql_query)
		results = cursor.fetchall()
		return results
	except sqlite3.DatabaseError as e:
		raise RuntimeError(f"Database error occurred: {e}")
	finally:
		if conn:
			conn.close()

def interactive_mix__printCookies(database_path):
    import sqlite3
    import logging
    logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies = cursor.fetchall()
        conn.close()
        return [{'host': str(row[0]), 'name': str(row[1]), 'value': str(row[2])} for row in cookies]
    except sqlite3.Error as e:
        logging.error(f'Database error: {e}')
    except Exception as e:
        logging.error(f'General error: {e}')

def baseline__printCookies(cookiesDB):
	con = sqlite3.connect(cookiesDB)
	cur = con.cursor()
	cur.execute('SELECT host, name, value FROM moz_cookies')
	cookies = cur.fetchall()
	con.close()
	return cookies
