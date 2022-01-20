

def getIntInput():

    while (True):
        inputNumber = input("inserire un numero intero\n")
        try:
            return int(inputNumber)
        except:
            print("l'input deve essere un numero intero")


def sumOf_Fixed(numberString):
    return int(numberString) + int(numberString + numberString ) + int(numberString + numberString + numberString)

def sumOf_custom(numberString, numberOfDigits):

    totalsum = 0
    minusOneDigitNumber = numberString

    for x in range(0, numberOfDigits):
        print(minusOneDigitNumber)
        totalsum += int(minusOneDigitNumber)
        minusOneDigitNumber += numberString

    return totalsum

       
inputNumberStr = str(getIntInput())

print(sumOf_Fixed(inputNumberStr))

print("--------------------")

print(sumOf_custom(inputNumberStr, 5))


