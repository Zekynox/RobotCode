# reads and runs tank runner format
import sys
import time
import RPi.GPIO as GPIO

filename = sys.argv[1]
f = open(filename, "r")
commands = f.readlines()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PWMSleep = 0.03

IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

pwm_ENA = pwm_ENB = None


def stop():
    global pwm_ENA
    global pwm_ENB
    pwm_ENA.start(0)
    pwm_ENB.start(0)


def motor_init():
    global pwm_ENA
    global pwm_ENB
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    # Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    stop()


def forward(speed, timeAt):
    stop()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(timeAt)


def backward(speed, timeAt):
    stop()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(timeAt)


def right(speed, timeAt):
    stop()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(timeAt)


def left(speed, timeAt):
    stop()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)


def findAction(x):
    if x == "w":
        return "forward"
    elif x == "s":
        return "backward"
    elif x == "a":
        return "left"
    elif x == "d":
        return "right"


motor_init()

for command in commands:
    cmd = command.strip().split()
    if command[0] == "#" or len(cmd) != 3:
        print(command.strip())

    else:
        action = findAction(cmd[0])
        speed = cmd[1]
        timeAt = cmd[2]
        cmd_to_eval = f"{action}({speed}, {timeAt})"
        print(cmd_to_eval)
        eval(cmd_to_eval)
    stop()
