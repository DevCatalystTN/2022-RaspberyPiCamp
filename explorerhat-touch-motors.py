#will move a motor forward or backward
#whenever the 1 or 3 button on an explorer hat
#is being held
import explorerhat
from time import sleep
from gpiozero import Button

def redOn(channel, event):  #turns on red LED and motor forward
    explorerhat.light[2].on()
    explorerhat.motor.one.forward(25)

def blueOn(channel, event): #turns on blue LED and motor backward
    explorerhat.light[0].on()
    explorerhat.motor.one.backward(25)

def blueOff(channel, event):    #reverse of blueOn
    explorerhat.light[0].off()
    explorerhat.motor.one.stop()

def redOff(channel, event):     #reverse of redOn
    explorerhat.light[2].off()
    explorerhat.motor.one.stop()



while True:    #infinite loop
    explorerhat.touch.one.pressed(blueOn)
    #returns true when the 1 button is pressed and runs blueOn

    explorerhat.touch.three.pressed(redOn)
    #returns true when the 3 button is pressed and runs redOn

    explorerhat.touch.one.released(blueOff)
    #returns true when the 1 button is released and runs blueOff

    explorerhat.touch.three.released(redOff)
    #returns true when the 3 button is released and runs redOff
        

    

    
