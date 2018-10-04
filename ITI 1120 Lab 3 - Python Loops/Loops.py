def TenToOne():
    #Set value for countdown
    counter = 10

    #Used loop to print values, modify value for countdown
    while (counter != 0):
        print (counter)
        counter = counter-1


def ForPrintNumbersTo(n):

    #Used for loop to print numbers from 1 to input
    for number in range(1,n+1):
        print(number)

def WhilePrintNumbersTo(n):

    #Used while loop to print numbers from 1 to input
    number = 1
    while (number != n+1):
        print(number)
        number = number+1

def GuessingGame():

    #Import random function to generate randon number
    import random

    #Determine number to guess, declare value for tries
    number = int(10*random.random())+1
    tries = 0

    #Ask for input
    guess = int(input("Please guess a number between 1 to 10: "))

    #Determine if correct answer was stated, increase num of tries if not
    while (guess != number):
        tries = tries+1

        #Determine a hint to tell user
        if guess > number:
            print ("Lower")
        else:
            print ("Higher")

        #Ask for input again
        guess = int (input("Try again: "))

    #If answer is correct
    tries = tries+1
    print("You got it! Tries: ", tries)

def Factorial(n):

    #Determine if input is acceptable
    while n<0:
        #Request for appropriate input
        n = int(input("The number should not be negative. \n Please try another number: "))

    #Call function to perform calculation, print result
    print (ComputeFact(n))
    

def ComputeFact(n):

    #Declare valriable
    factorialcalc = 1    

    #If user wants 0!, print 1
    if n==0:
        return(factorialcalc)
    else:
        #Perform factorial calculation
        for number in range (1,n+1):
            factorialcalc = factorialcalc*number
        return(factorialcalc)
    
