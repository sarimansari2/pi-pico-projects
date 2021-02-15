from seven_seg import convert
from time import sleep
from machine import Pin

# This is the Example of Seven segment display Driver 

while True:
    for i in range(10):
        convert(i)
        sleep(1)
        