#import I2C_LCD_driver
import RPi_I2C_driver
import RPi.GPIO as GPIO 
from keypad import keypad
from time import *


GPIO.setwarnings(False)

mylcd = RPi_I2C_driver.lcd()


if __name__ == '__main__':
    # Initialize
    kp = keypad(columnCount = 4)
    mylcd.lcd_display_string("Password:",1)
     
    sleep(1)
   # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
   # Print result
    print(digit)
    sleep(0.5)
    
    ###### 4 Digit wait ######
    seq = []
    for i in range(4):
        digit = None
        while digit == None:
            digit = kp.getKey()
        seq.append(digit)
        mylcd.lcd_display_string_pos(str(digit),1,0x09 + i)
        sleep(0.4)
        
        print(digit)
        sleep(0.3)
 
    # Check digit code
    print(seq)
    if seq == [1, 2, 3, 4]:
       print ("Door is OPEN")
       mylcd.lcd_display_string(' *Door is OPEN*',2)
