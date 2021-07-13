#!/usr/bin/env python3

import time
import serial

ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)



while 1:
  # Transmit your message
  s = input('Please type your message: ')
  s = s + '\n'
  ser.write(s.encode())
  time.sleep(1)



