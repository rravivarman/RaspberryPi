import time
import board
import busio
import digitalio
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from tkinter import *
from tkinter import messagebox
from RpiMotorLib import RpiMotorLib

GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 20       # Direction -> GPIO Pin
step = 21      # Step -> GPIO Pin
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

i2c = busio.I2C(board.SCL, board.SDA)
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c)
apds.enable_color = True

blue_count = 0
red_count = 0
green_count = 0

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

def clicked():
    red_count_txt = txt1.get()
    green_count_txt = txt2.get()
    blue_count_txt = txt3.get()
    if(red_count_txt != ""):
        red_count = int(red_count_txt)
    else:
        red_count = 0
        
    if(green_count_txt != ""):
        green_count = int(green_count_txt)
    else:
        green_count = 0
        
    if(blue_count_txt != ""):
        blue_count = int(blue_count_txt)
    else:
        blue_count = 0
        
    if ( red_count < 1  or green_count < 1 or blue_count < 1):
        messagebox.showinfo("Alert", "Enter all the object counts!!!")
    else:
        print("red count:{}, green count:{}, blue count:{} ".format(red_count, green_count, blue_count))
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


    if( r <= 13 and g <= 13 and b <= 13 ):
        print ("TRAY FOUND NO OBEJECT")
    elif(r > g and r > b):
        print ("~~~~~~~~RED OBJECT FOUND")
    elif (g > r and g > b):
        print ("~~~~~~~~GREEN OBJECT FOUND")
    elif (b > r and b > g):
        print ("~~~~~~~~BLUE OBJECT FOUND")
    else:
        print ("TRAY FOUND NO OBEJECT")
        
    time.sleep(1)
