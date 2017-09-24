import os
import datetime, json
import RPi.GPIO as GPIO
import time
import face as f
import light as l
import tag as t
import ultranew as u
from twilio.rest import Client

account_sid = "AC0af2539a4b3464099277e467b55416e2"
auth_token = "6b0795ad780fce6469afe57f6724a557"
client = Client(account_sid, auth_token)

l.setup()

right = 19
left = 13
middle = 26

def speak_name(personsName):
	with open('DATA.txt','w') as dataFile:
		json.dump(personsName, dataFile)
	os.system('node texttospeechv1.js')
def sendsms():
	message = client.api.account.messages.create(to="+17036095733",
                                             from_="+12402610654",
                                             body="Enter Name for New Face, Just enter Name: No spaces",)
def get_name():
	f = open("name.txt","r")
	name = f.readlines()
	name = name[0]
	print(name)
	return name
def setup_switch():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(right,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(middle,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(left,GPIO.IN, pull_up_down=GPIO.PUD_UP)

if __name__ == '__main__':
	setup_switch()
	while True:
		print("Reading")
		time.sleep(0.2)
		#os.system("clear")
		input_stateright = GPIO.input(right)
		input_statemiddle = GPIO.input(middle)
		input_stateleft = GPIO.input(left)
		if input_stateright == False:
			print("Right Button Pressed")
			time.sleep(1)
			l.red_on()
			while True:
				inp = GPIO.input(right)
				if inp == False:
					l.red_off()
					l.yellow_on()
					time.sleep(0.3)
					l.yellow_off()
					time.sleep(0.3)
					l.yellow_on()
					os.system("fswebcam -r 1280x720 imageread.jpg")
					time.sleep(3)
					ret = f.recognize_face("imageread.jpg","mainppl")
					print("Rec Face:" + str(ret))
					speak_name(ret)
					os.system("aplay output.wav")
					l.yellow_off()
					l.green_on()
					time.sleep(1)
					l.green_off()
					print("Done")
					break
		if input_stateleft == False:
			print("Left Button Pressed")
			time.sleep(1)
			l.red_on()
			while True:
				inp = GPIO.input(left)
				if inp == False:
					l.red_off()
					l.yellow_on()
					time.sleep(0.3)
					l.yellow_off()
					time.sleep(0.3)
					l.yellow_on()
					os.system("fswebcam -r 1280x720 imagetag.jpg")
					time.sleep(2)
					op = t.get_tags("imagetag.jpg")
					print(op)
					l.yellow_off()
					l.green_on()
					time.sleep(1)
					l.green_off()
					print("Done")
					break
		if input_statemiddle == False:
			print("Middle Button Pressed")
			time.sleep(1)
			l.red_on()
			while True:
				inp = GPIO.input(middle)
				if inp == False:
					l.red_off()
					l.yellow_on()
					time.sleep(0.3)
					l.yellow_off()
					time.sleep(0.3)
					l.yellow_on()
					os.system("fswebcam -r 1280x720 image.jpg")
					time.sleep(1)
					sendsms()
					print("sending sms")
					time.sleep(20)
					print("getting name")
					name = get_name()
					print(name)
					time.sleep(3)
					print("enrolling face")
					f.enroll_face("image.jpg",name,"mainppl")
					l.yellow_off()
					l.green_on()
					time.sleep(2)
					l.green_off()
					print("Face Added")
					break				

