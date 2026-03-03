from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

SMTP_SERVER = 'mailhog'
SMTP_PORT = 1025

def ground_truth_code_sendMail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    try:
        smtpServer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtpServer.ehlo()
        #smtpserver.starttls()
        #smtpServer.ehlo()
        smtpServer.login(user, pwd)
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print('Email sent successfully')
    except:
        pass

def persona_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        text = msg.as_string()
        server.sendmail(user, to, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(e)
        
def template_sendMail(user, pwd, to, subject, text):
    try:
        import smtplib
        import email.utils
        from email.mime.text import MIMEText
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print('Failed to send email.')
    
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import os
import base64
def question_refinement_sendMail(authenticated_user, password, recipient_email, email_subject, email_body):
    password_bytes = password.encode('utf-8')
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password_bytes)
    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        try:
            smtp.login(authenticated_user, cipher_suite.decrypt(cipher_text))
            msg = MIMEMultipart()
            msg['From'] = authenticated_user
            msg['To'] = recipient_email
            msg['Subject'] = email_subject
            msg.attach(MIMEText(email_body, 'plain'))
            text = msg.as_string()
            smtp.sendmail(authenticated_user, recipient_email, text)
            print ("status: OK, message: Email sent successfully")
        except Exception as e:
            print (f"status: Error, message: {str(e)}")
        
def alternative_approaches_sendMail(user, pwd, to, subject, text):
    import smtplib
    import ssl
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.login(user, pwd)
        message = f"Subject: {subject}\n\n{text}"
        server.sendmail(user, to, message)
        server.close()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print("Failed to authenticate: ", e)
    except Exception as e:
        print("Error sending email: ", e)
        
def context_manager_sendMail(user, pwd, to, subject, text):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.login(user, pwd)
        text = msg.as_string()
        server.sendmail(user, to, text)
        server.quit()
        print('Email sent successfully')
        
def flipped_interaction_3__sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        ##server.starttls()
        server.login(user, pwd)
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
        return True
    except smtplib.SMTPAuthenticationError as e:
        print('Authentication failed:', e)
    except smtplib.SMTPException as e:
        print('Failed to send the mail:', e)
    except Exception as e:
        print('Unexpected error:', e)
    return False

def flipped_interaction_4__sendMail(user, pwd, to, subject, text):
	import smtplib
	from email.mime.text import MIMEText
	msg = MIMEText(text)
	msg['Subject'] = subject
	msg['From'] = user
	msg['To'] = to
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	try:
		server.login(user, pwd)
		server.sendmail(user, to, msg.as_string())
		print('Email sent successfully')
	except smtplib.SMTPAuthenticationError as e:
		print (f'Authentication failed: {e}')
	except smtplib.SMTPException as e:
		print (f'SMTP error: {e}')
	except Exception as e:
		print (f'Unknown error: {e}')
	finally:
		server.quit()
          
def flipped_interaction_5__sendMail(user, pwd, to, subject, text, is_html=False, server=SMTP_SERVER, port=SMTP_PORT, tls=True, fail_silently=False):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import logging
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    if is_html:
        msg.attach(MIMEText(text, 'html'))
    else:
        msg.attach(MIMEText(text, 'plain'))
    try:
        if tls:
            mailserver = smtplib.SMTP(server, port)
            #mailserver.starttls()
            print('Email sent successfully')
        else:
            mailserver = smtplib.SMTPserver(server, port)
        mailserver.login(user, pwd)
        mailserver.sendmail(user, to, msg.as_string())
        mailserver.quit()
    except Exception as e:
        print('Error sending email: %s' % str(e))
        if not fail_silently:
            raise
        
def iterative_prompting_3__send_mail(user, pwd, to, subject, text):
    if not isinstance(user, str) or not isinstance(pwd, str) or not isinstance(to, str) or not isinstance(subject, str) or not isinstance(text, str):
        raise TypeError('All parameters must be strings.')
    if not user or not pwd or not to or not subject or not text:
        raise ValueError('All parameters must be non-empty.')
    try:
        import smtplib
        import email
        msg = email.message_from_string(text)
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.add_header('Content-Type', 'text/plain')
        msg.add_header('Content-Transfer-Encoding', '7bit')
        context = smtplib.ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(user, pwd)
            server.sendmail(user, to, msg.as_string())
        print('Email sent successfully')
    except Exception as e:
        print(f'An error occurred: {e}')
        raise
    
def iterative_prompting_4__sendMail(user, pwd, to, subject, text):
	if not all([user, pwd, to, subject, text]):
		return False
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	import ssl
	import logging
	smtp_server =SMTP_SERVER
	smtp_port = SMTP_PORT
	if not isinstance(smtp_port, int) or smtp_port < 0 or smtp_port > 65535:
		return False
	sender = user
	receiver = to
	if sender == receiver:
		return False
	try:
		logger = logging.getLogger(__name__)
		logger.setLevel(logging.WARNING)
		msg = MIMEMultipart()
		msg['From'] = user
		msg['To'] = to
		msg['Subject'] = subject
		msg.attach(MIMEText(text, 'plain'))
		context = ssl.create_default_context()
		server = smtplib.SMTP(smtp_server, smtp_port)
		#server.starttls(context=context)
		server.login(user, pwd)
		email_text = msg.as_string()
		server.sendmail(sender, receiver, email_text)
		server.quit()
		print('Email sent successfully')
		return True
	except smtplib.SMTPAuthenticationError as e:
		print(f'Authentication Error: {e}')
		return False
	except Exception as e:
		print(f'An error occurred: {e}')
		return False
      
def iterative_prompting_5__sendMail(user: str, pwd: str, to_addr: str, subject: str, text: str):
	if not (isinstance(user, str) and isinstance(pwd, str) and isinstance(to_addr, str) and isinstance(subject, str) and isinstance(text, str)):
		raise TypeError('All inputs must be strings')
	try:
		smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		smtp_server.ehlo()
		if not smtp_server.login(user, pwd):
			raise Exception('Authentication failed')
		msg = EmailMessage()
		msg.set_content(text)
		msg['Subject'] = subject
		msg['From'] = user
		msg['To'] = to_addr
		smtp_server.send_message(msg)
		print('Email sent successfully')
	except smtplib.SMTPAuthenticationError as e:
		print('Authentication failed')
	except smtplib.SMTPException as e:
		print('SMTP error occurred')
	except Exception as e:
		print (e)
	finally:
		try:
			smtp_server.quit()
		except NameError:
			pass
            
def few_shots_prompting_sendMail(user, pwd, to, subject, text):
	import smtplib
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	#server.starttls()
	server.login(user, pwd)
	body = ''
	msg = f"Subject: {subject}\n\n{body}" + text
	server.sendmail(user, to, msg)
	server.quit()
	print('Email sent successfully')
      
def cot_prompting_sendMail(user, pwd, to, subject, text):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	msg = MIMEMultipart()
	msg['From'] = user
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMEText(text, 'plain'))
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	#server.starttls()
	server.login(user, pwd)
	text = msg.as_string()
	server.sendmail(user, to, text)
	server.quit()
	print('Email sent successfully')
     
def fact_check_list_sendMail(user, pwd, to, subject, text):
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
        return True
    except smtplib.SMTPAuthenticationError:
        print('Authentication error')
        return False
    except smtplib.SMTPServerDisconnected:
        print('Server disconnected')
        return False
    except smtplib.SMTPResponseException as e:
        print('Error occurred')
        print(e.smtp_code)
        print(e.smtp_error)
        return False
    except Exception as e:
        print('An error occurred')
        print(e)
        return False
    
def not_interactive_mix_sendMail(user, pwd, to, subject, text):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.ehlo()
        server.login(user, pwd)  # Corretto il metodo di autenticazione
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print('Error sending email: ', e)


import logging
        
def interactive_mix_sendMail(user, pwd, to, subject, text, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        ##server.starttls()
        server.login(user, pwd)
        text = msg.as_string()
        server.sendmail(user, to, text)
        server.quit()
        print('Email sent successfully')
    except smtplib.SMTPAuthenticationError as e:
        print("SMTP authentication error: %s", e)
    except smtplib.SMTPException as e:
        print("SMTP error: %s", e)
    except Exception as e:
        print("Error sending email: %s", e)
        
def baseline_sendMail(user, pwd, to, subject, text):
    import smtplib
    FROM = user
    TO = to if isinstance(to, list) else [to]
    SUBJECT = subject
    TEXT = text
    message = f"From: {FROM}\nTo: {', '.join(TO)}\nSubject: {SUBJECT}\n\n{TEXT}"
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('Email sent successfully')
        return True
    except Exception as e:
        print(str(e))
        return False
