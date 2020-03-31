# Author : Sietze Min
# Date : 30-03-2020

import sys
import threading
import random
import time
import os
from tkinter import *
from pynput import keyboard

print(sys.version)
def main():
    class App:
        def __init__(self, root, width=500, height = 500):
            self.root = root
            root.title = "Snake"
            self.c = Canvas(root, width = 500, height = 500, bg ="black")
            self.c.pack()
            self.snakeLength = 1 # initial value should be 10
            self.snakeTail = []
            self.screenWidth = width
            self.screenHeight = height
            self.snakeDirection = random.randint(0,3) # 0 = up, 1 = left, 2 = down, 3 = right, inital direction is random
            # self.snakeDirection = 3 # 0 = up, 1 = left, 2 = down, 3 = right, inital direction is random
            self.gameSpeed = 0.5 # determines the speed the snake moves, initial value should be 0.5 (Actually the time the program sleeps in between moves)
            self.MAXSPEED = 0.010
            self.gameOver = False
            self.score = 10
            self.food = Food(self.screenWidth, self.screenHeight)

            # Calculate start position
            self.start_x = (width / 2) - 10 # substract 10 to correct for size of snake body
            self.start_y = (height / 2 ) - 10
            self.snakeHeadPosition = (self.start_x, self.start_y)
            self.snake = Snake(1,self.c, self.snakeHeadPosition) # placeholder snake

            # Initiate thread to update screen
            self.updatethread = threading.Thread(target = self.updateScreen)
            self.updatethread.start()

            self.showScoreLbl = Label(root, text="SCORE : " + str(self.score), fg="red", font=("Helvetica", 12), bg="black")
            self.showScoreLbl.place(x = 390, y = 20)

            # Initiate keyboard listener
            self.globalListener()

            # Draw food on screen
            self.drawFood(self.c, self.food)

        # This method draws the food
        def drawFood(self, c, food):
            "Everytime method is called, a new food object is created"
            c.create_rectangle(food.coordinates[0],food.coordinates[1],food.coordinates[2],food.coordinates[3], fill = "red")

        def drawSnake(self,c, snake_length, start_position):
            self.snake = Snake(self.snakeLength,c, start_position) # Overwrites placeholder snake with initial snake
                
        def updateScreen(self):
            while(True):
                self.drawSnake(self.c ,self.snakeLength, self.snakeHeadPosition)
                self.checkIfSnakeHitsFood()
                self.checkIfHitWall()
                
                #Check if gameOver boolean is false, if so, all is good and game will continue
                if self.gameOver == False:
                    if self.snakeDirection == 0: # UP
                        self.setNewHeadPosition(self.snakeHeadPosition, 0,-10,) # x1 stays the same, decrease y1 with 10
                    
                    if self.snakeDirection == 1: # RIGHT
                        self.setNewHeadPosition(self.snakeHeadPosition, 10,0) # increase x1 with 10, y1 stays the same
                    
                    if self.snakeDirection == 2: # DOWN
                        self.setNewHeadPosition(self.snakeHeadPosition, 0,10) # x1 stays the same, increase y1 with 10

                    if self.snakeDirection == 3: # LEFT
                        self.setNewHeadPosition(self.snakeHeadPosition, -10,0) # x1 decreases with 10, y1 stays the same
                        
                else:
                    print("The game is over!")
                    self.showGameOverScreen()

                time.sleep(self.gameSpeed)
                root.update()

                self.removeTrail(self.snakeLength)
                # print('last element in snakeTail : ', self.snakeTail[-1])
                print('step')

        def callBackReplayBtn(self):
            self.root.destroy()
            main()

            # self.score = 0
            # self.snakeLength = 0
            # self.snakeTail = []
            # self.gameSpeed = 0.5
            # self.gameOver = False
            # self.c = Canvas(root, width = 500, height = 500, bg ="black")
            # # updatethread = threading.Thread(target = self.updateScreen)
            # # updatethread.start()
            # self.showGameOverScreen()
            # root.update()

        def showGameOverScreen(self):
            gameOverTextLbl = Label(root, text="GAME OVER!", fg="white", font=("Helvetica", 24), bg="black")
            totalScoreLbl = Label(root, text = "SCORE "+ str(self.score), fg="GREEN", font=("Helvetica", 12), bg="black")
            replayBtn = Button(root, text = "Replay", command = self.callBackReplayBtn)

            if(self.gameOver == True):
                gameOverTextLbl.place(x = 170, y = 235)
                totalScoreLbl.place(x = 170, y = 270)
                replayBtn.place(x = 180, y = 420)

            if(self.gameOver == False):
                print("FALSE!!!!")
                gameOverTextLbl.place_forget()
                totalScoreLbl.place_forget()
                replayBtn.place_forget()
                root.update()

        def setNewHeadPosition(self, old_head_position,newX, newY):
            self.snakeTail.append(old_head_position)                                                # Appends the last position of snake head to the history list
            new_head_position = ((old_head_position[0]+ newX), (old_head_position[1] + newY))
            self.snakeHeadPosition = new_head_position
            return new_head_position
        
        def removeTrail(self, snake_length):
            """Removes the trail of the snake, minus its current length"""
            if self.snakeLength != 0:
                x1 = self.snakeTail[-self.snakeLength][0]
                y1 = self.snakeTail[-self.snakeLength][1]
                self.c.create_rectangle(x1,y1,x1+10,y1+10, fill = "black")

        def globalListener(self):
            def on_press(key):
                try:
                    print('alphanumeric key {0} pressed'.format(key.char))
                except AttributeError:
                    print('special key {0} pressed'.format(key))

            def on_release(key):
                print('{0} released'.format(key))

                if key == keyboard.Key.up:
                    self.snakeDirection = 0

                if key == keyboard.Key.right:
                    self.snakeDirection = 1

                if key == keyboard.Key.down:
                    self.snakeDirection = 2

                if key == keyboard.Key.left:
                    self.snakeDirection = 3

            listener = keyboard.Listener(on_press=on_press,on_release=on_release)
            listener.start()
            
        def calculateScore(self):
            self.score = self.score + 10

        def checkIfSnakeHitsFood(self):
            if self.snakeHeadPosition[0] == self.food.coordinates[0] and self.snakeHeadPosition[1] == self.food.coordinates[1]:
                self.food = Food(self.screenWidth, self.screenHeight)
                self.drawFood(self.c, self.food)

                # increase score
                self.calculateScore()
                
                # add 1 block to snake tail
                self.snakeLength = self.snakeLength + 1
                # self.snake.drawBodyExtension()
            
                # increase gameSpeed
                self.increaseGameSpeed()

                self.showScoreLbl = Label(root, text="SCORE :" + str(self.score), fg="red", font=("Helvetica", 12), bg="black")
                self.showScoreLbl.place(x=390, y=20)
                root.update()

        def checkIfHitWall(self):
            """Checks if the snake hits a wall, if so its game over"""

            if self.snakeHeadPosition[0] not in range(0, self.screenWidth): 
                self.gameOver = True

            if self.snakeHeadPosition[1] not in range(0, self.screenHeight):
                self.gameOver = True

        def increaseGameSpeed(self):
            if self.gameSpeed - 0.10 >= self.MAXSPEED:
                self.gameSpeed = self.gameSpeed - 0.10

    class Snake:
        def __init__(self, snake_length, c, position):

            self.length = snake_length
            self.headColor = "white"
            self.bodyColor = "green"

            self.x1 = position[0]
            self.y1 = position[1]
            self.x2 = position[0] + 10
            self.y2 = position[1] + 10
            c.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill = self.headColor)

        # def drawBodyExtension(self, head_position,c):
        #     """Extends the snake body by adding one block behind its head on its previous coordinates"""
        #     c.create_rectangle(x1,y1,x2,y2, fill = self.bodyColor)

        #     print('draw snake body trailing from head position')

        
    class Food:
        "Place food on a random location on the screen"
        def __init__(self, boundX, boundY):
            self.boundsX = boundX
            self.boundsY = boundY
            self.coordinates = self.calcRandomSpawnPoint()

        def calcRandomSpawnPoint(self):
            spawnX = random.randrange(0, self.boundsX,10)
            spawnY = random.randrange(0, self.boundsY,10)
            
            coordinates = (spawnX, spawnY, (spawnX+10), (spawnY+10))
            return coordinates

    root = Tk()
    app = App(root)
    root.mainloop()

main()