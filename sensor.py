#!/usr/bin/env python

from gpiozero import MotionSensor
from time import sleep
from signal import pause

pir = MotionSensor(27)

def sendmessage():
    print('motion detected')
    sleep(5)

count = 0

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    pir.wait_for_no_motion()
    print("Motion Stopped")
