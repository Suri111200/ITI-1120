#Binary Search algorithm

def BinarySearch(values,item):

    first = 0
    last = len(values)-1
    found = False
    steps=0
    
    while first <= last and found== False:
        middle = (last+first)//2
        #print(middle)
        steps+=1
        if values[middle]==item:
            #print("middle")
            found = True
            break
        elif item > values[middle]:
            first = middle+1
        else:
            last = middle-1
    print(found, ". Steps:",steps)
