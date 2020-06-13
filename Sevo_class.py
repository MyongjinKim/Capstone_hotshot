import RPi.GPIO as GPIO   # Import the GPIO library.
from time import sleep

class MyServo:
    # 생성자
    def __init__(self):
        self.gpio = GPIO
        self.gpio.setmode(gpio.BOARD) 
        self.gpio.setup(12, gpio.OUT) 
        self.gpio.setup(11, gpio.OUT) 
        self.gpio.setup(13, gpio.OUT) 
        self.pwm = GPIO.PWM(12, 100)  
        self.pwm.start(0)
        # 소멸자

