def a1q3():
    
    lightyears = float(input("Input a number of light years: "))
    seconds = lightyears*365.26*24*60*60
    distance = seconds*300000
    print ("The number of seconds is ",seconds, "\nThe distance is ",distance, "km")

    star1 = float(input("Input the distance to the first star, in light years: "))
    star2 = float(input("Input the distance to the second star, in light years: "))
    lightyears = abs(star2-star1)
    seconds = lightyears*365.26*24*60*60
    distance = seconds*300000
    print ("The distance between the two stars is ",distance, " km")
