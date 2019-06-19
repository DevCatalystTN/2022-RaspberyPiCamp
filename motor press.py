#Turns a motor whenever the touch buttons are pressed
import explorerhat
from time import sleep
from gpiozero import Button

def lightR():
    explorerhat.light[2].on()

def motorF(channel, event):
    explorerhat.motor.one.forward(100)

def motorR(channel, event):
    explorerhat.motor.one.backward(100)

def handle(channel, event):
           if(channel == 'one' and event == 'press'):
           
    
#while True:
    ##explorerhat.touch.is_held(motorR())

while True:
    explorerhat.touch.is_held(handler_function)
        



#explorerhat.motor.one.forward(100)
