"""
Spin motors for 1 minute
"""
from machine import Pin, PWM
from time import sleep
# config pins
INA_LEFT = Pin(22, Pin.OUT) #3,8
INB_LEFT = Pin(26, Pin.OUT) #4,9
INA_LEFT.off() #INA_LEFT.VALUE(0)
INB_LEFT.off()
PWM_LEFT = PWM(Pin(21)) #2,7
PWM_LEFT.freq(1000)
INA_RIGHT = Pin(6, Pin.OUT) #3,8
INB_RIGHT = Pin(5, Pin.OUT) #4,9
INA_RIGHT.off() #INA_LEFT.VALUE(0)
INB_RIGHT.off()
PWM_RIGHT = PWM(Pin(8)) #2,7
PWM_RIGHT.freq(1000)
#Forward
INB_LEFT.on()
PWM_LEFT.duty_u16(int(65025/2)) #1/2 max speed
INB_RIGHT.on()
PWM_RIGHT.duty_u16(int(65025/2)) #1/2 max speed
sleep(60) #spin 60 sec
# Stop
PWM_LEFT.duty_u16(0)
INA_LEFT.off()
INB_LEFT.off()
PWM_RIGHT.duty_u16(0)
INA_RIGHT.off()
INB_RIGHT.off()


