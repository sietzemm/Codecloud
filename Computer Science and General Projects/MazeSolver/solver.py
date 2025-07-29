import random 
import sys 

# Creation date : 16-07-2019
# Author : Sietze Min
# Desc : To write an algorithm that is able to solve a simple maze.

def main():
    print("Maze solver by Sietze Min.")
    """  Rules for a maze :
    1 : The first row of the maze needs to only one 0. This is the entrance
    2 : The last row needs to have only one 0. This is the exit
    3 : The maze must be of equal dimensions (n*n maze)
    print('MazeSolver by Sietze Min')
    """
    entrance_pos = 0
    history = []
    maze = [[1,0,1],[1,0,1],[1,0,1]]
    
    for elem in maze : print(elem)
    
    def solver(entrance):
        current_pos = [0, entrance]
        print("Location in maze : ", current_pos) # the 0 is already known by definition because rule 1.

        # while(True):
        #     # check all directions
        #     # break when an exit has been found
        #     if current_pos[0]-1 == len(maze[0]):
        #         print("You have reached the exit!")
        #         break


        # #Check north
        # def checkN():
        #     pass
        # def checkE():
        #     pass
        # def checkS():
        #     pass
        # def checkW():
        #     pass
        print("Checking north side.")
        if current_pos[0] != 0: 
            #we zitten niet in de bovenste rij. Dus controlleer 1 rij erboven.
            if maze[current_pos[1] - 1] == 0:
                print("Valid path")
                # Update current pos
                current_pos[0] = current_pos[0] - 1

            if maze[current_pos[1] - 1 != 0]:
                print("not a valid path.")
        else : print("not a valid path to the north.")

        # #Check east
        if current_pos[1] < len(maze): # not on the far right side
            print("checking east side : ", maze[current_pos[1] + 1][0])
            if maze[current_pos[1] + 1][0] != 1:
                print("Valid path.")
                # Update current pos
                current_pos[1] = current_pos[1] + 1
            else : print("not a valid path to the east : ", current_pos[0],current_pos[1]+1)

        else : print("Must be on the far right side : ", current_pos)

        # Check south
        print("Checking south : current position ", current_pos)
        if current_pos[0] < len(maze[0]):
            # not on the bottom 
            if maze[current_pos[0] + 1][current_pos[1]] != 1:
                print("Valid path to the south.")
                # Update current pos
                current_pos[0] = current_pos[0] + 1
            else : print("Not a valid path to the right.")

        # check west
        print("Checking west : current position ", current_pos)
        if current_pos[1] != 0:
            #not at the far left side 
            if maze[current_pos[0]][current_pos[1]-1] != 1:
                print("valid path")
                #Update current pos
                current_pos[1] = current_pos[1] - 1
            else : 
                print("Not a valid path to the left.")

        # Force exit
        current_pos[0] = len(maze[0])
    # First it needs to check where the entrance is
    for elem in maze[0]:
        print(elem)
        # check if elem[0] equals 0, if so entrance found
        if elem == 0:
            print("entrance found on location : (0,", entrance_pos,")")
            break
        entrance_pos = entrance_pos + 1

    solver(entrance_pos)

    def mazeGenerator(length, height):
        maze = []
        for row in range(height):
            maze.append([])
            for j in range(length):
                rand = random.randint(0,1)
                maze[row].append(rand)

        # Make the first row all 1
        for k in range(len(maze[0])):
            maze[0][k] = 1
        
        # Make the last row all 1 
        for k1 in range(len(maze[len(maze)-1])):
            maze[len(maze)-1][k1] = 1
        return maze

    ma = mazeGenerator(14,14)
    for row in ma:
        print(row)

    mazeGenerator(4,4)
main()