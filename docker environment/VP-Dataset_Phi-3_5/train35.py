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
    cursor = downloadDB.cursor()
    query = "SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def template_printDownloads(downloadDB):
    import sqlite3
    try:
        connection = sqlite3.connect(downloadDB)
        cursor = connection.cursor()
        query = "SELECT name, source, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return f

def question_refinement_printDownloads(downloadDB):
    try:
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor = downloadDB.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print({'name': row[0], 'source': row[1], 'endTime': row[2]})
    except Exception as e:
        print(f"An error occurred: {e}")
        cursor.close()
        downloadDB.close()

def alternative_approaches_printDownloads(downloadDB):
    import mysql.connector
    try:
        connection = mysql.connector.connect(host='hostname', database=downloadDB, user='username', password='password')
        cursor = connection.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as error:
        print(f'Error: {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def context_manager_printDownloads(downloadDB):
    query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
    results = downloadDB.execute(query).fetchall()
    return results

def iterative_prompting_3_print_downloads(cursor, connection_details):
    try:
        if not connection_details or 'host' not in connection_details or 'user' not in connection_details:
            raise ValueError('Invalid connection details provided')
        connection = establish_connection(**connection_details)
        if not connection:
            raise ConnectionError('Failed to establish database connection')
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except ValueError as ve:
        print(f'ValueError: {ve}')
    except ConnectionError as ce:
        print(f'ConnectionError: {ce}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
def establish_connection(host, user):
    pass

import pymysql
from pymysql.constants import ER as PYMYSQL_ERRLOCK
from dotenv import load_dotenv
import os
load_dotenv()
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
def iterative_prompting_4_print_downloads(download_db):
    required_keys = ['host', 'user', 'password', 'database']
    if not all(key in download_db for key in required_keys):
        raise ValueError("The provided dictionary does not contain the required keys.")
    try:
        connection = pymysql.connect(
            host=download_db['host'],
            user=download_db['user'],
            password=download_db['password'],
            database=download_db['database'],
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        with connection.cursor() as cursor:
            sql = ""
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except pymysql.MySQLError as e:
        if e.args[0] == PYMYSQL_ERRLOCK.CONNECT_ERROR:
            print("Failed to connect to the database. Attempting to reconnect...")
        elif e.args[0] == PYMYSQL_ERRLOCK.CONVERSION_ERROR:
            print("An error occurred during data conversion. Data might be corrupted.")
        elif e.args[0] == PYMYSQL_ERRLOCK.DRIVER_ERROR:
            print("A database driver error occurred. Rechecking database connection parameters...")
        else:
            print(f"An unexpected error occurred at code execution: {e}")
    except Exception as e:
        print(f"An unanticipated exception occurred: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()
            print("Database connection closed safely.")

def iterative_prompting_5_print_downloads(downloadDB):
    try:
        cursor = downloadDB.cursor()
        query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.DatabaseError as e:
        print(f"SQLite error: {e}")
        return None
    except Exception as e:
        print(f"General error: {e}")
        raise
    finally:
        cursor.close() if cursor else None

def few_shots_prompting_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    results = c.fetchall()
    return results

def cot_prompting_printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()
    c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
    result = c.fetchall()
    conn.close()
    return result

def fact_check_list_printDownloads():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;")
        records = cursor.fetchall()
        for record in records:
            print(record)

import mysql.connector
from mysql.connector import Error
def not_interactive_mix_printDownloads(downloadDB):
    try:
        connection = mysql.connector.connect(
            host=downloadDB['host'],
            user=downloadDB['user'],
            password=downloadDB['password'],
            database=downloadDB['database']
        )
        cursor = connection.cursor()
        query = ("SELECT name, source, UNIX_TIMESTAMP(endTime/1000000) AS endTime_unix FROM moz_downloads")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
downloadDB_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

def baseline_printDownloads(downloadDB):
    cursor = downloadDB.cursor()
    query = "SELECT name, source, datetime(endTime/1000000,'unixepoch') FROM moz_downloads;"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

