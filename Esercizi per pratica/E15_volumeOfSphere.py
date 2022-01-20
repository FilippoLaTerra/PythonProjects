
from math import pi


def getFloatInput():

    while (True):
        inputNumber = input("inserire un numero:\n")
        try:
            return float(inputNumber)
        except:
            print("l'input deve essere un numero")

def calculateVolume(radius):
    return 4/3 * pi * radius**3

radius = getFloatInput()

print(calculateVolume(radius)) 
