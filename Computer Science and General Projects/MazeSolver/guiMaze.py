# Date : 16-07-2019
from tkinter import *
import sys

print(sys.version)

class App:
    maze = [[1,0,1],[1,0,1],[1,0,1]]

    def __init__(self, root, width=750, height=550):
        root.title("Maze solver by Sietze Min")
        fullscreen_width = root.winfo_screenwidth()
        fullscreen_screen_height = root.winfo_screenheight()
        c = Canvas(root, width=fullscreen_width,height=fullscreen_screen_height,bg="black")
        c.pack(side=TOP)

        # Draw a 3*3 maze.
        self.drawMaze(c,3)

    def drawMaze(self, c,size):
        row_x = 50
        row_y = 50
        row_x2 = 70
        row_y2 = 70

        for row in range(size): # Draw [size] rows of [size] columns
            for column in range(size):
                dot = c.create_oval(row_x,row_y,row_x2,row_y2,fill="white")
                row_x = row_x + 50
                row_x2 = row_x2 + 50
            row_x = 50
            row_x2 = 70
            row_y = row_y + 50
            row_y2 = row_y2 + 50


        root.update()



root = Tk()
app = App(root)
root.mainloop()
