#!/usb/bin/python3

import os
base_dir = os.path.dirname(__file__)
env_dir = os.path.join(base_dir, '/venv/bin')
activate_this = os.path.join(env_dir, 'activate_this.py')

with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, base_dir)

from app import app as application