from gpiozero import Button#import the button utilities
import pygame.mixer#import the python game instance library

pygame.init()#starts a game instance

button = Button(17)#shortens button syntax
doorbell = pygame.mixer.Sound('/home/pi/doorbell-1.wav')
#shortens sound syntax and specifies the sound byte

while True:#infinite loop
    if button.is_pressed:#checks for pressed button
        doorbell.play()#plays the sound specified

     
