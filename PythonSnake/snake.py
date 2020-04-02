# Author : Sietze Min
# Date : 30-03-2020, last modified on 01-04-2020

import sys
import threading
import random
import time
import os
from tkinter import *
from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play

print(sys.version)
def main():
    class App:
        def __init__(self, root, width=500, height = 500):
            self.root = root
            root.title = "Snake"
            self.c = Canvas(root, width = 500, height = 500, bg ="black")
            self.gameOverSound = AudioSegment.from_wav('/Users/sietzem/dependencies/PythonSnake/audio/gameover2.wav')
            self.soundBool = True
            self.c.pack()
            self.snakeLength = 1 # initial value should be 10
            self.snakeTail = [] # Length of snakeTail[] should not exceed length of snake body
            self.screenWidth = width
            self.screenHeight = height
            self.snakeDirection = random.randint(0,3) # 0 = up, 1 = left, 2 = down, 3 = right, inital direction is random
            # self.snakeDirection = 3 # 0 = up, 1 = left, 2 = down, 3 = right, inital direction is random
            self.gameSpeed = 0.5 # determines the speed the snake moves, initial value should be 0.5 (Actually the time the program sleeps in between moves)
            self.MAXSPEED = 0.010 # This is the time in seconds the game sleeps between steps. Lower value mean higher speed.
            self.gameOver = False
            self.stopThreads = False
            self.score = 10
            self.food = Food(0,0) # Food placeholder obj
            print(self.food.x1, self.food.y1, 'FOOD COORDINATES')
            # Calculate start position
            self.start_x = (width / 2) - 10 # substract 10 to correct for size of snake body (left offset)
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
            self.drawFood(self.c)

        # This method draws the food on screen
        def drawFood(self, c):
            """Place food on a  (semi) random location on the screen"""
            while(True):
                # 1 calculate coordinates
                spawnX = random.randrange(0, self.screenWidth,10)
                spawnY = random.randrange(0, self.screenHeight,10)
                print('I hang here')

                if len(self.snakeTail) == 0:
                    # On the off change initial food coordinate coincides with start position of snake head, check this
                    if spawnX == 240 and spawnY == 240:
                        continue
                    print('length is 0!')
                    break # break out of loop if length is 0
                
                else: # Length of snake tail is not 0! calculate new coordinate
                    for x in range(len(self.snakeTail)):
                        if spawnX == self.snakeTail[x][0] and spawnY == self.snakeTail[x][1]:
                            continue
                        if spawnX == self.snakeHeadPosition[0] and spawnY == self.snakeHeadPosition[1]:
                            continue
                        else: 
                            break # No matches in snakeTail, break out of loop
                    break
            

            print('out of loop')
            self.food.x1 = spawnX
            self.food.y1 = spawnY
            c.create_rectangle(spawnX,spawnY,spawnX+10,spawnY+10, fill="red")
            print('Drawing food : ', spawnX, spawnY)



        def drawSnake(self,c, snake_length, start_position):
            self.snake = Snake(self.snakeLength,c, start_position) # Overwrites placeholder snake with initial snake
                
        def updateScreen(self):
            print("Start coordinates : ", self.snakeHeadPosition)
            while(True):
                print(self.gameOver)
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
                    if self.soundBool == True:
                        play(self.gameOverSound)
                        self.soundBool == False
                #Check if snake head collides with own body
                self.checkIfSnakeHitSelf()

                time.sleep(self.gameSpeed)
                root.update()

                self.removeTrail(self.snakeLength)
                # print('last element in snakeTail : ', self.snakeTail[-1])
                # print("Current head position : ", self.snakeHeadPosition)
                # print("previous head position : ", self.snakeTail[-1])
                print('step')

        def callBackReplayBtn(self):
            self.root.destroy()
            main()

        def showGameOverScreen(self):
            gameOverTextLbl = Label(root, text="GAME OVER!", fg="white", font=("Helvetica", 24), bg="black")
            totalScoreLbl = Label(root, text = "SCORE "+ str(self.score), fg="GREEN", font=("Helvetica", 12), bg="black")
            replayBtn = Button(root, text = "Replay", command = self.callBackReplayBtn)

            if(self.gameOver == True):
                gameOverTextLbl.place(x = 170, y = 235)
                totalScoreLbl.place(x = 170, y = 270)
                replayBtn.place(x = 180, y = 420)

        def setNewHeadPosition(self, old_head_position,newX, newY):
             # Appends the last position of snake head to the history list
            self.snakeTail.append(old_head_position)    
            # print(old_head_position,' toegevoegd aan snakeTail.')         
            del self.snakeTail[:-(self.snakeLength)]                                  

            new_head_position = ((old_head_position[0]+ newX), (old_head_position[1] + newY))
            self.snakeHeadPosition = new_head_position
        
        def removeTrail(self, snake_length):
            """Removes the trail of the snake, minus its current length"""
            x1 = (self.snakeTail[-len(self.snakeTail)][0])
            y1 = (self.snakeTail[-len(self.snakeTail)][1])
            
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

        def checkIfSnakeHitSelf(self):
            print('snake tail content : ', self.snakeTail)
            for x in range(len(self.snakeTail)):
                # print('checking : ', self.snakeHeadPosition[0], 'against : ', self.snakeTail[x][0])

                if self.snakeHeadPosition[0] == (self.snakeTail[x][0]) and self.snakeHeadPosition[1] == (self.snakeTail[x][1]):
                    self.gameOver = True
        
        def checkIfSnakeHitsFood(self):
            print('checking food')
            if self.snakeHeadPosition[0] == self.food.x1 and self.snakeHeadPosition[1] == self.food.y1:
                print('hit! condition true')
                # Draw new food object on screen
                self.drawFood(self.c)

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
        def __init__(self, x1, y1):
            self.x1 = x1
            self.y1 = y1


    root = Tk()
    app = App(root)
    root.mainloop()

main()