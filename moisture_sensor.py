#!/usr/bin/python

import RPi.GPIO as GPIO 
import time

def MoistureRead():
    if GPIO.input(sensorChannel):
        return False
    else:
        return True

GPIO.setmode(GPIO.BCM)

sensorChannel = 17

GPIO.setup(sensorChannel, GPIO.IN)
