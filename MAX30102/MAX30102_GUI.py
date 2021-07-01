import tkinter

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)

import max30102
import hrcalc

print("[INFO] MAX30102 Channel & I2C Address.")
m = max30102.MAX30102()
hr2 = 0
sp2 = 0


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.TitleLbl = tkinter.Label(window, text="MAX30102 WITH RASPBERRY PI",font=("Arial", 20, 'bold'), fg = "black",relief="raised",borderwidth = 2)
        self.TitleLbl.pack(anchor=tkinter.CENTER, expand=True)

        self.TitleLbl = tkinter.Label(window, text="DEVELOPER : RAVIVARMAN RAJENDIRAN",font=("Arial", 15, 'bold'), fg = "dark orchid",relief="raised",borderwidth = 1)
        self.TitleLbl.pack(anchor=tkinter.CENTER, expand=True)
        
        self.PulseLbl = tkinter.Label(window, text="[Heart Pulse Rate    : ]",font=("Arial", 20), fg = "red",relief="ridge",borderwidth = 2)
        self.PulseLbl.pack(anchor=tkinter.CENTER, expand=True)

        self.SPO2Lbl = tkinter.Label(window, text="[Oxygen Saturation   : ]",font=("Arial", 20), fg ="blue",relief="ridge",borderwidth = 2)
        self.SPO2Lbl.pack(anchor=tkinter.CENTER, expand=True)
       
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 30
        self.update()

        self.window.mainloop()

 
    def update(self):
        if(GPIO.input(18)==0):
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            if(hrb == True and hr != -999 and hr < 105):
                hr2 = int(hr)
                #print("Heart Rate : ",hr2)
                self.PulseLbl['text'] = "[Heart Pulse Rate    : "+str(hr2)+"bpm]"
            if(spb == True and sp != -999 and sp < 100):
                sp2 = int(sp)
                #print("SPO2       : ",sp2)
                self.SPO2Lbl['text'] = "[Oxygen Saturation   : "+str(sp2)+"%]"
        self.window.after(self.delay, self.update)


# Create a window and pass it to the Application object
root = tkinter.Tk()
root.geometry("+{}+{}".format(250, 50))
App(root, "PULSE OXIMETER")
