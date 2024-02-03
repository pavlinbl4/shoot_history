import os
import subprocess

# Single sudo command
# subprocess.run(['sudo', 'apt', 'update'])

# Script with sudo

import subprocess
import getpass

script_path = '/Volumes/big4photo/Scripts/move_new_chromdriver.sh'



def run_script():
    # sudo_prompt = '[sudo] password for %p: '
    p = '198217'

    process = subprocess.Popen(['sudo', '-S', 'bash', script_path],
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)

    stdout, stderr = process.communicate(input=p + "\n")

    if process.returncode != 0:
        print(stderr)
        raise Exception("Script failed!")
    else:
        print(stdout)


if __name__ == "__main__":
    run_script()
