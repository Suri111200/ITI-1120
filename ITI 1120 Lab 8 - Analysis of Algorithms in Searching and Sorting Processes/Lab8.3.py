import random
#Generates random list
#Requests for value from user
#Checks how many times it appears inlist
#Print result
def TimesInList():
    v = int(input("What number are you looking for? "))
    matches=0
    for i in listofnums:
        if v == i:
            matches+=1
    return matches

listofnums = []
for i in range(1000):
    listofnums.append(random.randint(-100,100))
num = TimesInList()
print("The number appears",num,"times.")
