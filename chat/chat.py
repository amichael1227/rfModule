#!/usr/bin/env python3
# File Name:
# chat.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 14, 2021
# Decription:
# This program allows for messages to be sent back and forth over UART.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import time
import serial
import threading
import sys

# Sets up the serial port for the RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)

# Creates the global variable needed for later
message = ''


# Function to get and decode the message
def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    message = x.decode()


# Function to transmit the message
def transmit(arg1):
    print("Transmitting...")
    while 1:
        s = sys.stdin.readline()
        ser.write(s.encode())
        time.sleep(0.25)

# Function to recieve the message
def recieve(arg1):
    global message
    print("Recieving... \n")
    while 1:
        # Get the decoded message and format it
        readAndDecode()
        message = message.replace('\n', '')
        print(message)
        time.sleep(0.25)


# Try loop to allow for graceful exit
try:
    # Create and start the threads that allow the devices to chat
    transmitThread = threading.Thread(name="sending", target=transmit, args=(1,)).start()
    recieveThread = threading.Thread(name="recieving", target=recieve, args=(1,)).start()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    sys.exit("Program exiting!")