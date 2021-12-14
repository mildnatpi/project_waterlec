import tkinter as tk
from tkinter import GROOVE

import frame_2
import frame_4
import frame_6
import frame_7


LARGE_FONT = ("Verdana", 10)

class Frame_3(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        btn1 = tk.Button(self, text='Electricity bill', fg="black", relief=GROOVE, width = 20, height = 2, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_4.Frame_4))
        btn1.pack(padx = 30, pady = 15)

        btn2 = tk.Button(self, text='Electricity budget', fg = "black", relief = GROOVE, width = 20, height = 2, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_7.Frame_7))
        btn2.pack(padx = 30, pady = 20)

        btn1 = tk.Button(self, text='Tricks & Tips', fg = "black", relief = GROOVE, width = 20, height = 2, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_6.Frame_6))
        btn1.pack(padx = 30, pady = 21)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_2.Frame_2))
        btn1.pack(padx = 30, pady = 25)



class Frame_3_water(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        btn1 = tk.Button(self, text='Water bill', fg="black", relief=GROOVE, width = 20, height = 2, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_4.Frame_4_water))
        btn1.pack(padx = 30, pady = 15)

        btn2 = tk.Button(self, text='Water budget', fg = "black", relief = GROOVE, width = 20, height = 2, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_7.Frame_7_water))
        btn2.pack(padx = 30, pady = 20)

        btn1 = tk.Button(self, text='Tricks & Tips', fg = "black", relief = GROOVE, width = 20, height = 2, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_6.Frame_6_water))
        btn1.pack(padx = 30, pady = 21)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_2.Frame_2))
        btn1.pack(padx = 30, pady = 25)