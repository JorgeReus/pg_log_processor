import cProfile
import subprocess

def subprocess_one(filename):
    line = subprocess.check_output(['tail', '-1', filename])

def manual_one(filename):   
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print(last_line)

if __name__ == '__main__':
    cProfile.run('subprocess_one("alters-raw.sql")')
    cProfile.run('manual_one("alters-raw.sql")')
    # Manual one wins
