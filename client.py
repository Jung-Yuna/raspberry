import socket
import RPi_I2C_driver
import RPi.GPIO as GPIO 
from keypad import keypad
from time import *

HOST = '172.30.1.10'
# Enter IP or Hostname of your server
PORT = 12345
# Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

GPIO.setwarnings(False)

mylcd = RPi_I2C_driver.lcd()
pin=18
 
GPIO.setmode(GPIO.BCM)          
GPIO.setup(pin,GPIO.OUT)      
p=GPIO.PWM(pin,50)             
p.start(0)

#Lets loop awaiting for your input
while True:
    kp = keypad(columnCount = 4)
         
    sleep(1)
    
    #command = raw_input('Enter your command: ')
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
            p.ChangeDutyCycle(2.5)  
            sleep(3)
            mylcd.lcd_clear()
            p.ChangeDutyCycle(7.5)
            
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
                
                #command = digit
                s.send(digit)
                
                reply = s.recv(1024).decode()
                    
                print reply
                if reply == 'open':
                    p.ChangeDutyCycle(2.5)  
                    sleep(3)
                    p.ChangeDutyCycle(7.5)
                    sleep(3)
                    mylcd.lcd_clear()

                break
            else:
                mylcd.lcd_display_string_pos(str(digit),1,0x08 + i)
                sleep(0.3)
                continue
                    
            
            #s.send(command)
            
            
            
        
        


     


