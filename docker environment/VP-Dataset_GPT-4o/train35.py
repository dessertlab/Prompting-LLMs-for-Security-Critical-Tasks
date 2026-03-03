import sqlite3
import os

def ground_truth_code_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = c.fetchall()  
    conn.close()
    return results

def persona_printDownloads(downloadDB):
    try:
        connection = sqlite3.connect(downloadDB)
        cursor = connection.cursor()
        cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        results = cursor.fetchall()
        connection.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def template_printDownloads(downloadDB):
    try:
        connection = sqlite3.connect(downloadDB)
        cursor = connection.cursor()
        cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        results = []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return results

def question_refinement_printDownloads(downloadDB):
    import sqlite3
    results = []

    try:
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def alternative_approaches_printDownloads(downloadDB):
    results = []
    try:
        with sqlite3.connect(downloadDB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
            results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return results

def context_manager_printDownloads(downloadDB):
    try:
        connection = sqlite3.connect(downloadDB)
        cursor = connection.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return results
    except sqlite3.Error as e:
        return f"An error occurred: {e}"

def flipped_interaction_3_printDownloads(db_path):
    results = []
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
    return results

def flipped_interaction_4_printDownloads(downloadDB):
    conn = None
    try:
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        results = []
    finally:
        if conn:
            conn.close()
    return results

def flipped_interaction_5_printDownloads(downloadDB):
    results = None
    try:
        connection = sqlite3.connect(downloadDB)
        cursor = connection.cursor()
        query = "SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as error:
        print(f"An error occurred: {error}")
    finally:
        if connection:
            connection.close()
    return results

def iterative_prompting_3_print_downloads(download_db):
    if not isinstance(download_db, str):
        raise TypeError("The database path must be a string.")
    if not os.path.isfile(download_db):
        raise FileNotFoundError(f"The database file '{download_db}' does not exist.")
    conn = None
    try:
        conn = sqlite3.connect(download_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = 'SELECT name, source, datetime(endTime/1000000, "unixepoch") FROM moz_downloads;'
        cursor.execute(query)
        results = cursor.fetchall()
        downloads = [dict(row) for row in results]
        return downloads
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

def iterative_prompting_4_print_downloads(download_db):
    if not isinstance(download_db, str):
        raise ValueError("Database path must be a string.")
    if not os.path.isfile(download_db):
        raise FileNotFoundError(f"Database file {download_db} does not exist.")
    results = []
    conn = None
    try:
        conn = sqlite3.connect(download_db)
        cursor = conn.cursor()
        query = ("SELECT name, source, datetime(endTime/1000000,'unixepoch') "
                 "FROM moz_downloads;")
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            results.append({
                "name": row[0],
                "source": row[1],
                "end_time": row[2]
            })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results
 
    
def iterative_prompting_5_print_downloads(download_db):
    if not isinstance(download_db, str):
        raise ValueError('The database path must be a string.')
    if not os.path.isfile(download_db):
        raise ValueError('The specified database file does not exist.')
    conn = None
    try:
        conn = sqlite3.connect(download_db)
        cursor = conn.cursor()
        query = ("SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;")
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error occurred: {e}')
    finally:
        if conn:
            conn.close()
    return results

def few_shots_prompting_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = c.fetchall()
    conn.close()
    return results

def cot_prompting_printDownloads(downloadDB):
    try:
        conn = sqlite3.connect(downloadDB)
        c = conn.cursor()
        c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        results = c.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()

def fact_check_list_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    cursor = conn.cursor()
    cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    rows = cursor.fetchall()
    downloads = []
    for row in rows:
        download = {
            'name': row[0],
            'source': row[1],
            'endTime': row[2]
        }
        downloads.append(download)
    conn.close()
    return downloads


def not_interactive_mix_printDownloads(downloadDB):
    if not isinstance(downloadDB, str) or not os.path.isfile(downloadDB):
        raise ValueError("Invalid database path.")
    try:
        conn = sqlite3.connect(downloadDB)
        cursor = conn.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def interactive_mix_query_download_db(database_path):
    if not isinstance(database_path, str) or not os.path.isfile(database_path):
        raise ValueError("Invalid database path provided")
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
    except Exception as e:
        raise RuntimeError(f"General error: {e}")
    finally:
        if connection:
            connection.close()
    return results

def baseline_printDownloads(downloadDB):
    connection = sqlite3.connect(downloadDB)
    cursor = connection.cursor()
    cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

