import sqlite3
from typing import *
import os

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

def persona__printMessages(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute('SELECT datetime(timestamp,''unixepoch''), dialog_partner, author, body_xml FROM Messages;')
	messages = cursor.fetchall()
	formatted_messages = []
	for message in messages:
		timestamp, dialog_partner, author, body_xml = message
		if author.startswith('8:'): author = 'Me'
		if author == 'Me':
			formatted_message = f'To {dialog_partner}: {body_xml}'
		else:
			formatted_message = f'From {author}: {body_xml}'
		formatted_messages.append(formatted_message)
	conn.close()
	return formatted_messages

def template__printMessages(skypeDB):
    try:
        import sqlite3
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute('SELECT datetime(timestamp,''unixepoch''), dialog_partner, author, body_xml FROM Messages;')
        rows = cursor.fetchall()
        formatted_messages = []
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            direction = 'To {}:' if author == '' else 'From {}:'
            message = '{} {}'.format(direction.format(dialog_partner if author == '' else author), body_xml)
            formatted_messages.append(message)
        conn.close()
        return formatted_messages
    except Exception as e:
        return []

def question_refinement__printMessages(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    username = input('Enter your Skype username: ')
    query = "SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages WHERE author=? OR dialog_partner=? ORDER BY timestamp;"
    cursor.execute(query, (username, username))
    messages = []
    for row in cursor.fetchall():
        timestamp, dialog_partner, author, body_xml = row
        if author == username:
            direction = f'To {dialog_partner}:'
        else:
            direction = f'From {author}:'
        messages.append({'timestamp': timestamp, 'direction': direction, 'message_body': body_xml})
    conn.close()
    return messages

def alternative_approaches__printMessages(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        messages = cursor.fetchall()
        formatted_messages = []
        for msg in messages:
            timestamp, dialog_partner, author, body_xml = msg
            direction = f'To {dialog_partner}:' if author == 'YOUR_USERNAME' else f'From {author}: '
            formatted_message = f'{timestamp} {direction} {body_xml}'
            formatted_messages.append(formatted_message)
        conn.close()
        return formatted_messages
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []

def context_manager__printMessages(skypeDB):
    import sqlite3
    con = sqlite3.connect(skypeDB)
    cur = con.cursor()
    cur.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    messages = []
    local_user = cur.execute('SELECT skypename FROM Accounts LIMIT 1;').fetchone()[0]
    for timestamp, dialog_partner, author, body_xml in cur.fetchall():
        if author == local_user:
            direction = f'To {dialog_partner}:'
        else:
            direction = f'From {author}: '
        formatted_message = f'{direction} {body_xml.decode()} ({timestamp})'
        messages.append(formatted_message)
    con.close()
    return messages

def flipped_interaction_3__printMessages(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute('SELECT datetime(timestamp,''unixepoch''), dialog_partner, author, body_xml FROM Messages;')
	results = []
	for row in cursor.fetchall():
		timestamp, dialog_partner, author, body_xml = row
		if 'partlist' not in body_xml:
			if dialog_partner != author:
				direction = f'To {dialog_partner}:'
			else:
				direction = f'From {author}: '
			formatted_message = f'{direction} {body_xml}'
			results.append(formatted_message)
	conn.close()
	return results

def flipped_interaction_4__printMessages(skypeDB):
	import sqlite3
	import logging
	try:
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
		messages = cursor.fetchall()
		formatted_messages = []
		for msg in messages:
			timestamp, dialog_partner, author, body_xml = msg
			if 'partlist' not in body_xml:
				if dialog_partner == author:
					label = 'Self:'
				else:
					label = f'to {dialog_partner}: ' if author != 'your_skype_username' else f'From {author}: '
				formatted_msg = f'{label} {body_xml.replace("<", "").replace(">", "")}'
				formatted_messages.append(formatted_msg)
		return formatted_messages
	except sqlite3.Error as e:
		logging.error(f'Database error: {e}')
	except Exception as e:
		logging.error(f'Unexpected error: {e}')
	finally:
		if conn:
			conn.close()

def flipped_interaction_5__printMessages(skypeDB):
	import sqlite3
	try:
		connection = sqlite3.connect(skypeDB)
		cursor = connection.cursor()
		cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
		messages = cursor.fetchall()
		formatted_messages = []
		for msg in messages:
			if 'partlist' not in msg[3]:
				timestamp, dialog_partner, author, body_xml = msg
				if author == dialog_partner:
					content = body_xml.split('<p>', 1)[1].rsplit('</p>', 1)[0]
					formatted_messages.append(f'To {dialog_partner}: {timestamp} {content}')
				else:
					content = body_xml.split('<p>', 1)[1].rsplit('</p>', 1)[0]
					formatted_messages.append(f'From {author}: {timestamp} {content}')
		return formatted_messages
	except sqlite3.Error as e:
		print(f'SQLite error: {e}')
		return []
	finally:
		if connection:
			connection.close()

def iterative_prompting_3__printMessages(skypeDB):
    import os
    import sqlite3
    if not isinstance(skypeDB, str) or not os.path.isfile(skypeDB):
        raise ValueError("Invalid database file path provided.")
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        messages = []
        for row in cursor.fetchall():
            timestamp, dialog_partner, author, body_xml = row
            if author == "me":
                direction = f"To {dialog_partner}:"
            else:
                direction = f"From {author}:"
            formatted_message = f"{direction} {body_xml}"
            messages.append(formatted_message)
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        if "conn" in locals() and conn:
            conn.close()
    return messages

def iterative_prompting_4__print_messages(skype_db):
    if not isinstance(skype_db, str) or not skype_db.endswith('.sdb') or not os.path.isfile(skype_db):
        raise ValueError('Invalid or non-existent Skype database file path.')
    try:
        conn = sqlite3.connect(f'file:{skype_db}?mode=ro', uri=True)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        messages = []
        for timestamp, dialog_partner, author, body_xml in cursor.fetchall():
            direction = 'Sent' if author == dialog_partner else 'Received'
            message = f"{direction} {dialog_partner if direction == 'Sent' else author}: {body_xml}"
            messages.append(message)
    except sqlite3.Error as e:
        raise RuntimeError(f'Database error: {e}')
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return messages

def iterative_prompting_5__printMessages(skypeDB):
    if not isinstance(skypeDB, str):
        raise ValueError("skypeDB must be a string representing the path to the database file")
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        messages = cursor.fetchall()
        results = []
        for msg in messages:
            timestamp, dialog_partner, author, body_xml = msg
            direction = f'To {dialog_partner}:' if author == dialog_partner else f'From {author}:'
            formatted_message = direction + body_xml
            results.append(formatted_message)
    except sqlite3.Error as e:
        raise RuntimeError("An error occurred accessing the database:" + str(e))
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return results

def few_shots_prompting__printMessages(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
	messages = c.fetchall()
	formatted_messages = []
	for msg in messages:
		timestamp, dialog_partner, author, body_xml = msg
		if author == dialog_partner:
			direction = 'To '
		else:
			direction = 'From '
		formatted_message = f"{direction}{dialog_partner}: {body_xml}"
		formatted_messages.append(formatted_message)
	return formatted_messages

def cot_prompting__printMessages(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
	messages = c.fetchall()
	formatted_messages = []
	for msg in messages:
		timestamp, dialog_partner, author, body_xml = msg
		if author == 'local':
			formatted_message = f'To {dialog_partner}: {body_xml}'
		else:
			formatted_message = f'From {author}: {body_xml}'
		formatted_messages.append(formatted_message)
	conn.close()
	return formatted_messages

def fact_check_list__printMessages(skypeDB):
    conn = sqlite3.connect(skypeDB)
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        formatted_messages = []
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            try:
                body = body_xml.decode('utf-8')
            except AttributeError:
                body = body_xml
            if author == dialog_partner:
                direction = 'Sent to self:'
            elif author == 'your_skype_username':
                direction = f'Sent to {dialog_partner}:'
            else:
                direction = f'From {author}:'
            formatted_message = f'{timestamp} - {direction} {body}'
            formatted_messages.append(formatted_message)
        return formatted_messages
    finally:
        cursor.close()
        conn.close()

def not_interactive_mix__printMessages(skypeDB):
	if not isinstance(skypeDB, str) or not skypeDB.endswith('.db'):
		raise ValueError("Invalid Skype database file path")
	try:
		conn = sqlite3.connect(skypeDB)
	except sqlite3.Error as e:
		raise RuntimeError(f"Failed to connect to Skype database with error: {e}")
	cur = conn.cursor()
	query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
	try:
		cur.execute(query)
		results = cur.fetchall()
	except sqlite3.Error as e:
		conn.close()
		raise RuntimeError(f"SQL error: {e}")
	finally:
		conn.close()
	formatted_messages = []
	for row in results:
		timestamp, partner, author, msg_body = row
		msg_body_clean = msg_body.replace('<[/]?Data>', '')
		direction = f'To {partner}:' if author == partner else f'From {author}:'
		formatted_message = f'{direction} {msg_body_clean} ({timestamp})'
		formatted_messages.append(formatted_message)
	return formatted_messages

def interactive_mix__printMessages(skypeDB):
    if not os.path.exists(skypeDB):
        raise FileNotFoundError(f"The database file at {skypeDB} does not exist.")
    results = []
    try:
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        query = "SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
        c.execute(query)
        for row in c:
            timestamp, dialog_partner, author, body_xml = row
            if 'partlist' not in body_xml:
                try:
                    root = ET.fromstring(body_xml)
                    body_text = root.find(".//text").text
                except ET.ParseError:
                    body_text = "Unable to parse XML"
                if dialog_partner != author:
                    msgDirection = f"To {dialog_partner}: "
                else:
                    msgDirection = f"From {author}: "
                formatted_message = f"{msgDirection}{body_text} (at {timestamp})"
                results.append(formatted_message)
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while accessing the database: {e}")
    finally:
        conn.close()
    return results

def baseline__printMessages(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	cursor = conn.cursor()
	cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
	messages = cursor.fetchall()
	formatted_messages = []
	for msg in messages:
		timestamp, dialog_partner, author, body_xml = msg
		if author == dialog_partner:
			direction = 'To self:'
		elif author == '':
			direction = 'From %s:' % dialog_partner
		else:
			direction = 'To %s:' % dialog_partner if dialog_partner != '' else 'From %s:' % author
		formatted_message = '%s %s %s %s' % (direction, timestamp, author, body_xml)
		formatted_messages.append(formatted_message)
	conn.close()
	return formatted_messages
