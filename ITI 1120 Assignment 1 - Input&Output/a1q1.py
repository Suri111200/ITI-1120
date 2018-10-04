def a1q1 ():

    #Ask for input
    pounds = int(input("Enter the weight in pounds: "))
    ounces = int(input("Enter the number of ounces: "))

    #Input into conversion equation
    kg = pounds*0.4534+ounces*0.02834

    #Print output
    print (pounds, "pounds and ", ounces, " ounces is approximately ",kg, "kilograms.")
