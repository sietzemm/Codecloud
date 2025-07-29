# Date of creation : 13-10-2018
# Author : Sietze Min

# Small exercise : Write a function that takes two points and calculates the distance between them.
c1 = (1,2)  # coordinate 1
c2 = (-1,1) # coordinate 2

import math
import sys
print(sys.version)
# arguments need to be of type tuple
def calc_distance(c1,c2):

    #Type checking
    if(type(c1) and type(c2) == tuple):
        """
        Calculates the distance between two coordinates by triangle calculation and
        the Pythagorean theorem to calculate the final distance.
        """
        a,b = c1,c2
        c = tuple()                         # Create empty tuple placeholder for the C coordinate

        Cx = abs(b[1]) - abs(a[0])          # Calculate the C coordinate (Cx and Cy)
        Cx = abs(Cx) + b[0]                 # Create the C x coordinate value deriven from the length diff between A and B

        Cy = b[1]                           # Creates C y coordinate value deriven from the B coordinate
        c = (Cx,Cy)                         # Assigns Cx and Cy to the C coordinate tuple

        line_bc = abs(b[0] - abs(c[0]))     # creates side BC for the triangle
        line_ac = abs(a[1] + abs(c[1]))     # creates side AC for the traigle (AB is the hypotenuse and still unkown)

                                            # Use Pythagorean theorem (a^2 + b^2 = c^2)
        a = math.pow(line_bc,2)             # creates A^2
        b = math.pow(line_ac,2)             # creates B^2
        c = str(round(math.sqrt(a + b),2))  # creates c, and performs round operation up to 2 decimals
        result = 'Distance between coordinates : ',c1, 'and ',c2,'is : ',c
        return result
    else:
        print('incorrect input types specified')
        return False

print(calc_distance(c1,c2))
#print(calc_distance('2',2))
