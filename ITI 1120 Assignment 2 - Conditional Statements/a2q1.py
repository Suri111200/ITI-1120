def a2q1():

    weight = float(input("Please input weight in kilograms: "))
    height = float(input("Please input height in meters: "))
    BMI = weight/height/height
    if BMI < 18.5:
        print ("Underweight")
    elif BMI >= 18.5 and BMI <= 25:
        print ("Normal weight")
    else:
        print ("Overweight")
