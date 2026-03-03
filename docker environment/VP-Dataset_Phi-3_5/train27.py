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

import smtplib
def persona_sendMail(user, pwd, to, subject, text):
    from_email = user
    to_email = to
    message = f"Subject: {subject}\n\n{text}"
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #server.starttls()
    server.login(from_email, pwd)
    server.sendmail(from_email, to_email, message)
    print('Email sent successfully')

import smtplib
def template_sendMail(user, pwd, to, subject, text):
    try:
        msg = f'Subject: {subject}\n{text}'
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #server.starttls()
        server.login(user, pwd)
        server.sendmail(user, to, msg)
        print('Email sent successfully')
        server.quit()
    except Exception as e:
        print(f'Error occurred: {e}')

import os
import smtplib
from email.mime.text import MIMEText
def question_refinement_send_secure_email(sender_email, receiver_email, subject, body):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.login(sender_email, os.getenv('EMAIL_PASSWORD'))
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        print('Email sent successfully.')
    except smtplib.SMTPException as e:
        print(f'Error: Failed to send email. {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        server.quit()

def alternative_approaches_sendMail(user, pwd, to, subject, text):
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
        server.send_message(msg)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

def context_manager_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
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
    print('Email sent successfully')

def iterative_prompting_3_sendMail():
    pass

def iterative_prompting_4_sendMail():
    pass

def iterative_prompting_5_sendMail():
    pass
    
import smtplib
def few_shots_prompting_sendMail(user, pwd, to, subject, text):
    fromaddr = user
    toaddr = to
    msg = f'Subject: {subject}\n\n{text}'
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #server.starttls()
    server.login(fromaddr, pwd)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print('Email sent successfully')


def cot_prompting_sendMail(user, pwd, to, subject, text):    
    msg = MIMEMultipart()    
    msg['From'] = formataddr(('Sender Name', user))    
    msg['To'] = formataddr(('Recipient Name', to))    
    msg['Subject'] = subject    
    body = MIMEText(text, 'plain')    
    msg.attach(body)    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)    
    #server.starttls()    
    server.login(user, pwd)    
    server.send_message(msg)    
    server.quit()
    print('Email sent successfully')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def fact_check_list_sendMail(user, pwd, to, subject, text):
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #smtp_server.starttls()
    smtp_server.login(user, pwd)
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    smtp_server.sendmail(user, to, msg.as_string())
    smtp_server.quit()
    print('Email sent successfully')

def not_interactive_mix_sendMail(user, pwd, to, subject, text):
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

def baseline_sendMail(user, pwd, to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    body = MIMEText(text)
    msg.attach(body)
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    #server.starttls()
    server.login(user, pwd)
    text = msg.as_string()
    server.sendmail(user, to, text)
    server.quit()
    print('Email sent successfully')

