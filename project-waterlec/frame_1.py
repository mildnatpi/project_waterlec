import tkinter as tk
from tkinter import TOP, GROOVE

import frame_2

class Frame_1(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file="WELCOmE TO waterlec (3).png")
        label = tk.Label(image=photo)
        label.image = photo
        imgLabel = tk.Label(self, image=photo)
        imgLabel.pack(side=TOP)

        btn = tk.Button(self, text="Let's go", fg="black", relief=GROOVE, command=lambda: parent.show_frame(
            frame_2.Frame_2))
        btn.pack()
