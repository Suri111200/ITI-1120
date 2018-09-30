def TenToOne():
    counter = 10
    while (counter != 0):
        print (counter)
        counter = counter-1


def ForPrintNumbersTo(n):
    for number in range(1,n+1):
        print(number)

def WhilePrintNumbersTo(n):
    number = 1
    while (number != n+1):
        print(number)
        number = number+1

def GuessingGame():

    import random

    number = int(10*random.random())+1
    tries = 0
    print(number)

    guess = int(input("Please guess a number between 1 to 10: "))

    while (guess != number):
        tries = tries+1

        if guess > number:
            print ("Lower")
        else:
            print ("Higher")
        guess = int (input("Try again: "))

    tries = tries+1
    print("You got it! Tries: ", tries)

def Factorial(n):
    factorialcalc = 1
    while n<0:
        n = int(input("The number should not be negative. \n Please try another number: "))

    print (ComputeFact(n))
    

def ComputeFact(n):
    factorialcalc = 1    

    if n==0:
        return(factorialcalc)
    else:
        for number in range (1,n+1):
            factorialcalc = factorialcalc*number
        return(factorialcalc)
    
