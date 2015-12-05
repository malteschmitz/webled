#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

WHITE_PIN = 37 # GPIO26
GREEN_PIN = 35 # GPIO19
RED_PIN   = 33 # GPIO13
BLUE_PIN  = 31 # GPIO6

GPIO.setmode(GPIO.BOARD)
GPIO.setup(WHITE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

white = GPIO.PWM(WHITE_PIN, 100)
green = GPIO.PWM(GREEN_PIN, 100)
red = GPIO.PWM(RED_PIN, 100)
blue = GPIO.PWM(BLUE_PIN, 100)

white.start(0)
green.start(0)
red.start(0)
blue.start(0)

def cycle(p):
  for dc in range(0, 101, 10):
    p.ChangeDutyCycle(dc)
    time.sleep(0.1)
  for dc in range(100, -1, -10):
    p.ChangeDutyCycle(dc)
    time.sleep(0.1)

cycle(white)
cycle(green)
cycle(red)
cycle(blue)

white.stop
green.stop
red.stop
blue.stop

GPIO.cleanup()