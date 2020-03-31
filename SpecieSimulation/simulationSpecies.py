import sys
import random
import math
from tkinter import *

class Organism:
    def __init__(self,x,y):
        id = '0'
        self.x = x
        self.y = y

    def checkSurrounding(self,population):
        pass

    def reproduce():
        pass

    def die():
        pass

class App:
    def __init__(self, root):
        e = []
        root.title = "Species simulation"
        self.fullscreen_width = root.winfo_screenwidth()
        self.fullscreen_screen_height = root.winfo_screenheight()
        c = Canvas(root, width=self.fullscreen_width, height=self.fullscreen_screen_height, bg='black')
        c.pack(side=BOTTOM)
        species1 = self.SpawnSpecies(100,c,"green",e)
        species2 = self.SpawnSpecies(50,c,"red",species1)
        # self.SpawnSpecies(100,c,"yellow")
        # self.SpawnSpecies(100,c,"blue")

    
    def SpawnSpecies(self,amount,c,color,pop):
        population = []
        #Define a random spawn point in the designated area
        x = random.randint(0,(self.fullscreen_width - 40))
        y = random.randint(0,(self.fullscreen_screen_height - 50))
        spawnPoint = [x,y]
        x2 = x + 10
        y2 = y + 10

        print('SpawnPoint : ', spawnPoint)
        spawnP = c.create_oval(x,y,x2,y2,fill='white')
        # radius = random.randint(25,125) # 100 pixels to the left or right from spawnPoint, same goes for up and down
        radius = random.randint(45,125)

        # punt is (0,0), radius is 20
        # Een punt kan in alleen in het cirkelvormige gebiedt om het middelpunt liggen als zijn x coordinaat tussen het middelpunt (0,0) en de radius ligt. 
        # middelpunt = 0, radius = 10. Range is dus 0 < range < 10 (oftewel 10)
        # De y-waarde van het punt is ook de radius. dus de y-waarde moet ook als volgt : middelpunt < y-waarde < radius

        for i in range(amount):
            lower_boundX = spawnPoint[0]-radius
            upper_boundX = spawnPoint[0]+radius

            lower_boundY = spawnPoint[1]-radius
            upper_boundY = spawnPoint[1]+radius
            x1 = random.randint(min(upper_boundX,lower_boundX),max(upper_boundX,lower_boundX))
            y1 = random.randint(min(upper_boundY,lower_boundY),max(upper_boundY,lower_boundY))

            x2 = x1 + 10
            y2 = y1 + 10

            # print('x1', x1)
            # print('y1',y1)
            if spawnPoint[0]-radius < x1 < spawnPoint[0] + radius and spawnPoint[1] - radius < y1 < spawnPoint[1] + radius:
                # print('x value of point is within limits : ',x1)
                # print('y value of point is within limits : ',y2)
                point = c.create_oval(x1,y1,x2,y2,fill=color)
                organism = Organism(x1,y1)
                organism.checkSurrounding(pop)
                population.append(organism)
                # print('coordinate : ', x1,y1,x2,y2,color)

            root.update()
        return population



root = Tk()
app = App(root)
root.mainloop()

