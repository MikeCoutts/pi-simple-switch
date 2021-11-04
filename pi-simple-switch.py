# Copyright The Kavinjka Software Company 2021
#
# Authour MikeC@kavinjka.com

import RPi.GPIO as GPIO
import time # for sleep functions

from signal import signal, SIGINT # for Cntrl-C
from sys import exit

# define the GPIO port for the Button
button = 16

# define the GPIO ports for the Traffic Lights
green = 26
amber = 19
red = 13

# define the GPIO ports for the Cross Walk Signal 
combi_red = 22
combi_green = 27
combi_blue = 17

# define the GPIO port for the Buzzer Activation
buzzer = 23

# Define an exit handler for the program (called on Cntrl-C)
def CntrlCHandler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    GPIO.cleanup()
    exit(0)

# setup  the Cntrl-C handler
signal(SIGINT, CntrlCHandler)

# Initialize the  GPIO Infrastructure to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Setup all the Input and Output GPIO Pins
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 (button) to be an input pin and set initial value to be pulled low (off)

GPIO.setup(green, GPIO.OUT) 
GPIO.setup(amber, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

GPIO.setup(combi_red, GPIO.OUT)
GPIO.setup(combi_green, GPIO.OUT)
GPIO.setup(combi_blue, GPIO.OUT) 

GPIO.setup(buzzer, GPIO.OUT)

#initialise a previous_input variable to 0 (assume button not pressed on startup)
previous_input = 0
crossing = False 

# turn on the Green Light and red cross walk light, Assume the cross-Walk is Cars through.
def InitializeCrossWalk():
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(amber, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(combi_red, GPIO.HIGH)
    GPIO.output(combi_blue, GPIO.LOW)
    GPIO.output(combi_green, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)

InitializeCrossWalk()

# infinate loop for the main thread (Use Cntrl-C to exit)
while True:
  # take a reading from the switch
  input = GPIO.input(button)
 
  # if the last reading was high and this one is low, signal Button Released
  if ((previous_input) and not input):
    print("Button Released")
  
    if crossing == True: 
      GPIO.output(green, GPIO.HIGH)
      GPIO.output(amber, GPIO.LOW)
      GPIO.output(red, GPIO.LOW)

      GPIO.output(buzzer, GPIO.LOW)
      crossing = False

      # make the Combi LED Red)
      GPIO.output(combi_red, GPIO.HIGH)
      GPIO.output(combi_green, GPIO.LOW)
      GPIO.output(combi_blue, GPIO.LOW) 
    else:
      GPIO.output(green, GPIO.LOW)
      GPIO.output(amber, GPIO.HIGH)
      GPIO.output(red, GPIO.HIGH)

      GPIO.output(buzzer, GPIO.HIGH)
      crossing = True

      # make the Combi LED White 
      GPIO.output(combi_green, GPIO.HIGH)
      GPIO.output(combi_blue, GPIO.HIGH)
      GPIO.output(combi_red, GPIO.HIGH)

  # update prev_input value 
  previous_input = input
 
  #slight pause to debounce
  time.sleep(0.05)
