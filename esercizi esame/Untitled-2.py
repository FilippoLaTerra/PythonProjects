

inputList = [2, 3, 9]
outputList = []

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


def createFibList(n):
    i = 0
    sequenceList = []
    while n >= fibonacci(i):
        sequenceList.append(fibonacci(i))
        i += 1

    return sequenceList


def checkIfInputIsValid(input):

    if len(input) != 3:
        return False

    for n in input:
        if (n < 0 or not isinstance(n, int)):
            return False

    return True
        

if checkIfInputIsValid(inputList):
    for n in inputList:
        outputList.append(createFibList(n))

    for list in outputList:
        print("[", end="")

        for n in list:
            numberToPrint = str(n)

            if n != list[-1]:
                numberToPrint += ", "
            print(numberToPrint, end="")
            
        print("]")

else:
    print("Exception: input must be 3 number all >= 0")

