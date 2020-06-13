import RPi.GPIO as GPIO   # Import the GPIO library.
from time import sleep


# init GPIO module
def init_moter():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(12, GPIO.OUT) 
    GPIO.setup(11, GPIO.OUT) 
    GPIO.setup(13, GPIO.OUT) 
    pwm = GPIO.PWM(12, 100)  
    pwm.start(0)
    return pwm

def set_dir(input):
    if input == 1:
        GPIO.output(11,True)
        GPIO.output(13,False)
    else :
        GPIO.output(13,True)
        GPIO.output(11,False)

def pwm_control(pwmobject, value):
    pwmobject.ChangeDutyCycle(float(value))

if __name__ == "__main__":
    pwm = init_moter()
    while True:
        flag = input().split() # receve
        if flag[0] == "fire" and len(flag) == 3:
            print("The distance is ",float(flag[1]), "m. So the required force is ",float(flag[2]),"N")
            set_dir(1)
            pwm_control(pwm,int(flag[2]))
            sleep(5)
            set_dir(0)
            
            # return ok
        elif flag[0] == "stop":
            break 

        else :
            # return err
            continue
