def count_pos(raw_input):

    #Initialize new list for floats
    float_input = []
    positivenums= 0
    
    #Convert Strings to Float
    for i in range (len(raw_input)):
            float_input.append(float(raw_input[i]))
            #Test list for positive numbers
            if float_input[i] > 0:
                positivenums += 1

    return positivenums

def main():

    #Request input, split into a list
    raw_input = input("Please input a string of numbers separated by a space: ").strip().split()

    #Call function count_pos to determine result
    answer = count_pos(raw_input)

    print ("There are", answer, "positive numbers in your list.")    
