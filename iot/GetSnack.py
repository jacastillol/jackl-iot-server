#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

# Reading the card
try:
    print('Now place your tag to write to get your snack!')
    id, text = reader.read()
    print(id)
    print('Card was readed', text)
finally:
    GPIO.cleanup()


# sending POST request
import requests

session = requests.Session()
data = {
    'name':text,
}
req = session.post('http://userd.thejacklrobot.com/getsnack', data=data)

print(req.status_code)
