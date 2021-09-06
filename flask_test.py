from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
# Make flask run on this machine's IP address
app.run(host="10.14.25.25")

#blinking = False

# Inizalizing gpio pins
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)

# Light Status
ledStatus = "LED OFF"


@app.route("/")
def hello():
    return "<p>hello</p>"

@app.route("/on")
def on():
    global ledStatus
    
    GPIO.output(21, GPIO.HIGH)
    ledStatus = "LED ON"
    return "light on"
    
@app.route("/off")
def off():
    global ledStatus
    
    blinking = False
    GPIO.output(21, GPIO.LOW)
    ledStatus = "LED OFF"
    return "light off"

@app.route("/blink/", defaults={"seconds" : 10})
@app.route("/blink/<seconds>")
def blink(seconds):
    global ledStatus
    
    seconds = int(seconds)
    ledStatus = "LED BLINKING"
    
    for i in range(seconds):
        GPIO.output(21, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(21, GPIO.LOW)
        time.sleep(0.5)
    ledStatus = "LED FINISHED BLINKING"
   ## ledStatus = "LED OFF"
    return "blinking"

@app.route("/status")
def status():
    return ledStatus

    
