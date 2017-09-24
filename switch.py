import RPi.GPIO as GPIO
import time

def setup_switch():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)


if __name__ == '__main__':
	setup_switch()
	while True:
		input_state = GPIO.input(18)
		if input_state == False:
			print("Button Pressed")
			time.sleep(0.2)
