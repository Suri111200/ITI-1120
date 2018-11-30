def main():
    #Request input, split into a list
    raw_input = input("Please input a string of numbers separated by a space: ").strip().split()

    #Call function to determine result
    answer = longest_run(raw_input)

    print (answer)    

def longest_run(raw_input):
    #Initilize new list for floats
    float_input = []
    longest_run = 1
    run = 1
    
    #Convert string to float
    for i in range (len(raw_input)):
            float_input.append(float(raw_input[i]))

    #If list has one value then all if statements will be skipped
    #1 will be returned

    #If list is empty
    if not float_input:
        return 0
    #If list is not empty, and more than one value in list
    elif len(float_input) > 1:
        #if 2nd value is equal to 1st value, run=2, longest_run=2
        if float_input[1] == float_input[0]:
            run+=1
            longest_run+=1
    #If list has 3 or more values        
    if len(float_input) > 2:
        #Commence for loop for length of list, starting at 3rd value
        for i in range(2, len(float_input)):
            #if i is equal to i-1, run+=1
            if float_input[i] == float_input[i-1]:
                run+=1
            #if i is not equal to i-1, but i-1 is equal to i-2
            #check if current run is greater than longest run
            #If so, change longest run value
            #Reset run value regardless once done
            elif float_input[i-1] == float_input[i-2]:
                if longest_run < run:
                    longest_run = run
                run = 1

    #After for loop, if current run longer than longest, change longest run val
    if run > longest_run:
        longest_run = run
    #Return longest run
    return longest_run
