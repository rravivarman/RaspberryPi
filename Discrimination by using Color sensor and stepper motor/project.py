import time
import board
import busio
import digitalio
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from tkinter import *
from tkinter import messagebox
from time import sleep
import RPi.GPIO as GPIO

DIR = 20       # Direction GPIO Pin
STEP = 21      # Step GPIO Pin
CW = 1         # Clockwise Rotation
CCW = 0        # Counterclockwise Rotation
SPR = 200       # Steps per Revolution (360 / 1.8)

IR = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(IR, GPIO.IN)

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

i2c = busio.I2C(board.SCL, board.SDA)
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c)
apds.enable_color = True

blue_count = 0
red_count = 0
green_count = 0

max_blue_count = 0
max_red_count = 0
max_green_count = 0

red_counter = 0
green_counter = 0
blue_counter = 0
invalid_counter = 0
excess_counter = 0

objDetected = False


current_box = "red"
next_box = ""

window =Tk()
window.title("COUNTS")

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))

lbl1 = Label(window, text="RED OBJECT COUNT:")
lbl1.grid(column=0,row=0)

txt1 = Entry(window,width=10)
txt1.grid(column=2,row=0)

lbl2 = Label(window, text="GREEN OBJECT COUNT:")
lbl2.grid(column=0,row=1)

txt2 = Entry(window,width=10)
txt2.grid(column=2,row=1)

lbl3 = Label(window, text="BLUE OBJECT COUNT:")
lbl3.grid(column=0,row=2)

txt3 = Entry(window,width=10)
txt3.grid(column=2,row=2)

def select_box():
    global current_box
    global next_box
    print("current_box:{}, next_box:{} ".format(current_box,next_box))
    if(current_box=="red" and next_box=="red"):
        current_box=next_box
        print("++++++++++++++++++++++Red box selected");
    if(current_box=="red" and next_box=="blue"):
        GPIO.output(DIR, CW)
        step_count = SPR * 5
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Blue box selected");
        
    if(current_box=="red" and next_box=="green"):
        GPIO.output(DIR, CW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Green box selected");

    if(current_box=="red" and next_box=="excess"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Excess box selected");

    if(current_box=="red" and next_box=="invalid"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Invalid box selected");

    #~~~~~~~~~~~~~~~BLUE~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    if(current_box=="blue" and next_box=="red"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Red box selected");

    if(current_box=="blue" and next_box=="green"):
        GPIO.output(DIR, CW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Green box selected");

    if(current_box=="blue" and next_box=="excess"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Excess box selected");

    if(current_box=="blue" and next_box=="invalid"):
        GPIO.output(DIR, CW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Invalid box selected");
    #~~~~~~~~~~~~~~~GREEN~~~~~~~~~~~~~~~~~~~~~~~~~~    

    if(current_box=="green" and next_box=="red"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Red box selected");
        
    if(current_box=="green" and next_box=="blue"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Blue box selected");
        
    if(current_box=="green" and next_box=="excess"):
        GPIO.output(DIR, CW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Excess box selected");

    if(current_box=="green" and next_box=="invalid"):
        GPIO.output(DIR, CW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Invalid box selected");
        
    #~~~~~~~~~~~~~~~EXCESS~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    if(current_box=="excess" and next_box=="red"):
        GPIO.output(DIR, CW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Red box selected");

    if(current_box=="excess" and next_box=="green"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Green box selected");
        
    if(current_box=="excess" and next_box=="blue"):
        GPIO.output(DIR, CW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Blue box selected");

    if(current_box=="excess" and next_box=="invalid"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Invalid box selected");
        
    #~~~~~~~~~~~~~~~INVALID~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    if(current_box=="invalid" and next_box=="red"):
        GPIO.output(DIR, CW)
        step_count = SPR * 13
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box="red"
        print("++++++++++++++++++++++Red box selected");
        
    if(current_box=="invalid" and next_box=="green"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Green box selected");
        
    if(current_box=="invalid" and next_box=="blue"):
        GPIO.output(DIR, CCW)
        step_count = SPR * 12
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Blue box selected");
        
    if(current_box=="invalid" and next_box=="excess"):
        GPIO.output(DIR, CW)
        step_count = SPR * 6
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)
        current_box=next_box
        print("++++++++++++++++++++++Excess box selected");
        
def clicked():
    global max_red_count
    global max_green_count
    global max_blue_count
    
    red_count_txt = txt1.get()
    green_count_txt = txt2.get()
    blue_count_txt = txt3.get()
    if(red_count_txt != ""):
        max_red_count = int(red_count_txt)
    else:
        max_red_count = 0
        
    if(green_count_txt != ""):
        max_green_count = int(green_count_txt)
    else:
        max_green_count = 0
        
    if(blue_count_txt != ""):
        max_blue_count = int(blue_count_txt)
    else:
        max_blue_count = 0
        
    if ( max_red_count < 1  or max_green_count < 1 or max_blue_count < 1):
        messagebox.showinfo("Alert", "Enter all the object counts!!!")
    else:
        print("red count:{}, green count:{}, blue count:{} ".format(max_red_count, max_green_count, max_blue_count))
        messagebox.showinfo("Bye", "Press CLOSE button to continue")
        
btn1 = Button(window, text="OK", command=clicked)
btn1.grid(column=1,row=3)
btn2 = Button(window, text="CLOSE", command=window.destroy)
btn2.grid(column=2,row=3)
window.mainloop()

while True:
    
    while not apds.color_data_ready:
        time.sleep(0.005)
    r, g, b, c = apds.color_data

    print("red:{}, green:{}, blue:{} ".format(r, g, b))

    irData = GPIO.input(IR);

    if(objDetected == False and irData == False):
        objDetected = True
        print("####################Object Found")
        if(red_counter > green_counter and red_counter > blue_counter and red_counter > excess_counter and red_counter > invalid_counter):
            next_box = "red"
            if(red_count < max_red_count):
                red_count = red_count + 1
            else:
                next_box = "excess"
        if(green_counter > red_counter and green_counter > blue_counter and green_counter > excess_counter and green_counter > invalid_counter):
            next_box = "green"
            if(green_count < max_green_count):
                green_count = green_count + 1
            else:
                next_box = "excess"
        if(blue_counter > green_counter and blue_counter > red_counter and blue_counter > excess_counter and blue_counter > invalid_counter):
            next_box = "blue"
            if(blue_count < max_blue_count):
                blue_count = blue_count + 1
            else:
                next_box = "excess"
        if(invalid_counter > green_counter and invalid_counter > blue_counter and invalid_counter > excess_counter and invalid_counter > red_counter):
            next_box = "invalid"
        select_box()
    elif(objDetected == True and irData == True):
        objDetected = False
        red_counter = 0
        green_counter = 0
        blue_counter = 0
        invalid_counter = 0
        excess_counter = 0
        print("####################Object Passed")

    print("Red count:{}".format(red_count))
    print("Green count:{}".format(green_count))
    print("Blue count:{}".format(blue_count))

    print("Max Red count:{}".format(max_red_count))
    print("Max Green count:{}".format(max_green_count))
    print("Max Blue count:{}".format(max_blue_count))
                
    if( r <= 200 and g <= 200 and b <= 200):
        print ("OBJECT NOT FOUND")
    elif(r > g and r > b):
        red_counter = red_counter + 1
        print ("~~~~~~~~~~~~~~~~RED OBJECT FOUND")
                    
    elif (g > r and g > b):
        green_counter = green_counter + 1
        print ("~~~~~~~~~~~~~~~~GREEN OBJECT FOUND")
                
    elif (b > r and b > g):
        blue_counter = blue_counter + 1
        print ("~~~~~~~~~~~~~~~~BLUE OBJECT FOUND")
        
    else:
        invalid_counter = invalid_counter + 1
        print ("INVALID OBECT FOUND")
                
    time.sleep(1)
