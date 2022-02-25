#!/usr/bin/env python

from picamera import PiCamera
import tweepy
import time
from time import sleep
from credentials import *
from gpiozero import MotionSensor
from signal import pause


pir = MotionSensor(27)

camera = PiCamera()

filename = "null"

def takepicture():
    camera.start_preview()
    filename = "/home/pi/birdyshots/picture_" + str(time.time()) + ".jpg"
    camera.capture(filename)
    camera.stop_preview()
    sleep(2)
    return filename

def tweetpicture(picturepath):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = "Bird Detected"
    status = api.update_with_media(picturepath, tweet)
    api.update_status(status = tweet)

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    picturepath = takepicture()
    tweetpicture(picturepath)
    pir.wait_for_no_motion()
    print("Motion Stopped")




