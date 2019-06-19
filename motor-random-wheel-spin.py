#the motor will run for a randomized amount of time
from time import sleep
import explorerhat
import random

spin = random.uniform(0.5, 5)

explorerhat.motor.one.forward(100)

sleep(spin)

explorerhat.motor.one.stop()
