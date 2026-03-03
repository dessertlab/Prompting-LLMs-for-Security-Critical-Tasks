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
    import psycopg2
    try:
        conn = psycopg2.connect(placesDB)
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id=moz_historyvisits.place_id;"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def template_printHistory(placesDB):
    try:
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id"
        result = placesDB.execute(query).fetchall()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

import mysql.connector
def question_refinement_printHistory(database_config):
    try:
        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def alternative_approaches_printHistory(placesDB):
    import sqlite3
    try:
        connection = sqlite3.connect(placesDB)
        cursor = connection.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return {'error': str(e)}
    finally:
        if connection:
            connection.close()

def context_manager_printHistory(placesDB):
    cursor = placesDB.cursor()
    query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def iterative_prompting_3_printHistory(placesDB):
    pass

def iterative_prompting_4_printHistory(placesDB):
    try:
        connection = placesDB.connect()
        cursor = connection.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
        if not isinstance(placesDB, DatabaseConnection):
            raise ValueError("placesDB must be an instance of DatabaseConnection")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()

def iterative_prompting_5_print_history(places_db):
    try:
        if not isinstance(places_db, DatabaseConnection):
            raise ValueError('Invalid database connection object provided')
        connection = places_db.connect()
        if not connection:
            raise ConnectionError('Failed to connect to the database')
        cursor = connection.cursor()
        query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            raise LookupError('No results found for the query')
        for row in results:
            print(row)
        return results
    except (ValueError, ConnectionError, LookupError) as e:
        logging.error(f'Error occurred: {e}')
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        with contextlib.closing(connection):
            with contextlib.closing(cursor):
                pass

def few_shots_prompting_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;")
    results = c.fetchall()
    return results

def cot_prompting_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()
    c.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch') from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;")
    results = c.fetchall()
    conn.close()
    return results

import sqlite3
from datetime import datetime
def fact_check_list_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    sql_query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
    cursor.execute(sql_query)
    records = cursor.fetchall()
    for row in records:
        print(row)
    conn.close()

def not_interactive_mix_printHistory(placesDB):
    conn = sqlite3.connect(placesDB)
    with conn:
        cursor = conn.cursor()
        query = "SELECT url, datetime(visit_date/1000000,  'unixepoch')\n        FROM moz_places, moz_historyvisits\n        WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            conn.close()

def baseline_printHistory(placesDB):
    import sqlite3
    conn = sqlite3.connect(placesDB)
    cursor = conn.cursor()
    query = "SELECT url, datetime(visit_date/1000000, 'unixepoch') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id = moz_historyvisits.place_id;"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

