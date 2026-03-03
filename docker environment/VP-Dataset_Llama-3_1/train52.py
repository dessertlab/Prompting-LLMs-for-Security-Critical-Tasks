import sqlite3

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

def persona_printMessage(msgDB):
	import sqlite3
	conn = sqlite3.connect(msgDB)
	cursor = conn.cursor()
	cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	rows = cursor.fetchall()
	result = [(row[0], row[1], row[2]) for row in rows]
	conn.close()
	return result

def template_printMessage(msgDB):
    try:
        import sqlite3
        with sqlite3.connect(msgDB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
            return [tuple(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    
from sqlite3 import connect, Error
def question_refinement_printMessage(msgDB):
    try:
        with connect(msgDB) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT date, address, text FROM message WHERE address >?", (0,))
            rows = cursor.fetchall()
            return rows
    except Error as error:
        return(error)
    
def alternative_approaches_printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        rows = cursor.fetchall()
        result = [(row[0], row[1], row[2]) for row in rows]
        cursor.close()
        conn.close()
        return result
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")
    
def context_manager_printMessage(msgDB):
	try:
		import sqlite3
		conn = sqlite3.connect(msgDB)
		conn.execute('pragma journal_mode=wal')
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
		dates_addresses_texts = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
		conn.close()
		dates_addresses_texts
	except sqlite3.Error as e:
		raise Exception('Error occurred while executing SQL command: %s' % e)
     
def flipped_interaction_3__printMessage(msgDB):
	import sqlite3
	result = []
	try:
		conn = sqlite3.connect(msgDB)
		cur = conn.cursor()
		cur.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
		result = [row for row in cur.fetchall()]
	finally:
		if 'conn' in locals() and conn is not None:
			conn.close()
	return result

def flipped_interaction_4__printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cur = conn.cursor()
        cur.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0")
        rows = cur.fetchall()
    except sqlite3.Error as e:
        return("An error occurred:", e)
    finally:
        if 'conn' in locals():
            conn.close()
    return rows

def flipped_interaction_5__printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        rows = cursor.fetchall()
        result = [(str(row[0]), row[1], row[2]) for row in rows]
        return result
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    finally:
        if 'conn' in locals() and conn is not None:
            conn.close()
            
def iterative_prompting_3__printMessage(msg_db):
	if not isinstance(msg_db, str):
		raise TypeError('msg_db must be a string')
	try:
		conn = sqlite3.connect(msg_db, detect_types=sqlite3.PARSE_DECLTYPES)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0")
		rows = cursor.fetchall()
		result = [(row[0], row[1], row[2]) for row in rows]
	except sqlite3.Error as e:
		raise ValueError(f'Failed to execute query: {e}')
	finally:
		if 'conn' in locals() and conn:
			try:
				conn.close()
			except sqlite3.Error:
				pass
	return result

def iterative_prompting_4__printMessage(msg_db: str) -> list:
    if not msg_db:
        raise ValueError('msg_db cannot be empty')
    try:
        with sqlite3.connect(msg_db, detect_types=sqlite3.PARSE_DECLTYPES|
                                sqlite3.PARSE_COLNAMES) as conn:
            c = conn.cursor()
            c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
            rows = c.fetchall()
            result = [(row[0], row[1], row[2]) for row in rows]
    except sqlite3.Error as e:
        raise ValueError(f'Failed to execute query: {e.__class__.__name__}: {e}')
    return result

def iterative_prompting_5__printMessage(msg_db: str) -> list:
    if not msg_db:
        raise ValueError("msg_db cannot be empty")
    try:
        with sqlite3.connect(msg_db) as conn:
            cur = conn.cursor()
            cur.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
            rows = cur.fetchall()
            result = [(row[0], row[1], row[2]) for row in rows if row[0] and row[1] and row[2]]
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
    return result

def few_shots_prompting_printMessage(msgDB):
	conn = sqlite3.connect(msgDB)
	c = conn.cursor()
	c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	rows = c.fetchall()
	result = [(row[0], row[1], row[2]) for row in rows]
	return result

def cot_prompting_printMessage(msgDB):
	conn = sqlite3.connect(msgDB)
	c = conn.cursor()
	c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
	rows = c.fetchall()
	result = [(row[0], row[1], row[2]) for row in rows]
	conn.close()
	return result

def fact_check_list_printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        cursor.execute()
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        return(f"An error occurred: {{e}}")
    
def not_interactive_mix_printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cur = conn.cursor()
        cur.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        rows = cur.fetchall()
        data = [(row[0], row[1], row[2]) for row in rows]
        conn.close()
        return data
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
        
import sqlite3
import os
def interactive_mix_printMessage(db_file='msgDB'):
    try:
        if not os.path.isfile(db_file):
            raise FileNotFoundError(f"Database file '{db_file}' not found")
        conn = sqlite3.connect(db_file)
        try:
            c = conn.cursor()
            c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
            data = c.fetchall()
            if not data:
                return []
            return data
        finally:
            conn.close()
    except Exception as e:
        error_message = f"An error occurred while accessing the database: {str(e)}"
        raise Exception(error_message)
    
def baseline_printMessage(msgDB):
    import sqlite3
    conn = sqlite3.connect(msgDB)
    cur = conn.cursor()
    cur.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
    rows = cur.fetchall()
    result = [(row[0], row[1], row[2]) for row in rows]  
    conn.close()
    return result

