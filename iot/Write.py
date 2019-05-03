#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print('Now place your tag to write')
    text = input('New Data:')
    reader.write(text)
    print('written')
finally:
    GPIO.cleanup()
