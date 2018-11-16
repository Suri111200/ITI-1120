import random

def isitThere():
    #Request for user input
    value = int(input("Enter a value you would like to check is in the list: "))
    #Initialize number of tries counter
    numoftries = 0
    #For loop checks every entry, prints number of tries and True if found
    for i in listofnums:
                numoftries+=1
                if i == value:
                    print("True\nNumber of executions:", numoftries)
                    return
    #False is printed if loop completes
    print("False")

#Create lists with 1000 random values
listofnums = []
for i in range(1000):
    listofnums.append(random.randint(-100,100))
isitThere()
