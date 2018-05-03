import time
import playsound
import RPi.GPIO as GPIO

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	#take a reading
	input = GPIO.input(7)
	#print(input)
	#if the last reading was low and this one high, print)
	if ((not prev_input) and input):
		print(input)
		playsound.playsound(True)
	#update previous input
	prev_input = input
	#slight pause to debounce
	time.sleep(0.05)
