def a2q1():

    #Input values
    weight = float(input("Please input weight in kilograms: "))
    height = float(input("Please input height in meters: "))

    #Perform calculation based on values
    BMI = weight/height/height

    #Determine result to print
    if BMI < 18.5:
        print ("Underweight")
    elif BMI >= 18.5 and BMI <= 25:
        print ("Normal weight")
    else:
        print ("Overweight")
