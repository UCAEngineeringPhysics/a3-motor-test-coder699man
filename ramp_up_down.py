"""
Ramp up motors' speed forward in 4 seconds. 
Slow down motors' speed forward in 4 seconds. 
Ramp up motors' speed backward in 4 seconds. 
Slow down motors' speed backward in 4 seconds. 
Stop motors.
"""
from machine import Pin, PWM
from time import sleep

# I used AI to deal with the acceleration and deceleration time

# config pins
INA_LEFT = Pin(22, Pin.OUT)
INB_LEFT = Pin(26, Pin.OUT)
PWM_LEFT = PWM(Pin(21))
PWM_LEFT.freq(1000)

INA_RIGHT = Pin(6, Pin.OUT)
INB_RIGHT = Pin(5, Pin.OUT)
PWM_RIGHT = PWM(Pin(8))
PWM_RIGHT.freq(1000)

# Define the time duration for acceleration and deceleration
acceleration_time = 4  # seconds
deceleration_time = 4  # seconds
# Define the number of steps for smooth acceleration/deceleration
steps = 100  
# Calculate the time delay for each step
accel_step_delay = acceleration_time / steps
decel_step_delay = deceleration_time / steps

# forward
INA_LEFT.off()
INB_LEFT.on()
INA_RIGHT.off()
INB_RIGHT.on()

for duty in range(0, 65025, 65026 // steps):
    PWM_LEFT.duty_u16(duty)
    PWM_RIGHT.duty_u16(duty)
    sleep(accel_step_delay)

for duty in range(65025, -1, -(65026 // steps)):
    PWM_LEFT.duty_u16(duty)
    PWM_RIGHT.duty_u16(duty)
    sleep(decel_step_delay)

# backward
INA_LEFT.on()
INB_LEFT.off()
INA_RIGHT.on()
INB_RIGHT.off()

for duty in range(0, 65025, 65026 // steps):
    PWM_LEFT.duty_u16(duty)
    PWM_RIGHT.duty_u16(duty)
    sleep(accel_step_delay)

for duty in range(65025, -1, -(65026 // steps)):
    PWM_LEFT.duty_u16(duty)
    PWM_RIGHT.duty_u16(duty)
    sleep(decel_step_delay)

# Stop the motors
PWM_LEFT.duty_u16(0)
INA_LEFT.off()
INB_LEFT.off()

PWM_RIGHT.duty_u16(0)
INA_RIGHT.off()
INB_RIGHT.off()

