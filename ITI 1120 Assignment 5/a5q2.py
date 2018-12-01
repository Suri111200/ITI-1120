#Function takes in numbner, prints star pattern using recursive function


def stars(num):
    #Error handling-- return value error if number inputted is not greater than 0
    if num<1:
        raise ValueError("Input must be greater than 0")
    #Call recursive function
    print_star(num,num+1)

#Recursive function- has two integer parameters, one boolean parameter
def print_star(start,stop, Descending=True):
    #If descending, print number of stars as "start" value
    #Then, call function again, reduce "Start" by 1
    if start>0 and Descending==True:
        print('*'*start)
        return print_star(start-1,stop)
    #If start equal to 0, change boolean parameter to False (now ascending)
    #Start increasing Start Value
    if start ==0:
        return print_star(start+1,stop,Descending=False)

    #Check if the stop value has been reached     
    if start != stop:
        #If start value is greater than 0 and pattern is ascending
        #Print number of stars as start value
        #Call function again, increase start by 1, boolean is false
        if start >0 and Descending == False:
            print('*'*start)
            return print_star(start+1,stop,Descending=False)

    #If none of the above statements are true, return None, end recursion
    return

#Function takes in list, list length, outputs sum of positive values
def sumListPos_rec(lists,length,i=0,val=0):
    #If i(index) is equal to length of list, return sum of positive integers
    if i == length:
        return val
    #If i (index) in list is greater than 0, add to sum calculation
    elif lists[i] >0:
        val+=lists[i]
    #If none of the above conditions are met, call the function again
    #Specify 3rd arameter as i+1, specify 4th parameter as current value of sum
    return sumListPos_rec(lists,length,i+1,val)
