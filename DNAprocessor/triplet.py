# Date : 16-02-2020
# Author : Sietze Min

import sys
import os
import math
# print(sys.version)

# DNA = 'ATGGAGACTGGTACGCGTAA'
def inputReader(filename):
    """
    File needs to be in the same directory as the program to work. Do not change filenames!
    """
    path = __file__
    path = path[:-10]
    path = path + filename # Extend path with filename
    f = open(path, "r")
    sequence = list(f)
    return sequence

output = inputReader('sequence.txt')
# print(type(output))

def processDNA(DNA):
    sequence = []

    DNA = str(DNA)
    DNA = DNA[2:-2]
    for x in range(len(DNA)):
        # print(DNA[x])
        if x % 3 == 0:
            sequence.append(DNA[x:x+3])

    print('Length of sequence : ', len(DNA))

    remainder = len(DNA) - (math.floor(len(DNA)/ 3) * 3)
    print('Number of triplets in sequence : ', math.floor((len(DNA) / 3)), 'remaining :', remainder)
    # print('Sequence : ', sequence)

def findSequence(DNA, sequence):
    listDNA = []
    matchesLOC = []
    DNA = str(DNA)
    DNA = DNA[2:-2]
    # print(DNA)
    for x in range(len(DNA)):
        # Loop through sequence to find
        for y in range(len(sequence)):
            # print('value X :',x, DNA[x], ' value Y : ',y, sequence[y])
    
            if DNA[x] != sequence[y]:
                break # Break out of for loop (y)
        
            else:
                # print('match on x value :', x, 'with : ',DNA[x], ' and : ', sequence[y])
                # print('location in DNA : ',x)
                y = y + 1
                x = x + 1        
                # print(x,y)
                #If complete match is present add loction to matchesLOC
                if y == len(sequence):
                    matchesLOC.append(x - (len(sequence)))
                    # print(x,y)

                if x == len(DNA):
                    print('Reached end of line. Last triplet : ',DNA[x-3:x])
                    break

    print('matches : ', len(matchesLOC), 'for sequence :', sequence)
    # print('MatchesLOC location : ',matchesLOC)
    print('MatchesLOC location : ',matchesLOC[:3])

print(processDNA(output))
print(findSequence(output, 'TATA'))
print('Finished.')

