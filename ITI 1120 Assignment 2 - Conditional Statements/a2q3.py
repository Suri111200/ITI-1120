def a2q3():

    import random

    gameChoice = 2

    while gameChoice !=0 and gameChoice !=1:
        gameChoice = int(input("Please specify which game you would like to play.\nFor addition, enter 0. \nFor multiplication, enter 1. \nChoice: "))

    count = 0
    correct = 0

    while count<10:
        num1 = int(10*random.random())+1
        num2 = int(10*random.random())+1
        if gameChoice==0:
            correctAns = num1+num2
            print("Please answer the following: ",num1,"+",num2,"= ")
        else:
            correctAns = num1*num2
            print("Please answer the following: ",num1,"x",num2,"= ")
        guess = int(input()) 
        if guess == correctAns:
            print ("Correct!")
            correct = correct+1
        else:
            print ("Wrong answer. The answer is: ", correctAns)
        count = count+1
    print ("Correct Answers: ",correct)

    if correct>6:
        print ("Congratulations!")
    else:
        print("Please ask your teacher for help.")
