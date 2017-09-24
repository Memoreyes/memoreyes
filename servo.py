
import RPi.GPIO as GPIO
import time
import light as l

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
l.setup()
pwm = GPIO.PWM(18, 100)
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

def open():
	pwm.start(5)
	pwm.ChangeDutyCycle(12.5)
	time.sleep(1)

def close():
	pwm.ChangeDutyCycle(4.5)
	time.sleep(1)
if __name__ == '__main__':
	
	open()
	close()
