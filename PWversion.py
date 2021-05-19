import RPi_I2C_driver
import RPi.GPIO as GPIO 
from keypad import keypad
from time import *


GPIO.setwarnings(False)

mylcd = RPi_I2C_driver.lcd()


if __name__ == '__main__':
    # Initialize
    while True:
        kp = keypad(columnCount = 4)
        
         
        sleep(1)
      # waiting for a keypress
        digit = None
        while digit == None:
            digit = kp.getKey()
            
        
        if digit == '#':
            sleep(0.5)
            seq = []
            mylcd.lcd_display_string(" Password:",1)
                
            for i in range(4):
                digit = None
                while digit == None:
                    digit = kp.getKey()
                seq.append(digit)
                mylcd.lcd_display_string_pos("*",1,0x0A + i)
                sleep(0.3)
                
                print(digit)
                sleep(0.3)
            print(seq)
            if seq == [1, 2, 3, 4]:
                print ("Door is OPEN")
                mylcd.lcd_display_string(' *Door is OPEN*',2)
                sleep(3)
                mylcd.lcd_clear()
                
            else:
                print ("Wrong Password")
                mylcd.lcd_display_string(' Wrong Password',2)
                sleep(3)
                mylcd.lcd_clear()
               
        else:
            seq = []
            mylcd.lcd_display_string_pos("HOME:",1,0x03)
            for i in range(5):
                digit = None
                while digit == None:
                    digit = kp.getKey()
                seq.append(digit)
                print(digit)
                sleep(0.3)
                if 'A' in seq:
                    sleep(0.5)
                    print(seq)
                    mylcd.lcd_display_string('  ***CALLING***',2)
                    sleep(3)
                    mylcd.lcd_clear()
                    break
                        
                mylcd.lcd_display_string_pos(str(digit),1,0x08 + i)
                sleep(0.3)
                
 
                
                
   

