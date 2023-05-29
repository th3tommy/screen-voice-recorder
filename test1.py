import datetime
import tkinter
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from tkinter import *
import customtkinter
import sounddevice as sound
from scipy.io.wavfile import write


class Recorder:
    def __init__(self):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        self.e = customtkinter.CTk()
        self.e.bind("<KeyRelease>", lambda: self.fun)
        # gui part:
        self.e.geometry('1200x1200')
        self.e.title('ESR')
        d = customtkinter.CTkLabel(master=self.e, text='EMARY SCREEN RECORDER', font=('Courier', 20))
        d.pack(fill=X)
        # frame
        fr1 = customtkinter.CTkFrame(master=self.e, width=300, height=300)
        fr1.pack()
        lbl1 = customtkinter.CTkLabel(fr1, text='The main', font=('Mongolian Baiti', 12), fg_color='transparent')
        lbl1.place(relx=0.5, y=10, anchor=tkinter.CENTER)
        z = customtkinter.CTkButton(master=fr1, text='rec', command=self.rec1, width=100, font=('Mongolian Baiti', 12))
        z.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        exit = customtkinter.CTkButton(master=fr1, command=self.e.quit(), text='exit', font=('Mongolian Baiti', 12))
        exit.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label2 = customtkinter.CTkLabel(master=fr1, text="The recording app", fg_color="transparent",
                                        font=('Mongolian Baiti', 12), corner_radius=0.3)
        label2.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        ''''screen recorder'''
        frg = customtkinter.CTkFrame(master=self.e, width=200, height=300)
        frg.place(x=800, y=40)
        n = StringVar()
        n.set('Enter number of secs')
        b = StringVar()
        b.set('Enter name of wav')
        self.duration = customtkinter.CTkEntry(master=frg, textvariable=n, font=('Mongolian Baiti', 13))
        self.duration.place(x=35, y=75)
        butto = customtkinter.CTkButton(master=frg, text='rec', command=lambda: self.record(), width=70, font=('Mongolian Baiti', 13))
        butto.place(x=65, y=125)
        lml = customtkinter.CTkLabel(master=frg, text='voice rec', font=('Mongolian Baiti', 13))
        lml.place(x=75, y=165)
        v = customtkinter.CTkEntry(master=frg, textvariable=b, font=('Mongolian Baiti', 13))
        v.place(x=35, y=25)
        self.e.mainloop()
    def rec1(self):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        timec = datetime.datetime.now().strftime('%H-%M-%S')
        filename = f'{timec}.mp4'
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        captured = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

        while not cv2.waitKey(10) == ord('q'):
            img = ImageGrab.grab(bbox=(0, 0, width, height))
            img_np = np.array(img)
            imgfin = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            cv2.imshow('emary capture', imgfin)
            captured.write(imgfin)
            self.e.quit()

    def fun(self, event):
        print(event.keysym, event.keysym == 'F7')
        if event.keysym == 'F7':
            self.e.quit()
        else:
            pass
    def record(self):
        freq = 44100
        dur = int(self.duration.get())
        recording = sound.rec(dur * freq, samplerate=freq, channels=2)
        sound.wait()
        write(str(self.e.get()) + '.wav', freq, recording)



if __name__ == '__main__':
    Recorder()
