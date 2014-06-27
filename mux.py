import RPi.GPIO as GPIO
import time

count = 0
# blinking function 
while( count == 0 ):
 
	#def blink(pin):
        #GPIO.output(13,GPIO.HIGH)
        	#time.sleep(1)
        	#GPIO.output(pin,GPIO.LOW)
        	#time.sleep(1)
        	#return
	# to use Raspberry Pi board pin numbers  
	GPIO.setmode(GPIO.BOARD)
	# set up GPIO output channel  
	GPIO.setup(3, GPIO.OUT)
	GPIO.setup(5, GPIO.OUT)
	GPIO.setup(10, GPIO.OUT)
	GPIO.setup(8, GPIO.OUT)
	GPIO.setup(7, GPIO.OUT)

	GPIO.output(7,GPIO.HIGH)
	#I/O=13
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)

	#I/O=12
	GPIO.output(3,GPIO.HIGH)	
	GPIO.output(5,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)

	#I/0=11
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)

	#I/O=10
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)

	#I/0=9
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(10,GPIO.HIGH)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)
	
	#I/0=8
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(10,GPIO.HIGH)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)

	#I/O=7
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(10,GPIO.HIGH)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)
	
	#I/O=6
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(10,GPIO.HIGH)
	GPIO.output(8,GPIO.LOW)
	time.sleep(2)
	
	#I/0=5
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.HIGH)
	time.sleep(2)
	
	#I/0=4
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.HIGH)
	time.sleep(2)
		
	#I/0=3
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.HIGH)
	time.sleep(2)
	
	#I/0=2
	GPIO.output(3,GPIO.HIGH)
	GPIO.output(5,GPIO.HIGH)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(8,GPIO.HIGH)
	time.sleep(2)
	
	count = 1

while( count == 1 ):

        #def blink(pin):
        #GPIO.output(13,GPIO.HIGH)
                #time.sleep(1)
                #GPIO.output(pin,GPIO.LOW)
                #time.sleep(1)
                #return
        # to use Raspberry Pi board pin numbers  
        GPIO.setmode(GPIO.BOARD)
        # set up GPIO output channel  
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)

        GPIO.output(7,GPIO.LOW)
        #I/O=13
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/O=12
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/0=11
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/O=10
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/0=9
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/0=8
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/O=7
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
	time.sleep(2)

        #I/O=6
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        time.sleep(2)

        #I/0=5
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(2)

        #I/0=4
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(2)

        #I/0=3
        GPIO.output(3,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(2)

        #I/0=2
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(2)
	
	count = 2













	
	   

