# Date 10-09-2019
# Author : Sietze Min
import sys
import math
import random
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
        self.drawGrid(c)
        # self.fillMiddleCell(c)
        # self.cellularAutomata(c)


    def drawGrid(self, c):
        res = 10 # resultion
        x1 = 0
        y1 = 0
        rows = round(self.fullscreen_screen_height / res)
        columns = round(self.fullscreen_width / res)

        # draw grid
        # grid = [rows,[columns]] # create a grid consisting of the rows and columns defined above. 
        grid = [[random.randint(0,1) for x in range(rows)] for y in range(columns)] 
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                point = c.create_rectangle(x1,0,x1+2,self.fullscreen_screen_height, fill="grey")
                x1 = x1 + res
                
                point = c.create_rectangle(0,y1,self.fullscreen_width,y1+2,fill="grey")
                y1 = y1 + res
                
                if grid[i][j] == 1:
                    cell = c.create_rectangle(i*res,j*res,(i*res)+res,(j*res)+res,fill="white")
                    # root.update()

        root.update()

    def cellularAutomata(self, c):
        generation = []
        neighbours = []
        print(type(generation))
root = Tk()
app = App(root)
root.mainloop()