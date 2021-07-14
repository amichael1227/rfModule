#!/usr/bin/env python3

# Import libraries we need
import time
import serial
import threading


# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = '/dev/ttyS0',
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
state = State.EMPTY


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
        time.sleep(0.5)
        readAndDecode()
        # Set the state based on the message
        if(message.upper == "IDLE"):
            state = State.IDLE
        elif(message.upper == "LED_ON"):
            state = State.LED_ON
        elif(message.upper == "EMPTY"):
            state = State.EMPTY

        

# Function to perform actions based on the state
def action(arg1):
    global message
    global state
    while 1:
        time.sleep(0.5)
        # Depending on the state, do a thing
        if(state == State.IDLE):
            print(message) 
        elif(state == State.LED_ON):
            print(message)


# Create and start the threads
getAndSaveThread = threading.Thread(name='getAndSave', target=setState, args=(1,)).start()
actionThread = threading.Thread(name='action', target=action, args=(1,)).start()