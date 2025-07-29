# Date 13-12-2018
# Author : Sietze Min

from tkinter import *
import math
import random
import sys
print(sys.version)


class App:
    bg_color = "red"
    seed_points = []

    def __init__(self,root, width=750, height=550):
        screen_width = width
        screen_height = height

        fullscreen_width = root.winfo_screenwidth()
        fullscreen_screen_height = root.winfo_screenheight()

        c = Canvas(root, width=fullscreen_width,height=fullscreen_screen_height,bg="black")
        c.pack() 
        # root.resizable(False,False)
        root.title("Chaos Game Creation by Sietze Min")
        # self.center_on_screen(root)
        # self.draw(c,screen_width,screen_height)
        # self.drawRectangle(c, screen_width,screen_height,(100,100),100)
        self.drawRandomPoints(c,screen_width, screen_height,4)
        # self.drawSierpinskiTriangle(c,screen_width,screen_height)
        # self.drawSierpinskiTriangleStraight(c,fullscreen_width, fullscreen_screen_height)


    def draw(self,c, width, height):
        init_x = 5.0
        init_y = 5.0

        end_x = 8
        end_y = 8

        while end_x < width:
            point = c.create_oval(init_x, init_y,end_x, end_y,fill="white")
            init_x = init_x + 5
            end_x = end_x + 5       
            root.update()
    
    def drawSierpinskiTriangle(self,c,width,height):
        # (1) create three seed points
        self.drawRandomPoints(c,width,height,4)
        # (2) random number between [0,2], this corresponds with the inital_point variable to choose a first move (direction to go to halfway)
        
        for i in range(5000):
            r = random.randint(0,2)
            if(r == 0):
                # move halfway to point A (seed_point[0])
                # print(self.seed_points[0])
                new_x = self.seed_points[0][0]
                print(new_x)
                new_x = abs(int(self.seed_points[-1][0]) - int(self.seed_points[0][0]))
                new_y = abs(int(self.seed_points[-1][1]) - int(self.seed_points[0][1]))
        
                new_x = new_x / 2
                new_y = new_y / 2
            
                x2 = min(self.seed_points[-1][0],self.seed_points[0][0])
                y2 = min(self.seed_points[-1][1], self.seed_points[0][1])
                print('x2', x2)
                print('y2', y2)

                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                print('final values')            
                print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                self.seed_points[-1][0] = new_x
                self.seed_points[-1][1] = new_y
                root.update()
    
            elif(r == 1):
                # move halfway to point B (seed_point[1])
                new_x = self.seed_points[0][0]
                print(new_x)
                new_x = abs(int(self.seed_points[-1][0]) - int(self.seed_points[1][0]))
                new_y = abs(int(self.seed_points[-1][1]) - int(self.seed_points[1][1]))
        
                new_x = new_x / 2
                new_y = new_y / 2
            
                x2 = min(self.seed_points[-1][0],self.seed_points[1][0])
                y2 = min(self.seed_points[-1][1], self.seed_points[1][1])
                print('x2', x2)
                print('y2', y2)

                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                print('final values')            
                print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                self.seed_points[-1][0] = new_x
                self.seed_points[-1][1] = new_y
                root.update()

            elif(r == 2):
                new_x = self.seed_points[0][0]
                print(new_x)
                new_x = abs(int(self.seed_points[-1][0]) - int(self.seed_points[2][0]))
                new_y = abs(int(self.seed_points[-1][1]) - int(self.seed_points[2][1]))
        
                new_x = new_x / 2
                new_y = new_y / 2
            
                x2 = min(self.seed_points[-1][0],self.seed_points[2][0])
                y2 = min(self.seed_points[-1][1], self.seed_points[2][1])
                print('x2', x2)
                print('y2', y2)

                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                print('final values')            
                print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                self.seed_points[-1][0] = new_x
                self.seed_points[-1][1] = new_y
                root.update()
                #move halfway to point C (seec_point[2])
        
        root.update()

    def drawSierpinskiTriangleStraight(self,c,width,height):
        seed_points = []
        ax = width / 2
        ay = 0
        
        bx = 0
        by = height
        
        cx = width
        cy = height

        init_point = [random.randint(0,width),random.randint(0,height)]
        # draw initial seed points
        # point_1 = c.create_oval(ax - 3,ay,ax + 3,ay + 6,fill="red")
        # point_2 = c.create_oval(bx,by,bx+6,by-6,fill="red")
        # point_3 = c.create_oval(cx,cy,cx-6,cy-6,fill="red")
        # init_p = c.create_oval(init_point[0],init_point[1],init_point[0] +3, init_point[1] + 3,fill='red')

        seed_points.append([ax,ay,bx,by,cx,cy,init_point[0],init_point[1]])

        for i in range(1000):
            r = random.randint(0,2)
            if(r == 0):
                # move halfway to point A (seed_point[0])
                new_x = abs(seed_points[0][0] - seed_points[0][-2])
                new_y = abs(seed_points[0][1] - seed_points[0][-1])

                new_x = new_x / 2
                new_y = new_y / 2
            
                x2 = min(seed_points[0][0], seed_points[0][-2])
                y2 = min(seed_points[0][1], seed_points[0][-1])

                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                print('final values')            
                print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                seed_points[0][-2] = new_x
                seed_points[0][-1] = new_y
                root.update()

            elif(r == 1):
                # move halfway to point A (seed_point[1])
                new_x = abs(seed_points[0][2] - seed_points[0][-2])
                new_y = abs(seed_points[0][3] - seed_points[0][-1])

                new_x = new_x / 2
                new_y = new_y / 2
            
                x2 = min(seed_points[0][2], seed_points[0][-2])
                y2 = min(seed_points[0][3], seed_points[0][-1])

                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                print('final values')            
                print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                seed_points[0][-2] = new_x
                seed_points[0][-1] = new_y
                root.update()

            elif(r == 2):
                  # move halfway to point A (seed_point[1])
                new_x = abs(seed_points[0][4] - seed_points[0][-2])
                new_y = abs(seed_points[0][5] - seed_points[0][-1])

                new_x = new_x / 2
                new_y = new_y / 2
            
                x2 = min(seed_points[0][4], seed_points[0][-2])
                y2 = min(seed_points[0][5], seed_points[0][-1])

                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                print('final values')            
                print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                seed_points[0][-2] = new_x
                seed_points[0][-1] = new_y
                root.update()

        root.update()

    def drawRandomPoints(self,c,width,height,amount):
        glob_xy = [random.randint(0,(width-3)),random.randint(0,(height-3))]
        # print("globxy : ",glob_xy)

        for i in range(amount):
            random_x  = random.randint(0,(width - 3))
            random_y = random.randint(0,(height - 3))
            x1 = random_x
            y1 = random_y
            x2 = random_x + 3
            y2 = random_y + 3
            self.seed_points.append([x1,y1,x2,y2])
            root.update()
      
        # init_point = c.create_oval(glob_xy[0],glob_xy[1],glob_xy[0] + 3,glob_xy[1]+3,fill="red")
        self.seed_points.append(glob_xy)
        root.update()

    def drawRectangle(self, c, width,height,origin_pos,dimensions):
        """
        c = canvas object
        widht = screen width in px
        height = screen height in px
        origin_pos = tuple of original x,y start coordinates of the square
        dimensions = the length (and widht) of the square
        """
        origin_x = origin_pos[0]
        origin_y = origin_pos[1]

        # print(origin_x,origin_y)
        init_x = origin_x
        init_y = origin_y

        end_x = origin_x + 3
        end_y = origin_y + 3

        lengt_of_square = int(origin_pos[0]) + dimensions
        
        # upper line
        while end_x < lengt_of_square:
            point = c.create_oval(init_x, init_y,end_x, end_y,fill="white")
            init_x = init_x + 5
            end_x = end_x + 5      

        while end_y < lengt_of_square:
            point = c.create_oval(init_x, init_y,end_x, end_y,fill="white")
            init_y = init_y + 5
            end_y = end_y + 5     

        while end_x > origin_pos[0]:
            point = c.create_oval(init_x, init_y,end_x, end_y,fill="white")
            init_x = init_x - 5
            end_x = end_x - 5  

        while end_y > origin_pos[1]:
            point = c.create_oval(init_x, init_y,end_x, end_y,fill="white")
            init_y = init_y - 5
            end_y = end_y - 5   

            root.update()

    def center_on_screen(self,root):
            w = 750
            h = 550
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()

            x = (screen_width - w)/2
            y = (screen_height - h)/2

            root.geometry('%dx%d+%d+%d' % (w, h, x, y))
 

root = Tk()
app = App(root)
root.mainloop()
