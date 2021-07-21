# Date : 10-07-2019
# Author : Sietze Min

import sys
print(sys.version)

def tempCalc(t,unit):
    substances = {
    "Benzeen" : (279,6,353,80),
    "Kamfer" : (453,180,480)
    }
    unit = unit.lower()

    if unit == "c":
        """input given is in celsius"""
        print('You entered : ', t, "in degrees celsius")
        for substance in substances:
            if t in substances[substance]:
                print('Based on the entered substance properties its probably : ', substance,".")
        return t + 273

    if unit == "k":
        """inpit given is in Kelvin"""
        print('You entered : ', t, "in degrees kelvin")
        for substance in substances:
            if t in substances[substance]:
                print('Based on the entered substance properties its probably : ', substance,".")

        temp = str(t - 273)
        return "Meltpoint : " + temp + ", in celsius."


print(tempCalc(279,"k"))
# print(tempCalc(453,"k"))
