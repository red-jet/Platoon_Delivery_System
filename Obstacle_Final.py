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


def Sensor_setup():
    GPIO.setup(IR_sensor1, GPIO.IN)
    GPIO.setup(IR_sensor2, GPIO.IN)
    # GPIO.setup(servo_pin, GPIO.OUT)


def Motor_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.setup(Motor2A, GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def Ultrasonic_setup():
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    time.sleep(0.2)


def Ultrasonic_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    # print(f"Distance (cm) = {distance}")
    return distance


def forward():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 1)
    for x in range(10):
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
        if x == 59:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)


def right():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 1)

    for x in range(8):
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 1)
        time.sleep(0.0435)
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 0)
        time.sleep(0.02)

        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 1)
        time.sleep(0.019)
        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 0)
        time.sleep(0.02)
        if x == 29:
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


# default in left side of the road
Left_Road = 1

if __name__ == '__main__':  # Program start from here
    Motor_setup()
    Ultrasonic_setup()
    # Servo_run()

    i = 0
    while i < 15:
        try:
            distance_platoon = Ultrasonic_distance()
            print("distace_platoon",distance_platoon)
            if 50 <= distance_platoon <= 60:
                print("inside")
                time.sleep(.1)
                if Left_Road == 1:
                    right()
                    forward()
                    right()
                    forward()
                    forward()
                    forward()
                    left()
                    left()
                    
                    
                    #forward()
                    Left_Road = 0
                else:
                    left()
                    left()
                    forward()
                    right()
            elif distance_platoon <= 30:
                print("obstacle too near chances of hitting ----")
                print("Will Not move futher")
                Stop()
                break
                
            print("this forward")    
            forward()
            #left()
            
            i += 1
                
            if i == 2:
                Stop()
                print("ended")
          
        except KeyboardInterrupt:
            destroy()
