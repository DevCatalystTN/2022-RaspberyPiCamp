# Flashing LED

from gpiozero import LED
from time import sleep

# the LED pin number should match your wires

myled = LED(17)

while True:
    myled.on()
    sleep(1)
    myled.off()
    sleep(1)


