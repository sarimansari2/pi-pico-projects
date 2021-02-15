from seven_seg import decode
from time import sleep
from machine import Pin

# This is the Example of Seven segment display Driver 

while True:
    for i in range(10):
        decode(i)
        sleep(1)
        