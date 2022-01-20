

PI = 3.148

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

area = PI * (raggio * raggio)

print(area)