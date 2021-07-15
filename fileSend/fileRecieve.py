#!/usr/bin/env python3
# File Name:
# fileRecieve.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 14, 2021
# Decription:
# This program allows for files to be recieved over UART.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import time
import serial
import threading
import sys

# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)