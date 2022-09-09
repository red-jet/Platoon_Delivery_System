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
IR_sensor1 = 2       # Right
IR_sensor2 = 3       # Left

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
    GPIO.setup(servo_pin, GPIO.OUT)


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




def Forward_platoon():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 1)
    for x in range(5):
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
        if x == 4:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)


def Right_platoon():
    GPIO.output(Motor1E, 1)
    GPIO.output(Motor2E, 0)

    for x in range(3):
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 1)
        time.sleep(0.05)
        GPIO.output(Motor1A, 0)
        GPIO.output(Motor1B, 0)
        time.sleep(0.02)

        if x == 2:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)


def Left_platoon():
    GPIO.output(Motor1E, 0)
    GPIO.output(Motor2E, 1)

    for x in range(3):
        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 1)
        time.sleep(0.05)
        GPIO.output(Motor2A, 0)
        GPIO.output(Motor2B, 0)
        time.sleep(0.02)

        if x == 2:
            GPIO.output(Motor1E, 0)
            GPIO.output(Motor2E, 0)


def Stop():
    GPIO.output(Motor1E, 0)
    GPIO.output(Motor2E, 0)


def Servo_run():
    servo1 = GPIO.PWM(servo_pin, 50)
    servo1.start(0)
    print("servo detected")


if __name__ == '__main__':  # Program start from here
    Motor_setup()
    Sensor_setup()
    Ultrasonic_setup()
    Servo_run()
    i=0
    end_check = 0

    while i<3000:
        try:
            ir_val_r = GPIO.input(int(IR_sensor1))
            ir_val_l = GPIO.input(int(IR_sensor2))
            print(f"i={i}\tIR1={ir_val_r}\tIR2={ir_val_l}")
            distance_platoon = Ultrasonic_distance()
            print(f"Distance_p (cm) = {distance_platoon}")

            #print("Starting to follow")
            if (ir_val_r == 0) and (distance_platoon >= 7 and distance_platoon <= 50) and (ir_val_l == 0):
                Forward_platoon()
            elif (ir_val_r == 1) and (ir_val_l == 0):
                Left_platoon()
            elif (ir_val_r == 0) and (ir_val_l == 1):
                Right_platoon()
            elif (ir_val_r == 0) and (ir_val_l == 0) and distance_platoon > 1 and distance_platoon < 30:
                time.sleep(0.1)
                
                print("Reached")
                dis_check = Ultrasonic_distance()
                if dis_check >=7:
                    print("distance_platoon pass lable")
                    pass
                else:
                    end_check += 1
                    print ("end check = ",end_check)
                    if end_check == 50:
                        Stop()
                        print("End Check Stop")
                        break

            i += 1
            #print("ended")
        except KeyboardInterrupt:
            destroy()
