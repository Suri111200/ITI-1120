def Average(num):

    #Ask for values (num) times
    numbers = []
    for i in range (0, num):
        x = int(input("Please enter value: "))
        numbers.append(x)

    a=0
    sum =0

    #Sum numbers
    while a!= len(numbers):
        sum = sum + numbers[a]
        a=a+1

    #Determine average
    average = sum/len(numbers)

    #return value
    return average
    
def MarksCalc(num):

    #Ask for values (num) times
    numbers = []
    for i in range (0, num):
        x = int(input("Please enter value: "))
        numbers.append(x)

    max = 0
    min = 100
    sum = 0
    a=0

    #Analyze each number, determine max, min, sum
    while a!= len(numbers):
        if max < numbers[a]:
            max= numbers[a]
        if min > numbers[a]:
            min = numbers[a]
        sum = sum + numbers[a]
        a = a + 1

    #Find Average
        average = sum/len(numbers)

    #Create list with results
    results = [max, min, average]

    print(results)

def BallToss(velocity):

    a = 0
    distance = []

    #Loop until 90 degrees
    while a < 91:
        #Call function to do calc
        distance.append(DistanceCalc(a, velocity))
        a = a+10

    #Print array
    print(distance)

def DistanceCalc(angle, velocity):
    #Import library necessary for calculation
    import math

    x = (velocity**2 * math.sin(2*math.radians(angle)))/9.8
    return x

def SD():

    #Ask for input, generate into list
    print ("Print all values divided by spaces: ")
    val = [int(x) for x in input().split()]

    i = 0
    sum = 0

    #While loop to determine sum, then use to determine average
    while i != (len(val)):
        sum = sum+val[i]
        i = i+1
    a = sum/len(val)

    i=0
    numerator =0
    
    #Use loop to determine numerator of SD calc using average
    while i != (len(val)):
        numerator = numerator +((val[i]-a)**2)
        i = i+1

    #Use numerator value to find SD
    s = (numerator/(len(val)-1))**0.5

    print(s)
    
    
