#will light a different light for each numbered button
import explorerhat
from time import sleep
from gpiozero import Button

def red(channel, event):
    explorerhat.light[2].on()
    sleep(1)
    explorerhat.light[2].off()

def blue(channel, event):
    explorerhat.light[0].on()
    sleep(1)
    explorerhat.light[0].off()

def green(channel, event):
    explorerhat.light[3].on()
    sleep(1)
    explorerhat.light[3].off()

def yellow(channel, event):
    explorerhat.light[1].on()
    sleep(1)
    explorerhat.light[1].off()

x = True

while x == True:
    explorerhat.touch.one.pressed(blue)
    
    explorerhat.touch.two.pressed(yellow)
      
    explorerhat.touch.three.pressed(red)
        
    explorerhat.touch.four.pressed(green)
        

    

    
