import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 0.2)
p.start(0.4)
input('Press return to stop:')
p.stop()
GPIO.cleanup()