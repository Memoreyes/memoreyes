import time
import RPi.GPIO as GPIO

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.OUT)
	GPIO.output(4,GPIO.LOW)

	
def green_on():
	GPIO.output(4,GPIO.HIGH)

def green_off():
	GPIO.output(4,GPIO.LOW)

def cleanup():	
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	green_on()
