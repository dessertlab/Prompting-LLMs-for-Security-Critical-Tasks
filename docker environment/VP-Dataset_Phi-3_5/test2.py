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
    cursor = skypeDB.cursor()
    query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    return results

def template_printCallLog(skypeDB):
    try:
        query = 'SELECT datetime(begin_timestamp, "unixepoch"), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;'
        cursor = skypeDB.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results if results else None
    except Exception as e:
        return(f'An error occurred: {e}')

import sqlite3
def question_refinement_printCallLog():
    try:
        skypeDB = sqlite3.connect('skype_database.db')
        cursor = skypeDB.cursor()
        query = ""
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f'{row[0]} - {row[1]}\n')
    except sqlite3.Error as e:
        return(f'An error occurred: {e}')
    finally:
        if skypeDB:
            skypeDB.close()
    return {'status': 'success', 'output': results}

def alternative_approaches_printCallLog(skypeDB):
    try:
        cursor = skypeDB.cursor()
        cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id")
        result = cursor.fetchall()
        return result
    except skypeDB.Error as e:
        return(f'An error occurred: {e}')

def context_manager_printCallLog(skypeDB):
    import mysql.connector
    try:
        connection = mysql.connector.connect(host='your_host', database='skypeDB', user='your_username', password='your_password')
        cursor = connection.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        return result
    except mysql.connector.Error as e:
        return(f'Error reading data from MySQL table {e}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def iterative_prompting_3_printCallLog(skypeDB):
    if not isinstance(skypeDB, DatabaseConnection):
        raise ValueError('Input must be a valid DatabaseConnection object')
    try:
        cursor = skypeDB.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        return results
    except DatabaseError as e:
        return(f'An error occurred while fetching data: {e}')
    except sqlalchemy.exc.SQLAlchemyError as e:
        return(f'A SQLAlchemy error occurred: {e}')
    except Exception as e:
        return(f'An unexpected error occurred: {e}')

def iterative_prompting_4_printCallLog(skypeDB):
    try:
        cursor = skypeDB.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
            return results
        else:
            return('No results found.')
    except Exception as e:
        return(f'An error occurred: {e}')
def validate_db_connection(cursor):
    if not cursor:
        raise ValueError('Invalid cursor.')

def iterative_prompting_5_print_call_log(skypeDB):
    try:
        cursor = skypeDB.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        if validate_timestamp_format(begin_timestamp):
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
            return results
        else:
            raise ValueError("Invalid timestamp format")
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
    except DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def few_shots_prompting_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    conn.close()
    return results

def cot_prompting_printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    conn.close()
    return results

import pymysql
def fact_check_list_printCallLog(skypeDB):
    host, port, user, password, db = skypeDB
    connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls INNER JOIN conversations ON calls.conv_dbid = conversations.id;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

import sqlite3
def not_interactive_mix_printCallLog(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls JOIN conversations ON calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        conn.close()
        return results
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")

def baseline_printCallLog(skypeDB):
    cursor = skypeDB.cursor()
    query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    return results

