import sys
import math
print(sys.version)

def calcCircumference(radius):
    return round((2*math.pi)*math.pow(radius,2))

def calcSphereVolume(radius):
    return round(((4/3)*math.pi)*math.pow(radius,3))

print(calcCircumference(5))
print(calcSphereVolume(5))