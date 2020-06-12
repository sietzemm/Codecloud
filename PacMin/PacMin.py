# Author : Sietze Min
# Date : 11-06-2020, last modified on : 12-06-2020
# Description : Recreation of the classic Pac man arcade game from scratch

import sys
from tkinter import *
from pynput import keyboard

# print(sys.version)

class Game:
    def __init__(self, root):
        self.root = root
        self.title = "PacMin"
        self.screenHeight = root.winfo_screenheight()
        self.screenWidth = root.winfo_screenwidth()
        self.screen = Canvas(root, width = self.screenWidth, height = self.screenHeight, bg="black")
        self.screen.pack()
        self.screen.create_text(self.screenWidth/2,self.screenHeight/2,fill="white",font="Times 40 bold",text="PACMIN 2020")

        self.startScreenBool = True
        self.gameScreenBool = False
        self.scoreScreen = False

        self.foodLocation = []
    
        if self.startScreenBool == True:
            self.startScreen(self.screen, self.root)

    def startGame(self):
        pass

    def startScreen(self, screen, root):
        screen.create_text(self.screenWidth/2, ((self.screenHeight/2)+50), fill = "white", font="Times 20", text = "Made by Sietze Min")
        startBTN = screen.create_rectangle(self.screenWidth/2, self.screenWidth/2, (self.screenWidth/2)+100, (self.screenWidth/2)+20, fill="green", outline="grey60")

        # def StartScreen(screen, root):
    
        # StartScreen(self.screen, self.root)
        
    def updateGameScreen(self, root):
        pass

    def placeFood(self, root):
        pass

    def placePowerUp(self, root):
        pass


class Ghost:
    def __init__(self):
        self.__str__="I am a ghost"
        self.lifespan = 10

    def move(direction):
        if direction == 'north':
            checkMove()
        if direction == 'south':
            checkMove()
        if direction == 'east':
            checkMove()
        if direction == 'west':
            checkMove()

    def checkMove(boardCoordinates):
        #Check coordinates
        pass
    
class PacMin:
    def __init__(self):
        self.isAlive = True

    def eat():
        pass
        #Check if current location contains food, if so eat it. 

class Food:
    def __init__(self,x,y):
        self.location = (x,y)

class PowerUp:
    def __init__(self, x,y):
        self.location = (x,y)


root = Tk()
app = Game(root)
root.mainloop()
