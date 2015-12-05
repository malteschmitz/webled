#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

WHITE_PIN = 37 # GPIO26
GREEN_PIN = 35 # GPIO19
RED_PIN   = 33 # GPIO13
BLUE_PIN  = 31 # GPIO6

PWM_FREQUENCY = 100 # Hz

GPIO.setmode(GPIO.BOARD)
GPIO.setup(WHITE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

pwms = {
  'white': GPIO.PWM(WHITE_PIN, PWM_FREQUENCY),
  'green': GPIO.PWM(GREEN_PIN, PWM_FREQUENCY),
  'red': GPIO.PWM(RED_PIN, PWM_FREQUENCY),
  'blue': GPIO.PWM(BLUE_PIN, PWM_FREQUENCY)
}

values = {
  'white': 0,
  'green': 0,
  'red': 0,
  'blue': 0
}

for name in pwms:
  pwms[name].start(values[name])

from flask import Flask, request, url_for, redirect
app = Flask(__name__, static_url_path='')

@app.route("/", methods=['GET'])
def index():
  return redirect(url_for('static', filename='index.html'))

@app.route("/<name>", methods=['GET'])
def read(name):
  if name == 'index.html':
    return app.send_static_file('index.html')
  if name in pwms:
    return str(values[name])
  return "Not found", 404

@app.route("/<name>", methods=['PUT'])
def write(name):
  if name in pwms:
    try:
      value = int(request.data)
      if (value < 0 or value > 255):
        return "Invalid argument", 422
      values[name] = value
      pwms[name].ChangeDutyCycle(value)
    except ValueError:
      return "Invalid argument", 422
    print("DutyCycle of " + name + " set to " + str(value))
    return "", 200
  return "Not found", 404  

app.run(host='0.0.0.0', port=80)

for name in pwms:
  pwms[name].stop()

GPIO.cleanup()