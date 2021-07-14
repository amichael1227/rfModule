#!/usr/bin/env python3

# Import libraries we need
import time
import serial


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


# Sets up the serial port for our RF Modules
while 1:
  # Transmit your message
  s = input('Please type your message: ')
  s = s + '\n'
  ser.write(s.encode())