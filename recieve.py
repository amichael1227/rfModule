#!/usr/bin/env python3

from ast import Num
import time
import serial
import threading

ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)

num = 'meh'

# background
def recieve(arg1):
    while 1:
        #global num
        # Recieve your message
        x = ser.readline()
        while (x.decode() == ''):
            x = ser.readline()
        num = x.decode()
        #return x.decode()
        

# foreground
def foreground(arg1):
    #global num
    print('foreground')
    input('Press Enter')
    print(num)


b = threading.Thread(name='background', target=recieve, args=(1,), daemon=True)
f = threading.Thread(name='foreground', target=foreground, args=(1,), daemon=True)



b.start()
f.start()