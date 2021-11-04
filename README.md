# pi-simple-switch
A Simple Raspberry PI GPIO Input from a momentary switch to drive an LED via a GPIO Output

Read the status of a momentary switch on GPIO Pin 16 (note the use of a Blue LED in place of a 10k Ohm Pull down resistor)

On detection of the trailing edge (as the switch is released) change the state of a variable and various LED's tied to GPIO PINs

Change the state of a GPIO Output pin that drives a Buzzer via direct input from a GPIO pin to Ground.

![Alt text](https://github.com/MikeCoutts/pi-simple-switch/blob/main/images/IMG_20211103_225959778.jpg?raw=true "Traffic Lights")

# Simple Rasbpery Pi Bread Board wiring for this project
[Buzzer](https://www.amazon.com/dp/B07S85WRSZ?psc=1&ref=ppx_yo2_dt_b_product_details) ground on 5V GND line with +ve into GPIO 23
Blue (GPIO 17), Green (GPIO 23) and Red (GPIO 22) connected to White Led BGR Anodes via 10K Ohm Resitors with Cathod to Ground.
Red (GPIO 13), Amber/Yellow (GPIO 19), Green (GPIO 26) connected to Red/Amber/Green LED's via 10K Ohm resitors.
10K Ohm resiter supplying power to momentary switch with a Blue line (connected to GPIO Input 16) being drawn down by a Blue LED.

# Operation of the Program
On Initialization Green LED is on for traffic progression and "Combination White" LED is Red to stop People crossing.

Upon Button depression the Blue LED get's a simple direct power supply (via a 10K Ohm resister) with the side effect of bringing the "Button" Line Low
Upon release the pi-simple-switch program detects the rising edge and flips from car mode to pedistrain mode:

Green Off, RED/Amber On and all of the combi giving a White light to pedestrians plus a screatching Buzzer for ADA.

A second depression and release of the Button flips the lights back to Car Mode.
