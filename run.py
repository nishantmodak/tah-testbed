import RPi.GPIO as GPIO
import time
import os
import lcd_rpi
import lcd_fail

#adjust for where your switch is connected

while True:
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(11,GPIO.IN)
  GPIO.setup(23,GPIO.OUT)
  GPIO.setup(13,GPIO.IN)
  prev_input = 0

  #take a reading
  input = GPIO.input(11)
  input2 = GPIO.input(13)	
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23,GPIO.LOW)
    #once the button is pressed, the script will run and there will be a single beep sound.
    os.system("make")
    os.system("make upload")
    lcd_rpi.testing()	 
    os.system('python /home/pi/Ali/tah-testbed/tah_final.py')
    #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
  
  if ((not prev_input) and input2):
    GPIO.output(23,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23,GPIO.LOW)
    lcd_fail.main()
    time.sleep(1)		
  #prev_input = input2
 	
  #slight pause to debounce
  time.sleep(0.05)	
  	

