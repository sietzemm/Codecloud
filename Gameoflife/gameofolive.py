# Date 10-09-2019, last modified 22-10-2019
# Author : Sietze Min
import sys
import math
import random
import threading
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
        res = 60 # resolution
        # cols = 0 
        # rows = 0
        rows = round(self.fullscreen_screen_height / res)
        columns = round(self.fullscreen_width / res)
        
        # draw grid
        # grid = [rows,[columns]] # create a grid consisting of the rows and columns defined above. 
        grid = [[random.randint(0,1) for x in range(rows)] for y in range(columns)] 
        for i in range(len(grid)):
             for j in range(len(grid[i])):
                 if grid[i][j] == 1:
                     cell = c.create_rectangle(i*res,j*res,(i*res)+res,(j*res)+res,fill="white")               
       

     
        # This loop goes as long as the duration is set <========================================================================================================================================
        # def thread_function(grid):
        while(TRUE):
            # counter = sys.t
        
                
            # print('current state')
            # for i in range(len(grid)):
            #     print(grid[i])

            # Placeholder for the next state, just an empty same size grid
            next = [[0 for x in range(rows)] for y in range(columns)]  

            def countNeighborsSimple(self, grid, x,y):
                sum = 0
                i = -1
                j = -1
                for i in range(2):
                    for j in range(2):
                        col = (x+ i + columns) % columns
                        row =(y+ j + rows) % rows
                        sum += grid[col][row]
                sum -= grid[x][y]
                return sum
            
            def countNeighbors(self, grid, x,y):
                sum = 0

                # Top left corner
                if x == 0 and y == 0 :
                    # print('top left corner, value : ', grid[x][y], 'local coordinates : ',x, y)

                    if grid[x][y + 1] == 1: # middle right
                        sum += 1
                    if grid[x+1][y + 1] == 1: # lower right
                        sum += 1
                    if grid[x + 1][y] == 1: # lower middle
                        sum += 1

                #Between top left and right corner
                if x == 0 and 0 < y < len(grid[x]) -1:
                    # print('between top left and right corner, value : ', grid[x][y], 'local coordinates : ', x,y)

                    if grid[x][y-1] == 1: # middle left
                        sum += 1
                    if grid[x+1][y-1] == 1: # lower left
                        sum += 1
                    if grid[x+1][y] == 1: #lower middle
                        sum += 1
                    if grid[x][y+1] == 1: # middle right
                        sum += 1
                    if grid[x+1][y+1] == 1: #lower right
                        sum += 1

                # Top right corner
                if x == 0 and y == len(grid[x]) -1:
                    # print('top right corner, value : ', grid[x][y], 'local coordinates : ',x, y)
                
                    if grid[x][y-1] == 1: # middle left
                        sum +=1
                    if grid[x+1][y-1] ==1: # lower left
                        sum += 1
                    if grid[x+1][y] == 1: # lower middle
                        sum += 1

                # Bottom left corner
                if x == (len(grid) -1) and y == 0:
                    # print('bottom left corner, value : ', grid[x][y]) 

                    if grid[x -1][y] == 1: #upper middle
                        sum += 1
                    if grid[x -1][y + 1] == 1: #upper right
                        sum += 1
                    if grid[x][y+1] == 1: #middle right
                        sum += 1

                # Between bottom left and right corner
                if x == (len(grid) -1) and 0 < y < (len(grid[x]) -1):
                    # print('between bottom left and right corner, value : ', grid[x][y], 'local coordinates : ', x, y)

                    if grid[x-1][y-1] == 1: # upper left
                        sum += 1
                    if grid[x -1][y] == 1: #upper middle
                        sum += 1
                    if grid[x -1][y + 1] == 1: #upper right
                        sum += 1
                    if grid[x][y-1] == 1: #middle left
                        sum += 1
                    if grid[x][y+1] == 1: #middle right
                        sum += 1
                    
                # Bottom right corner
                if x == (len(grid) -1) and y == (len(grid[x]) -1):
                    # print('bottom right corner, value: ', grid[x][y], 'local coordinates : ', x, y)
                    if grid[x-1][y-1] == 1: # upper left
                        sum += 1
                    if grid[x -1][y] == 1: #upper middle
                        sum += 1
                    if grid[x][y-1] == 1: #middle left
                        sum += 1
                    
                # far left column between top and bottom
                if 0 < x < len(grid)-1 and y == 0:
                    # print('far left column, value : ', grid[x][y], 'local coordinates : ', x, y)
                
                    if grid[x -1][y] == 1: #upper middle
                        sum += 1
                    if grid[x -1][y + 1] == 1: #upper right
                        sum += 1
                    if grid[x][y+1] == 1: #middle right
                        sum += 1
                    if grid[x+1][y + 1] == 1: # lower right
                        sum += 1
                    if grid[x+1][y] == 1: # lower middle
                        sum += 1

                # far right column between top and bottom
                if 0 < x < len(grid) -1 and y == len(grid[x]) -1:
                    # print('far right column, value : ', grid[x][y], 'local coordindates : ', x,y)
                    if grid[x -1][y] == 1: #upper middle
                        sum += 1
                    if grid[x-1][y-1] == 1: # upper left
                        sum += 1
                    if grid[x][y-1] == 1: #middle left
                        sum += 1
                    if grid[x+1][y-1] ==1: # lower left
                        sum += 1
                    if grid[x+1][y] == 1: # lower middle
                        sum += 1

                # alle else coordinates
                if 0 < x < len(grid)-1 and 0 < y < len(grid[x])-1:
                    # print('normal value : ', x,y, '###')
                    if grid[x-1][y-1] == 1: # upper left
                        sum += 1
                    if grid[x -1][y] == 1: #upper middle
                        sum += 1
                    if grid[x -1][y + 1] == 1: #upper right
                        sum += 1
                    if grid[x][y+1] == 1: #middle right
                        sum += 1
                    if grid[x+1][y + 1] == 1: # lower right
                        sum += 1
                    if grid[x+1][y] == 1: # lower middle
                        sum += 1
                    if grid[x+1][y-1] ==1: # lower left
                        sum += 1
                    if grid[x][y-1] == 1: #middle left
                        sum += 1

                        # sum = sum - grid[x][y]
                return sum 
            
            # (1) Compute new state =================================================================================================================
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    state = grid[i][j]
                    
                    sum = 0
                    neighbors = countNeighbors(self,grid, i,j)
                    
                    # print('neighbors', neighbors)
                    # Ruleset
                    if state == 0 and neighbors == 3:
                        next[i][j] = 1
                    elif state == 1 and neighbors < 2 or neighbors > 3:
                        next[i][j] = 0
                    else:
                        next[i][j] = state

            # print('next state before overwritting')
            # for i in range(len(next)):
            #     print(next[i])
            
            # print('current state')
            # for i in range(len(grid)):
            #     print(grid[i])

            # Overwrite the current generation with the computed values, so it becomes the next generation
            grid = next
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        cell = c.create_rectangle(i*res,j*res,(i*res)+res,(j*res)+res,fill="white")   
                    if grid[i][j] == 0:
                        cell = c.create_rectangle(i*res,j*res,(i*res)+res,(j*res)+res,fill="black")  
            root.update()
        
        # x = threading.Thread(target=thread_function, args=(grid,), daemon=TRUE)
        # x.start()
            # print('next state')
            # for i in range(len(grid)):
            #     print(grid[i])

            # (3) Update the screen
        # root.update()

root = Tk()
app = App(root)
root.mainloop()