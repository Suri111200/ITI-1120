def a1q3():

    #Ask for input    
    lightyears = float(input("Input a number of light years: "))

    #Perform calculations
    seconds = lightyears*365.26*24*60*60
    distance = seconds*300000

    #print result
    print ("The number of seconds is ",seconds, "\nThe distance is ",distance, "km")

    #input for next question
    star1 = float(input("Input the distance to the first star, in light years: "))
    star2 = float(input("Input the distance to the second star, in light years: "))

    #Perform calculations
    lightyears = abs(star2-star1)
    seconds = lightyears*365.26*24*60*60
    distance = seconds*300000

    #Print result
    print ("The distance between the two stars is ",distance, " km")
