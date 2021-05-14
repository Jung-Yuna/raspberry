import RPi_I2C_driver
import RPi.GPIO as GPIO 
from keypad import keypad
from time import *


 
GPIO.setwarnings(False)



if __name__ == '__main__':
    # Initialize
    kp = keypad(columnCount = 4)
    lcd = RPi_I2C_driver.lcd(0x27)
    lcd.cursor()
    Lprint("Hello")

    sleep(1)
   # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    # Print result
    #print(digit)
    sleep(0.5)
    
    
    ###### 4 Digit wait ######
    seq = []
    for i in range(4):
        digit = None
        while digit == None:
            digit = kp.getKey()
        seq.append(digit)
        sleep(0.4)
        
        print(digit)
        sleep(1)
 
    # Check digit code
    print(seq)
    if seq == [1, 2, 3, 4]:
       print ("Code accepted")