#Inputs 2D Array and integer
#Tracks number of times integer appears in 2D array
#Returns number of times it appears
def numoftimes(M,v):
    numoftimes = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == v:
                numoftimes+=1
    return numoftimes
