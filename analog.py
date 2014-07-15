import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel  
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7,GPIO.HIGH)

#A0
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.LOW)	
time.sleep(2)

#A1
GPIO.output(3,GPIO.HIGH)	
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(2)

#A2
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(2)

#A3
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(2)
	
#A4
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(2)
	
#A5
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(2)

GPIO.output(7,GPIO.LOW)


#A0
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.LOW)	
time.sleep(2)

#A1
GPIO.output(3,GPIO.HIGH)	
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(2)

#A2
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(2)

#A3
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(2)

#A4
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(2)
	
#A5
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(2)

	
