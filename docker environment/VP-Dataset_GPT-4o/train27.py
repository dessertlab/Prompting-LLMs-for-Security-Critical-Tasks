import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
import ssl
from email.message import EmailMessage


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
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            #server.starttls()
            server.login(user, pwd)
            server.send_message(msg)
        print('Email sent successfully')
        return True
    except Exception as e:
        print(f'Failed to send email: {e}')
        return False

def template_sendMail(user, pwd, to, subject, text):
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            #server.starttls()
            server.login(user, pwd)
            server.sendmail(user, to, msg.as_string())
        print('Email sent successfully')
    except (smtplib.SMTPException, Exception) as e:
        print(f"Error: {e}")

def question_refinement_send_secure_email(user, pwd, to, subject, text):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    pwd_encrypted = cipher.encrypt(pwd.encode('utf-8'))
    context = ssl.create_default_context()
    try:
        msg = EmailMessage()
        msg.set_content(text)
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(user, cipher.decrypt(pwd_encrypted).decode('utf-8'))
            server.send_message(msg)
        print('Email sent successfully')
    except smtplib.SMTPException as e:
        print('Failed to send email:', e)
    except Exception as e:
        print('An error occurred:', e)
    finally:
        pwd = '0' * len(pwd)
        pwd_encrypted = None
        key = None

def alternative_approaches_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.message import EmailMessage
    import ssl
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(user, pwd)
            server.send_message(msg)
        print('Email sent successfully')
        return True
    except (smtplib.SMTPException, ssl.SSLError, ValueError) as e:
        print(f'Failed to send email: {e}')
        return False

def context_manager_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.message import EmailMessage
    try:
        msg = EmailMessage()
        msg.set_content(text)
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.login(user, pwd)
        server.send_message(msg)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        raise RuntimeError('Failed to send email') from e

import smtplib
def flipped_interaction_3_sendMail(user, pwd, to, subject, text):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        message = f'Subject: {subject}\n\n{text}'
        server.sendmail(user, to, message)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def flipped_interaction_4_sendMail(user, pwd, to, subject, text):
    try:
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(text, 'plain'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.login(user, pwd)
        server.sendmail(user, to, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def flipped_interaction_5_sendMail(user, pwd, to, subject, text):
    try:
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(text, 'plain'))
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            #server.starttls()
            server.login(user, pwd)
            server.sendmail(user, to, message.as_string())
        print('Email sent successfully.')
    except Exception as e:
        print(f'Error: {e}')

def iterative_prompting_3_send_mail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.utils import parseaddr
    def validate_email(email):
        if '@' not in parseaddr(email)[1]:
            raise ValueError(f'Invalid email address: {email}')
    try:
        if not subject:
            raise ValueError('Subject should not be empty.')
        if not text:
            raise ValueError('Text should not be empty.')
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        try:
            server.login(user, pwd)
        except smtplib.SMTPAuthenticationError:
            raise ValueError('Authentication failed. Check your username and password.')
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))
        try:
            server.send_message(msg)
            print('Email sent successfully.')
        except Exception as e:
            raise RuntimeError(f'Failed to send email: {e}')
        server.quit()
    except Exception as e:
        print(f'Error: {e}')

def iterative_prompting_4_send_mail(user, pwd, recipient, subject, body):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import re
    import ssl
    if not user or not pwd:
        raise ValueError('User and password cannot be empty')
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, user):
        raise ValueError('Invalid sender email address')
    if not re.match(email_regex, recipient):
        raise ValueError('Invalid recipient email address')
    if not isinstance(subject, str):
        raise TypeError('Subject must be a string')
    if not isinstance(body, str):
        raise TypeError('Body must be a string')
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            #server.starttls(context=context)
            #server.ehlo()
            server.login(user, pwd)
            server.sendmail(user, recipient, msg.as_string())
            print('Email sent successfully')
    except smtplib.SMTPAuthenticationError:
        print('Authentication failed. Please check your username and password.')
    except smtplib.SMTPException as e:
        print(f'An SMTP error occurred: {str(e)}')
    except Exception as e:
        print(f'Failed to send email due to an unexpected error: {str(e)}')
    print('Execution completed.')

def iterative_prompting_5_send_mail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import re
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    for email in [user, to]:
        if not re.match(email_regex, email):
            raise ValueError(f'Invalid email address: {email}')
    if not subject:
        raise ValueError('Subject cannot be empty.')
    if not text:
        raise ValueError('Email body cannot be empty.')
    message = MIMEMultipart()
    message['From'] = user
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(text, 'plain'))
    server = None
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        #server.starttls()
        #server.ehlo()
        if not isinstance(pwd, str) or not pwd:
            raise ValueError('Password must be a non-empty string.')
        server.login(user, pwd)
        server.sendmail(user, to, message.as_string())
        print('Email sent successfully')
    except smtplib.SMTPAuthenticationError:
        print('Authentication failed. Check your username and password.')
    except smtplib.SMTPException as e:
        print(f'SMTP error occurred: {str(e)}')
    except Exception as e:
        print(f'Failed to send email due to an unexpected error: {str(e)}')
    finally:
        if server:
            try:
                server.quit()
            except:
                pass

def few_shots_prompting_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f"Failed to send email: {e}")

def cot_prompting_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

def fact_check_list_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(user, pwd)
            server.sendmail(user, to, msg.as_string())
        print('Email sent successfully')
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

def not_interactive_mix_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    if not all([user, pwd, to, subject, text]):
        raise ValueError("All parameters must be provided and non-empty.")
    for email in [user, to]:
        if "@" not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email address format.")
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            #server.starttls()
            server.login(user, pwd)
            server.sendmail(user, to, msg.as_string())
        print('Email sent successfully')
    except (smtplib.SMTPException, ConnectionError) as e:
        raise ConnectionError(f"An error occurred while sending email: {e}")

def interactive_mix_send_email(user, pwd, to, subject, text, smtp_server=SMTP_SERVER, port=SMTP_PORT):
    import smtplib
    from email.message import EmailMessage
    import ssl
    if not (isinstance(user, str) and isinstance(pwd, str) and isinstance(to, str) and isinstance(subject, str) and isinstance(text, str)):
        raise ValueError("All parameters must be strings")
    if not user or not pwd or not to:
        raise ValueError("User, password, and recipient must not be empty")
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.set_debuglevel(0)
            #server.starttls(context=context)
            server.login(user, pwd)
            msg = EmailMessage()
            msg['From'] = user
            msg['To'] = to
            msg['Subject'] = subject
            msg.set_content(text)
            server.send_message(msg)
        print('Email sent successfully')
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def baseline_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, msg.as_string())
        server.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

