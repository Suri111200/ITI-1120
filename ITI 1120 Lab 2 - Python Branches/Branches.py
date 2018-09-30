def AgeCheck(age):
    
    if age>=18 and age<=55:
        isAge = True
    else:
        isAge = False
        
    if isAge== True:
        print ("Transaction accepted")
    else:
        print ("Transaction refused")

def Activity(temp):

    if temp >= 80.0:
        activity = 1
    elif temp < 40.0:
        activity = 4
    elif temp < 60.0:
        activity = 3
    else:
        activity =2

    if activity ==1:
        print ("Swimming")
    elif activity ==2:
        print ("Soccer")
    elif activity ==3:
        print ("Volleyball")
    else:
        print ("Skying")

def isDivisible(num):

    if num%2==0 and num%3==0:
        isit = 1
    elif num%2==0 or num%3==0:
        isit = 2
    else:
        isit = 0
    return(isit)

def RealRoots(a,b,c):
    answer = (b**2) - (4*a*c)
    #print(answer)
    if answer == 0:
        print ("1")
    elif answer < 0:
        print ("0")
    else:
        print ("2")
