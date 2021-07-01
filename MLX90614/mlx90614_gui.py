import os
import tkinter

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)

from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)


class App:
    def __init__(self, window, window_title):
        self.window = window

        self.TitleLbl = tkinter.Label(window, text="MLX90614 WITH RASPBERRY PI",font=("Arial", 20, 'bold'), fg = "black",relief="raised",borderwidth = 2)
        self.TitleLbl.pack(anchor=tkinter.CENTER, expand=True)

        self.TitleLbl = tkinter.Label(window, text="DEVELOPER : RAVIVARMAN RAJENDIRAN",font=("Arial", 15, 'bold'), fg = "dark orchid",relief="raised",borderwidth = 1)
        self.TitleLbl.pack(anchor=tkinter.CENTER, expand=True)
        
        self.Temp1Lbl = tkinter.Label(window, text="[Body Temperature    : ]",font=("Arial", 20), fg = "orange",relief="ridge",borderwidth = 2)
        self.Temp1Lbl.pack(anchor=tkinter.CENTER, expand=True)

        self.Temp2Lbl = tkinter.Label(window, text="[Ambient Temperature : ]",font=("Arial", 20), fg = "dark green",relief="ridge",borderwidth = 2)
        self.Temp2Lbl.pack(anchor=tkinter.CENTER, expand=True)
        
        self.delay = 30
        self.update()

        self.window.mainloop()

 
    def update(self):
        if(GPIO.input(18)==0):
            celcius = sensor.get_object_1();
            faren = (celcius*1.8)+32
            ambient = sensor.get_ambient()
            self.Temp1Lbl['text'] = "[Body Temperature    : "+str(round(faren, 2))+u"\N{DEGREE SIGN}F]"
            self.Temp2Lbl['text'] = "[Ambient Temperature : "+str(round(ambient, 2))+u"\N{DEGREE SIGN}C]"
        self.window.after(self.delay, self.update)
            


# Create a window and pass it to the Application object
root = tkinter.Tk()
root.geometry("+{}+{}".format(250, 50))
App(root, "INFRARED TEMPERATURE SENSOR")
