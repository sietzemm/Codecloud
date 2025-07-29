## Date : 20-11-2020
import sys
import random

print('Simple DNA generator')

def main(length):
    DNAlib = []
    for x in range(length):
        seednum = random.randint(1,4)

        if seednum == 1:
            DNAlib.append("A")
        
        if seednum == 2: 
            DNAlib.append("T")
        
        if seednum == 3:
            DNAlib.append("C")
        if seednum == 4:
            DNAlib.append("G")

    resultStr = ""
    for x in range(len(DNAlib)):
        resultStr = resultStr + str(DNAlib[x])

    print(resultStr)




main(30)