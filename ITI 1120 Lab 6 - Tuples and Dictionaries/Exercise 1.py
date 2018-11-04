def Histogram (letters):
    dictionary = {} #create empty dictionary
    for letter in letters:
        dictionary[letter] = dictionary.get(letter,0)+1 #for loop adds 1 to entry, else creates entry
    return dictionary #return dictionary    

#main

letters = input("Please input a string of characters: ") #Asks for string input
dictionary = Histogram(letters) #sends raw input to function, expects dictionary returned
dictionary_sorted = list(dictionary.items()) #put dictionary into list
dictionary_sorted.sort() #sort list
print(dictionary_sorted) #return sorted list
