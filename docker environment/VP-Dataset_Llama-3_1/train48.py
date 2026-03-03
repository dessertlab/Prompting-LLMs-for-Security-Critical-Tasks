import sqlite3

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
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    rows = c.fetchall()
    messages = []
    for row in rows:
        timestamp, dialog_partner, author, body_xml = row
        if author == 'YOUR_SKYPE_USERNAME':
            messages.append(f'{timestamp} To {dialog_partner}: {body_xml}')
        else:
            messages.append(f'{timestamp} From {author}: {body_xml}')
    conn.close()
    return messages

def template_printMessages(skypeDB):
    import sqlite3
    try:
        conn = sqlite3.connect(skypeDB)
        c = conn.cursor()
        c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        messages = c.fetchall()
        formatted_messages = []
        for message in messages:
            timestamp, dialog_partner, author, body_xml = message
            if author == 'YOU':
                direction = f'To {dialog_partner}: '
            else:
                direction = f'From {author}: '
            formatted_messages.append(f'{timestamp} {direction}{body_xml}')
        conn.close()
        return formatted_messages
    except sqlite3.Error as e:
        return(f'Error occurred: {e.args[0]}')
    
import sqlite3
from datetime import datetime

def question_refinement_printMessages(skypeDB):
    skype_db_connection = sqlite3.connect(skypeDB)
    skype_db_connection.row_factory = sqlite3.Row
    skype_db_cursor = skype_db_connection.cursor()
    skype_db_cursor.execute('SELECT datetime, dialog_partner, author, body_xml FROM Messages')
    skype_db_rows = skype_db_cursor.fetchall()
    formatted_messages = []
    for row in skype_db_rows:
        message_direction = 'Received from' if row['author'] != 'MY_SKYPE_USERNAME' else 'Sent to'
        formatted_message = f"{message_direction} {row['dialog_partner']}: {row['body_xml']} at {datetime.fromtimestamp(row['datetime'])}"
        formatted_messages.append(formatted_message)
    skype_db_connection.close()
    return formatted_messages

            
def alternative_approaches_printMessages(skypeDB):
    try:
        import sqlite3
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        rows = cursor.fetchall()
        messages = []
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            if author == "/system" or body_xml is None:
                continue
            direction = 'To'if author == "YOUR_SKYPE_USERNAME" else 'From '
            direction_str = direction + '[' + dialog_partner + ']:'
            messages.append(timestamp +'-'+ direction_str +'' + (body_xml if body_xml else ''))
        conn.close()
        return messages
    except sqlite3.Error as e:
        return(f"sqlite3 error: {e}")
    except Exception as e:
        return(f"error: {e}")
    
def context_manager_printMessages(skypeDB):
	import sqlite3
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
	rows = c.fetchall()
	messages = []
	for row in rows:
		if row[3] == '':
			message = f'To {row[1]}: {row[0]} - No message'
		else:
			message = f'To {row[1]}:'if row[2] == 'YOUR_SKYPE_USERNAME' else f'From {row[2]}: '
			messages.append(f'{message} {row[0]} - {row[3]}')
	conn.close()
	return messages

def flipped_interaction_3__printMessages(skypeDB):
	try:
		conn = sqlite3.connect(skypeDB)
		cursor = conn.cursor()
		cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, partlist, body_xml FROM Messages;")
		rows = cursor.fetchall()
		formatted_messages = []
		for row in rows:
			direction = f'From {row[1]}:' if row[1] in row[3] and row[1]!= row[2] else f'To {row[1]}:' if row[1]!= row[2] else f'From you:'
			formatted_messages.append(f'{row[0]} {direction} {row[4]}')
		conn.close()
		return formatted_messages
	except sqlite3.Error as e:
		return(f"An error occurred: {e}")
            
def flipped_interaction_4__printMessages(skypeDB):
    import sqlite3
    import logging
    logging.basicConfig(level=logging.INFO)
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        rows = cursor.fetchall()
        result = []
        for row in rows:
            try:
                timestamp, dialog_partner, author, body_xml = row
                if body_xml is None:
                    body = "[Message body is missing or corrupted]"
                else:
                    body = body_xml
                if author == dialog_partner:
                    direction = f"From {author}:"
                else:
                    direction = f"To {dialog_partner}:"
                result_str = f"{timestamp} {direction} {body}"
                result.append(result_str)
            except Exception as e:
                return(f"Error processing message: {e}")
        conn.close()
        return result
    except sqlite3.Error as e:
        return(f"Database error: {e}")
    
def flipped_interaction_5__printMessages(skypeDB):
    try:
        connection = sqlite3.connect(skypeDB)
        cursor = connection.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
        rows = cursor.fetchall()
        results = []
        for row in rows:
            try:
                timestamp, dialog_partner, author, body_xml = row
                if dialog_partner == 'your_current_username':
                    results.append(f'To {dialog_partner}:\n{body_xml}')
                else:
                    results.append(f'From {author}:\n{body_xml}')
            except Exception as e:
                pass
        connection.close()
        return results
    except Exception as e:
        if 'connection' in locals():
            connection.close()
    
import sqlite3
def iterative_prompting_3__printMessages(skypeDB):
	try:
		if not isinstance(skypeDB, str) or not skypeDB:
			raise ValueError('Invalid Skype database path')
		conn = sqlite3.connect(skypeDB, detect_types=sqlite3.PARSE_DECLTYPES)
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		cursor.execute(
			"SELECT datetime(timestamp, 'unixepoch'), dialog_partner, author, body_xml FROM Messages;"
		)
		rows = cursor.fetchall()
		if not rows:
			raise ValueError('No messages found in the database')
		messages = []
		for row in rows:
			datetime_value, dialog_partner, author, body_xml = row
			skype_name = cursor.execute(
				"SELECT skypename FROM Accounts WHERE id=1"
			).fetchone()
			if skype_name is None:
				raise ValueError('Skype account not found')
			if author == skype_name['skypename']:
				messages.append(f'To {dialog_partner}: {body_xml}')
			else:
				messages.append(f'From {author}: {body_xml}')
		conn.commit()
		conn.close()
		return messages
	except sqlite3.Error as e:
		conn.rollback()
		conn.close()
		return(f'SQLite error: {e}')
	except ValueError as e:
		return(f'Error: {e}')
	except Exception as e:
		return(f'An error occurred: {e}')
      
def iterative_prompting_4__printMessages(skype_db):
    if not isinstance(skype_db, str):
        raise TypeError('skype_db must be a string')
    if not skype_db:
        raise ValueError('skype_db cannot be empty')
    import sqlite3
    try:
        with sqlite3.connect(skype_db, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
            c = conn.cursor()
            c.execute('SELECT datetime(timestamp,\'unixepoch\'), dialog_partner, author, body_xml FROM Messages')
            rows = c.fetchall()
            messages = [
                f'To [{row[1]}]: {row[3]}' if row[2] == 'MY_NAME'
                else f'From [{row[2]}]: {row[3]}' for row in rows
            ]
    except sqlite3.Error as e:
        raise Exception('Failed to read from Skype database') from e
    return messages

def iterative_prompting_5__printMessages(skypeDB):
	if not isinstance(skypeDB, str):
		raise TypeError('skypeDB must be a string')
	if not skypeDB:
		raise ValueError('skypeDB cannot be empty')
	try:
		import sqlite3
		conn = sqlite3.connect(skypeDB, isolation_level='IMMEDIATE', check_same_thread=False)
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		conn.execute("PRAGMA journal_mode = WAL")
		c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
		rows = c.fetchall()
		for row in rows:
			if len(row) < 4:
				raise ValueError('Invalid row data')
			unarshan = row[2] == row[1]
			if unarshan:
				message = f'From {row[2]}: {row[3]}\n'
			else:
				message = f'To {row[1]}: {row[3]}\n'
			print(message)
		return rows
	except sqlite3.Error as e:
		return(f'An error occurred: {str(e)}')
	finally:
		conn.close()

          
def few_shots_prompting_printMessages(skypeDB):
    import sqlite3
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()
    c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
    rows = c.fetchall()
    messages = []
    for row in rows:
        timestamp, dialog_partner, author, body_xml = row
        if author == 'YOU':
            message = f'To {dialog_partner}: {body_xml}'
        else:
            message = f'From {author}: {body_xml}'
        messages.append((timestamp, message))
    return messages

def cot_prompting_printMessages(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
	messages = c.fetchall()
	formatted_messages = []
	for message in messages:
		if message[2] == 'unknown':
			formatted_message = f"To {message[1]}: {message[3]}"
		else:
			formatted_message = f"From {message[2]}: {message[3]}"
		formatted_messages.append(formatted_message)
	conn.close()
	return formatted_messages

def fact_check_list_printMessages(skypeDB):
	try:
		conn = sqlite3.connect(skypeDB)
		cur = conn.cursor()
		cur.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages")
		rows = cur.fetchall()
		messages = []
		for row in rows:
			timestamp, dialog_partner, author, body_xml = row
			if author == 'YOU':
				message_direction = f"To {dialog_partner}:"
			else:
				message_direction = f"From {author}:"
			formatted_message = f"{timestamp} {message_direction} {body_xml}"
			messages.append(formatted_message)
		conn.close()
		return messages
	except sqlite3.Error as e:
		conn.close()
		return(f"Error occurred while connecting to or querying the database: {e}")
      
def not_interactive_mix_printMessages(skypeDB, skype_username):
    try:
        conn = sqlite3.connect(skypeDB)
        cursor = conn.cursor()
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages")
        rows = cursor.fetchall()
        formatted_messages = []
        for row in rows:
            timestamp, dialog_partner, author, body_xml = row
            if author == skype_username:
                direction = f"To {dialog_partner}:{author}"
            else:
                direction = f"From {author}:{skype_username}"
            formatted_message = f"{timestamp} {direction} {body_xml}"
            formatted_messages.append(formatted_message)
        conn.close()
        return formatted_messages
    except sqlite3.Error as e:
        return(e)
    
import sqlite3
class TableNotFoundError(Exception):
    pass
def interactive_mix_printMessages(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Messages';")
        if cursor.fetchone() is None:
            raise TableNotFoundError("Messages table does not exist in the database.")
        cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author FROM Messages ORDER BY timestamp;")
        rows = cursor.fetchall()
        messages = []
        for row in rows:
            if row[2]!= row[1]:
                direction = 'To {}:'.format(row[1])
            else:
                direction = 'From {}:'.format(row[2])
            messages.append(direction)
        conn.close()
        return messages
    except sqlite3.Error as e:
        return("An error occurred:", e.args[0])
    
def baseline_printMessages(skypeDB):
	import sqlite3
	from sqlite3 import Error
	connection = sqlite3.connect(skypeDB)
	cursor = connection.cursor()
	cursor.execute("SELECT datetime(timestamp,'unixepoch'), dialog_partner, author, body_xml FROM Messages;")
	rows = cursor.fetchall()
	messages = []
	for row in rows:
		if row[2] == row[1]:
			messages.append('To'+ row[1] + ':'+ row[3])
		else:
			messages.append('From'+ row[2] + ':'+ row[3])
	connection.close()
	return messages
