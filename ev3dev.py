#!/usr/bin/env python3
from ev3dev.ev3 import *
# Run the motor from Port A
go = ev3.LargeMotor('outA')
go.run_timed(time_sp=3000, speed_sp=500)

#Run the Large Motor from Port B
a = ev3.LargeMotor('outB')
a.run_timed(time_sp=3000, speed_sp=500)

ts = TouchSensor() #Touch Sensor Function

while True:
    if ts.value()==1:  #if ts is pressed
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        Leds.set_color(Leds.RIGHT, Leds.GREEN)
        b = ev3.LargeMotor('outA')
        b.run_timed(time_sp=3000, speed_sp=-500)
        a = ev3.LargeMotor('outB')
        a.run_timed(time_sp=3000, speed_sp=-500)
    else:
        Leds.set_color(Leds.LEFT, Leds.YELLOW)
        Leds.set_color(Leds.RIGHT, Leds.YELLOW)   #Turn the Leds yellow to sgnify something is wrong
        ev3.Sound.speak('Something is wrong').wait()  #EV3 says something is wrong        
        
     
