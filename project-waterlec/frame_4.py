import tkinter as tk
from tkinter import GROOVE

import frame_5
import frame_3

LARGE_FONT = ("Roboto Medium", 12)

class Frame_4(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        this_month = tk.StringVar()
        last_month = tk.StringVar()
        rate = tk.StringVar()

        label = tk.Label(self, text="amount of unit(last month)", font=LARGE_FONT)
        label.pack(padx = 10, pady = 7)
        E = tk.Entry(self, bd=3, width=10, textvariable=last_month, font=LARGE_FONT)
        E.pack(padx = 10, pady = 8)

        label = tk.Label(self, text="amount of unit(this month)", font=LARGE_FONT)
        label.pack(padx = 10, pady = 9)
        E = tk.Entry(self, bd=3, width=10, textvariable=this_month, font=LARGE_FONT)
        E.pack(padx = 10, pady = 10)

        label = tk.Label(self, text="rate of your electricity(baht/unit)", font=LARGE_FONT)
        label.pack(padx = 10, pady = 11)
        E = tk.Entry(self, bd=3, width=10, textvariable=rate, font=LARGE_FONT)
        E.pack(padx = 10, pady = 12)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width=2, height=1, font=LARGE_FONT,
                        command=lambda: self.bills(this_month, last_month, rate))
        btn.pack(padx = 1, pady = 2)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=4, height=1, font=LARGE_FONT,
                         command=lambda: parent.show_frame(frame_3.Frame_3))
        btn1.pack(padx = 10, pady = 2)

    def bills(self, this_month, last_month, rate):
        try:
            t = float(this_month.get())
            l = float(last_month.get())
            r = float(rate.get())
            b = (t - l) * r
            for widget in self.parent.frame[frame_5.Frame_5].winfo_children():
                widget.destroy();
            if b <= 0:
                label = tk.Label(self, text="**You should enter the numbers correctly**", font=LARGE_FONT, fg="red")
                label.pack()
            else:
                self.parent.frame[frame_5.Frame_5].getData(b)
                self.parent.show_frame(frame_5.Frame_5)
        except ValueError:
            label = tk.Label(self, text="**You should put number in the box**", font=LARGE_FONT, fg="red")
            label.pack()



class Frame_4_water(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        last_month = tk.StringVar()
        this_month = tk.StringVar()
        rate = tk.StringVar()

        label = tk.Label(self, text="amount of unit(last month)", font=LARGE_FONT)
        label.pack(padx = 10, pady = 7)
        E = tk.Entry(self, bd=3, width=10, textvariable=last_month, font=LARGE_FONT)
        E.pack(padx = 10, pady = 8)

        label = tk.Label(self, text="amount of unit(this month)", font=LARGE_FONT)
        label.pack(padx = 10, pady = 9)
        E = tk.Entry(self, bd=3, width=10, textvariable=this_month, font=LARGE_FONT)
        E.pack(padx = 10, pady = 10)

        label = tk.Label(self, text="rate of your water(baht/unit)", font=LARGE_FONT)
        label.pack(padx = 10, pady = 11)
        E = tk.Entry(self, bd=3, width=10, textvariable=rate, font=LARGE_FONT)
        E.pack(padx = 10, pady = 12)

        btn = tk.Button(self, text='Ok', fg="black", relief=GROOVE, width=2, height=1, font=LARGE_FONT,
                        command=lambda: self.bills(this_month, last_month, rate))
        btn.pack(padx = 1, pady = 2)

        btn1 = tk.Button(self, text='Back', fg="black", relief=GROOVE, width=4, height=1, font=LARGE_FONT,
                         command=lambda: parent.show_frame(frame_3.Frame_3_water))
        btn1.pack(padx = 10, pady = 2)

    def bills(self, this_month, last_month, rate):
        try:
            t = float(this_month.get())
            l = float(last_month.get())
            r = float(rate.get())
            b = (t - l) * r
            for widget in self.parent.frame[frame_5.Frame_5_water].winfo_children():
                widget.destroy();
            if b <= 0:
                label = tk.Label(self, text="**You should enter the numbers correctly**", font=LARGE_FONT, fg="red")
                label.pack()
            else:
                self.parent.frame[frame_5.Frame_5_water].getData_2(b)
                self.parent.show_frame(frame_5.Frame_5_water)
        except ValueError:
            label = tk.Label(self, text="**You should put number in the box**", font=LARGE_FONT, fg="red")
            label.pack()
