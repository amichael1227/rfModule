#!/usr/bin/env python3
# File Name:
# recieveCMD.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# Alexander Corey
# ajcorey@wpi.edu
# July 14, 2021
# Decription:
# This program recieves messages over UART and executes commands based on what that message says.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/amichael1227/rfModule/blob/master/LICENSE


# Import libraries the program need
import time
import serial
import threading


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = "/dev/ttyS0",
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)


# Define the states
class State():
    IDLE = 0
    LED_ON = 1
    EMPTY = 2


# Creates the global variables needed later
message = ''
state = None


# Function to get and decode the message
def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    message = x.decode()


# Function to set a state based on the message 
def setState(arg1):
    global message
    global state
    while 1:
        # Wait
        time.sleep(1)
        
        # Get the decoded message and format it
        readAndDecode()
        message = message.replace('\n', '').upper()
        
        # Set the state based on the message
        if(message == "IDLE"):
            state = State.IDLE
        elif(message == "LED_ON"):
            state = State.LED_ON
        elif(message.upper() == "EMPTY"):
            state = State.EMPTY
        else:
            pass
        

# Function to perform actions based on the state
def action(arg1):
    global message
    global state
    while 1:
        time.sleep(1)
        # Depending on the state, do a thing
        if(state == State.IDLE):
            print("IDLE")
        elif(state == State.LED_ON):
            print("LED_ON")
        elif(state == State.EMPTY):
            print("EMPTY")
        else:
            pass


# Create and start the threads
getAndSaveThread = threading.Thread(name="getAndSave", target=setState, args=(1,)).start()
actionThread = threading.Thread(name="action", target=action, args=(1,)).start()