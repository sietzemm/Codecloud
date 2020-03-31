import sys
import random
import os
# print(sys.version)

def writeToFile(sequence):
    path = __file__
    path = path[:-15]
    print(path)
    outputname = path+'sequence.txt'
    print(outputname)
    f = open(outputname, "a")
    f.write(str(sequence))
    f.close

    print("Generated DNA sequence with length : ", len(sequence),'bp.')

def generator(length):
    sequence = []

    for x in range(length):
        number = random.randint(0,3)

        if number == 0:
            sequence.append('A')
        if number == 1: 
            sequence.append('T')
        if number == 2:
            sequence.append('C')
        if number == 3: 
            sequence.append('G')
    output = ""
    return output.join(sequence)

writeToFile(generator(pow(10,3)))

