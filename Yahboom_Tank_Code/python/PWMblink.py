import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1)
p.start(100)
input('Press return to stop:')
p.stop()
GPIO.cleanup()