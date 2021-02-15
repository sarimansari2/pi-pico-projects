'''
    author:     Syeed Mohd Ameen                                          DATE: 14-02-2021
    mail:       ameensyeed2@gmail.com
    License:    GPLv3 
    

    DRIVER FOR 4-DIGIT SEVEN SEGMENT DISPLAY 


    SEGMENT PINS (GPIO)

                a = gpio 0
                b = gpio 1
                c = gpio 2 
                d = gpio 3 
                e = gpio 4 
                f = gpio 5 
                g = gpio 6 
                dot = gpio 7 

    ENABLE PINS (GPIO)
                SEG 1 = gpio 8 
                SEG 2 = gpio 9 
                SEG 3 = gpio 10
                SEG 4 = gpio 11 

    
        SEVEN SEGEMENT DISPLAY

                  a
                -----
             f |     | b 
               |  g  |
                -----
             e |     | c 
               |     |
                -----
                  d 
    
'''



from machine import Pin
from time import sleep 


# Registers for different segments (store as a string type) 
REG1 = 0
REG2 = 0
REG3 = 0
REG4 = 0

# segment pins (GPIO)
pin = [0,1,2,3,4,5,6,7]

# segment enable pins (4 digit)
pin_en = [8,9,10,11]



# constant declaration here
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
dot = 7 


A = 7
B = 8
C = 9
D = 10 


# initilize segment, enable pins
for i in range(8):
    pin[i] = Pin(pin[i],Pin.OUT)

for i in range(4):
    pin_en[i] = Pin(pin_en[i],Pin.OUT)
    

    
# Decoder Function that set the segment pins according to number 
def decode(number):
    global l                 # global segment
    
    if number == '.':
        pin[a].low()
        pin[b].low()
        pin[c].low()
        pin[d].low()
        pin[e].low()
        pin[f].low()
        pin[g].low()
        pin[dot].high()


    # check the possible combination 
    else:
        number = int(number)

        if number == 0:
            pin[a].high()
            pin[b].high()
            pin[c].high()
            pin[d].high()
            pin[e].high()
            pin[f].high()
            pin[g].low()
            pin[dot].low()

           
        elif number == 1:
            pin[a].low()
            pin[b].high()
            pin[c].high()
            pin[d].low()
            pin[e].low()
            pin[f].low()
            pin[g].low()
            pin[dot].low()
        
        elif number == 2:
            pin[a].high()
            pin[b].high()
            pin[c].low()
            pin[d].high()
            pin[e].high()
            pin[f].low()
            pin[g].high()
            pin[dot].low()
        
    
        elif number == 3:
            pin[a].high()
            pin[b].high()
            pin[c].high()
            pin[d].high()
            pin[e].low()
            pin[f].low()
            pin[g].high()
            pin[dot].low()
            
        
        elif number == 4:
            pin[a].low()
            pin[b].high()
            pin[c].high()
            pin[d].low()
            pin[e].low()
            pin[f].high()
            pin[g].high()
            pin[dot].low()
        
        elif number == 5:
            pin[a].high()
            pin[b].low()
            pin[c].high()
            pin[d].high()
            pin[e].low()
            pin[f].high()
            pin[g].high()
            pin[dot].low()
        
        elif number == 6:
            pin[a].high()
            pin[b].low()
            pin[c].high()
            pin[d].high()
            pin[e].high()
            pin[f].high()
            pin[g].high()
            pin[dot].low()
        
        elif number == 7:
            pin[a].high()
            pin[b].high()
            pin[c].high()
            pin[d].low()
            pin[e].low()
            pin[f].low()
            pin[g].low()
            pin[dot].low()
        
        elif number == 8:
            pin[a].high()
            pin[b].high()
            pin[c].high()
            pin[d].high()
            pin[e].high()
            pin[f].high()
            pin[g].high()
            pin[dot].low()
        
        else:
            pin[a].high()
            pin[b].high()
            pin[c].high()
            pin[d].high()
            pin[e].low()
            pin[f].high()
            pin[g].high()
            pin[dot].low()
        


# set the register value into segment 
def enable():
    global pin_en          # enable pin number 
    global REG1          
    global REG2            # segment registers 
    global REG3
    global REG4
    
    decode(REG1)
    pin_en[0].high()
    sleep(0.005)           # delay upto 5 ms
    pin_en[0].low()
    
    decode(REG2)
    pin_en[1].high()
    sleep(0.005)
    pin_en[1].low()
    
    decode(REG3)
    pin_en[2].high()
    sleep(0.005)
    pin_en[2].low()
    
    decode(REG4)
    pin_en[3].high()
    sleep(0.005)
    pin_en[3].low()
    


def convert(number):
    global REG1
    global REG2
    global REG3
    global REG4
    l = []
    
    l = str(number)
    
    REG1 = l[0]
    REG2 = l[1]
    REG3 = l[2]
    REG4 = l[3]

    enable()
    