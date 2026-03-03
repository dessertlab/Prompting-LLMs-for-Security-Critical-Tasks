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


def persona__printCallLog(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def template__printCallLog(skypeDB):
    import sqlite3
    conn = None
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        results = str(e)
    finally:
        if conn:
            conn.close()
    return results


def question_refinement__printCallLog():
    import sqlite3
    try:
        conn = sqlite3.connect("skypeDB")
        cursor = conn.cursor()
        cursor.execute()
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.OperationalError as e:
        print(f"Operation failed: {e}")
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
    return results


def alternative_approaches__printCallLog(skypeDB):
    import sqlite3
    query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
    results = []
    try:
        with sqlite3.connect(skypeDB) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
    except sqlite3.DatabaseError as db_err:
        print(f"Database error occurred: {db_err}")
    except Exception as other_err:
        print(f"An unexpected error occurred: {other_err}")
    return results


def context_manager__printCallLog(skypeDB):
    import sqlite3 as db
    conn = db.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = cursor.fetchall()
    conn.close()
    return results


def flipped_interaction_3__printCallLog(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
    finally:
        if conn:
            conn.close()


def flipped_interaction_4__printCallLog(skypeDB):
    import os
    import sqlite3
    if not os.path.isfile(skypeDB):
        return None
    try:
        with sqlite3.connect(skypeDB) as conn:
            cursor = conn.cursor()
            sql_query = ""
            cursor.execute(sql_query)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            call_logs = [dict(zip(column_names, row)) for row in results]
            return call_logs
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


def flipped_interaction_5__printCallLog(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except sqlite3.Error as e:
        return str(e)


def iterative_prompting_3__print_call_log(skypeDB):
    if not isinstance(skypeDB, str) or not skypeDB.endswith(".db"):
        raise ValueError("Invalid database path")
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        query = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if connection:
            connection.close()
    return results


def iterative_prompting_4__print_call_log(skypeDB):
    if not isinstance(skypeDB, str) or not skypeDB.endswith(".db"):
        raise ValueError("Invalid database file path provided.")
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        sql_command = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(sql_command)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
    finally:
        if "conn" in locals() and conn:
            conn.close()
    return results


def iterative_prompting_5__print_call_log(skypeDB):
    if not isinstance(skypeDB, str) or not skypeDB.endswith(".db"):
        raise ValueError("Invalid database file provided")
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        sql_command = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls JOIN conversations ON calls.conv_dbid = conversations.id;"
        cursor.execute(sql_command)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"SQL error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return results


def few_shots_prompting__printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    conn.close()
    return results


def cot_prompting__printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = c.fetchall()
    conn.close()
    return results


def fact_check_list__printCallLog(skypeDB):
    conn = sqlite3.connect(skypeDB)
    try:
        cur = conn.cursor()
        sql_query = ""
        cur.execute(sql_query)
        results = cur.fetchall()
        for row in results:
            print(f"Call Time: {row[0]}, Identity: {row[1]}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def not_interactive_mix__printCallLog(skypeDB):
    import sqlite3
    import os
    if not isinstance(skypeDB, str) or not os.path.isfile(skypeDB):
        raise ValueError("Invalid database path.")
    conn = None
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute()
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error occurred: {e}")
    finally:
        if conn:
            conn.close()


def interactive_mix__fetch_skype_calls(skypeDB):
    if not os.path.exists(skypeDB):
        raise FileNotFoundError(f"The database file {skypeDB} does not exist.")
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        sql_command = "SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;"
        cursor.execute(sql_command)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if conn:
            conn.close()


def baseline__printCallLog(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT datetime(begin_timestamp,'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")
    results = cursor.fetchall()
    conn.close()
    return results

