import tkinter as tk
from tkinter import GROOVE

import frame_3
import frame_8

LARGE_FONT = ("Roboto Medium", 12)

class Frame_7(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        budget = tk.StringVar()
        rate_2 = tk.StringVar()

        label = tk.Label(self, text="Your budget (baht)", font = LARGE_FONT)
        label.pack(padx = 10, pady = 7)
        E = tk.Entry(self, bd=3, width=10, textvariable=budget, font = LARGE_FONT)
        E.pack(padx = 10, pady = 9)

        label = tk.Label(self, text="rate of your electricity (baht/units)", font = LARGE_FONT)
        label.pack(padx = 10, pady = 11)
        E = tk.Entry(self, bd=3, width=10, textvariable=rate_2, font = LARGE_FONT)
        E.pack(padx = 10, pady = 13)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width = 2, height = 1, font = LARGE_FONT,
                        command=lambda: self.budget(budget, rate_2))
        btn.pack(padx = 10, pady = 2)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=4, height=1, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_3.Frame_3))
        btn1.pack(padx = 10, pady = 2)

    def budget(self, budget, rate_2):
        try:
            bg = float(budget.get())
            r_2 = float(rate_2.get())
            bgt = round(bg / r_2, 2)
            for widget in self.parent.frame[frame_8.Frame_8].winfo_children():
                widget.destroy();
            self.parent.frame[frame_8.Frame_8].getData(bgt)
            self.parent.show_frame(frame_8.Frame_8)
        except ValueError:
            label = tk.Label(self, text="**You should put number in the box**", font = LARGE_FONT, fg = "red")
            label.pack()



class Frame_7_water(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        budget_2 = tk.StringVar()
        rate_2_2 = tk.StringVar()

        label = tk.Label(self, text="Your budget (baht)", font = LARGE_FONT)
        label.pack(padx = 10, pady = 7)
        E = tk.Entry(self, bd=3, width=10, textvariable=budget_2, font = LARGE_FONT)
        E.pack(padx = 10, pady = 9)

        label = tk.Label(self, text="rate of your water (baht/units)", font = LARGE_FONT)
        label.pack(padx = 10, pady = 11)
        E = tk.Entry(self, bd=3, width=10, textvariable=rate_2_2, font = LARGE_FONT)
        E.pack(padx = 10, pady = 13)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width = 2, height = 1, font = LARGE_FONT,
                        command=lambda: self.budget(budget_2, rate_2_2))
        btn.pack(padx = 10, pady = 2)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=3, height=1, font = LARGE_FONT,
                         command=lambda: parent.show_frame(frame_3.Frame_3_water))
        btn1.pack(padx = 10, pady = 2)

    def budget(self, budget_2, rate_2_2):
        try:
            bg = float(budget_2.get())
            r_2 = float(rate_2_2.get())
            bgt = round(bg / r_2, 2)
            for widget in self.parent.frame[frame_8.Frame_8_water].winfo_children():
                widget.destroy();
            self.parent.frame[frame_8.Frame_8_water].getData_2(bgt)
            self.parent.show_frame(frame_8.Frame_8_water)
        except ValueError:
            label = tk.Label(self, text="**You should put number in the box**", font = LARGE_FONT, fg = "red")
            label.pack()

