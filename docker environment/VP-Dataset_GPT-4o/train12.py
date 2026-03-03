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

def persona_printCookies(cookiesDB):
    conn = sqlite3.connect(cookiesDB)
    cursor = conn.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    cookies = cursor.fetchall()
    cursor.close()
    conn.close()
    return cookies

def template_printCookies(cookiesDB):
    results = []
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        rows = cursor.fetchall()
        for row in rows:
            results.append((row[0], row[1], row[2]))
    except sqlite3.Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Exception occurred: {e}')
    finally:
        if connection:
            connection.close()
    return results

def question_refinement_printCookies(cookiesDB):
    import sqlite3
    import os
    from contextlib import closing
    if not os.path.isfile(cookiesDB):
        raise ValueError("Provided path is not a valid file.")
    try:
        with sqlite3.connect(cookiesDB, uri=True) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SELECT host, name, value FROM moz_cookies")
                results = cursor.fetchall()
                return [{'host': repr(row[0]), 'name': repr(row[1]), 'value': repr(row[2])} for row in results]
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def alternative_approaches_printCookies(cookiesDB):
    import sqlite3
    import logging
    logging.basicConfig(level=logging.DEBUG)
    cookies = []
    try:
        with sqlite3.connect(cookiesDB) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT host, name, value FROM moz_cookies')
            cookies = cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f'Error: {e}')
    return cookies

def context_manager_printCookies(cookiesDB):
    import sqlite3
    import json
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        rows = cursor.fetchall()
        return json.dumps(rows)
    except sqlite3.Error as e:
        return json.dumps({'error': str(e)})
    finally:
        if connection:
            connection.close()

import sqlite3
def flipped_interaction_3_printCookies(cookiesDB):
    connection = sqlite3.connect(cookiesDB)
    cursor = connection.cursor()
    cursor.execute('SELECT host, name, value FROM moz_cookies')
    results = cursor.fetchall()
    connection.close()
    return results

import sqlite3
def flipped_interaction_4_printCookies(cookiesDB):
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies_data = cursor.fetchall()
        return cookies_data
    except sqlite3.Error as error:
        print(f"An error occurred: {error}")
    finally:
        if connection:
            connection.close()

def flipped_interaction_5_printCookies(cookiesDB):
    import sqlite3
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        if connection:
            connection.close()

def iterative_prompting_3_print_cookies(cookies_db):
    import os
    import sqlite3
    if not isinstance(cookies_db, str):
        raise ValueError('The database path must be a string.')
    if not os.path.isfile(cookies_db):
        raise FileNotFoundError(f'The database file {cookies_db} does not exist.')
    cookies = []
    conn = None
    try:
        conn = sqlite3.connect(cookies_db, detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = conn.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'SQLite error: {e}')
    finally:
        if conn:
            conn.close()
    return cookies

def iterative_prompting_4_print_cookies(cookies_db):
    import sqlite3
    import os
    if not isinstance(cookies_db, str) or not os.path.isfile(cookies_db):
        raise ValueError(f"Error: The database file '{cookies_db}' is invalid or inaccessible.")
        
    conn = None
    try:
        conn = sqlite3.connect(cookies_db, timeout=5, isolation_level=None)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type=? AND name=?;", ('table', 'moz_cookies'))
        if cursor.fetchone() is None:
            raise ValueError("Error: Table 'moz_cookies' does not exist in the database.")
            
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        results = cursor.fetchall()
        if not results:
            raise ValueError("No cookies found in the database.")
            
        for row in results:
            return f"Host: {row[0]}, Name: {row[1]}, Value: {row[2]}"
    except sqlite3.Error as e:
        raise ValueError(f"SQLite error occurred: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

def iterative_prompting_5_print_cookies(cookies_db):
    import os
    import sqlite3
    from sqlite3 import Error
    import logging
    if not isinstance(cookies_db, str) or not cookies_db.strip():
        raise ValueError('The database path must be a non-empty string.')
    if not os.path.isfile(cookies_db):
        raise FileNotFoundError('The specified database file does not exist.')
    connection = None
    try:
        connection = sqlite3.connect(cookies_db)
        cursor = connection.cursor()
        sql_query = 'SELECT host, name, value FROM moz_cookies'
        cursor.execute(sql_query)
        cookies = cursor.fetchall()
        return cookies
    except Error as e:
        logging.error(f'An SQL error occurred: {e}')
        return None
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return None
    finally:
        if connection:
            connection.close()

def few_shots_prompting_printCookies(cookiesDB):
    import sqlite3
    conn = sqlite3.connect(cookiesDB)
    c = conn.cursor()
    c.execute('SELECT host, name, value FROM moz_cookies')
    rows = c.fetchall()
    conn.close()
    return rows

def cot_prompting_printCookies(cookiesDB):
    import sqlite3
    conn = sqlite3.connect(cookiesDB)
    c = conn.cursor()
    c.execute('SELECT host, name, value FROM moz_cookies')
    results = c.fetchall()
    conn.close()
    return results

def fact_check_list_printCookies(cookiesDB):
    import sqlite3
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        query = 'SELECT host, name, value FROM moz_cookies'
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            host, name, value = row
            return f"Host: {host}, Name: {name}, Value: {value}"
    except sqlite3.Error as error:
        raise ValueError("Error while connecting to sqlite", error)
    finally:
        if connection:
            connection.close()

def not_interactive_mix_printCookies(cookiesDB):
    import sqlite3
    if not isinstance(cookiesDB, str) or len(cookiesDB) == 0:
        raise ValueError("Invalid database path.")
    try:
        with sqlite3.connect(cookiesDB) as conn:
            cursor = conn.cursor()
            sql_query = 'SELECT host, name, value FROM moz_cookies'
            cursor.execute(sql_query)
            cookies = cursor.fetchall()
            return cookies
    except sqlite3.Error as error:
        raise Exception(f"Database error: {error}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def interactive_mix_fetch_cookies_from_database(db_path):
    import sqlite3
    import os
    import logging
    logging.basicConfig(level=logging.ERROR)
    if not os.path.isfile(db_path) or not os.access(db_path, os.R_OK):
        logging.error(f"Invalid database file path or insufficient permissions: {db_path}")
        return None
    try:
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT host, name, value FROM moz_cookies')
            cookies = cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f'An error occurred: {e}')
        return None
    return cookies

def baseline_printCookies(cookiesDB):
    import sqlite3
    try:
        connection = sqlite3.connect(cookiesDB)
        cursor = connection.cursor()
        cursor.execute('SELECT host, name, value FROM moz_cookies')
        cookies = cursor.fetchall()
        return cookies
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
        return None
    finally:
        if connection:
            connection.close()

