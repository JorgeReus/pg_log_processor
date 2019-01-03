# pg_log_processor
A simple python script that processes postgresql csv log file and logs INSERT, UPDATE, DROP and ALTER statements to a human redable .sql file

**Tested and developed in python 3.6.7**

## Requirements
pandas==0.23.4

## Usage
python pg_log_processor.py (Must change paths)

## Notes
The postgresql.conf is a sample file with all the configurations I used.
The important stuff is located in the ERROR REPORTING AND LOGGING section, which is as follows:
- log_destination = 'csvlog, stderr'
- logging_collector = on
- log_directory = 'pg_log'
- log_filename = 'postgresql-log-raw.log' (for a single log file)
- log_min_duration_statement = 0
- log_duration = off
- log_statement = 'mod'

Just change these and you're good to go.
