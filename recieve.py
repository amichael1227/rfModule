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

def recieve(arg1):
    # Recieve your message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    num = x.decode()
    #return x.decode()
    

t = threading.Thread(target=recieve, args=(1,), daemon=True).start()


while 1:
    print(num)
    time.sleep(1)