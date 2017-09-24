import time
import RPi.GPIO as GPIO

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(35,GPIO.OUT)
	GPIO.output(35,GPIO.LOW)
	GPIO.setup(37,GPIO.OUT)
	GPIO.output(37,GPIO.LOW)

def red_on():
	GPIO.output(35,GPIO.HIGH)

def red_off():
	GPIO.output(35,GPIO.LOW)
	
def green_on():
	GPIO.output(37,GPIO.HIGH)

def green_off():
	GPIO.output(37,GPIO.LOW)

def yellow_on():
	red_on()
	green_on()

def yellow_off():
	red_off()
	green_off()

def cleanup():	
	GPIO.cleanup()
