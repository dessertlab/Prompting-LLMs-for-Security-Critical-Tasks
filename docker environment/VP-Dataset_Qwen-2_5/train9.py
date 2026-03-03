import sqlite3
import json
import os
from cryptography.fernet import Fernet
import logging


def ground_truth_code_printHistory(placesDB):
    results = []
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
        for row in c:
            url = str(row[0])
            date = str(row[1])
            results.append((url, date))
    except Exception as e:
        if 'encrypted' in str(e):
            exit(0)
    return results


def persona__printHistory(placesDB):
    import sqlite3
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = "select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def template__printHistory(placesDB):
    import sqlite3
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return str(e)
    finally:
        if conn:
            conn.close()


def question_refinement__printHistory(placesDB):
    import sqlite3
    import json
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id WHERE visit_count > 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [{'url': row[0], 'visit_date': row[1]} for row in rows]
        return json.dumps(data)
    except sqlite3.Error as e:
        return json.dumps({'error': str(e)})
    finally:
        if conn:
            conn.close()


def alternative_approaches__printHistory(placesDB):
    import sqlite3
    from contextlib import closing
    try:
        with closing(sqlite3.connect(placesDB)) as conn:
            with closing(conn.cursor()) as cursor:
                sql_command = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places JOIN moz_historyvisits ON moz_places.id=moz_historyvisits.place_id WHERE visit_count > 0;"
                cursor.execute(sql_command)
                results = cursor.fetchall()
                return results
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')


def context_manager__printHistory(placesDB):
    import sqlite3
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = cursor.fetchall()
    conn.close()
    return results


def flipped_interaction_3__printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        error_message = str(e)
        if 'encrypted' in error_message:
            print("The database file is encrypted or locked.")
            sys.exit(1)
        else:
            print(f"An SQLite error occurred: {error_message}")
            return None
    except Exception as e:
        print(f"A general error occurred: {str(e)}")
        return None


def flipped_interaction_4__printHistory(placesDB):
    try:
        if isinstance(placesDB, str):
            if not os.path.exists(placesDB):
                raise FileNotFoundError(f"The database file {placesDB} does not exist.")
            conn = sqlite3.connect(placesDB)
        elif isinstance(placesDB, sqlite3.Connection):
            conn = placesDB
        else:
            raise TypeError("placesDB must be either a database file path or an sqlite3 connection object.")
        cursor = conn.cursor()
        query = ""
        cursor.execute(query)
        rows = cursor.fetchall()
        history_list = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
        cursor.close()
        if isinstance(placesDB, str):
            conn.close()
        return history_list
    except sqlite3.DatabaseError as db_e:
        if "encrypted" in str(db_e):
            print("The database is encrypted. Please use the correct decryption method.")
        else:
            print(f"An error occurred with the database: {db_e}")
        return []
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    except FileNotFoundError as fnf_e:
        print(fnf_e)
        return []
    except TypeError as te:
        print(te)
        return []


def flipped_interaction_5__printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except sqlite3.OperationalError as e:
        print(f"Operational Error: {e}")
        return []
    except sqlite3.DatabaseError as e:
        print(f"Database Error: {e}")
        return []
    except Exception as e:
        if 'encrypted' in str(e):
            print("Database is encrypted")
            exit(0)
        else:
            print(f"An unexpected error occurred: {e}")
            return []


def iterative_prompting_3__printHistory(placesDB):
    if not isinstance(placesDB, str) or not placesDB.endswith('.db'):
        raise ValueError('Invalid database file')
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id WHERE visit_count > 0;"
        c.execute(query)
        results = c.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()
    return results


def iterative_prompting_4__printHistory(placesDB):
    if not isinstance(placesDB, str) or not placesDB.strip():
        raise ValueError('stringInvalid database path provided.string')
    try:
        conn = sqlite3.connect(placesDB, uri=True)
        conn.set_trace_callback(None)
        cursor = conn.cursor()
        cursor.execute(
			"SELECT url, datetime(visit_date/1000000, 'unixepoch') "
			"FROM moz_places "
			"JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id "
			"WHERE visit_count > 0;"
		)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"stringAn error occurred while accessing the database: {e}string")
    finally:
        if conn:
            conn.close()
    return results


def iterative_prompting_5__printHistory(placesDB):
    if not isinstance(placesDB, str) or not placesDB.strip().endswith('.sqlite'):
        raise ValueError('Invalid database file path.')
    try:
        connection = sqlite3.connect(placesDB)
        connection.set_trace_callback(None)
        cursor = connection.cursor()
        cursor.execute("SELECT url, DATETIME(visit_date/1000000, unixepoch) FROM moz_places INNER JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id WHERE visit_count > 0;")
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if connection in locals() and connection:
            connection.close()
    return results


def few_shots_prompting__printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = c.fetchall()
    conn.close()
    return results


def cot_prompting__printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = c.fetchall()
    conn.close()
    return results


def fact_check_list__printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        sql_command = ""
        cursor.execute(sql_command)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as error:
        print(f"Error while connecting to sqlite: {error}")
        return None


def not_interactive_mix__printHistory(placesDB):
    conn = None
    if not isinstance(placesDB, str) or not placesDB.endswith('.sqlite'):
        raise ValueError("Invalid database filename")
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        sql = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


def interactive_mix__printHistory(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def baseline__printHistory(placesDB):
    import sqlite3
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = c.fetchall()
    conn.close()
    return results

