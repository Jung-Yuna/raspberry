# This example is a hello world example
# for using a keypad with the Raspberry Pi


import RPi.GPIO as GPIO
from time import sleep 



L1 = 5
L2 = 6
L3 = 13
L4 = 19


C1 = 12
C2 = 16
C3 = 20
C4 = 21


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)


GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

keypadPressed = -1
input =""

def keypadCallback(channel):
    global keypadPressed
    
    if (keypadPressed == -1):
        keypadPressed = channel
        
GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)

def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)
    
def specialKeyPress():
    global input
    pressed = False
    
    GPIO.output(L3, GPIO.HIGH)
    
    if (GPIO.input(C4) == 1):
        print("Input reset")
        pressed = True
        
    GPIO.output(L3, GPIO.LOW)
    
    GPIO.output(L1, GPIO.HIGH)
    
    if (not pressed and GPIO.input(C4) ==1):
        print("Your entered value is "+input)
        pressed = True
        
    GPIO.output(L1, GPIO.LOW)
    
    if(pressed):
        input =""
        
    return pressed


def readLine(line, characters):
    global input
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        sleep(0.3)
        input = input + characters[0]
    if(GPIO.input(C2) == 1):
        sleep(0.3)
        input = input + characters[1]
    if(GPIO.input(C3) == 1):
        sleep(0.3)
        input = input + characters[2]
    if(GPIO.input(C4) == 1):
        sleep(0.3)
        input = input + characters[3]
    GPIO.output(line, GPIO.LOW)


try:
    while True:
        if(keypadPressed != -1):
            setAllLines(GPIO.HIGH)
            if(GPIO.input(keypadPressed) == 0):
                keypadPressed = -1
                
            else:
                sleep(0.1)
        else:
            if(not specialKeyPress()):
                readLine(L1, ["1","2","3","A"])
                readLine(L2, ["4","5","6","B"])
                readLine(L3, ["7","8","9","C"])
                readLine(L4, ["*","0","#","D"])
                sleep(0.1)
            else:
                sleep(0.1)
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
