#16x4 LCD INTERFACE WITH RASPBERRY PI.  

##LCD Module Hrdware

The pinout :  

1. Ground
2. Vcc (5V)
3. Contrast Adjustment (10k potentiometer)
4. Register Select(RS) - RS=0: command, RS=1: data
5. Read/Write(R/W) - R/W=0: Write, R/W: Read
6. Enable
7. Bit 0(Not required in 4-bit operation) 
8. Bit 1(Not required in 4-bit operation)
9. Bit 2(Not required in 4-bit operation)
10. Bit 3(Not required in 4-bit operation)
11. Bit 4
12. Bit 5
13. Bit 6
14. Bit 7
15. LED Backlight Anode(+)
16. LED Backlight Cathode(-)

Usually the device requires 8 data lines to provide data to Bits 0-7. However the device can be set to a “4 bit” mode which allows you to send data in two chunks (or nibbles) of 4 bits. This is great as it reduces the number of GPIO connections you require when interfacing with your Pi.

Wire up LCD to Raspberry Pi.

LCD Pin|Function|Pi Function|Pi Pin
01|GND|GND|P1-06
02|+5V|+5V|P1-02
03|Contrast(POT)|GND|P1=06
04|RS|GPIO7|P1-26
05|RW|GND|P1-06
06|E|GPIO-8|P1-24
07| - | - | -
08| - | - | -
09| - | - | -
10| - | - | -
11|Data 4|GPIO25|P1-22
12|Data 5|GPIO24|P1-18
13|Data 6|GPIO23|P1-16
14|Data 7|GPIO18|P1-12
15|+5V| - | -
16|GND| - |P1-06

**NOTE:** In order to control the contrast you can adjust the voltage presented to Pin 3 using a potentiometer. This must be between 0 and 5V.

<img src="lcd_int.png" height="200"  > 

##Python

You can control a HD44780 style display using any programmming environment you like but my weapon of choice is Python. Download [RPi.GPIO library](http://www.raspberrypi-spy.co.uk/2012/07/install-rpi-gpio-library-in-raspbian/) to provide access to the GPIO.

###CODE:

``#!/usr/bin/python``  
``#``  
``# HD44780 LCD Test Script for``  
``# Raspberry Pi``  

 
``# The wiring for the LCD is as follows:``  
``# 1 : GND``  
``# 2 : 5V``  
``# 3 : Contrast (0-5V)*``  
``# 4 : RS (Register Select)``  
``# 5 : R/W (Read Write)       - GROUND THIS PIN``  
``# 6 : Enable or Strobe``  
``# 7 : Data Bit 0             - NOT USED``  
``# 8 : Data Bit 1             - NOT USED``  
``# 9 : Data Bit 2             - NOT USED``  
``# 10: Data Bit 3             - NOT USED``  
``# 11: Data Bit 4``  
``# 12: Data Bit 5``  
``# 13: Data Bit 6``  
``# 14: Data Bit 7``  
``# 15: LCD Backlight +5V**``  
``# 16: LCD Backlight GND``  


``#import``  
``import RPi.GPIO as GPIO``  
``import time``	  
  
``# Define GPIO to LCD mapping``  
``LCD_RS = 7``  
``LCD_E  = 8``  
``LCD_D4 = 25``  
``LCD_D5 = 24``  
``LCD_D6 = 23``  
``LCD_D7 = 18``  
 
``# Define some device constants``  
``LCD_WIDTH = 16    # Maximum characters per line``  
``LCD_CHR = True``  
``LCD_CMD = False``  
  
``LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line``  
``LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line``  
 
``# Timing constants``  
``E_PULSE = 0.00005``  
``E_DELAY = 0.00005``  
  
``def main():``  
``  # Main program block``  
 
 `` GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers``  
 `` GPIO.setup(LCD_E, GPIO.OUT)  # E``  
 `` GPIO.setup(LCD_RS, GPIO.OUT) # RS``  
 `` GPIO.setup(LCD_D4, GPIO.OUT) # DB4``  
 `` GPIO.setup(LCD_D5, GPIO.OUT) # DB5``  
 `` GPIO.setup(LCD_D6, GPIO.OUT) # DB6``  
 `` GPIO.setup(LCD_D7, GPIO.OUT) # DB7``  
 
``  # Initialise display``  
``  lcd_init()``  
 
``  # Send some test``  
``  lcd_byte(LCD_LINE_1, LCD_CMD)``  
``  lcd_string("Rasbperry Pi")``  
``  lcd_byte(LCD_LINE_2, LCD_CMD)``  
``  lcd_string("Model B")``  
  
``  time.sleep(3) # 3 second delay``  
  
``  # Send some text``  
``  lcd_byte(LCD_LINE_1, LCD_CMD)``  
``  lcd_string("Raspberrypi-spy")``  
``  lcd_byte(LCD_LINE_2, LCD_CMD)``  
``  lcd_string(".co.uk")``  
 
`` time.sleep(20)``  
 
``def lcd_init():``  
``  # Initialise display``  
``  lcd_byte(0x33,LCD_CMD)``  
``  lcd_byte(0x32,LCD_CMD)``  
``  lcd_byte(0x28,LCD_CMD)``  
``  lcd_byte(0x0C,LCD_CMD)``  
``  lcd_byte(0x06,LCD_CMD)``  
``  lcd_byte(0x01,LCD_CMD) ``  
 
``def lcd_string(message):``  
``  # Send string to display``  
 
``  message = message.ljust(LCD_WIDTH," ") ``  
 
``  for i in range(LCD_WIDTH):``  
``    lcd_byte(ord(message[i]),LCD_CHR)``  
  
``def lcd_byte(bits, mode):``  
``  # Send byte to data pins``  
``  # bits = data``  
``  # mode = True  for character``  
``  #        False for command``  
  
``  GPIO.output(LCD_RS, mode) # RS``  
 
``  # High bits``  
``  GPIO.output(LCD_D4, False)``  
``  GPIO.output(LCD_D5, False)``  
``  GPIO.output(LCD_D6, False)``  
``  GPIO.output(LCD_D7, False)``  
``  if bits&0x10==0x10:``  
``    GPIO.output(LCD_D4, True)``  
``  if bits&0x20==0x20:``  
``    GPIO.output(LCD_D5, True)``  
``  if bits&0x40==0x40:``  
``    GPIO.output(LCD_D6, True)``  
``  if bits&0x80==0x80:``  
``    GPIO.output(LCD_D7, True)``  
   
``  # Toggle 'Enable' pin``  
``  time.sleep(E_DELAY)``  
``  GPIO.output(LCD_E, True)``  
``  time.sleep(E_PULSE)``  
``  GPIO.output(LCD_E, False)``  
``  time.sleep(E_DELAY)``  
``  # Low bits``  
``  GPIO.output(LCD_D4, False)``  
``  GPIO.output(LCD_D5, False)``  
``  GPIO.output(LCD_D6, False)``  
``  GPIO.output(LCD_D7, False)``  
``  if bits&0x01==0x01:``  
``    GPIO.output(LCD_D4, True)``  
``  if bits&0x02==0x02:``  
``    GPIO.output(LCD_D5, True)``  
``  if bits&0x04==0x04:``  
``    GPIO.output(LCD_D6, True)``  
``  if bits&0x08==0x08:``  
``    GPIO.output(LCD_D7, True)``  
  
``  # Toggle 'Enable' pin``  
``  time.sleep(E_DELAY)``  
``  GPIO.output(LCD_E, True)``  
``  time.sleep(E_PULSE)``  
``  GPIO.output(LCD_E, False)``  
``  time.sleep(E_DELAY)  ``  
  
``if __name__ == '__main__':``  
``  main()``  




