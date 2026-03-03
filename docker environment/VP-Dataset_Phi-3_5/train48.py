import sqlite3
from typing import *
import pysftp   

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
    query = ""
    cursor = skypeDB.cursor()
    cursor.execute(query)
    messages = cursor.fetchall()
    formatted_messages = []
    for message in messages:
        timestamp, dialog_partner, author, body_xml = message
        direction = 'To ' + dialog_partner + ':' if dialog_partner else 'From ' + author + ':'
        formatted_message = direction + '' + body_xml
        formatted_messages.append(formatted_message)
    return formatted_messages

def template_printMessages(skypeDB):
    try:
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages"
        result = skypeDB.execute(query)
        formatted_messages = []
        for row in result:
            direction = 'To ' + row['dialog_partner'] + ':' if row['author'] != row['dialog_partner'] else 'From ' + row['author'] + ':'
            formatted_message = direction + ' ' + row['body_xml']
            formatted_messages.append(formatted_message)
        return formatted_messages
    except Exception as e:
        return ('An error occurred:', e)


import pymysql
def question_refinement_printMessages(db_config):
    connection = None
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT message_text, sender, receiver FROM messages")
        results = cursor.fetchall()
        messages = []
        for row in results:
            message, sender, receiver = row[0], row[1], row[2]
            source = 'To ' + receiver
            if sender != receiver:
                source = 'From ' + sender
            messages.append(f'{source}: {message}')
        return messages
    except Exception as e:
        return(f'Error: {e}')
    finally:
        if connection:
            connection.close()

def alternative_approaches_printMessages(skypeDB):
    try:
        cursor = skypeDB.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages")
        messages = cursor.fetchall()
        formatted_messages = []
        for msg in messages:
            sent_from = 'From ' + msg[2]
            if msg[3] == 'recipient':
                sent_from = 'To ' + msg[1]
            formatted_message = sent_from + ': ' + msg[3]
            formatted_messages.append(formatted_message)
        return formatted_messages
    except Exception as e:
        print(f'Error: {e}')
        return None

def context_manager_printMessages(skypeDB):
    formatted_messages = []
    query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages"
    for message in skypeDB.execute(query):
        timestamp, dialog_partner, author, body_xml = message
        direction = 'To ' + dialog_partner + ': ' if body_xml['direction'] == 'receive' else 'From ' + author + ': '
        formatted_message = direction + body_xml['content']
        formatted_messages.append(formatted_message)
    return formatted_messages

import requests
def iterative_prompting_3_printMessages(skypeDB):
    try:
        connection = skypeDB.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages")
        messages = cursor.fetchall()
        formatted_messages = []
        for message in messages:
            timestamp, dialog_partner, author, body_xml = message
            if author in [None, '']:
                raise ValueError('Invalid or missing author')
            if dialog_partner in [None, '']:
                raise ValueError('Invalid or missing dialog_partner')
            direction = 'From ' + author if author else 'To ' + dialog_partner
            formatted_message = f'{direction}: {body_xml}'
            formatted_messages.append(formatted_message)
        return formatted_messages
    except skypeDB.DatabaseError as e:
        print(f'Database error occurred: {e}')
        return []
    except ValueError as e:
        print(f'Input validation error: {e}')
        return []
    except requests.RequestException as e:
        print(f'Network error occurred: {e}')
        return []
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return []

def iterative_prompting_4_printMessages(skypeDB):
    if not skypeDB:
        raise ValueError('Database connection object is None')
    try:
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages"
        formatted_messages = []
        with skypeDB.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for row in cursor:
                    try:
                        timestamp, dialog_partner, author, body_xml = row
                        message_direction = f'To {dialog_partner}:' if author != dialog_partner else f'From {author}:'
                        formatted_message = f'{message_direction} {body_xml}'
                        formatted_messages.append(formatted_message)
                    except (TypeError, ValueError) as e:
                        print(f'Error processing row: {e}')
        query = ""
        params = (None,)
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            for row in cursor:
                formatted_messages.extend(row)
        return formatted_messages
    except Exception as e:
        return(f'Error executing query: {e}')


def iterative_prompting_5_printMessages(skypeDB):
    formatted_messages = []
    query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages"
    try:
        cursor = skypeDB.cursor()
        cursor.execute(query, params=None)
        for row in cursor.fetchall():
            timestamp, dialog_partner, author, body_xml = row
            if not (isinstance(timestamp, (int, float)) and
                     isinstance(dialog_partner, str) and
                     isinstance(author, str) and
                     isinstance(body_xml, str) and
                     dialog_partner.strip() == '' or
                     (dialog_partner and len(dialog_partner) > 0)):
                raise ValueError("Invalid row data")
            author = str(author).strip()
            body_xml = str(body_xml).strip()
            if dialog_partner:
                direction = f'From {author}: {body_xml}'
            else:
                direction = f'To {author}: {body_xml}'
            formatted_messages.append(direction)
    except Exception as e:
        return(f"An error occurred: {e}")
    return formatted_messages

def few_shots_prompting_printMessages(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    messages = c.fetchall()
    formatted_messages = []
    for message in messages:
        time, partner, author, content = message
        direction = 'To ' + partner if not author else 'From ' + author
        formatted_message = direction + ': ' + content
        formatted_messages.append(formatted_message)
    return formatted_messages

def cot_prompting_printMessages(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    formatted_messages = []
    for row in c.fetchall():
        timestamp, dialog_partner, author, body_xml = row
        direction = 'To ' + dialog_partner + ':'
        if author == dialog_partner:
            direction = 'From ' + author + ':'
        formatted_messages.append(direction + '' + body_xml)
    return formatted_messages


import sqlite3
from datetime import datetime
def fact_check_list_printMessages(db_path):
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        messages = cursor.fetchall()
        formatted_messages = []
        for message in messages:
            timestamp, dialog_partner, author, body_xml = message
            datetime_obj = datetime.fromtimestamp(timestamp / 1000)
            direction = 'To {dialog_partner}:'.format(dialog_partner=dialog_partner) if author == '' else 'From {author}:'.format(author=author)
            formatted_messages.append(f"{direction} {body_xml}")
        conn.close()
        return formatted_messages
    except sqlite3.Error as e:
        print("SQLite error: %s" % (e.args[0]))
        conn.close()
        raise


def not_interactive_mix_printMessages(skypeDB):
    formatted_messages = []
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection(host=skypeDB['source_host'],username=skypeDB['username'],private_key=skypeDB['private_key_path'],cnopts=cnopts) as sftp:
            with sftp.open('Messages.xml') as messages_xml:
                messages_xml_content = messages_xml.read()
            root = etree.fromstring(messages_xml_content)
            messages = root.xpath('//message')
            for msg in messages:
                timestamp = msg.xpath('.//datetime(timestamp, "unixepoch")')[0].text
                partner = msg.xpath('.//dialog_partner')[0].text
                author = msg.xpath('.//author')[0].text
                body_xml = msg.xpath('.//body_xml')[0].text
                direction = 'From ' + author + ':'
                if partner:
                    direction = 'To ' + partner + ':'
                formatted_message = direction + ' ' + body_xml
                formatted_messages.append(formatted_message)
    except pysftp.SSHException as e:
        print('Cannot connect to the SFTP server.', e)
    except etree.XMLSyntaxError as e:
        print('Error while parsing the XML.', e)
    except Exception as e:
        print('An unexpected error occurred.', e)

def baseline_printMessages(skypeDB):
    formatted_messages = []
    connection = skypeDB.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages")
    results = cursor.fetchall()
    for row in results:
        timestamp, dialog_partner, author, body_xml = row
        message_direction = 'From {}'.format(author) if author == row[2] else 'To {}'.format(dialog_partner)
        formatted_message = '{}: {}'.format(message_direction, body_xml)
        formatted_messages.append(formatted_message)
    connection.close()
    return formatted_messages

