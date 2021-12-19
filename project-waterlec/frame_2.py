import tkinter as tk
import frame_3

LARGE_FONT = ("Roboto Medium", 16)

class Frame_2(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        btn1 = tk.Button(self, text='ELECTRICITY', fg = "black", width = 20, height = 2, font = LARGE_FONT, command=lambda: parent.show_frame(
            frame_3.Frame_3))
        btn1.pack(padx = 30, pady = 40)

        btn2 = tk.Button(self, text='WATER', fg = "black", width = 20, height = 2, font = LARGE_FONT, command=lambda: parent.show_frame(
            frame_3.Frame_3_water))
        btn2.pack(padx = 30, pady = 60)



