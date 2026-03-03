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
        return None

def persona__isMessageTable(iphoneDB):
	import sqlite3
	try:
		conn = sqlite3.connect(iphoneDB)
		cursor = conn.cursor()
		cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
		tables = cursor.fetchall()
		conn.close()
		return any('message' in table[0] for table in tables)
	except Exception as e:
		return False

def template__isMessageTable(iphoneDB):
	try:
		import sqlite3
		conn = sqlite3.connect(iphoneDB)
		cursor = conn.cursor()
		cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
		tables = cursor.fetchall()
		conn.close()
		return any('message' in table[0] for table in tables)
	except Exception as e:
		return False

def question_refinement__isMessageTable():
    try:
        conn = sqlite3.connect('iphoneDB.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT tbl_name FROM sqlite_master WHERE type==?", ("table",))
        tables = cursor.fetchall()
        conn.close()
        for (tbl_name,) in tables:
            if 'message' in tbl_name:
                return True
        return False
    except Exception as e:
        return False

def alternative_approaches__isMessageTable(iphoneDB):
    import sqlite3
    try:
        with sqlite3.connect(iphoneDB) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
            tables = cursor.fetchall()
            return any('message' in str(table) for table in tables)
    except sqlite3.Error:
        return False

def context_manager__isMessageTable(iphoneDB):
    import sqlite3
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        if '消息' in [c[0] for c in cursor.fetchall()]:
            return True
        return False
    except:
        return False

def flipped_interaction_3__isMessageTable(iphoneDB):
    conn = None
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        for table in tables:
            if 'message' in table[0]:
                return True
        return False
    except:
        return False
    finally:
        if conn:
            conn.close()

def flipped_interaction_4__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        for table in tables:
            if 'message' in table[0]:
                return True
        return False
    except sqlite3.Error as e:
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def flipped_interaction_5__isMessageTable(iphoneDB):
	try:
		conn = sqlite3.connect(iphoneDB)
		c = conn.cursor()
		c.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
		for row in c:
			if 'message' in row[0].lower():
				return True
	except:
		return False
	finally:
		if conn:
			conn.close()

def iterative_prompting_3__isMessageTable(iphoneDB):
        if not isinstance(iphoneDB, str):
                return False
        if not iphoneDB.endswith(".db"):
                return False
        try:
                conn = sqlite3.connect(iphoneDB, uri=True)
                cursor = conn.cursor()
                cursor.execute("SELECT tbl_name FROM sqlite_master WHERE type=='table';")
                tables = cursor.fetchall()
                for table in tables:
                        if "message" in table[0]:
                                return True
                return False
        except sqlite3.Error as e:
                return False

def iterative_prompting_4__isMessageTable(iphoneDB):
    if not isinstance(iphoneDB, (sqlite3.Connection,)):
        return False
    try:
        cursor = iphoneDB.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = cursor.fetchall()
        if not isinstance(tables, list):
            return False
        return any(isinstance(table, tuple) and len(table) > 0 and 'message' in table[0] for table in tables)
    except Exception as e:
        return False

def iterative_prompting_5__isMessageTable(iphoneDB):
    if not hasattr(iphoneDB, 'cursor') or not callable(iphoneDB.cursor):
        return False
    try:
        cursor = iphoneDB.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type==')
    except: pass

def few_shots_prompting__isMessageTable(iphoneDB):
	try:
		conn = sqlite3.connect(iphoneDB)
		c = conn.cursor()
		c.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
		tables = c.fetchall()
		for table in tables:
			if 'message' in table[0].lower():
				return True
		return False
	except:
		return False

def cot_prompting__isMessageTable(iphoneDB):
	try:
		conn = sqlite3.connect(iphoneDB)
		c = conn.cursor()
		c.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
		tables = c.fetchall()
		conn.close()
		return any("message" in table[0].lower() for table in tables)
	except:
		return False

def fact_check_list__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = cursor.fetchall()
        cursor.close()
        conn.close()
        for table in tables:
            if 'message' in table[0]:
                return True
        return False
    except sqlite3.Error as e:
        return False

def not_interactive_mix__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = [table[0] for table in cursor.fetchall()]
        conn.close()
        return 'message' in tables
    except sqlite3.Error as e:
        return False

def interactive_mix__isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        for table in tables:
            if 'message' in table[0].lower():
                return True
    except Exception as e:
        return False
    finally:
        conn.close()

def baseline__isMessageTable(iphoneDB):
	try:
		cursor = iphoneDB.cursor()
		cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
		tables = cursor.fetchall()
		return any('message' in table[0] for table in tables)
	except:
		return False
