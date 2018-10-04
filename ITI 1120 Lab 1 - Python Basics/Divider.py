def Divider(num1,num2):

    #Perform result and print result
    print ("Division equals ", num1//num2," and remainder equals ",num1%num2)

def TempConverter(temp_Celsius):

    #Perform calculation with inputted value, return result
    temp_Fahrenheit = (9.0/5.0*temp_Celsius+32)
    return temp_Fahrenheit

def FinalGrade (hw_Average,midterm,final):

    #Perform calculation with inputted value, return result
    note = (hw_Average*25/100 + midterm*25/100 + final*50/100)
    return note

def Triangle (side1,side2,side3):

    #Perform calculation with inputted value, return result
    import math 
    p = side1+side2+side3
    area = math.sqrt(p*(p-2*side1)*(p-2*side2)*(p-2*side3))/4
    return area
