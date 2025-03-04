# Created by Clara T

# Created on Feb 2025

# Blink with Breadboard and LED with resistor

# Turns LED on for one second, the off for one second, each time increases each time by 1 more second


import time
import board
import digitalio

while True:
        pin12write_digital(0)     # Red
        pin11write_digital(0) 
        pin13write_digital(1)
        sleep(1)
        pin13write_digital(0)    # Green
        pin11write_digital(1)
        pin12write_digital(0)
        sleep(1)
        pin13write_digital(0) 
        pin11write_digital(0)    # Blue
        pin12write_digital(1)
        sleep(1)
        pin11write_digital(0)    # Magenta
        pin13write_digital(1)
        pin12write_digital(1)
        sleep(1)
        pin12write_digital(0)     #  Yellow
        pin13write_digital(1)
        pin11write_digital(1)
        sleep(1)
        pin13write_digital(0)   # Cyan
        pin11write_digital(1)
        pin12write_digital(1)
        sleep(1)
        pin13write_digital(1)     # White
        pin12write_digital(1)
        pin11write_digital(1)
        sleep(1)
        pin13write_digital(0)
        pin11write_digital(0)
        pin12write_digital(0)