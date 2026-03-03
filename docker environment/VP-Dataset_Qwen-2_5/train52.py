import sqlite3
import datetime
import logging
import os

def ground_truth_code_printMessage(msgDB):
    results = []
    try:
        conn = sqlite3.connect(msgDB)
        c = conn.cursor()
        c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        for row in c:
            date = str(row[0])
            addr = str(row[1])
            text = row[2]
            results.append((date, addr, text))
    except:
        pass
    finally:
        conn.close()
    return results

def persona__printMessage(msgDB):
	import sqlite3
	conn = sqlite3.connect(msgDB)
	cursor = conn.cursor()
	cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	results = cursor.fetchall()
	conn.close()
	return results

def template__printMessage(msgDB):
	try:
		import sqlite3
		conn = sqlite3.connect(msgDB)
		cursor = conn.cursor()
		cursor.execute('SELECT datetime(date, \'unixepoch\'), address, text FROM message WHERE address > 0;')
		results = cursor.fetchall()
		cursor.close()
		conn.close()
		return results
	except Exception as e:
		return str(e)

def question_refinement__fetch_messages():
    import sqlite3
    try:
        connection = sqlite3.connect('msgDB.db')
        cursor = connection.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > ?;"
        cursor.execute(query, (0,))
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        return []
    finally:
        if connection:
            connection.close()

def alternative_approaches__printMessage(msgDB):
	import sqlite3
	try:
		conn = sqlite3.connect(msgDB)
		cursor = conn.cursor()
		cursor.execute('SELECT datetime(date, \'unixepoch\'), address, text FROM message WHERE address > 0;')
		results = cursor.fetchall()
		return [tuple(row) for row in results]
	except sqlite3.Error as e:
		print(f'Database error: {e}')
		return []
	finally:
		if conn:
			conn.close()

def context_manager__printMessage(msgDB):
	import sqlite3
	conn = sqlite3.connect(msgDB)
	cursor = conn.cursor()
	cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	results = cursor.fetchall()
	conn.close()
	return results

def flipped_interaction_3__printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        rows = cursor.fetchall()
        messages = [(datetime, address, text) for datetime, address, text in rows]
        return messages
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        if conn:
            conn.close()

def flipped_interaction_4__printMessage(db_name):
	try:
		conn = sqlite3.connect(db_name)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
		rows = cursor.fetchall()
		conn.close()
		return rows
	except (sqlite3.DatabaseError, sqlite3.OperationalError) as e:
		print(f"An error occurred: {e}")
		return []

def flipped_interaction_5__printMessage(msgDB):
	try:
		conn = sqlite3.connect(msgDB)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
		messages = cursor.fetchall()
		return messages
	except sqlite3.Error as e:
		print(f"An error occurred: {e}")
		return []
	finally:
		if conn:
			conn.close()

def iterative_prompting_3__printMessage(msgDB):
        if not isinstance(msgDB, str) or not msgDB:
                raise ValueError("Invalid database path")
        try:
                conn = sqlite3.connect(msgDB, uri=True)
                cursor = conn.cursor()
                query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
        except sqlite3.Error as e:
                raise RuntimeError("An error occurred while accessing the database: " + str(e))
        finally:
                if conn:
                        if cursor:
                                cursor.close()
                        conn.close()

def iterative_prompting_4__print_message(msg_db):
    if not isinstance(msg_db, str):
        raise ValueError('msg_db must be a string representing the database file path')
    if not os.path.isfile(msg_db):
        raise FileNotFoundError(f'No such file: {msg_db}')
    try:
        conn = sqlite3.connect(msg_db, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
        return []
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return result

def iterative_prompting_5__printMessage(msgDB):
	if not isinstance(msgDB, str):
	    raise ValueError('Database path must be a string')
	if not os.path.isfile(msgDB):
	    raise FileNotFoundError('Database file does not exist')
	try:
		conn = sqlite3.connect(msgDB, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
		cursor = conn.cursor()
		cursor.execute('SELECT datetime(date, \'unixepoch\'), address, text FROM message WHERE address > 0;')
		results = cursor.fetchall()
		cursor.close()
		conn.close()
	except sqlite3.Error as e:
		raise RuntimeError(f'SQLite error: {e}')
	return results

def few_shots_prompting__printMessage(msgDB):
	conn = sqlite3.connect(msgDB)
	c = conn.cursor()
	c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	results = c.fetchall()
	conn.close()
	return results

def cot_prompting__printMessage(msgDB):
	conn = sqlite3.connect(msgDB)
	c = conn.cursor()
	c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	messages = c.fetchall()
	conn.close()
	return messages

def fact_check_list__printMessage(msgDBPath):
    messages = []
    connection = sqlite3.connect(msgDBPath)
    try:
        cursor = connection.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            messages.append(row)
    finally:
        cursor.close()
        connection.close()
    return messages

def not_interactive_mix__printMessage(msgDB):
    results = []
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        sql_query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        cursor.execute(sql_query)
        messages = cursor.fetchall()
        for message in messages:
            results.append(message)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results

def interactive_mix__printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        c = conn.cursor()
        c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        results = c.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"General error: {e}")
        return None

def baseline__printMessage(msgDB):
	conn = sqlite3.connect(msgDB)
	cursor = conn.cursor()
	cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	results = cursor.fetchall()
	conn.close()
	return results
