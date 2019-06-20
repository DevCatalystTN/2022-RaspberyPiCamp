# makes motor 1 plugged into explorer hat go forwards

import explorerhat
from time import sleep

explorerhat.motor.one.forward(25)
#starts the motor moving forwards
sleep(3)
#keeps the motor spinning for 3 seconds
explorerhat.motor.one.stop()
#stops the motor
