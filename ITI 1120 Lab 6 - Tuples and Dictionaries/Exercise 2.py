def histo_n(x):
    dictionary = {}
    for val in x:
        dictionary[val] = dictionary.get(val,0)+1 #adds 1 to dictionary val, creates entry if not present
    return dictionary

#Main
raw_input = input('Enter a tuple : ') #Ask user to input tuple ie."(1,2,3,4,5,6)"
modified_input = raw_input.replace("(","").replace(")","") #Remove brackets from "tuple" inputted
into_list = [int(n) for n in modified_input.split(',')] #Convert given data to list
t = tuple(into_list) #convert list to tuple
dictionary =(histo_n(t)) #call function to return dictionary
lists = list(dictionary.items()) #creates list of dictionary entries
lists.sort() #sorts list based on alphabetical order
print(lists) #prints sorted list
    
