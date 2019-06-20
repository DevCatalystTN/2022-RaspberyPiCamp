#makes motor 1 plugged into explorer hat go backwards

import explorerhat
from time import sleep

explorerhat.motor.one.backward(25)
#makes the motor spin backwards 
sleep(3)
#Keeps the motor spinning for 3 seconds
explorerhat.motor.one.stop()
#stops the motor
