# playing a noise when motion is sensed using a PIR sensor and a speaker

from gpiozero import MotionSensor#imports motion sensor
import pygame.mixer#imports the pygame instance library

sensor = MotionSensor(5)#shortens the sensor syntax

pygame.init()#begins an instance of pygame
sound  = pygame.mixer.Sound('/home/pi/doorbell-1.wav')
#sets the sound to be played

while True:#infinite loop
    if sensor.motion_detected:#checks for motion
        sound.play()#plays the specified noise
