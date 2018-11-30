def main():
    #Request input
    raw_input = input("Please input a list of numbers separated by a space: ").strip().split()
    #Call function to determine if run is present, return boolean
    answer = two_length_run(raw_input)
    #Print Result
    print(answer)

def two_length_run(raw_input):
    #Initilize new list for floats
    float_input = []

    #Convert string to float
    for i in range (len(raw_input)):
            float_input.append(float(raw_input[i]))
            #After 2 Strings converted to float, begin testing for run of 2
            if i>0 and float_input[i] == float_input[i-1]:
                #Stop and return True if found
                return True
    #Return false if loop complete, true condition is not met
    return False
