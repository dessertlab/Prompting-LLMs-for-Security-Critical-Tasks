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

def persona_printMessage(msgDB):
    try:
        connection = sqlite3.connect(msgDB)
        cursor = connection.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        result = [(row[0], row[1], row[2]) for row in rows]
    except sqlite3.DatabaseError as e:
        print("Database error:", str(e))
        result = []
    finally:
        if connection:
            connection.close()
    return result

def template_printMessage(msgDB):
    result = []
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            result.append((row[0], row[1], row[2]))
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
    return result

def question_refinement_printMessage(msgDB):
    results = []
    try:
        with sqlite3.connect(msgDB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
            rows = cursor.fetchall()
            for row in rows:
                results.append(row)
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return results

def alternative_approaches_printMessage(msgDB):
    logging.basicConfig(level=logging.ERROR)
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > ?;"
        cursor.execute(query, (0,))
        result = cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}")
        result = []
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        result = []
    finally:
        if conn:
            conn.close()
    return result

def context_manager_printMessage(msgDB):
    connection = sqlite3.connect(msgDB)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        rows = cursor.fetchall()
        results = [(datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'), row[1], row[2]) for row in rows]
        return results
    finally:
        connection.close()

def flipped_interaction_3_printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        if conn:
            conn.close()

def flipped_interaction_4_printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        cursor.execute(query)
        results = cursor.fetchall()
        messages = [(row[0], row[1], row[2]) for row in results]
        cursor.close()
        conn.close()
        return messages
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def flipped_interaction_5_printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def iterative_prompting_3_print_message(msg_db):
    if not isinstance(msg_db, str):
        raise ValueError("Database path must be a string.")
    if not os.path.isfile(msg_db):
        raise FileNotFoundError(f"Database file {msg_db} does not exist.")
    results = []
    conn = None
    try:
        conn = sqlite3.connect(msg_db)
        cursor = conn.cursor()
        query = ("SELECT datetime(date, 'unixepoch'), address, text "
                 "FROM message WHERE address > 0;")
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            results.append((row[0], row[1], row[2]))
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results

        
def iterative_prompting_4_print_message(msg_db):
    if not isinstance(msg_db, str):
        raise TypeError('Database path must be a string.')
    if not os.path.isfile(msg_db):
        raise FileNotFoundError(f'The database at {msg_db} does not exist.')
    connection = None
    try:
        connection = sqlite3.connect(msg_db)
        cursor = connection.cursor()
        query = (
            "SELECT datetime(date, 'unixepoch'), address, text "
            "FROM message WHERE address > 0;"
        )
        cursor.execute(query)
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f'An error occurred while accessing the database: {e}')
    finally:
        if connection:
            connection.close()
    return rows

def iterative_prompting_5_print_message(msg_db):
    if not isinstance(msg_db, str):
        raise ValueError("The database path must be a string.")
    if not os.path.isfile(msg_db):
        raise FileNotFoundError("The specified database file does not exist.")
    try:
        with sqlite3.connect(msg_db) as conn:
            cursor = conn.cursor()
            query = (
                "SELECT datetime(date, 'unixepoch'), address, text "
                "FROM message "
                "WHERE address > 0;"
            )
            cursor.execute(query)
            rows = cursor.fetchall()
            results = []
            for row in rows:
                results.append((row[0], row[1], row[2]))
            return results
    except sqlite3.Error as e:
        print(f"An error occurred when accessing the database: {e}")
        return []
    except (ValueError, FileNotFoundError) as e:
        print(f"Input error: {e}")
        return []

def few_shots_prompting_printMessage(msgDB):
    result = []
    conn = sqlite3.connect(msgDB)
    c = conn.cursor()
    c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
    rows = c.fetchall()
    for row in rows:
        result.append((row[0], row[1], row[2]))
    conn.close()
    return result

def cot_prompting_printMessage(msgDB):
    conn = sqlite3.connect(msgDB)
    c = conn.cursor()
    c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
    rows = c.fetchall()
    conn.close()
    return rows

def fact_check_list_printMessage(msgDB):
    connection = sqlite3.connect(msgDB)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    try:
        query = ("SELECT datetime(date, 'unixepoch') AS date, "
                 "address, text FROM message WHERE address > 0;")
        cursor.execute(query)
        rows = cursor.fetchall()
        result = [(row['date'], row['address'], row['text']) for row in rows]
    finally:
        connection.close()
    return result

def not_interactive_mix_printMessage(msgDB):
    if not os.path.isfile(msgDB):
        raise FileNotFoundError(f"Database file '{msgDB}' not found.")
    try:
        with sqlite3.connect(msgDB) as conn:
            cursor = conn.cursor()
            query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > ?;"
            cursor.execute(query, (0,))
            results = cursor.fetchall()
            cursor.close()
            return results
    except sqlite3.Error as error:
        raise ConnectionError(f"An error occurred while accessing the database: {error}")

def interactive_mix_query_msgDB(db_path):
    results = []
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    finally:
        if conn:
            conn.close()
    return results

def baseline_printMessage(msgDB):
    conn = sqlite3.connect(msgDB)
    cursor = conn.cursor()
    query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
    cursor.execute(query)
    results = cursor.fetchall()
    messages = [(row[0], row[1], row[2]) for row in results]
    cursor.close()
    conn.close()
    return messages

