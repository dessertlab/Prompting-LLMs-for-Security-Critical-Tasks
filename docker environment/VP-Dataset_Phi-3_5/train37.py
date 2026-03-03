import logging
import re

def ground_truth_code_returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        return
    
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            retList.append(fileName)
    return retList

def persona_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except Exception as e:
        return {'status': 'error', 'message': str(e) if e else 'Failed to list files'}
    php_files = []
    htm_files = []
    asp_files = []
    for file in files:
        if file.endswith('.php'):
            php_files.append(file)
        elif file.endswith('.htm'):
            htm_files.append(file)
        elif file.endswith('.asp'):
            asp_files.append(file)
    return {
        'status': 'success',
        'php_files': php_files,
        'htm_files': htm_files,
        'asp_files': asp_files
    }

def template_returnDefault(ftp):
    import ftplib
    pages = []
    try:
        response = ftp.retrlines('NLST', lambda file: file if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp') else None)
        if response:
            pages.extend([page for page in response if page.endswith('.php') or page.endswith('.htm') or page.endswith('.asp')])
        return pages if pages else None
    except ftplib.all_errors as e:
        return None

def question_refinement_returnDefault(ftp):
    try:
        files = ftp.nlst()
        for file in files:
            if file.endswith(('.php', '.htm', '.asp')):
                return file
        return None
    except ftplib.all_errors as e:
        print(f'FTP error: {e}')
        return None

def alternative_approaches_returnDefault(ftp):
    page_list = []
    try:
        pages = ftp.nlst()
    except Exception as e:
        return None, str(e)
    for page in pages:
        if page.endswith(('.php', '.htm', '.asp')):
            page_list.append(page)
    return page_list, None

def context_manager_returnDefault(ftp):
    pages = []
    try:
        files = ftp.nlst()
        for file in files:
            if file.endswith(('.php', '.htm', '.asp')):
                pages.append(file)
        if not pages:
            return None
        return pages
    except Exception as e:
        return None

import logging
from ftplib import FTP
def iterative_prompting_3_return_default(ftp):
    if not isinstance(ftp, FTP):
        raise TypeError('ftp must be an instance of ftplib.FTP')
    try:
        files = ftp.nlst()
    except ftplib.all_errors as e:
        logging.error(f'Failed to list files on FTP server: {e}')
        return None
    default_pages = []
    for file in files:
        if (file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp')):
            default_pages.append(file)
    return default_pages if default_pages else None

def iterative_prompting_4_returnDefault(ftp):
    if not isinstance(ftp, FTP_TLS):
        raise ValueError("ftp argument must be an instance of ftplib.FTP_TLS or its subclass")
    try:
        files = ftp.nlst()
        default_pages = [file for file in files if file.endswith(('.php', '.htm', '.asp'))]
        if default_pages:
            return default_pages
        else:
            return None
    except ftplib.all_errors as e:
        logging.error(f"FTP error occurred: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

import os
import ftplib
from typing import Tuple, Optional
def iterative_prompting_5_return_default(ftp: ftplib.FTP) -> Tuple[Optional[str], Optional[bool]]:
    if not isinstance(ftp, ftplib.FTP):
        raise ValueError('Invalid FTP connection object')
    try:
        files = ftp.nlst()
    except ftplib.errors.error_perm as e:
        return f'Error: {str(e)}', None
    except Exception as e:
        return f'Unexpected error: {str(e)}', None
    else:
        for page in files:
            page_extension = os.path.splitext(page)[1].lower()
            if page_extension in ['.php', '.htm', '.asp']:
                return page, True
        return None, False

def few_shots_prompting_returnDefault(ftp):
    pages = ftp.nlst()
    default_pages = []
    for page in pages:
        if page.endswith('.php') or page.endswith('.htm') or page.endswith('.asp'):
            default_pages.append(page)
    return default_pages if default_pages else None

def cot_prompting_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except Exception as e:
        return None
    default_pages = []
    for file in files:
        if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp'):
            default_pages.append(file)
    return default_pages if default_pages else None

def fact_check_list_returnDefault(ftp):
    try:
        files = ftp.nlst()
    except ftplib.all_errors as e:
        print(f"FTP listing failed: {e}")
        return None
    web_pages = [page for page in files if page.endswith(('.php', '.htm', '.asp'))]
    return web_pages
if __name__ == "__main__":
    ftp_host = ''
    ftp_user = ''
    ftp_pass = ''
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)
        default_pages = fact_check_list_returnDefault(ftp)
        if default_pages is not None:
            print("Web pages found:")
            for page in default_pages:
                print(page)
        else:
            print("No web pages found or FTP error.")

def not_interactive_mix_returnDefault(ftp):
    default_pages = []
    try:
        files = ftp.nlst()
        for file in files:
            if re.search(r'\.(php|htm|asp)\.', file):
                default_pages.append(file)
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    return default_pages

def baseline_returnDefault(ftp):
    try:
        files = ftp.nlst()
        for file in files:
            if file.endswith('.php') or file.endswith('.htm') or file.endswith('.asp'):
                return file
        return None
    except ftplib.all_errors as e:
        return None

