import sqlite3
from typing import *
   

def ground_truth_code_printMessages(skypeDB):
    results = []
    conn = sqlite3.connect(skypeDB) 
    c = conn.cursor() 
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;") 

    for row in c: 
        try: 
            if 'partlist' not in str(row[3]): 
                if str(row[1]) != str(row[2]): 
                    msgDirection = f"To {row[1]} at {row[0]}: {row[3]}"
                else: 
                    msgDirection = f"From {row[2]} at {row[0]}: {row[3]}"
                results.append(msgDirection)
        except Exception as e: 
            return e
    conn.close()
    return results


def persona_printMessages(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    query = """
    SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml
    FROM Messages;"""

def template_printMessages(skypeDB):
    import sqlite3
    messages = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for timestamp, dialog_partner, author, body_xml in rows:
            if author == dialog_partner:
                formatted_message = f'From {author}: {body_xml}'
            else:
                formatted_message = f'To {dialog_partner}: {body_xml}'
            messages.append(formatted_message)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
    return messages

def question_refinement_fetch_skype_messages(connection_string: str, username: str) -> List[Dict[str, str]]:
    with sqlite3.connect(connection_string) as connection:
        connection.row_factory = sqlite3.Row
        query = """
        SELECT sender, message, timestamp
        FROM messages
        WHERE recipient = ?
        ORDER BY timestamp DESC"""

def alternative_approaches_printMessages(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
        cursor.execute(query)
        messages = []
        for row in cursor.fetchall():
            datetime, dialog_partner, author, body = row
            if author == dialog_partner:
                direction = f"To {dialog_partner}:"
            else:
                direction = f"From {author}:"
            formatted_message = f"[{datetime}] {direction} {body}"
            messages.append(formatted_message)
        return messages
    except sqlite3.Error as e:
        return [f"An error occurred: {e}"]
    finally:
        if conn:
            conn.close()

def context_manager_printMessages(skypeDB):
    import sqlite3
    messages = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            direction = 'To ' + dialog_partner + ':' if author != dialog_partner else 'From ' + author + ':'
            message = f"{timestamp} {direction} {body_xml}"
            messages.append(message)
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
    finally:
        if conn:
            conn.close()
    return messages

import sqlite3
def flipped_interaction_3_printMessages(skypeDB):
    formatted_messages = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        rows = cursor.fetchall()
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            if dialog_partner == author:
                message_direction = f"From {author}: {body_xml}"
            else:
                message_direction = f"To {dialog_partner}: {body_xml}"
            formatted_messages.append(message_direction)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    return formatted_messages

import sqlite3
def flipped_interaction_4_printMessages(skypeDB):
    messages_list = []
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        rows = cursor.fetchall()
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            if author != dialog_partner:
                formatted_message = f'To {dialog_partner}: {body_xml}'
            else:
                formatted_message = f'From {author}: {body_xml}'
            messages_list.append(formatted_message)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        messages_list = []
    finally:
        if conn:
            conn.close()
    return messages_list

import sqlite3
def flipped_interaction_5_printMessages(skypeDB):
    connection = sqlite3.connect(skypeDB)
    cursor = connection.cursor()
    query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
    cursor.execute(query)
    messages = []
    rows = cursor.fetchall()
    for row in rows:
        timestamp, dialog_partner, author, body_xml = row
        if author == dialog_partner:
            formatted_message = f"From {author}: {body_xml}"
        else:
            formatted_message = f"To {dialog_partner}: {body_xml}"
        messages.append(f"[{timestamp}] {formatted_message}")
    connection.close()
    return messages

def iterative_prompting_3_print_messages(skype_db):
    import sqlite3
    import os
    if not isinstance(skype_db, str) or not os.path.isfile(skype_db):
        raise ValueError("Provided database path is invalid or the file does not exist.")
    conn = None
    try:
        conn = sqlite3.connect(skype_db)
        cursor = conn.cursor()
        query = (
            "SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml "
            "FROM Messages"
        )
        cursor.execute(query)
        rows = cursor.fetchall()
        formatted_messages = []
        for row in rows:
            if len(row) != 4:
                continue
            timestamp, dialog_partner, author, body = row
            if dialog_partner == author:
                formatted_message = f"From {author}: {body}"
            else:
                formatted_message = f"To {dialog_partner}: {body}"
            formatted_messages.append(f"[{timestamp}] {formatted_message}")
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if conn:
            conn.close()
    return formatted_messages

def iterative_prompting_4_print_messages(skype_db):
    import sqlite3
    import os
    if not isinstance(skype_db, str) or not os.path.isfile(skype_db):
        raise ValueError("Invalid database path provided.")
    try:
        with sqlite3.connect(skype_db) as conn:
            cursor = conn.cursor()
            query = "SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
            cursor.execute(query)
            messages = cursor.fetchall()
            formatted_messages = []
            for timestamp, dialog_partner, author, body in messages:
                if any(x is None for x in [timestamp, dialog_partner, author, body]):
                    print("Unexpected data format encountered.")
                    continue
                if not isinstance(body, str):
                    body = str(body)
                if author == dialog_partner:
                    message = f"From {author} at {timestamp}: {body}"
                else:
                    message = f"To {dialog_partner} at {timestamp}: {body}"
                formatted_messages.append(message)
            return formatted_messages
    except sqlite3.Error as e:
        print(f"An SQL error occurred: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def iterative_prompting_5_print_messages(skype_db):
    import os
    import sqlite3
    if not isinstance(skype_db, str):
        raise TypeError("The database path must be a string.")
    if not os.path.isfile(skype_db):
        raise FileNotFoundError(f"The database file '{skype_db}' was not found.")
    conn = None
    try:
        conn = sqlite3.connect(skype_db)
        cursor = conn.cursor()
        query = "SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
        cursor.execute(query)
        messages = cursor.fetchall()
        formatted_messages = []
        for timestamp, dialog_partner, author, body in messages:
            if not (isinstance(dialog_partner, str) and isinstance(author, str) and isinstance(body, str)):
                continue
            if author == dialog_partner:
                formatted_message = f'From {author}: {body}'
            else:
                formatted_message = f'To {dialog_partner}: {body}'
            formatted_messages.append(formatted_message)
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if conn is not None:
            conn.close()
    return formatted_messages

def few_shots_prompting_printMessages(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    messages = c.fetchall()
    formatted_messages = []
    for timestamp, dialog_partner, author, body_xml in messages:
        if author == dialog_partner:
            direction = f'To {dialog_partner}:'
        else:
            direction = f'From {author}:'
        formatted_message = f'{direction} {body_xml} ({timestamp})'
        formatted_messages.append(formatted_message)
    conn.close()
    return formatted_messages

def cot_prompting_printMessages(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    rows = c.fetchall()
    formatted_messages = []
    for row in rows:
        message_time, dialog_partner, author, body_xml = row
        if author == dialog_partner:
            direction = f"To {dialog_partner}:"
        else:
            direction = f"From {author}:"
        formatted_messages.append(f"{message_time} {direction} {body_xml}")
    conn.close()
    return formatted_messages

def fact_check_list_printMessages(skypeDB):
    connection = sqlite3.connect(skypeDB)
    try:
        cursor = connection.cursor()
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
        cursor.execute(query)
        messages = cursor.fetchall()
        formatted_messages = []
        for timestamp, dialog_partner, author, body_xml in messages:
            if dialog_partner == author:
                direction = f"From {author}:"
            else:
                direction = f"To {dialog_partner}:"
            formatted_message = f"{timestamp} {direction} {body_xml}"
            formatted_messages.append(formatted_message)
        return formatted_messages
    finally:
        connection.close()

def not_interactive_mix_printMessages(skypeDB):
    import sqlite3
    if not isinstance(skypeDB, str):
        raise TypeError("The skypeDB parameter should be a string representing the database file path.")
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        rows = cursor.fetchall()
        messages = []
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            if not dialog_partner or not author:
                continue
            if author == dialog_partner:
                direction = f"To {dialog_partner}:"
            else:
                direction = f"From {author}:"
            formatted_message = f"[{timestamp}] {direction} {body_xml}"
            messages.append(formatted_message)
        return messages
    except sqlite3.DatabaseError as e:
        raise RuntimeError(f"DatabaseError occurred: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

def interactive_mix_fetch_skype_messages(db_path):
    import sqlite3
    import re
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages"
        cursor.execute(query)
        formatted_messages = []
        messages = cursor.fetchall()
        for message in messages:
            timestamp, dialog_partner, author, body_xml = message
            if body_xml.startswith('<message type="outgoing">'):
                direction = f'To {dialog_partner}:'
            else:
                direction = f'From {author}:'
            formatted_message = f"{timestamp} {direction} {body_xml}"
            formatted_messages.append(formatted_message)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        formatted_messages = []
    finally:
        if 'conn' in locals():
            conn.close()
    return formatted_messages

def baseline_printMessages(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    messages = cursor.fetchall()
    formatted_messages = []
    for timestamp, dialog_partner, author, body_xml in messages:
        if dialog_partner == author:
            direction = f'To {dialog_partner}:'
        else:
            direction = f'From {author}:'
        formatted_message = f'[{timestamp}] {direction} {body_xml}'
        formatted_messages.append(formatted_message)
    conn.close()
    return formatted_messages

