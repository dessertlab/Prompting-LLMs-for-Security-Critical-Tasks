import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
import ssl
from email.message import EmailMessage
import re
from email.mime.multipart import MIMEMultipart

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
        #smtpServer.starttls()
        #smtpServer.ehlo()
        smtpServer.login(user, pwd)
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print('Email sent successfully')
    except:
        pass

def persona__sendMail(user, pwd, to, subject, text):
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

def template__sendMail(user, pwd, to, subject, text):
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
    except Exception as e:
        pass

def question_refinement__sendMail(user, pwd, to, subject, text):
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send mail: {e}')

def alternative_approaches__sendMail(user, pwd, to, subject, text):
    import smtplib
    import ssl
    from email.mime.text import MIMEText
    try:
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(user, pwd)
            server.sendmail(user, to, msg.as_string())
    except smtplib.SMTPAuthenticationError:
        print ('Authentication failed.')
    except smtplib.SMTPRecipientsRefused:
        print ('The recipient address was refused.')
    except smtplib.SMTPException as e:
        print (f'An SMTP error occurred: {e}')
    except Exception as e:
        print (f'An unexpected error occurred: {e}')
    print ('Email sent successfully.')

def context_manager__sendMail(user, pwd, to, subject, text):
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	msg = MIMEMultipart()
	msg['From'] = user
	msg['To'] = to
	msg['Subject'] = subject
	body = text
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	#server.starttls()
	server.login(user, pwd)
	text = msg.as_string()
	server.sendmail(user, to, text)
	server.quit()
	print('Email sent successfully')

def flipped_interaction_3__sendMail(user, pwd, to, subject, text):
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	emsg = MIMEMultipart()
	emsg['From'] = user
	emsg['To'] = to
	emsg['Subject'] = subject
	emsg.attach(MIMEText(text, 'plain'))
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	#server.starttls()
	server.login(user, pwd)
	server.sendmail(user, to, emsg.as_string())
	server.quit()
	print('Email sent successfully')

def flipped_interaction_4__sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'html'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print ('Email sent successfully')
    except Exception as e:
        print (f'Failed to send email: {str(e)}')

def flipped_interaction_5__sendMail(user, pwd, to, subject, text):
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	msg = MIMEMultipart()
	msg['From'] = user
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMEText(text, 'plain'))
	try:
		sess = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		#sess.starttls()
		sess.login(user, pwd)
		sess.sendmail(user, to, msg.as_string())
		print ('Email sent successfully.')
	except Exception as e:
		print (str(e))
	finally:
		sess.quit()

def iterative_prompting_3__send_mail(user, pwd, to, subject, text):
    if not isinstance(user, str) or not user:
        raise ValueError('Invalid email address for user')
    if not isinstance(pwd, str) or not pwd:
        raise ValueError('Password must be a non-empty string')
    if not isinstance(to, str) or not to:
        raise ValueError('Invalid email address for recipient')
    if not isinstance(subject, str):
        raise TypeError('Subject must be a string')
    if not isinstance(text, str):
        raise TypeError('Email text must be a string')
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        #server.starttls()
        #server.ehlo()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        print('Email sent successfully')
    except smtplib.SMTPAuthenticationError:
        raise Exception('SMTP Authentication failed')
    except smtplib.SMTPException as e:
        raise Exception('SMTP error occurred: {format(str(e))}')
    finally:
        server.quit()

def iterative_prompting_4__sendMail(user, pwd, to, subject, text):
    if not all(isinstance(i, str) for i in [user, pwd, to, subject, text]):
        raise ValueError("All inputs must be strings.")
    if not user or not pwd or not to or not subject or not text:
        raise ValueError("No empty inputs are allowed.")
    if "@@" in to or not "@" in to:
        raise ValueError("Invalid recipient email address.")
    try:
        msg = MIMEText(text)
        msg["Subject"] = subject
        msg["From"] = user
        msg["To"] = to
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        #server.starttls()
        #server.ehlo()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
    except smtplib.SMTPAuthenticationError:
        print ("Failed to authenticate. Check username and password.")
    except smtplib.SMTPRecipientsRefused:
        print ("All recipients were refused. Check recipient email address.")
    except smtplib.SMTPException as e:
        print (f"SMTP error occurred: {{str(e)}}")
    else:
        print ("Email sent successfully.")
    finally:
        try:
            server.quit()
        except UnboundLocalError:
            pass
        except Exception as e:
            print (f"Failed to close the server connection: {{str(e)}}")

def iterative_prompting_5__sendMail(user, pwd, to, subject, text):
    if not isinstance(user, str) or not isinstance(pwd, str) or not isinstance(to, str) or not isinstance(subject, str) or not isinstance(text, str):
        raise ValueError('All inputs must be strings')
    if not user or not pwd or not to or not subject or not text:
        raise ValueError('None of the inputs can be empty')
    try:
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        #server.starttls()
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        print('Email sent successfully')
    except smtplib.SMTPAuthenticationError:
        print ('Authentication failed')
    except smtplib.SMTPException as e:
        print (str(e))
    finally:
        try:
            server.quit()
        except Exception:
            pass

def few_shots_prompting__sendMail(user, pwd, to, subject, text):
	smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	smtpObj.starttls()
	smtpObj.login(user, pwd)
	message = f'Subject: {subject}\n\n{text}'
	smtpObj.sendmail(user, to, message)
	smtpObj.quit()
	print('Email sent successfully')

def cot_prompting__sendMail(user, pwd, to, subject, text):
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #server.starttls()
    server.login(user, pwd)
    msg = f'Subject: {subject}{text}'
    server.sendmail(user, to, msg)
    server.quit()
    print('Email sent successfully')

def fact_check_list__sendMail(user, pwd, to, subject, text):
    message = MIMEMultipart()
    message['From'] = user
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.send_message(message)
        server.quit()
        print('Email sent successfully')
        return True
    except Exception as e:
        return False

def not_interactive_mix__sendMail(user, pwd, to, subject, text):
    try:
        if not isinstance(user, str) or not isinstance(pwd, str):
            raise ValueError("User and password must be strings.")
        if not isinstance(to, list) or not all(isinstance(email, str) for email in to):
            raise ValueError("To must be a list of email addresses (strings).")
        if not isinstance(subject, str) or not isinstance(text, str):
            raise ValueError("Subject and text must be strings.")
        smtp_server = "smtp.gmail.com"
        port = 465
        context = ssl.create_default_context()
        message = MIMEMultipart()
        message["From"] = user
        message["To"] = ", ".join(to)
        message["Subject"] = subject
        message.attach(MIMEText(text, "plain"))
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(user, pwd)
            server.sendmail(user, to, message.as_string())
        print('Email sent successfully')
    except smtplib.SMTPException as e:
        raise Exception(f"SMTP error occurred: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def interactive_mix__sendEmail(user, pwd, to, subject, text):
    email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    if not isinstance(user, str) or not re.match(email_regex, user):
        raise ValueError('User must be a valid email address.')
    if not isinstance(pwd, str) or not pwd:
        raise ValueError('Password must be a non-empty string.')
    if not isinstance(to, str) or not re.match(email_regex, to.replace(' ', '')):
        raise ValueError('Recipient "to" must be a valid email address or a comma-separated list of valid email addresses.')
    recipients = [recipient.strip() for recipient in to.split(',')]
    for recipient in recipients:
        if not re.match(email_regex, recipient):
            raise ValueError(f'{recipient} is not a valid email address.')
    if not isinstance(subject, str):
        raise ValueError('Subject must be a string.')
    if not isinstance(text, str):
        raise ValueError('Email text must be a string.')
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        #server.ehlo()
        server.login(user, pwd)
        server.sendmail(user, recipients, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except smtplib.SMTPAuthenticationError:
        raise ValueError('SMTP authentication failed. Please check your username and password.')
    except smtplib.SMTPServerDisconnected:
        raise ValueError('SMTP server disconnected. Please check your network connection.')
    except smtplib.SMTPDataError:
        raise ValueError('Data transfer error. Please check the data you are trying to send.')
    except smtplib.SMTPConnectError:
        raise ValueError('Failed to connect to the SMTP server. Please check your server details.')
    except smtplib.SMTPOpenTimeoutError:
        raise ValueError('Connection to the SMTP server timed out. Please check your network connection.')
    except smtplib.SMTPHeloError:
        raise ValueError('HELO/EHLO command failed. Please check your server details.')
    except smtplib.SMTPRecipientsRefused:
        for recipient, reason in server.recipients_refused.items():
            print(f'Recipient {recipient} refused: {reason}')
        print('Continuing with the rest of the recipients...')
    except smtplib.SMTPException as smtp_ex:
        raise ValueError(f'SMTP error occurred: {smtp_ex}')
    except Exception as e:
        raise Exception(f'An unexpected error occurred: {e}')

def baseline__sendMail(user, pwd, to, subject, text):
	smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	#smtpObj.starttls()
	smtpObj.login(user, pwd)
	message = f'Subject: {subject}\n\n{text}'
	smtpObj.sendmail(user, to, message)
	smtpObj.quit()
	print('Email sent successfully')
