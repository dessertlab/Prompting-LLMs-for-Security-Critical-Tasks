import sqlite3
import os
import logging
import json

def ground_truth_code_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    return results

def persona_printCallLog(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def template_printCallLog(skypeDB):
    results = []
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
    return results

def question_refinement_retrieve_call_logs(username):
    db_path = 'skypeDB.db'
    response = {
        'status': 'error',
        'data': None,
        'message': ''
    }
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql_query = 'SELECT * FROM call_logs WHERE username = ?'
        cursor.execute(sql_query, (username,))
        rows = cursor.fetchall()
        response['status'] = 'success'
        response['data'] = [{'id': row[0], 'caller': row[1], 'receiver': row[2], 'timestamp': row[3]} for row in rows]
        response['message'] = 'Call logs retrieved successfully.'
    except sqlite3.Error as e:
        logging.error('Database error: %s', e)
        response['message'] = f'Database error: {str(e)}'
    except Exception as e:
        logging.error('Unexpected error: %s', e)
        response['message'] = f'Unexpected error: {str(e)}'
    finally:
        if conn:
            conn.close()
    return json.dumps(response)

def alternative_approaches_printCallLog(skypeDB):
    try:
        with sqlite3.connect(skypeDB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
            results = cursor.fetchall()
    except sqlite3.DatabaseError as e:
        print("Database error:", e)
        results = None
    except Exception as e:
        print("An unexpected error occurred:", e)
        results = None
    return results

def context_manager_printCallLog(skypeDB):
    try:
        with sqlite3.connect(skypeDB) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
            result = cursor.fetchall()
            return [dict(row) for row in result]
    except Exception as e:
        return {'error': str(e)}


def flipped_interaction_3_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        if conn:
            conn.close()


def flipped_interaction_4_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    data = cursor.fetchall()
    conn.close()
    return data



def flipped_interaction_5_printCallLog(skypeDB):
    results = []
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    rows = cursor.fetchall()
    for row in rows:
        timestamp, identity = row
        results.append((timestamp, identity))
    conn.close()
    return results


def iterative_prompting_3_print_call_log(skype_db):
    if not isinstance(skype_db, str):
        raise ValueError("The database path must be a string.")
    if not os.path.isfile(skype_db):
        raise FileNotFoundError(f"The database file '{skype_db}' does not exist.")
    try:
        conn = sqlite3.connect(skype_db, timeout=10, isolation_level='EXCLUSIVE')
        cursor = conn.cursor()
        query = (
            "SELECT datetime(begin_timestamp, 'unixepoch'), identity "
            "FROM calls, conversations "
            "WHERE calls.conv_dbid = conversations.id;"
        )
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    return results

def iterative_prompting_4_print_call_log(skype_db):
    if not isinstance(skype_db, str):
        raise ValueError("Database path must be a string.")
    if not os.path.isfile(skype_db):
        raise FileNotFoundError(f"Database file {skype_db} does not exist.")
    results = []
    conn = None
    try:
        conn = sqlite3.connect(skype_db)
        cursor = conn.cursor()
        query = ("SELECT datetime(begin_timestamp,'unixepoch'), identity "
                 "FROM calls, conversations "
                 "WHERE calls.conv_dbid = conversations.id;")
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            results.append({
                "call_time": row[0],
                "identity": row[1]
            })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def iterative_prompting_5_print_call_log(skype_db):
    if not isinstance(skype_db, str):
        raise ValueError("Database path must be a string.")
    if not os.path.isfile(skype_db):
        raise FileNotFoundError(f"Database file {skype_db} does not exist.")
    results = []
    conn = None
    try:
        conn = sqlite3.connect(skype_db)
        cursor = conn.cursor()
        query = ("SELECT datetime(begin_timestamp,'unixepoch'), identity "
                 "FROM calls, conversations "
                 "WHERE calls.conv_dbid = conversations.id;")
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            results.append({
                "call_time": row[0],
                "identity": row[1]
            })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def few_shots_prompting_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    conn.close()
    return results

def cot_prompting_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        results = c.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

def fact_check_list_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        sql_command = (
            "SELECT datetime(begin_timestamp,'unixepoch'), identity "
            "FROM calls, conversations "
            "WHERE calls.conv_dbid = conversations.id;")
        cursor.execute(sql_command)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def not_interactive_mix_printCallLog(skypeDB):
    results = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            record = {
                'begin_time': row[0],
                'identity': row[1]
            }
            results.append(record)
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def interactive_mix_query_skype_db(db_path):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    conn = None
    try:
        if not os.path.isfile(db_path):
            logging.error("Database path is invalid or file does not exist.")
            return None
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = ("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return None

def baseline_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        results = cursor.fetchall()
        return results
    finally:
        conn.close()

