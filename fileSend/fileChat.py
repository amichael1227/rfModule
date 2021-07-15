#!/usr/bin/env python3
# File Name:
# fileSend.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# July 15, 2021
# Decription:
# This program allows for files to be sent and recieved over UART.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE

# Import libraries we need
import serial
from xmodem import XMODEM
import threading
import sys
import time


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


# Function to get and decode the message
def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    message = x.decode()


# Defines the function for getting a file
def getc(size, timout = 1):
  return ser.read(size) or None


# Defines the function for sending a file 
def putc(data, timeout = 1):
  return ser.write(data)

# Defines function to transmit a file
def transmit(arg1):
    print("Transmitting...")
    while 1:
        file = input("Please type file path...")
        fileName = ''
        while 1:
            stream = open(file, 'rb')
            modem.send(stream)
            time.sleep(0.25)

def recieve(arg1):
    print("Recieving... \n")
    while 1:
        stream = open('output.txt', 'wb')
        modem.recv(stream)



# Define the modem
modem = XMODEM(getc, putc)

# Try loop to allow for graceful exit
try:
    # Create and start the threads that allow the devices to chat
    transmitThread = threading.Thread(name="sending", target=transmit, args=(1,)).start()
    recieveThread = threading.Thread(name="recieving", target=recieve, args=(1,)).start()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    sys.exit("Program exiting!")