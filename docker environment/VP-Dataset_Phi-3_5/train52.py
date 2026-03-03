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
    cursor = msgDB.cursor()
    query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def template_printMessage(msgDB):
    try:
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
        records = msgDB.execute(query).fetchall()
        result = [(record['datetime(date, unixepoch)'], record['address'], record['text']) for record in records]
        return result
    except Exception as e:
        return(f'An error occurred: {e}')
        return None

import psycopg2
import json

def question_refinement_printMessage(conn):
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute()
        rows = cursor.fetchall()
        return [(row[0], row[1], row[2]) for row in rows]
    except Exception as e:
        return None
    finally:
        cursor.close()
        conn.close()

def alternative_approaches_printMessage(msgDB):
    try:
        connection = sqlite3.connect(msgDB)
        cursor = connection.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0"
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return results
    except sqlite3.Error as e:
        return(f'An error occurred: {e}')
        return None

def context_manager_printMessage(msgDB):
    sql = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
    rows = msgDB.execute(sql).fetchall()
    return rows

def iterative_prompting_3_printMessage(msgDB):
    try:
        cursor = msgDB.cursor()
        cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0")
        results = cursor.fetchall()
        return results
    except sqlite3.DatabaseError as e:
        return(f'An error occurred: {e}')
        return None
    except Exception as e:
        return(f'An unexpected error occurred: {e}')
        return None

def iterative_prompting_4_print_message(msgDB):
    try:
        cursor = msgDB.cursor()
        query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()

def iterative_prompting_5_printMessage(msgDB):
    if not isinstance(msgDB, DatabaseConnection):
        raise ValueError("msgDB must be a DatabaseConnection object.")
    connection = None
    try:
        with msgDB.cursor() as cursor:
            cursor.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
            results = cursor.fetchall()
            return results
    except Exception as e:
        return(f"An error occurred: {e}")
        
def few_shots_prompting_printMessage(msgDB):
    conn = sqlite3.connect(msgDB)
    c = conn.cursor()
    c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
    rows = c.fetchall()
    return rows

def cot_prompting_printMessage(msgDB):
    conn = sqlite3.connect(msgDB)
    c = conn.cursor()
    c.execute("SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;")
    rows = c.fetchall()
    return rows

import sqlite3
def fact_check_list_print_message(msgDB):
    conn = sqlite3.connect(msgDB)
    cursor = conn.cursor()
    cursor.execute('SELECT datetime(date, "unixepoch"), address, text FROM message WHERE address > 0')
    messages = cursor.fetchall()
    conn.close()
    return messages

import sqlite3
def not_interactive_mix_printMessage(msgDB):
    conn = sqlite3.connect(msgDB)
    cursor = conn.cursor()
    query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0;"
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        messages = [(datetime, address, text) for (datetime, address, text) in rows]
        return messages
    except sqlite3.Error as e:
        return(f"An error occurred: {e.args[0]}")
    finally:
        conn.close()

def baseline_printMessage(msgDB):
    cursor = msgDB.cursor()
    query = "SELECT datetime(date, 'unixepoch'), address, text FROM message WHERE address > 0"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

