import tkinter as tk
from tkinter import TOP, GROOVE
import frame_3

LARGE_FONT = ("Roboto Medium", 10)

class Frame_6(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file="C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/WELCOmE TO waterlec .png")
        label = tk.Label(image=photo)
        label.image = photo
        imgLabel = tk.Label(self, image=photo)
        imgLabel.pack(side=TOP)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width=2, height=1, font = LARGE_FONT,
                        command=lambda: parent.show_frame(frame_3.Frame_3))
        btn.pack()


class Frame_6_water(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file="C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/WELCOmE TO waterlec (2).png")
        label = tk.Label(image=photo)
        label.image = photo
        imgLabel = tk.Label(self, image=photo)
        imgLabel.pack(side=TOP)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width=2, height=1, font = LARGE_FONT,
                        command=lambda: parent.show_frame(frame_3.Frame_3_water))
        btn.pack()
