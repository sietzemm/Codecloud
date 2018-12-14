# Date : 11-12-2018
# Author : Sietze Min
from tkinter import *
import sys

print(sys.version)

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        root.title("area calculation")
        
        self.lbl = Label(frame, text="Calculate the area of a plane")
        self.lbl.grid(row=0,column=0)

        self.length_label = Label(frame, text="Length")
        self.length_label.grid(row=1,column=0)
        
        self.length_value = StringVar()
        self.length_value = Entry(frame, textvariable=self.length_value)
        self.length_value.grid(row=1,column=1)
        
        self.width_label = Label(frame, text="Width")
        self.width_label.grid(row=2,column=0)

        self.width_value = StringVar()
        self.width_value = Entry(frame, textvariable=self.width_value)
        self.width_value.grid(row=2,column=1)

        self.btn = Button(frame,text="Calculate area",fg="red",command=self.calculateArea)
        self.btn.grid(row=3,column=0)

        self.result_text = Text(frame,height=1, width=20)
        self.result_text.grid(row=3,column=1)

        # frame = Frame(master)

    def calculateArea(self):
        print("Hi There!")
        result = int(self.length_value.get()) * int(self.width_value.get())
        self.result_text.insert(END,result)

root = Tk() # init
app = App(root) #  instance creation of the class (object) App
root.mainloop()
