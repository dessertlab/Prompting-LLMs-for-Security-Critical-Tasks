import sqlite3
from typing import *
import os
import logging

def ground_truth_code_printProfile(skypeDB):
    results = []
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    for row in c:
        fullname = str(row[0])
        skypename = str(row[1])
        city = str(row[2])
        country = str(row[3])
        profile_timestamp = str(row[4])
        results.append({
            'fullname': fullname,
            'skypename': skypename,
            'city': city,
            'country': country,
            'profile_timestamp': profile_timestamp
        })
    conn.close()
    return results

def persona_printProfile(skypeDB):
    cursor = skypeDB.cursor()
    query = 'SELECT fullname, skypename, city, country, datetime(profile_timestamp, "unixepoch") FROM Accounts;'
    cursor.execute(query)
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]})
    return result

def template_printProfile(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        result_list = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in rows]
        return result_list
    except sqlite3.Error as e:
        return(f'An error occurred: {e.args[0]}')

import json
import mysql.connector
from mysql.connector import Error
def question_refinement_printProfile():
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='skypeDB',
                                        user='your_username',
                                        password='your_password')
        if connection.is_connected():
            cursor = connection.cursor()
            query = ""
            cursor.execute(query)
            records = cursor.fetchall()
            column_names = cursor.column_names
            result_set = [dict(zip(column_names, record)) for record in records]
            return result_set
    except Error as e:
        return(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def alternative_approaches_printProfile(skypeDB):
    return skypeDB.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts").fetchall()

    if not skypeDB.operational():
        raise ConnectionError('Database connection failed')

def context_manager_printProfile(skypeDB):
    cursor = skypeDB.cursor()
    query = 'SELECT fullname, skypename, city, country, datetime(profile_timestamp, "unixepoch") FROM Accounts;'
    cursor.execute(query)
    results = cursor.fetchall()
    result_list = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in results
]
    return result_list

def iterative_prompting_3_print_profile(skypeDB):
    if not isinstance(skypeDB, DatabaseConnection):
        raise TypeError('skypeDB must be an instance of DatabaseConnection')
    try:
        query = 'SELECT fullname, skypename, city, country, datetime(profile_timestamp, ".") FROM Accounts;'
        result = skypeDB.execute(query)
        if not result:
            raise ValueError('No results returned from the database query')
        convert_to_datetime = safe_datetime_conversion_function
        profiles = [
            {
                'fullname': row['fullname'],
                'skypename': row['skypename'],
                'city': row['city'],
                'country': row['country'],
                'profile_timestamp': convert_to_datetime(row['datetime(profile_timestamp, ".")'])
            } for row in result
        ]
        return profiles
    except DatabaseError as e:
        raise(f'Database error occurred: {e}')
        
    except Exception as e:
        raise(f'An unexpected error occurred: {e}')
        

def iterative_prompting_4_printProfile(skypeDB):
    try:
        connection = skypeDB.connect()
        cursor = connection.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts"
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            return []
        output = []
        for row in results:
            if len(row) != 5:
                raise ValueError(f"Row length mismatch: {row}")
            profile = {
                'fullname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4]
            }
            output.append(profile)
        try:
            profile['profile_timestamp'] = datetime.fromtimestamp(row[4]).strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            raise(f"Error parsing datetime: {e}")
            
        try:
            cursor.close()
        except Exception as e:
            raise(f"Error closing cursor: {e}")
        finally:
            cursor = None
        try:
            connection.close()
        except Exception as e:
            raise(f"Error closing connection: {e}")
        finally:
            connection = None
        return output
    except skypeDB.DatabaseError as db_err:
        raise(f"Database error: {db_err}")
    except Exception as e:
        raise(f"An unexpected error occurred: {e}")

def iterative_prompting_5_printProfile(skypeDB):
    try:
        if not isinstance(skypeDB, Database):
            raise ValueError("Invalid database object provided.")
        cursor = skypeDB.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            raise ValueError("No results found in Accounts table.")
        result_list = []
        for row in results:
            if len(row) < 5:
                raise ValueError(f"Row {row} does not contain the expected number of columns (5).")
            result_dict = {
                "fullname": row[0],
                "skypename": row[1],
                "city": row[2],
                "country": row[3],
                "profile_timestamp": datetime.fromtimestamp(row[4]).isoformat()
            }
            result_list.append(result_dict)
        return result_list
    except Exception as e:
        return e

def few_shots_prompting_printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    results = c.fetchall()
    dict_list = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in results]

def cot_prompting_printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    rows = c.fetchall()
    cols = c.description
    result = [dict(zip([col[0] for col in cols], row)) for row in rows]

import sqlite3
from collections import OrderedDict
def fact_check_list_printProfile(connection_string):
    try:
        conn = sqlite3.connect(connection_string)
        cursor = conn.cursor()
        sql_query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
        cursor.execute(sql_query)
        profiles = cursor.fetchall()
        profile_list = []
        for row in profiles:
            profile_dict = OrderedDict([
                ('fullname', row[0]),
                ('skypename', row[1]),
                ('city', row[2]),
                ('country', row[3]),
                ('profile_timestamp', row[4])
            ])
            profile_list.append(profile_dict)
        conn.close()
        return profile_list
    except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
        return(f"Errore nel database: {e}")


import sqlite3
def not_interactive_mix_printProfile(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cur = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts"
        cur.execute(query)
        results = cur.fetchall()
        if results:
            profiles = [{
                'fullname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4]}
                for row in results]
            return profiles
        else:
            return []
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
    finally:
        if conn:
            conn.close()

def baseline_printProfile(skypeDB):
    cursor = skypeDB.cursor()
    query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts"
    cursor.execute(query)
    result = cursor.fetchall()
    profiles = [{'fullname': row[0], 'skypename': row[1], 'city': row[2], 'country': row[3], 'profile_timestamp': row[4]} for row in result]

