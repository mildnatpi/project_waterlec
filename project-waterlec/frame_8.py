import tkinter as tk
from tkinter import LEFT, GROOVE

import frame_7
import frame_6

LARGE_FONT = ("Verdana", 24)

class Frame_8(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData(self, bgt):

        label = tk.Label(self, text="Amount of units that you can use", justify=LEFT)
        label.pack()
        E = tk.Label(self, bd=3, width=10, text = bgt)
        E.pack()

        label = tk.Label(self, text="See the tricks & trips")
        label.pack()
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width = 2, height = 1,
                        command=lambda: self.parent.show_frame(frame_6.Frame_6))
        btn.pack()

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1,
                         command=lambda: self.parent.show_frame(frame_7.Frame_7_water))
        btn1.pack()



class Frame_8_water(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData_2(self, bgt):

        label = tk.Label(self, text="Amount of units that you can use", justify=LEFT)
        label.pack()
        E = tk.Label(self, bd=3, width=10, text = bgt)
        E.pack()

        label = tk.Label(self, text="See the tricks & trips")
        label.pack()
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width = 2, height = 1,
                        command=lambda: self.parent.show_frame(frame_6.Frame_6_water))
        btn.pack()

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1,
                         command=lambda: self.parent.show_frame(frame_7.Frame_7_water))
        btn1.pack()