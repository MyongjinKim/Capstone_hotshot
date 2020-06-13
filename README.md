### Capstone_hotshot

## summary

* **06/13** : Test raspberryPi4 PWM 

   ```py
    import RPi.GPIO as GPIO   # Import the GPIO library.
    from time import sleep
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(pin, GPIO.OUT) 
        pwm = GPIO.PWM(pin, dutycycle)  
        pwm.start(pwmchanel)
   ```
   basic setup for PWM 

* 
