# Date 13-12-2018
# Author : Sietze Min

from tkinter import *
import math
import random
import sys
print(sys.version)

class App:
    seed_points = []
    global_counter = 0    
    
    def __init__(self,root, width=750, height=550):
        root.title("Chaos Game Creation by Sietze Min")
        # screen_width = width
        # screen_height = height
        fullscreen_width = root.winfo_screenwidth()
        fullscreen_screen_height = root.winfo_screenheight()
        
        self.display_counter = Entry(root)
        self.display_counter.pack(side=TOP)
        
        # label1 = Label(text="Seed point counter :")
        # label1.pack(side=TOP)

        c = Canvas(root, width=fullscreen_width,height=fullscreen_screen_height,bg="black")
        c.pack(side=BOTTOM) 
        # root.resizable(False,False)
        # self.centerOnScreen(root)
        # self.drawSierpinskiTriangle(c,screen_width,screen_height,5000)
        self.drawSierpinskiTriangleStraight(c,fullscreen_width, fullscreen_screen_height,5000)
        # self.drawRandomPoints(c,fullscreen_width,fullscreen_screen_height,100)

    def drawSierpinskiTriangle(self,c,width,height, resolution):
        """
        c = canvas object
        width = screen width
        height = screen height
        resolution = how many 'points' (vertices) the triangle consists of
        higher number give more detailed results
        """
        # (1) create three seed points
        self.drawRandomPoints(c,width,height,4)
        # (2) random number between [0,2], this corresponds with the inital_point variable to choose a first move (direction to go to halfway)
        
        for i in range(resolution):
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
                # print('x2', x2)
                # print('y2', y2)
                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)
                # print('final values')            
                # print(new_x,new_y)
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
                # print('x2', x2)
                # print('y2', y2)
                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)

                # print('final values')            
                # print(new_x,new_y)
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
                # print('x2', x2)
                # print('y2', y2)
                new_x = (x2 + new_x) 
                new_y = (y2 + new_y)
                # print('final values')            
                # print(new_x,new_y)
                point = c.create_oval(new_x,new_y,new_x+3,new_y+3,fill="yellow")

                # updates the values for iteration
                self.seed_points[-1][0] = new_x
                self.seed_points[-1][1] = new_y
                root.update()
                #move halfway to point C (seec_point[2])
        
        root.update()

    def drawSierpinskiTriangleStraight(self,c,width,height,resolution):
        """
        c = canvas object
        width = screen width
        height = screen height
        resolution = how many 'points' (vertices) the triangle consists of
        higher number give more detailed results
        """
        seed_points = []
        ax = width / 2
        ay = 0
        
        bx = 0
        by = height
        
        cx = width
        cy = height

        init_point = [random.randint(0,width),random.randint(0,height)]
        # draw initial seed points
        # point_1 = c.create_oval(ax - 3,ay,ax + 3,ay + 6,fill="blue")
        # point_2 = c.create_oval(bx,by,bx+6,by-6,fill="blue")
        # point_3 = c.create_oval(cx,cy,cx-6,cy-6,fill="blue")
        # init_p = c.create_oval(init_point[0],init_point[1],init_point[0] +3, init_point[1] + 3,fill='red')

        seed_points.append([ax,ay,bx,by,cx,cy,init_point[0],init_point[1]])

        for i in range(resolution):
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
                # print('final values')            
                # print(new_x,new_y)
                point = c.create_oval(new_x,new_y,new_x+1,new_y+1,fill="red")

                # updates the values for iteration
                seed_points[0][-2] = new_x
                seed_points[0][-1] = new_y

                self.global_counter = self.global_counter + 1
                self.display_counter.delete(0,END)
                self.display_counter.insert(0,self.global_counter)
                # print(self.global_counter)
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
                # print('final values')            
                # print(new_x,new_y)
                point = c.create_oval(new_x,new_y,new_x+1,new_y+1,fill="blue")

                # updates the values for iteration
                seed_points[0][-2] = new_x
                seed_points[0][-1] = new_y

                self.global_counter = self.global_counter + 1
                self.display_counter.delete(0,END)
                self.display_counter.insert(0,self.global_counter)
                # print(self.global_counter)
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
       
                # print(new_x,new_y)

                point = c.create_oval(new_x,new_y,new_x+1,new_y+1,fill="yellow")

                # updates the values for iteration
                seed_points[0][-2] = new_x
                seed_points[0][-1] = new_y

                self.global_counter = self.global_counter + 1
                self.display_counter.delete(0,END)
                self.display_counter.insert(0,self.global_counter)

                # print(self.global_counter)
                root.update()

        print(self.global_counter)
        root.update()

    def drawRandomPoints(self,c,width,height,amount):
        """
        c = canvas object
        width = screen width
        height = screen height
        amount = how many random points need to be drawn. 3 is needed for Sierpinski's triangle
        """
        glob_xy = [random.randint(0,(width-3)),random.randint(0,(height-3))]
        # print("globxy : ",glob_xy)

        for i in range(amount):
            random_x  = random.randint(0,(width - 3))
            random_y = random.randint(0,(height - 3))
            x1,y2 = random_x,random_y

            x2 = random_x + 3
            y2 = random_y + 3
            point = c.create_oval(x1,y1,x2,y2,fill="white")
            self.seed_points.append([x1,y1,x2,y2])
            root.update()
      
        init_point = c.create_oval(glob_xy[0],glob_xy[1],glob_xy[0] + 3,glob_xy[1]+3,fill="red")
        self.seed_points.append(glob_xy)
        root.update()

    def centerOnScreen(self,root):
            w,h = 750,550
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()

            x = (screen_width - w)/2
            y = (screen_height - h)/2
            root.geometry('%dx%d+%d+%d' % (w, h, x, y))
 
    
root = Tk()
app = App(root)
root.mainloop()
