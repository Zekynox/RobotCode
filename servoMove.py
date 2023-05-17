ServoPin = 23
import RPi.GPIO as GPIO
import time

#set up servo
global pwm_servo
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ServoPin, GPIO.OUT)
pwm_servo = GPIO.PWM(ServoPin, 50)
pwm_servo.start(0)

while True:
    pwm_servo.ChangeDutyCycle(2.5 + 10 * 50/180)
    time.sleep(1)