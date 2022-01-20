
filenameAndExtention = input("insert file name:\n")

fileSplitted = filenameAndExtention.split(".")
print(fileSplitted[len(fileSplitted)-1])