import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(26, GPIO.OUT) #setup pin 26 as an outpout pin

import time
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
light_on = False 

while True:
  #take a reading
  input = GPIO.input(16)
 
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
  
    if light_on == True : 
      GPIO.output(26, GPIO.LOW)
      light_on = False 
    else:
      GPIO.output(26, GPIO.HIGH)
      light_on = True

  # update prev_input value 
  prev_input = input
 
  #slight pause to debounce
  time.sleep(0.05)
