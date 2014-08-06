import RPi.GPIO as GPIO

def init():
	
	# to use Raspberry Pi board pin numbers 
	GPIO.setmode(GPIO.BOARD)
	# set up GPIO output channel 	 
	GPIO.setup(3, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(8, GPIO.OUT)	
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(3, GPIO.LOW)
        GPIO.setup(5, GPIO.LOW)
        GPIO.setup(10, GPIO.LOW)
        GPIO.setup(8, GPIO.LOW)
	GPIO.setup(23, GPIO.LOW) 
        GPIO.setup(7, GPIO.LOW)


