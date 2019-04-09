#!/user/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMRFC522

reader = SimpleMRFC522()

try:
    print('Now place your tag to read info')
    id, text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()

