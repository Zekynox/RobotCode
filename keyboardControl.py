import curses
import time
import RPi.GPIO as GPIO

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()
key = ""
PWMSleep = 0.03

IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(True)


def motor_init():
    global pwm_ENA
    global pwm_ENB
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    
    
def forward(speed): 
    stdscr.addstr(9, 5, "forward")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    #PWM duty cycle is set to 100（0--100）
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)

def backward(speed): 
    stdscr.addstr(9, 5, "backward")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    #PWM duty cycle is set to 100（0--100）
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)
    
def right(speed): 
    stdscr.addstr(9, 5, "right")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    #PWM duty cycle is set to 100（0--100）
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)

def left(speed): 
    stdscr.addstr(9, 5, "left")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    #PWM duty cycle is set to 100（0--100）
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)

def w():
    forward(50)
    
def s():
    backward(50)

def a():
    left(50)

def d():
    right(50) 

# fast
def W():
    forward(100)

def S():
    backward(100)

def A():
    pass

def D():
    pass 

motor_init()
stdscr.nodelay(True)
while key != ord("q"):
    key = stdscr.getch()
    if key < 0:
        pwm_ENA.start(0)
        pwm_ENB.start(0)
        continue
    stdscr.addch(2,25,key)
    stdscr.addstr(2, 30, f"key : {key}")
    stdscr.refresh()
    try:
        eval(f"{chr(key)}()")
    except NameError as e:
        stdscr.addstr(7, 10, "Bad Press")
    if key == curses.KEY_UP:
        stdscr.addstr(4, 20, "Up")
    elif key == curses.KEY_DOWN:
        stdscr.addstr(5, 20, "Down")

curses.endwin()

# normal


#ra : 261 la : 260 ua :259 da : 258
#shift ra : 402 la : 393 ua : 337 da : 336