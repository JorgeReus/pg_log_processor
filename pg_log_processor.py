#!/usr/bin/env python3

from pandas import read_csv, DataFrame
from datetime import datetime
import locale
from hashlib import md5
from io import StringIO
from typing import List


"""
    __author__ = "Jorge Reus"
    __license__ = "MIT"
    __version__ = "0.1"
    __maintainer__ = "Jorge Reus"
    __email__ = "j-g1996@live.com"
    __status__ = "Alpha"
"""


# Set the locale to mexican spanish
locale.setlocale(locale.LC_ALL, "es_MX.utf8")

# Processed data model modifications file path (a.k.a alters file)
ALTERS_PATH = '/home/reus/Desktop/pg_log_processor/alters-raw.sql'

# Source log file path
LOG_FILE_PATH = '/var/lib/postgresql/10/main/pg_log/postgresql-log-raw.csv'

def _get_last_hash(fname: str) -> str:
    """ This function gets the last hash of the log entry based on the one in the alters file """
    last_hash = None
    with open(fname) as f:
        for i, l in enumerate(f):
            if l[:2] == '--':
                last_hash = l.split(' - ')[1][16:]
    return last_hash


def _get_data_with_by_hash_offset(offset_hash: str) -> StringIO:
    """
        This function gets the data of the log file, based on the hash, an identifier of the last processed entry.
        So that the new data to be processed is not duplicated
    """
    with open(LOG_FILE_PATH) as f:
        # Stop at the line that matches the hash
        if offset_hash is not None:
            while True:
                line = f.readline()
                if str(md5(line.split(',')[0].encode('utf-8')).hexdigest()) == offset_hash or not line :
                    break
        # Store the data that comes after
        line = f.readline()
        lines = []
        while line:
            lines.append(line)
            line = f.readline()

        return StringIO(''.join(line for line in lines))

def read_log_file() -> DataFrame:
    """
        This function reads the postgres log file and parses it to a pandas dataframe
    """
    # Column names for the source log file (in csv format)
    column_names = ['log_time', 'user_name', 'database_name', 'process_id', 
        'connection_from', 'session_id', 'session_line_num', 'command_tag', 
        'session_start_time','virtual_transaction_id', 'transaction_id' , 'error_severity',
        'sql_state_code', 'message', 'detail', 'hint', 'internal_query',
        'internal_query_pos', 'context', 'query', 'query_pos', 'location', 'application_name']


    # Get the last hash, for calculating the position we have to use as start
    last_hash = _get_last_hash(ALTERS_PATH)

    # Get the lines after the hash offset
    data = _get_data_with_by_hash_offset(last_hash)

    # Open the csv file
    df = read_csv(data, header=None, names=column_names)
    return df

def log_alters(strings: List[str]) -> None:
    """
        This functions takes an iterable of strings, then logs them into a .sql file
    """
    with open(ALTERS_PATH, 'a') as alters_file:
        for string in strings:
            alters_file.write(string)

def main() -> None:
    """
        This function takes all the information I marked as important, 
        then formats it in a pretty and human readable sql file for logginc purposes.
    """
    df = read_log_file()
    log_strings = []
    # Iterate the rows of the dataframe
    for _, row in df.iterrows():
        # The command fo the log entry is 'idle'
        if(row['command_tag'] == 'idle'):
            # Split the command into two parts on a space
            message_parts = row['message'].split(' ', 1)
            # If the statement contains create, drop, update or insert
            if message_parts[0] == 'statement:' and  any(part in message_parts[1] for part in ('create', 'drop', 'update', 'insert')):
                # Hash the entry date
                date_hash = md5(row['log_time'].encode('utf-8')).hexdigest()
                # Format the data
                log_date = datetime.strptime(row['log_time'], "%Y-%m-%d %H:%M:%S.%f %Z").strftime('%d/%B/%Y %A a las %H:%M:%S')
                log_strings.append(f"--TIMESTAMP: {log_date} - TIMESTAMP_HASH: {date_hash} - USER: {row['user_name']} - DATABASE: {row['database_name']}\n{message_parts[1]}\n\n")
    # Log the data
    log_alters(log_strings)

if __name__ == '__main__':
    main()

