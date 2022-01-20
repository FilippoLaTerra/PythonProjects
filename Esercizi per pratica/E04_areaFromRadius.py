
from math import pi

def getInput():

    while(True):
        
        try:
            userInput = float(input("inserisci raggio del cerchio:\n"))
            
        except:
            print("input non valido, l'input deve essere un numero")

        else:
            print("input valido")
            return userInput

    

raggio = getInput()

area = pi * (raggio **2)

print(area)