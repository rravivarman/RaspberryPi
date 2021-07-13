from time import sleep
import RPi.GPIO as GPIO

DIR = 20       # Direction GPIO Pin
STEP = 21      # Step GPIO Pin
CW = 1         # Clockwise Rotation
CCW = 0        # Counterclockwise Rotation
SPR = 200       # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)


MODE = (14, 15, 18) # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

GPIO.output(MODE, RESOLUTION['1/32'])

delay = .005 / 32

#RB=32
#GB=12
#BB=6
#IB=18
#EB=25

RB=32
GB=12
BB=5
IB=18
EB=25

cb = "excess"
nb = "invalid"

#~~~~~~~~~~~~~~~RED~~~~~~~~~~~~~~~~~~~~~~~~~~

if(cb=="red" and nb=="blue"):
    GPIO.output(DIR, CW)
    step_count = SPR * 5
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb
    
if(cb=="red" and nb=="green"):
    GPIO.output(DIR, CW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb    

if(cb=="red" and nb=="excess"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

if(cb=="red" and nb=="invalid"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

#~~~~~~~~~~~~~~~BLUE~~~~~~~~~~~~~~~~~~~~~~~~~~
    
if(cb=="blue" and nb=="red"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

if(cb=="blue" and nb=="green"):
    GPIO.output(DIR, CW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb    

if(cb=="blue" and nb=="excess"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

if(cb=="blue" and nb=="invalid"):
    GPIO.output(DIR, CW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb   
#~~~~~~~~~~~~~~~GREEN~~~~~~~~~~~~~~~~~~~~~~~~~~    

if(cb=="green" and nb=="red"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb
    
if(cb=="green" and nb=="blue"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb
    
if(cb=="green" and nb=="excess"):
    GPIO.output(DIR, CW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

if(cb=="green" and nb=="invalid"):
    GPIO.output(DIR, CW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    ccb=nb
    
#~~~~~~~~~~~~~~~EXCESS~~~~~~~~~~~~~~~~~~~~~~~~~~
    
if(cb=="excess" and nb=="red"):
    GPIO.output(DIR, CW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

if(cb=="excess" and nb=="green"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb
    
if(cb=="excess" and nb=="blue"):
    GPIO.output(DIR, CW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb

if(cb=="excess" and nb=="invalid"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb
    
#~~~~~~~~~~~~~~~INVALID~~~~~~~~~~~~~~~~~~~~~~~~~~
    
if(cb=="invalid" and nb=="red"):
    GPIO.output(DIR, CW)
    step_count = SPR * 13
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb="red"
    
if(cb=="invalid" and nb=="green"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb
    
if(cb=="invalid" and nb=="blue"):
    GPIO.output(DIR, CCW)
    step_count = SPR * 12
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    ccb=nb
    
if(cb=="invalid" and nb=="excess"):
    GPIO.output(DIR, CW)
    step_count = SPR * 6
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
    cb=nb 
   


