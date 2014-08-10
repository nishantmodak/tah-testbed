import RPi.GPIO as GPIO
import time
import func
import lcd_rpi
import serial
import lcd_over

#inistilize all the pins to low.
func.init()
#We start testing the digital I/O, i.e from pin 2 to pin 13

GPIO.output(7,GPIO.HIGH)

#I/O=13
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=12
GPIO.output(3,GPIO.HIGH)	
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/0=11
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=10
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/0=9
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)
	
#I/0=8
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=7
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)
	
#I/O=6
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)
	
#I/0=5
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)
	
#I/0=4
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)
		
#I/0=3
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)
	
#I/0=2
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)
	

GPIO.output(7,GPIO.LOW)

#I/O=13
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=12
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)
     
#I/0=11
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=10
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/0=9
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/0=8
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=7
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/O=6
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
time.sleep(1)

#I/0=5
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)

#I/0=4
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)

#I/0=3
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)

#I/0=2
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.HIGH)
time.sleep(1)

#We start testing the analog I/O, i.e from pin A0-A5.

GPIO.output(7,GPIO.HIGH)

#A0
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)	
time.sleep(1)

#A1
GPIO.output(3,GPIO.HIGH)	
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
time.sleep(1)

#A2
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
time.sleep(1)

#A3
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
time.sleep(1)
	
#A4
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
time.sleep(1)
	
#A5
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
time.sleep(1)

GPIO.output(7,GPIO.LOW)


#A0
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)	
time.sleep(1)

#A1
GPIO.output(3,GPIO.HIGH)	
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
time.sleep(1)

#A2
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.HIGH)
time.sleep(1)

#A3
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.HIGH)
time.sleep(1)

#A4
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.HIGH)
GPIO.output(8,GPIO.LOW)
time.sleep(1)
	
#A5
GPIO.output(3,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
GPIO.output(8,GPIO.LOW)
time.sleep(1)

ser = serial.Serial('/dev/ttyACM0', 9600)
if ser == "ok":
        lcd_rpi.main()
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
elif ser == "fail":
        lcd_rpi.main()
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
        time.sleep(1)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
else
	lcd_over.main()
	GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23,GPIO.LOW)
	














	
	   

