import tkinter as tk
from tkinter import NW, N, W, CENTER, GROOVE

import frame_3
import frame_8

LARGE_FONT = ("Verdana", 24)

class Frame_7(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        budget = tk.StringVar()
        rate_2 = tk.StringVar()

        label = tk.Label(self, text="Your budget (baht)")
        label.pack(anchor=NW)
        E = tk.Entry(self, bd=3, width=10, textvariable=budget)
        E.pack(anchor=N)

        label = tk.Label(self, text="rate of your electricity (baht/units)")
        label.pack(anchor=W)
        E = tk.Entry(self, bd=3, width=10, textvariable=rate_2)
        E.pack(anchor=CENTER)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width = 2, height = 1,
                        command=lambda: self.budget(budget, rate_2))
        btn.pack()

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1,
                         command=lambda: parent.show_frame(frame_3.Frame_3))
        btn1.pack()

    def budget(self, budget, rate_2):
        try:
            bg = float(budget.get())
            r_2 = float(rate_2.get())
            bgt = round(bg / r_2, 2)
            budget.set(bgt)
            self.parent.frame[frame_8.Frame_8].getData(bgt)
            self.parent.show_frame(frame_8.Frame_8)
        except ValueError:
            label = tk.Label(self, text="**You should put number in the box**", font="times 10", fg = "red")
            label.pack()



class Frame_7_water(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        budget = tk.StringVar()
        rate_2 = tk.StringVar()

        label = tk.Label(self, text="Your budget (baht)")
        label.pack(anchor=NW)
        E = tk.Entry(self, bd=3, width=10, textvariable=budget)
        E.pack(anchor=N)

        label = tk.Label(self, text="rate of your water (baht/units)")
        label.pack(anchor=W)
        E = tk.Entry(self, bd=3, width=10, textvariable=rate_2)
        E.pack(anchor=CENTER)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width = 2, height = 1,
                        command=lambda: self.budget(budget, rate_2))
        btn.pack()

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1,
                         command=lambda: parent.show_frame(frame_3.Frame_3_water))
        btn1.pack()

    def budget(self, budget, rate_2):
        try:
            bg = float(budget.get())
            r_2 = float(rate_2.get())
            bgt = round(bg / r_2, 2)
            budget.set(bgt)
            self.parent.frame[frame_8.Frame_8_water].getData_2(bgt)
            self.parent.show_frame(frame_8.Frame_8_water)
        except ValueError:
            label = tk.Label(self, text="**You should put number in the box**", font="times 10", fg = "red")
            label.pack()

