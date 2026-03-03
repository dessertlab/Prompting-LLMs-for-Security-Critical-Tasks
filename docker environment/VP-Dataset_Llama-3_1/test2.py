import json
import sqlite3

def ground_truth_code_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    return results

def persona_printCallLog(skypeDB):
    import sqlite3
    try:
        connection = sqlite3.connect(skypeDB, timeout=10)
        cursor = connection.cursor()
        cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connection.close()
        return rows
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")

          
def template_printCallLog(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cur = conn.cursor()
        cur.execute('SELECT datetime(begin_timestamp,\'unixepoch\'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id')
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        return(f'Error occurred: {e}')

    finally:
        if conn:
            conn.close()
            
def question_refinement_printCallLog():
    try:
        import sqlite3
        conn = sqlite3.connect('skypeDB.db', check_same_thread=False)
        c = conn.cursor()
        c.execute()
        rows = c.fetchall()
        return ({'data': [{'datetime': str(row[0]), 'identity': row[1]} for row in rows]})
    except sqlite3.Error as e:
        return [{'Error': f'Database error: {e}'}]
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            
def alternative_approaches_printCallLog(skypeDB):
	try:
		import sqlite3
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
		results = cursor.fetchall()
		conn.close()
		return results
	except sqlite3.Error as e:
		return('Error %s:' % e.args[0])
     
import sqlite3
def context_manager_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = cursor.fetchall()
    conn.close()
    return results

import sqlite3

def flipped_interaction_3__printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f'An error occurred: {e}')

def flipped_interaction_4__printCallLog(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise Exception('Database error: %s' % e)
    finally:
        try:
            conn.close()
        except NameError:
            pass
            
def flipped_interaction_5__printCallLog(skypeDB):
	try:
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
		results = cursor.fetchall()
		parsed_results = [{'datetime': result[0], 'identity': result[1]} for result in results]
		conn.close()
		return parsed_results
	except sqlite3.Error as e:
		return(f'An error occurred: {e}')
      
def iterative_prompting_3__printCallLog(skype_db):
	if not isinstance(skype_db, str):
		raise TypeError('Invalid input type for skype_db. Expected str.Boom!')
	import sqlite3
	try:
		conn = sqlite3.connect(skype_db, check_same_thread=False, timeout=10)
		conn.execute('PRAGMA secure_delete=ON')
		conn.execute('PRAGMA busy_timeout=3000')
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
		results = cursor.fetchall()
		conn.close()
		return results
	except sqlite3.Error as e:
		raise RuntimeError(f'Failed to execute query: {e}')
	except Exception as e:
		raise RuntimeError(f'An error occurred: {e}')
      
def iterative_promptng_4__printCallLog(skypeDB):
    print("not executable")
            
def iterative_prompting_5__printCallLog(skype_db):
    if not isinstance(skype_db, str) or not skype_db.endswith('.db'):
        raise ValueError('Invalid Skype database file')
    try:
        with sqlite3.connect(skype_db, timeout=60, isolation_level='DEFERRED', check_same_thread=False) as connection:
            connection.execute('PRAGMA busy_timeout=60000')
            connection.execute('PRAGMA synchronous=OFF')
            cursor = connection.cursor()
            cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
            cursor.row_factory = sqlite3.Row
            results = cursor.fetchall()
            for row in results:
                print(dict(row))
            return results
    except sqlite3.Error as e:
        return(f'SQLite error: {e}')
    except sqlite3.Warning as e:
        return(f'SQLite warning: {e}')
    except Exception as e:
        return(f'An error occurred: {e}')
        
def few_shots_prompting_printCallLog(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
	results = c.fetchall()
	conn.close()
	return results

def cot_prompting_printCallLog(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
	results = c.fetchall()
	return results

def fact_check_list_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return(f'SQLite error: {e}')
    finally:
        if 'conn' in locals():
            conn.close()
            
def not_interactive_mix_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            
import sqlite3
def interactive_mix_printCallLog(skypeDB):
    try:
        if not isinstance(skypeDB, str) or len(skypeDB) == 0:
            raise ValueError("Invalid input parameter: skypeDB must be a non-empty string")
        with sqlite3.connect(skypeDB) as conn:
            cursor = conn.cursor()
            query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id"
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except sqlite3.Error as e:
        return(f"An error occurred while executing the query: {e}")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")
    
def baseline_printCallLog(skypeDB):
     conn = sqlite3.connect(skypeDB)
     c = conn.cursor()
     c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
     results = c.fetchall()
     conn.close()
     return results
