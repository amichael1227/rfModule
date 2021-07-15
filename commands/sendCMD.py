#!/usr/bin/env python3
# File Name:
# sendCMD.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# Alexander Corey
# ajcorey@wpi.edu
# July 14, 2021
# Decription:
# This program sends messages over UART for commands to be executed.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE


# Import libraries the program needs
import time
import serial


# Sets up the serial port for the RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


# Sets up the serial port for our RF Modules
while 1:
  # Transmit your message
  s = input("Please type your message: ")
  s = s + '\n'
  ser.write(s.encode())
  time.sleep(0.25)