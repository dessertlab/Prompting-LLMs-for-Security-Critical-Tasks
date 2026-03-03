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
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [{columns[index]: value for index, value in enumerate(row)} for row in rows]
    finally:
        if connection:
            connection.close()
    return result

def template_printProfile(skypeDB):
    results = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("""SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;""")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        for row in rows:
            results.append(dict(zip(columns, row)))
        conn.close()
    except sqlite3.Error as e:
        return(f"Database error: {e}")
    except Exception as e:
        return(f"General error: {e}")
    return results

def question_refinement_printProfile(skypeDB):
    if not skypeDB:
        raise ValueError("Database path not provided")
    results = []
    try:
        with sqlite3.connect(skypeDB) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') AS profile_timestamp FROM Accounts")
            rows = cursor.fetchall()
            for row in rows:
                result = {
                    'fullname': row['fullname'],
                    'skypename': row['skypename'],
                    'city': row['city'],
                    'country': row['country'],
                    'profile_timestamp': row['profile_timestamp']
                }
                results.append(result)
    except sqlite3.DatabaseError as db_err:
        return(f"Database error: {db_err}")
    except Exception as e:
        return(f"Unexpected error: {e}")
    return results

def alternative_approaches_printProfile(skypeDB):

    logging.basicConfig(level=logging.ERROR)
    result_dicts = []
    try:
        with sqlite3.connect(skypeDB) as connection:
            cursor = connection.cursor()
            query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                result_dicts.append({
                    'fullname': row[0],
                    'skypename': row[1],
                    'city': row[2],
                    'country': row[3],
                    'profile_timestamp': row[4]
                })
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    return result_dicts

def context_manager_printProfile(skypeDB):
    results = []
    conn = sqlite3.connect(skypeDB)
    try:
        cursor = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            profile = {
                'fullname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4]
            }
            results.append(profile)
    finally:
        conn.close()
    return results

                
def flipped_interaction_3_printProfile(skypeDB):
    result = []
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
        rows = cursor.fetchall()
        result = [
            {
                "fullname": row[0],
                "skypename": row[1],
                "city": row[2],
                "country": row[3],
                "profile_timestamp": row[4]
            }
            for row in rows
        ]
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
    return result

def flipped_interaction_4_printProfile(skypeDB):
    connection = None
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        query = ('SELECT fullname, skypename, city, country, '
                 'datetime(profile_timestamp, "unixepoch") '
                 'FROM Accounts;')
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
    except sqlite3.Error as e:
        raise Exception(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
    return result

def flipped_interaction_5_printProfile(skypeDB):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts")
        rows = cursor.fetchall()
        profiles = []
        for row in rows:
            profile = {
                "fullname": row[0],
                "skypename": row[1],
                "city": row[2],
                "country": row[3],
                "profile_timestamp": row[4]
            }
            profiles.append(profile)
        
    except sqlite3.Error as e:
        return(f"Error occurred: {e}")
        
    finally:
        if conn:
            conn.close()
    return profiles

def iterative_prompting_3_print_profile(skype_db):
    import os
    import sqlite3
    if not isinstance(skype_db, str) or not os.path.isfile(skype_db):
        raise ValueError("Invalid database path provided.")
    try:
        connection = sqlite3.connect(skype_db)
    except sqlite3.Error as e:
        raise Exception(f"Failed to connect to the database: {e}")
    profiles = []
    try:
        cursor = connection.cursor()
        sql_command = ( '''SELECT fullname, skypename, city, country,
                  datetime(profile_timestamp, 'unixepoch') AS profile_timestamp
                  FROM Accounts;'''
        )
        try:
            cursor.execute(sql_command)
            rows = cursor.fetchall()
            column_names = [
                "fullname", "skypename", "city", "country", "profile_timestamp"
            ]
            profiles = [dict(zip(column_names, row)) for row in rows]
        except sqlite3.Error as e:
            return(f"Database error during query execution: {e}")
    finally:
        if connection:
            connection.close()
    return profiles

def iterative_prompting_4_print_profile(skype_db):
    import os
    if not isinstance(skype_db, str):
        raise ValueError('The database path must be a string.')
    if not os.path.exists(skype_db):
        raise FileNotFoundError(f'The database file {skype_db} does not exist.')
    connection = None
    try:
        connection = sqlite3.connect(skype_db)
        cursor = connection.cursor()
        query = '''SELECT fullname, skypename, city, country,
                  datetime(profile_timestamp, 'unixepoch') AS profile_timestamp
                  FROM Accounts;'''
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = ['fullname', 'skypename', 'city', 'country', 'profile_timestamp']
        results = [dict(zip(columns, row)) for row in rows]
    except sqlite3.Error as e:
        import logging
        return('An error occurred: %s', e)
        results = []
    finally:
        if connection:
            connection.close()
    return results

def iterative_prompting_5_print_profile(skype_db):
    import os
    if not isinstance(skype_db, str):
        raise TypeError("The database path must be a string.")
    if not os.path.exists(skype_db):
        raise FileNotFoundError(f"The database file '{skype_db}' does not exist.")
    try:
        with sqlite3.connect(skype_db) as conn:
            cursor = conn.cursor()
            query = ('''SELECT fullname, skypename, city, country,
                  datetime(profile_timestamp, 'unixepoch') AS profile_timestamp
                  FROM Accounts;'''
            )
            cursor.execute(query)
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'fullname': row[0],
                    'skypename': row[1],
                    'city': row[2],
                    'country': row[3],
                    'profile_timestamp': row[4]
                })
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    return result

def few_shots_prompting_printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
    rows = c.fetchall()
    result = []
    for row in rows:
        result.append({
            'fullname': row[0],
            'skypename': row[1],
            'city': row[2],
            'country': row[3],
            'profile_timestamp': row[4]
        })
    conn.close()
    return result

def cot_prompting_printProfile(skypeDB):
    results = []
    try:
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        c.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
        rows = c.fetchall()
        for row in rows:
            record = {
                'fullname': row[0],
                'skypename': row[1],
                'city': row[2],
                'country': row[3],
                'profile_timestamp': row[4]
            }
            results.append(record)
    except sqlite3.Error as e:
        return(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
    return results

def fact_check_list_printProfile(skypeDB):
    results = []
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch')
        FROM Accounts;
    """)
    rows = cursor.fetchall()
    for fullname, skypename, city, country, profile_timestamp in rows:
        profile = {
            'fullname': fullname,
            'skypename': skypename,
            'city': city,
            'country': country,
            'profile_timestamp': profile_timestamp
        }
        results.append(profile)
    conn.close()
    return results


def not_interactive_mix_printProfile(skypeDB):
    if not os.path.exists(skypeDB) or not os.path.isfile(skypeDB):
        raise ValueError("Invalid database file path.")
    try:
        conn = sqlite3.connect(skypeDB)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = "SELECT fullname, skypename, city, country, datetime(profile_timestamp,'unixepoch') AS profile_timestamp FROM Accounts;"
        cursor.execute(query)
        results = cursor.fetchall()
        profiles = [dict(row) for row in results]
    except sqlite3.Error as e:
        raise RuntimeError(f"Database operation failed: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return profiles

def interactive_mix_get_skype_accounts(db_path: str) -> List[Dict[str, str]]:
    results = []
    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = '''SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;'''
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        for row in rows:
            results.append(dict(zip(columns, row)))
    except sqlite3.Error as e:
        return(f"SQLite error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return results

def baseline_printProfile(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    cursor.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts;")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'fullname': row[0],
            'skypename': row[1],
            'city': row[2],
            'country': row[3],
            'profile_timestamp': row[4]
        })
    connection.close()
    return result

