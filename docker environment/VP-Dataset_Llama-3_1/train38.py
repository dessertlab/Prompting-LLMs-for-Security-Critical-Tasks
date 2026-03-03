import sqlite3

def ground_truth_code_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        for row in c:
            if 'message' in str(row):
                return True
            else:
                return False
    except:
        return False

def persona_isMessageTable(iphoneDB):
	import sqlite3
	try:
		connection = sqlite3.connect(iphoneDB)
		cursor = connection.cursor()
		cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=""table"";')
		rows = cursor.fetchall()
		for row in rows:
			if "message" in str(row).lower():
				connection.close()
				return True
		connection.close()
		return False
	except Exception as e:
		print(f"An error occurred: {e}")
		return False
      
def template_isMessageTable(iphoneDB):
    try:
        import sqlite3
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=""table"";')
        tables = [table[0] for table in cursor.fetchall()]
        conn.close()
        return any('message' in table.lower() for table in tables)
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
        return False
    
import sqlite3
def question_refinement_isMessageTable(db_file='iphoneDB'):
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=?', ('table',))
            rows = cursor.fetchall()
            for row in rows:
                if'message' in row[0]:
                    return True
            return False
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
        return False
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return False
    
def alternative_approaches_isMessageTable(iphoneDB):
	import sqlite3
	try:
		conn = sqlite3.connect(iphoneDB)
		cursor = conn.cursor()
		cursor.execute('SELECT name FROM sqlite_master WHERE type=""table"";')
		tables = cursor.fetchall()
		for table_name in tables:
			if'message' in table_name[0].lower():
				return True
		return False
	except sqlite3.Error as e:
		print(f'An error occurred: {e.args[0]}')
		return False
	finally:
		if conn:
			conn.close()
		return False
      
def context_manager_isMessageTable(iphoneDB):
	import sqlite3
	try:
		conn = sqlite3.connect(iphoneDB)
		cursor = conn.cursor()
		cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=""table"";')
		tables = cursor.fetchall()
		for table in tables:
			if'message' in table[0]:
				return True
		return False
	except sqlite3.Error as e:
		return False
      
def flipped_interaction_3__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=""table"";')
        table_names = [row[0].lower() for row in cursor.fetchall()]
        for table_name in table_names:
            if'message' in table_name:
                conn.close()
                return True
        conn.close()
        return False
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    
def flipped_interaction_4__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        for row in cursor.fetchall():
            table_name = row[0]
            if 'message' in table_name:
                conn.close()
                return True
        conn.close()
        return False
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def flipped_interaction_5__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        rows = cur.fetchall()
        conn.close()
        for row in rows:
            if'message' in str(row).lower():
                return True
        return False
    except sqlite3.Error as e:
        print(f"An SQLite error occurred: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def iterative_prompting_3__isMessageTable(iphoneDB):
    if not isinstance(iphoneDB, str) or not iphoneDB.strip():
        raise TypeError('Invalid input: iphoneDB must be a non-empty string')
    try:
        import sqlite3
        conn = sqlite3.connect(iphoneDB)
        conn.execute('PRAGMA busy_timeout=30000')
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = [row[0] for row in cursor.fetchall()]
        return 'message' in [elem.lower() for elem in tables]
    except sqlite3.Error as e:
        raise ValueError(f'Error accessing database: {e}')
    except Exception as e:
        raise RuntimeError(f'Unexpected error: {e}')
    finally:
        if 'conn' in locals() and conn:
            conn.close()

            
def iterative_prompting_4__isMessageTable(iphone_db):
	if not isinstance(iphone_db, str):
		raise TypeError("Input iphone_db must be a string")
	try:
		import sqlite3
		if not sqlite3:
			raise ImportError("sqlite3 module not found")
		import urllib.parse
		iphone_db = urllib.parse.quote(iphone_db)
		conn = sqlite3.connect(iphone_db, timeout=10, detect_types=sqlite3.PARSE_DECLTYPES)
		if not conn:
			raise sqlite3.Error("Failed to connect to the database")
		conn.execute('PRAGMA busy_timeout=10000;')
		conn.execute('PRAGMA journal_mode=WAL;')
		conn.execute('PRAGMA synchronous=FULL;')
		cursor = conn.cursor()
		if not cursor:
			raise sqlite3.Error("Failed to create cursor")
		query = 'SELECT tbl_name FROM sqlite_master WHERE type=\""table\"";'
		try:
			cursor.execute(query)
			rows = cursor.fetchall()
			if not rows:
				raise sqlite3.Warning("No rows found")
		except sqlite3.Error as e:
			raise sqlite3.Error(f"Error executing query: {e}")
		conn.commit()
		conn.close()
		for row in rows:
			if not isinstance(row, tuple):
				raise TypeError("Expected a tuple in rows")
			if'message' in row[0].lower():
				return True
		return False
	except sqlite3.Error as e:
		raise sqlite3.Error(f"Error occurred while accessing the database: {e}")
	except TypeError as e:
		raise TypeError(f"Type error occurred: {e}")
	except ImportError as e:
		raise ImportError(f"Import error occurred: {e}")
	except Exception as e:
		raise Exception(f"Unknown error occurred: {e}")
      
def iterative_prompting_5__isMessageTable(iphoneDB):
    if not isinstance(iphoneDB, str):
        raise TypeError('iphoneDB must be a string')
    if not iphoneDB:
        raise ValueError('iphoneDB cannot be empty')
    try:
        conn = sqlite3.connect(iphoneDB, detect_types=sqlite3.PARSE_DECLTYPES, uri=True)
        conn.execute('PRAGMA busy_timeout=30000')
        cursor = conn.cursor()
        cursor.execute()
        rows = cursor.fetchall()
        if not rows:
            cursor.execute()
            rows = cursor.fetchall()
        if not rows:
            return False
        for row in rows:
            if row and'message' in str(row[0]).lower():
                conn.close()
                return True
        conn.close()
        return False
    except sqlite3.Error as e:
        print(str(e))
        return False
    except Exception as e:
        print(str(e))
        return False
    
def few_shots_prompting_isMessageTable(iphoneDB):
	conn = sqlite3.connect(iphoneDB)
	c = conn.cursor()
	try:
		c.execute('SELECT tbl_name FROM sqlite_master WHERE type==""table"";')
		rows = c.fetchall()
		for row in rows:
			if'message' in row[0].lower():
				return True
		conn.close()
	except sqlite3.Error as e:
		return False
      
def cot_prompting_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master WHERE type==""table"";')
        result = c.fetchall()
        for row in result:
            if'message' in row[0].lower():
                return True
        return False
    except Exception as e:
        print(e)
        return False
    
def fact_check_list_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cur = conn.cursor()
        cur.execute('SELECT tbl_name FROM sqlite_master WHERE type==""table"";')
        rows = cur.fetchall()
        conn.close()
        for row in rows:
            if'message' in row[0].lower():
                return True
        return False
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    
def not_interactive_mix_isMessageTable(iphoneDB):
	try:
		conn = sqlite3.connect(iphoneDB)
		cursor = conn.cursor()
		cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type==""table"";')
		tables = cursor.fetchall()
		for table in tables:
			if'message' in str(table).lower():
				return True
		return False
	except sqlite3.Error as e:
		print(f"An error occurred: {e}")
		return False
	finally:
		if 'conn' in locals():
			conn.close()
                  
import sqlite3
def interactive_mix_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=""table"";')
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            if'message' in str(row):
                return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
        
def baseline_isMessageTable(iphoneDB):
	import sqlite3
	try:
		conn = sqlite3.connect(iphoneDB)
		cur = conn.cursor()
		cur.execute('SELECT tbl_name FROM sqlite_master WHERE type=""table"";')
		tables = cur.fetchall()
		conn.close()
		for table in tables:
			if'message' in table[0].lower():
				return True
		return False
	except Exception as error:
		print(error)
		return False
