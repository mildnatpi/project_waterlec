import tkinter as tk
from frame_1 import Frame_1
from frame_2 import Frame_2
from frame_3 import Frame_3, Frame_3_water
from frame_4 import Frame_4, Frame_4_water
from frame_5 import Frame_5, Frame_5_water
from frame_6 import Frame_6, Frame_6_water
from frame_7 import Frame_7, Frame_7_water
from frame_8 import Frame_8, Frame_8_water
from frame_9 import Frame_9, Frame_9_water

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.frame = {}
        self.geometry("345x375")
        self.minsize(345, 375)
        self.maxsize(345, 375)
        self.title("WATERLEC")
        for F in (Frame_1, Frame_2, Frame_3, Frame_4, Frame_5, Frame_6, Frame_7, Frame_8, Frame_9, Frame_3_water,
                 Frame_4_water, Frame_5_water, Frame_6_water, Frame_7_water, Frame_8_water, Frame_9_water):
            frame = F(self)
            self.frame[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
            frame.configure(background='#d83731')


        self.show_frame(Frame_1)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()

window = Window();
window.mainloop()