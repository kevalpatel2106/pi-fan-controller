#!/usr/bin/env python3

import os
import time
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

DESIRED_TEMP = float(os.getenv('DESIRED_TEMP', 50))
FAN_PIN = int(os.getenv('FAN_PIN', 13))
READ_INTERVAL = int(os.getenv('READ_INTERVAL', 2))
fanState = False

def getCPUtemperature():
    temp = os.popen('cat /sys/class/thermal/thermal_zone*/temp').readline().replace('\n','')
    temp = float(temp)
    temp /= 1000.0
    return temp

def fanON():
    global fanState
    fanState = True
    GPIO.output(FAN_PIN, GPIO.HIGH)

def fanOFF():
    global fanState
    fanState = False
    GPIO.output(FAN_PIN, GPIO.LOW)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    fanOFF()
    while True:
        cpuTemp = float(getCPUtemperature())
        diff = cpuTemp - DESIRED_TEMP
        if diff > 0 and not fanState: 
            print(f'{datetime.now()} Fan on. Current cpu temprature is {cpuTemp}°C.')
            fanON()
        elif diff < 0 and fanState:
            print(f'{datetime.now()} Fan off. Current cpu temprature is {cpuTemp}°C.')
            fanOFF()
        sleep(READ_INTERVAL)
except KeyboardInterrupt:
    fanOFF()
finally:
    GPIO.cleanup()
