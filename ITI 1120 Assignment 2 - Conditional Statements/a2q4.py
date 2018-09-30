def a2q4():

    import random

    count = 0
    correct = 0

    while count<10:
        gameChoice = int(2*random.random())
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
