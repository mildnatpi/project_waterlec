import tkinter as tk
from tkinter import GROOVE, LEFT

import frame_6
import frame_9
import pandas as pd

LARGE_FONT = ("Roboto Medium", 10)


class Frame_5(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData(self, b):
        df1 = pd.read_csv("C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/data.csv");
        today = pd.to_datetime('today').normalize()
        df2 = pd.DataFrame({'Date': [today.strftime('%Y-%m-%d')],
                            'amount': [str(b)]})
        if str(df1['Date'].iloc[-1]) == str(pd.to_datetime(today).date()):
            df1.drop(df1.tail(1).index,inplace=True)
        df1 = df1.append(df2, ignore_index=True)

        df1["Date"] = pd.to_datetime(df1["Date"], format='%Y-%m-%d')
        df1.set_index('Date', inplace=True)
        df1["amount"] = df1["amount"].astype(float).astype(int);

        df1.to_csv('C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/data.csv')
        label = tk.Label(self, text="Your electricity bill", justify=LEFT, font=('Roboto Medium', 15))
        label.pack(padx = 10, pady = 8)
        text = tk.Label(self, text=b, justify=LEFT, bd=5, width=10, font=('Roboto Medium', 15))
        text.pack(padx = 10, pady = 10)

        label = tk.Label(self, text="See the graph to compare", font=LARGE_FONT)
        label.pack(padx = 10, pady = 5)
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width=2, height=1, font=LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_9.Frame_9))
        btn.pack(padx = 10, pady = 5)

        self.parent.frame[frame_9.Frame_9].getData(b)
        self.parent.show_frame(frame_9.Frame_9)

        label = tk.Label(self, text="See the tricks & trips", font=LARGE_FONT)
        label.pack(padx = 10, pady = 10)
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width=2, height=1, font=LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_6.Frame_6))
        btn.pack(padx = 10, pady = 10)


class Frame_5_water(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData_2(self, b):
        df1 = pd.read_csv("C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/data_water.csv");
        today = pd.to_datetime('today').normalize()
        df2 = pd.DataFrame({'Date': [today.strftime('%Y-%m-%d')],
                            'amount': [str(b)]})
        if str(df1['Date'].iloc[-1]) == str(pd.to_datetime(today).date()):
            df1.drop(df1.tail(1).index,inplace=True)
        df1 = df1.append(df2, ignore_index=True)
        df1["Date"] = pd.to_datetime(df1["Date"], format='%Y-%m-%d')
        df1.set_index('Date', inplace=True)
        df1["amount"] = df1["amount"].astype(float).astype(int);

        df1.to_csv('C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/data_water.csv')

        label = tk.Label(self, text="Your water bill", justify=LEFT, font=('Roboto Medium', 15))
        label.pack(padx = 10, pady = 8)
        E = tk.Label(self, text=b, justify=LEFT, bd=3, width=10, font=('Roboto Medium', 15))
        E.pack(padx = 10, pady = 10)

        label = tk.Label(self, text="See the graph to compare", font=LARGE_FONT)
        label.pack(padx = 10, pady = 5)
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width=2, height=1, font=LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_9.Frame_9_water))
        btn.pack(padx = 10, pady = 5)

        self.parent.frame[frame_9.Frame_9_water].getData_2(b)
        self.parent.show_frame(frame_9.Frame_9_water)

        label = tk.Label(self, text="See the tricks & trips")
        label.pack(padx = 10, pady = 10)
        btn = tk.Button(self, text='Go', fg="black", relief=GROOVE, width=2, height=1, font=LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_6.Frame_6_water))
        btn.pack(padx = 10, pady = 10)
