# This example is a hello world example
# for using a keypad with the Raspberry Pi
import I2C_LCD_driver
from time import *
import RPi.GPIO as GPIO
import time

mylcd = I2C_LCD_driver.lcd()

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

#------------GPIO pin setting------------------

GPIO.setwarnings(False)   #if 'setwarnig false' error
GPIO.setmode(GPIO.BCM)    #BCM mode


GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
#-----------pin output setting----------------
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
        
    if(GPIO.input(C2) == 1):
        print(characters[1])
        
    if(GPIO.input(C3) == 1):
        print(characters[2])
        
    if(GPIO.input(C4) == 1):
        print(characters[3])
        
    GPIO.output(line, GPIO.LOW)
    
mylcd.lcd_display_string("Password : ",1)
mylcd.lcd_display_string("*",1,0x0A)
mylcd.lcd_display_string("*",1,0x0B)
mylcd.lcd_display_string("*",1,0x0C)
mylcd.lcd_display_string("*",1,0x0D)

try:
    while True:
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
        
        
except KeyboardInterrupt:
    print("\nApplication stopped!")

