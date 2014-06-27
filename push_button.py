import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
input = GPIO.input(7)

while True:
	if(GPIO.input(7)):
		print("BUTTON PRESSED")

