# this is the test example for seven segment display driver 

from seven_seg import convert
from time import sleep


# loop section 
while True:
    for i in range(10):
        convert(i)
    