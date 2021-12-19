import tkinter as tk
from tkinter import GROOVE

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import frame_3

LARGE_FONT = ("Roboto Medium", 10)

class Frame_9(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData(self, b):
        df1 = pd.read_csv("C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/data.csv")
        #print(df1)

        today = pd.to_datetime('today').normalize()
        df2 = pd.DataFrame({'Date': [today.strftime('%Y-%m-%d')], 'amount': [str(b)]})

        #print(df2)
        df1 = df1.append(df2, ignore_index=True)
        df1["Date"] = pd.to_datetime(df1["Date"], format='%Y-%m-%d')
        df1.set_index('Date', inplace=True)
        df1["amount"] = df1["amount"].astype(float)

        #print(df1)
        #print(df1.info())

        btn = tk.Button(self, text='Back to Home', fg="black", relief=GROOVE, font = LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_3.Frame_3))
        btn.pack()

        px = 1/plt.rcParams['figure.dpi']
        figure = plt.Figure(figsize=(345*px, 370*px), dpi=100)
        ax = figure.add_subplot(111)
        for widget in self.winfo_children():
            widget.destroy()
        btn = tk.Button(self, text='Back to Home', fg="black", relief=GROOVE, font=LARGE_FONT,
                            command=lambda: self.parent.show_frame(frame_3.Frame_3))
        btn.pack()
        chart_type = FigureCanvasTkAgg(figure, self)
        chart_type.get_tk_widget().pack()
        df1.plot(kind = 'line', x_compat=True, title = "Electricity bills", ax=ax)


class Frame_9_water(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)

    def getData_2(self, b):
        df1 = pd.read_csv("C:/Users/Rat/PycharmProjects/pythonProject/project-waterlec/data_water.csv")
        #print(df1)

        today = pd.to_datetime('today').normalize()
        df2 = pd.DataFrame({'Date': [today.strftime('%Y-%m-%d')], 'amount': [str(b)]})

        #print(df2)
        df1 = df1.append(df2, ignore_index=True)
        df1["Date"] = pd.to_datetime(df1["Date"], format='%Y-%m-%d')
        df1.set_index('Date', inplace=True)
        df1["amount"] = df1["amount"].astype(float)

        #print(df1)
        #print(df1.info())

        btn = tk.Button(self, text='Back to Home', fg="black", relief=GROOVE, font = LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_3.Frame_3_water))
        btn.pack()

        px = 1 / plt.rcParams['figure.dpi']
        figure = plt.Figure(figsize=(345 * px, 370 * px), dpi=100)
        ax = figure.add_subplot(111)
        for widget in self.winfo_children():
            widget.destroy()
        btn = tk.Button(self, text='Back to Home', fg="black", relief=GROOVE, font=LARGE_FONT,
                        command=lambda: self.parent.show_frame(frame_3.Frame_3_water))
        btn.pack()
        chart_type = FigureCanvasTkAgg(figure, self)
        chart_type.get_tk_widget().pack()
        df1.plot(kind='line', x_compat=True, title="Water bills", ax=ax)




