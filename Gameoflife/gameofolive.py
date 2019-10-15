# Date 10-09-2019
# Author : Sietze Min
import sys
from tkinter import *


print(sys.version)

class App:
    def __init__(self,root, width=500, height=500):
        root.title = "Game of life"
        self.fullscreen_width = root.winfo_screenwidth()
        self.fullscreen_screen_height = root.winfo_screenheight()

        self.screenWidth = width
        self.screenHeight = height

        c = Canvas(root, width=self.fullscreen_width, height=self.fullscreen_screen_height, bg='black')
        c.pack(side=BOTTOM)

        self.drawSquare(c,5)

    def drawSquare(self, c, amount):
        x1 = 10
        y1 = 10
        for i in range(amount):
            point = c.create_rectangle(x1,y1,x1+10,y1+10,fill="white")
            x1 = x1 + 12
            print(x1)
            root.update()

root = Tk()
app = App(root)
root.mainloop()