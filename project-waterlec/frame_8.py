import tkinter as tk
from tkinter import LEFT, GROOVE

import frame_7
import frame_6

LARGE_FONT = ("Roboto Medium", 10)

class Frame_8(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData(self, bgt):

        label = tk.Label(self, text="Amount of units that you can use", justify=LEFT, font = ('Roboto Medium', 15))
        label.pack(padx = 10, pady = 8)
        E = tk.Label(self, bd=3, width=10, text = bgt, font = ('Roboto Medium', 15))
        E.pack(padx = 10, pady = 10)

        label = tk.Label(self, text="See the tricks & trips", font = LARGE_FONT)
        label.pack(padx = 10, pady = 5)

        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width = 2, height = 1, font = LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_6.Frame_6))
        btn.pack(padx = 10, pady = 5)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=4, height=1, font = LARGE_FONT,
                         command=lambda: self.parent.show_frame(frame_7.Frame_7))
        btn1.pack(padx = 10, pady = 8)



class Frame_8_water(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData_2(self, bgt):

        label = tk.Label(self, text="Amount of units that you can use", justify=LEFT, font = ('Roboto Medium', 15))
        label.pack(padx = 10, pady = 8)
        E = tk.Label(self, bd=3, width=10, text = bgt, font = ('Roboto Medium', 15))
        E.pack(padx = 10, pady = 10)

        label = tk.Label(self, text="See the tricks & trips")
        label.pack(padx = 10, pady = 5)
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width = 2, height = 1, font = LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_6.Frame_6_water))
        btn.pack(padx = 10, pady = 5)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=4, height=1, font = LARGE_FONT,
                         command=lambda: self.parent.show_frame(frame_7.Frame_7_water))
        btn1.pack(padx = 10, pady = 8)