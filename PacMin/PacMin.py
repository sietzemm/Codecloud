# Author : Sietze Min
# Date : 11-06-2020, last modified on : 23-07-2021
# Description : Recreation of the classic Pac man arcade game from scratch

import sys
from tkinter import *
from pynput import keyboard

# print(sys.version)

class Game:
    def __init__(self, root):
        self.root = root
        self.screenHeight = root.winfo_screenheight()
        self.screenWidth = root.winfo_screenwidth()
        # self.screen = Canvas(root, width = self.screenWidth, height = self.screenHeight, bg="black")
    
        self.startScreenBool = True
        # self.gameScreenBool = False
        # self.scoreScreen = False

        def startNewGameCallBack():
            print("execute newGameCallBack")
            self.startScreenBool = False
            self.root.after(100, main)

        def main():
  
            # init start screen
            if(self.startScreenBool == True):

                self.frameHeader = Frame(self.root, width = self.screenWidth, height=300, bg="black")
                self.frameHeader.grid(row=1, column=1)

                self.txtLbl01 = Label(self.root, text="PacMin", fg="white", bg="black", font=("Arial",25))
                self.txtLbl01.grid(row=2, column=1)

                self.txtLbl02 = Label(self.root, text="HIGHSCORES", bg="black", fg="white")
                self.txtLbl02.grid(row=3, column=1)

                self.newGameBtn = Button(self.root, text="new game", bg="gray", command = startNewGameCallBack, cursor="hand1")
                self.newGameBtn.grid(row=4, column=1)

                self.footerTxtLbl = Label(self.root, text="Made by Sietze Min", bg="black", fg="white")
                self.footerTxtLbl.grid(row=5, column=1, pady=(100,0))

                self.frameFooter = Frame(self.root, width=self.screenWidth, height=50, bg="black" )
                self.frameFooter.grid(row=6, column=1, sticky=S)
            else:
                self.txtLbl01.destroy()
                self.newGameBtn.destroy()
                self.txtLbl02.destroy()
                print("Else clause activated")

        # Initial execution
        main()

    # def placeFood(self, root):
    #     pass

    # def placePowerUp(self, root):
    #     pass


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
root.title = "PacMin"
app = Game(root)
root.mainloop()
