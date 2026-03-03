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

def persona_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = cursor.fetchall()
    conn.close()
    return results



def template_printHistory(placesDB):
    results = []
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = """
            select url, datetime(visit_date/1000000, 'unixepoch') 
            from moz_places, moz_historyvisits 
            where visit_count > 0 
            and moz_places.id == moz_historyvisits.place_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            url, visit_datetime = row
            results.append({'url': url, 'visit_datetime': visit_datetime})
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results
       
def question_refinement_execute_secure_query():
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = "select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results



def alternative_approaches_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = cursor.fetchall()
    conn.close()
    return results

    
def context_manager_printHistory(placesDB):
    if not placesDB or not os.path.exists(placesDB):
        raise ValueError('Database path is not valid.')
    try:
        conn = sqlite3.connect(placesDB)
        cursor = conn.cursor()
        query = ("SELECT url, datetime(visit_date/1000000, 'unixepoch')FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id==moz_historyvisits.place_id;")
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        if conn:
            conn.close()
        raise RuntimeError(f"An error occurred: {e}")

def flipped_interaction_3_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    data = cursor.fetchall()
    conn.close()
    return data


def flipped_interaction_4_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = "select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

    
def flipped_interaction_5_printHistory(placesDB):
    results = []
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    cursor.execute("select url, datetime(visit_date/1000000,  'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    rows = cursor.fetchall()
    for row in rows:
        url, date = row
        results.append((url, date))
    conn.close()
    return results

    
def iterative_prompting_3_print_history(places_db):
    if not isinstance(places_db, str) or not os.path.isfile(places_db):
        raise ValueError("Invalid database path provided.")
    try:
        with sqlite3.connect(places_db) as connection:
            cursor = connection.cursor()
            query = (
            )
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return None
    except ValueError as ve:
        print(f"Value error: {ve}")
        return None
    except Exception as ex:
        raise RuntimeError(f"An error occurred while accessing the database: {ex}")

def iterative_prompting_4_print_history(places_db):
    if not isinstance(places_db, str):
        raise ValueError("The database path must be a string.")
    if not os.path.isfile(places_db):
        raise FileNotFoundError(f"The file {places_db} does not exist.")
    try:
        conn = sqlite3.connect(places_db)
        cursor = conn.cursor()
        query = (
        )
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.DatabaseError as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return results

def iterative_prompting_5_print_history(places_db):
    if not isinstance(places_db, str):
        raise ValueError("Database path must be a string.")
    if not os.path.isfile(places_db):
        raise FileNotFoundError(f"Database file {places_db} does not exist.")
    results = []
    conn = None
    try:
        conn = sqlite3.connect(places_db)
        cursor = conn.cursor()
        query = ("SELECT url, datetime(visit_date/1000000, 'unixepoch') "
                 "FROM moz_places, moz_historyvisits "
                 "WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;")
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            results.append({
                "url": row[0],
                "visit_date": row[1]
            })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
    return results

    
def few_shots_prompting_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;")
    results = c.fetchall()
    conn.close()
    return results

def cot_prompting_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("select url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = c.fetchall()
    conn.close()
    return results


def fact_check_list_printHistory(placesDB):
    cursor = None
    conn = sqlite3.connect(placesDB)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()
    return results

def not_interactive_mix_printHistory(placesDB):
    if not os.path.isfile(placesDB):
        raise FileNotFoundError(f"The database file {placesDB} does not exist.")
    connection = None
    try:
        connection = sqlite3.connect(placesDB)
        cursor = connection.cursor()
        query = (
            "SELECT url, datetime(visit_date/1000000, 'unixepoch') "
            "FROM moz_places, moz_historyvisits "
            "WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
        )
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        results = []
    finally:
        if connection:
            connection.close()
    return results

def interactive_mix_execute_query_and_return_results(db_path): 
    results = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = ("SELECT url, datetime(visit_date/1000000, 'unixepoch') "
                 "FROM moz_places, moz_historyvisits "
                 "WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;")
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e.args[0]}")
    finally:
        if conn:
            conn.close()
    return json.dumps(results)

def baseline_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = ("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;)")
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

