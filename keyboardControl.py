import curses
import time
import sys

if len(sys.argv) == 2 and sys.argv[1].lower() == "ui":
    move_tank = False

else:
    try:
        import RPi.GPIO as GPIO
        move_tank = True
    except:
        pass
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(True)
stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.addstr(1,10,"Hit SPACEBAR to stop tank")
stdscr.refresh()
key = ""
PWMSleep = 0.03
lastAngle = 500

IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24

#Definition of servo pin
ServoPin = 23


if move_tank:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


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
    #set up servo
    global pwm_servo
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)

    
    
def forward(speed): 
    stdscr.addstr(9, 5, "forward")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)

def backward(speed): 
    stdscr.addstr(9, 5, "backward")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)
    
def right(speed): 
    stdscr.addstr(9, 5, "right")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(PWMSleep)

def left(speed): 
    stdscr.addstr(9, 5, "left")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    #time.sleep(PWMSleep)
    
def wanderReturn(speed):
    forward(speed)
    time.sleep(1)
    left(100)
    time.sleep(1.27)
    #left(50)
    #time.sleep(1.28)
    forward(speed)
    time.sleep(1)
    motor_init()

def lights(servo, r, g, b):
    global lastAngle
    stdscr.addstr(9, 5, "lights")
    if lastAngle != servo:
        pwm_servo.ChangeDutyCycle(2.5 + 10 * servo/180)
        lastAngle = servo
        stdscr.addstr(10, 5, str(servo))
        stdscr.refresh()
    # GPIO.output(LED_R, r)
    # GPIO.output(LED_G, g)
    # GPIO.output(LED_B, b)
    time.sleep(2)
    stdscr.addstr(10, 5, "             ")


# speed(robot messurment)*time(seconds) = degrees r = 2.88
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

def o():
    wanderReturn(20)

def l():
    lights(50, 1, 0, 0)

if move_tank:
    motor_init()

stdscr.nodelay(True)
if not move_tank:
    stdscr.addstr(7, 10, "UI only")

last_key = 0
while key != ord("q"):
    key = stdscr.getch()
    if key < 0:
        continue
    # display key
    if key != last_key:
        last_key = key
        if key == ord(" "):
            # clear the key display
            stdscr.addstr(2, 25, " " * 15)
            stdscr.addstr(9, 5, " " * 10)
        else:
            stdscr.addch(2,25, key)
            stdscr.addstr(2, 30, f"key : {key}")
        stdscr.refresh()
    if not move_tank:
        continue

    # move the tank
    try:
        if key == 32:
            pwm_ENA.start(0)
            pwm_ENB.start(0)
        else:
            eval(f"{chr(key)}()")
    except NameError as e:
        stdscr.addstr(7, 10, "Bad Press " + str(key) )
        print(e)
curses.endwin()

if move_tank:
    GPIO.setup(ENA,GPIO.LOW)
    GPIO.setup(IN1,GPIO.LOW)
    GPIO.setup(IN2,GPIO.LOW)
    GPIO.setup(ENB,GPIO.LOW)
    GPIO.setup(IN3,GPIO.LOW)
    GPIO.setup(IN4,GPIO.LOW)
# normal


#ra : 261 la : 260 ua :259 da : 258
#shift ra : 402 la : 393 ua : 337 da : 336