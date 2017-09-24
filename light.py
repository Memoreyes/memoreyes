import time
import RPi.GPIO as GPIO

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.OUT)
	GPIO.output(4,GPIO.LOW)
	GPIO.setup(17,GPIO.OUT)
	GPIO.output(17,GPIO.LOW)

	
def green_on():
	GPIO.output(4,GPIO.HIGH)

def green_off():
	GPIO.output(4,GPIO.LOW)


def red_on():
	GPIO.output(17,GPIO.HIGH)

def red_off():
	GPIO.output(17,GPIO.LOW)

def cleanup():	
	GPIO.cleanup()
def yellow_on():
	red_on()
	green_on()
def yellow_off():
	red_off()
	green_off()

