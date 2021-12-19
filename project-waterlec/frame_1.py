import tkinter as tk
from tkinter import TOP, GROOVE

import frame_2

LARGE_FONT = ("Roboto Medium", 10)

class Frame_1(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.photo = tk.PhotoImage(file="C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/WELCOmE TO waterlec (3).png")
        label = tk.Label(image=self.photo)
        label.image = self.photo
        imgLabel = tk.Label(self, image=self.photo)
        imgLabel.pack(side=TOP)

        btn = tk.Button(self, text="Let's go", fg="black", relief=GROOVE, font = LARGE_FONT, command=lambda: parent.show_frame(
            frame_2.Frame_2))
        btn.pack()
