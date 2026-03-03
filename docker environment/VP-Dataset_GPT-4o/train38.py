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

def persona_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = cursor.fetchall()
        conn.close()
        return any('message' in table[0] for table in tables)
    except sqlite3.Error:
        return False

def template_isMessageTable(iphoneDB):
    import sqlite3
    try:
        connection = sqlite3.connect(iphoneDB)
        cursor = connection.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        return any('message' in table[0] for table in tables)
    except sqlite3.Error as e:
        return False
    finally:
        if 'connection' in locals():
            connection.close()

def question_refinement_check_table_name_contains_message():
    import sqlite3
    try:
        conn = sqlite3.connect('iphoneDB')
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=?;', ("table",))
        tables = cursor.fetchall()
        for tbl in tables:
            if 'message' in tbl[0]:
                return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
    return False

def alternative_approaches_isMessageTable(iphoneDB):
    import sqlite3
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = [row[0] for row in cursor.fetchall()]
        return 'message' in tables
    except sqlite3.Error:
        return False
    finally:
        if conn:
            conn.close()

def context_manager_isMessageTable(iphoneDB):
    try:
        connection = sqlite3.connect(iphoneDB, timeout=5, isolation_level=None)
        cursor = connection.cursor()
        cursor.execute('PRAGMA read_uncommitted = True;')
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = cursor.fetchall()
        connection.close()
        return any('message' in table[0].lower() for table in tables)
    except sqlite3.Error:
        return False

import sqlite3
def flipped_interaction_3_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        conn.close()
        for table in tables:
            if 'message' in table:
                return True
        return False
    except Exception as e:
        return False

import sqlite3
def flipped_interaction_4_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        for table in tables:
            if 'message' in table[0]:
                return True
    except sqlite3.Error:
        return False
    finally:
        conn.close()
    return False

import sqlite3
def flipped_interaction_5_isMessageTable(iphoneDB):
    try:
        connection = sqlite3.connect(iphoneDB)
        cursor = connection.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        for (table_name,) in tables:
            if 'message' in table_name.lower():
                return True
        connection.close()
        return False
    except sqlite3.Error:
        return False

def iterative_prompting_3_is_message_table(iphone_db):
    import sqlite3
    import os
    if not isinstance(iphone_db, str):
        raise ValueError('The database path must be a string.')
    if not os.path.isfile(iphone_db):
        raise FileNotFoundError(f'Database file not found: {iphone_db}')
    try:
        with sqlite3.connect(iphone_db) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
            tables = cursor.fetchall()
            return any('message' in table[0] for table in tables)
    except sqlite3.DatabaseError as db_err:
        print(f'Database error: {db_err}')
        return False
    except Exception as e:
        print(f'Unexpected error: {e}')
        return False

def iterative_prompting_4_is_message_table(iphone_db):
    import os
    import sqlite3
    if not isinstance(iphone_db, str) or not iphone_db.strip():
        raise ValueError("Database path must be a non-empty string.")
    if not os.path.isfile(iphone_db):
        raise ValueError(f"Database file does not exist: {iphone_db}")
    try:
        with sqlite3.connect(iphone_db) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
            tables = cursor.fetchall()
            for table in tables:
                if 'message' in table[0]:
                    return True
            return False
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def iterative_prompting_5_is_message_table(iphone_db):
    import sqlite3
    import os
    if not isinstance(iphone_db, str) or not os.path.isfile(iphone_db):
        raise ValueError('The provided database path is not valid or does not exist.')
    conn = None
    try:
        conn = sqlite3.connect(iphone_db)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = cursor.fetchall()
        for table in tables:
            if 'message' in table[0].lower():
                return True
        return False
    except sqlite3.Error as e:
        print(f"SQLite error: {e.args[0]}")
        return False
    finally:
        if conn:
            conn.close()

def few_shots_prompting_isMessageTable(iphoneDB):
    import sqlite3
    try:
        conn = sqlite3.connect(iphoneDB)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = c.fetchall()
        for table in tables:
            if 'message' in table[0]:
                return True
    except:
        return False
    finally:
        c.close()
        conn.close()
    return False

def cot_prompting_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        c = conn.cursor()
        c.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = c.fetchall()
        for table in tables:
            if 'message' in table[0]:
                return True
        return False
    except:
        return False
    finally:
        if 'conn' in locals():
            conn.close()

import sqlite3
def fact_check_list_isMessageTable(iphoneDB):
    try:
        connection = sqlite3.connect(iphoneDB)
        cursor = connection.cursor()
        query = 'SELECT tbl_name FROM sqlite_master WHERE type="table";'
        cursor.execute(query)
        tables = cursor.fetchall()
        for table in tables:
            if 'message' in table[0]:
                return True
        return False
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        if 'connection' in locals():
            connection.close()

def not_interactive_mix_isMessageTable(iphoneDB):
    import sqlite3
    try:
        conn = sqlite3.connect(iphoneDB)
        if not conn:
            return False
        cur = conn.cursor()
        cur.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
        tables = cur.fetchall()
        for table in tables:
            if 'message' in table[0].lower():
                return True
        return False
    except sqlite3.Error:
        return False
    finally:
        if conn:
            conn.close()

def interactive_mix_check_for_message_table(db_path):
    import sqlite3
    try:
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type="table";')
            tables = cursor.fetchall()
            for table in tables:
                if 'message' in table[0].lower():
                    return True
        return False
    except sqlite3.DatabaseError:
        return False
    except Exception:
        return False

def baseline_isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        cursor = conn.cursor()
        cursor.execute('SELECT tbl_name FROM sqlite_master WHERE type=="table";')
        tables = cursor.fetchall()
        conn.close()
        return any('message' in table[0] for table in tables)
    except Exception:
        return False

