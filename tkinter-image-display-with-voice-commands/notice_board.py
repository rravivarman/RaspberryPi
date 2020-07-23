import tkinter as tk
from PIL import Image,ImageTk
import os

import speech_recognition as sr

r = sr.Recognizer()
speech = sr.Microphone(device_index=0)

class ImageClassifyer(tk.Frame):


    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.root = parent
        self.root.wm_title("IoT Notification Board System")   
        src = "/home/pi/images/"

        self.list_images = []
        for d in os.listdir(src):
            self.list_images.append(d)

        self.frame1 = tk.Frame(self.root, width=self.root.winfo_screenwidth(), height=600, bd=2)
        self.frame1.grid(row=0, column=0)

        self.frame2 = tk.Frame(self.root, width=self.root.winfo_screenwidth(), height=600, bd=2)
        self.frame2.grid(row=1, column=0)
        
        self.cv1 = tk.Canvas(self.frame2, height=self.root.winfo_screenheight()-10, width=self.root.winfo_screenwidth()-10, background="white", bd=1, relief=tk.SUNKEN)
        self.cv1.grid(row=1,column=0)
        
        backButton = tk.Button(self.frame1, text='Back', height=2, width=10, command=self.Back)
        backButton.grid(row=0, column=0, padx=4, pady=2)

        nextButton = tk.Button(self.frame1, text='Next', height=2, width=10, command = self.next_image)
        nextButton.grid(row=0, column=1, padx=4, pady=2)

        self.counter = -1
        self.max_count = len(self.list_images)-1

        self.img = Image.open("/home/pi/INTRO.jpg")
        self.img = self.img.resize((self.root.winfo_screenwidth()-15, self.root.winfo_screenheight()-15), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.img)
        self.cv1.create_image(0, 0, anchor = 'nw', image = self.image)
         
        #self.next_image()

        
    def Back(self):
        print("Back Image")
        if self.counter < 1:
            print("No more images")
        else:
            self.counter -= 1
            print(self.counter)
            self.im = Image.open("{}{}".format("/home/pi/images/", self.list_images[self.counter]))
            self.im = self.im.resize((self.root.winfo_screenwidth()-15, self.root.winfo_screenheight()-15), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.im)

            if self.counter == self.max_count:
                self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
            else:
                self.cv1.delete("all")
                self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
                
    def next_image(self):
        print("Next Image")
        if self.counter > self.max_count-1:
            print("No more images")
        else:
            self.counter += 1
            print(self.counter)
            
            self.im = Image.open("{}{}".format("/home/pi/images/", self.list_images[self.counter]))
            self.im = self.im.resize((self.root.winfo_screenwidth()-10, self.root.winfo_screenheight()-10), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.im)

            if self.counter == 0:
                self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)

            else:
                self.cv1.delete("all")
                self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
            
        
        
#if __name__ == "__main__":
root = tk.Tk() 
MyApp = ImageClassifyer(root)
root.attributes('-fullscreen', True)

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=0.51)
        audio = recognizer.listen(source,None,1)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def task():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000
    microphone = sr.Microphone(device_index=0)
    
    print("Say something!")
    guess = recognize_speech_from_mic(recognizer, microphone)
    yousaid = guess["transcription"]
    print("You said: ",yousaid)
    
    if yousaid is not None:
        if yousaid == "next" or yousaid == "Next" or yousaid == "forward" or yousaid == "Forward" or yousaid == "password":
                MyApp.next_image()
        if yousaid == "back" or yousaid == "Back" or yousaid == "backward" or yousaid == "Backward" or yousaid == "Akbar":
                MyApp.Back()
    else:
        print("Can't get you");
        

    root.after(1000, task)  

root.after(1000, task)

tk.mainloop()
