def a2q2():

    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))

    if a<b:
        for x in range (a, b+1):
            print (x)
    else:
        for x in range (b, a+1):
            print (x)
