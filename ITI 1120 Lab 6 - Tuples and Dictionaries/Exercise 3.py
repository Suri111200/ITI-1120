def sum_of_three(x):

    #Automatically return false if tuple has less than 3 entries
    if len(x)< 3:
        return False
    #test each set of 3 consecutive values, reutrn true if sum equals 0
    for i in range(len(x)-2):
        if x[i]+x[i+1]+x[i+2] == 0:
            return True
    #Return false if above loop completes without being interrupted
    return False
