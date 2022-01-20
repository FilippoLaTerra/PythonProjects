

inputNumbers = input("Inserisci la lista di numeri").replace(" ", "")

numberList = inputNumbers.split(",")
numberTuple = tuple(inputNumbers.split(","))

print(numberList)
print(numberTuple)