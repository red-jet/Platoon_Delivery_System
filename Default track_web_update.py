import RPi.GPIO as GPIO
import time

# Pins for Motor Driver Inputs
# Left motor
Motor1A = 24
Motor1B = 23
Motor1E = 25

# Right motor
Motor2A = 5
Motor2B = 6
Motor2E = 26

# IR sensor
IR_sensor1 = 2  # Right
IR_sensor2 = 3  # Left

# Ultra sonic sensor
TRIG = 21
ECHO = 20

# Servo Motor
servo_pin = 17


def destroy():
    GPIO.cleanup()


def Motor_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.setup(Motor2A, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def forward():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 1)
    for x in range(8):
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 1)
        time.sleep(0.020)
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 0)
        time.sleep(0.02)

        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 1)
        time.sleep(0.019)
        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 0)
        time.sleep(0.02)
        if x == 79:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)


def right():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 1)

    for x in range(2):
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 1)
        time.sleep(0.05)
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 0)
        time.sleep(0.02)

        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 1)
        time.sleep(0.019)
        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 0)
        time.sleep(0.02)
        if x == 44:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)


def left():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 1)

    for x in range(8):
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 1)
        time.sleep(0.019)
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 0)
        time.sleep(0.02)

        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 1)
        time.sleep(0.0435)
        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 0)
        time.sleep(0.02)
        if x == 44:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)



def Stop():
    GPIO.output(Motor1E, 0)
    GPIO.output(Motor2E, 0)


def Servo_run():
    servo1 = GPIO.PWM(servo_pin, 50)
    servo1.start(0)


def default_track():
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()
    right()
    forward()

    st_reached_C = "The Platoon Leader has reached Destination B"
    Create_Txt(st_reached_C)
    


def Create_Txt(st):
    with open('value.txt', 'w', newline='') as f:
        f.write(st)
        f.close()


if __name__ == '__main__':  # Program start from here
    Motor_setup()
    #Servo_run()

    try:
        print("Setup Complete successfully")
        st_start = "The Platoon Leader started from Location A"
        Create_Txt(st_start)
        default_track()
        print("Program End")
    except KeyboardInterrupt:
        destroy()
