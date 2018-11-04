#task: move zeros to end of inputted list

def move_zeros_v1(lists):
    tmp = []
    zero = 0
    #For loop keeps track fo zeroes, appends value only if nonzero
    for val in lists:
        if val == 0:
            zero+=1
        else:
            tmp.append(val)

    #Next for loop adds number of zeroes found in list into end of list
    for zeros in range(zero):
        tmp.append(0)

    #Return new list
    return tmp

def move_zeros_v2(lists):
    zerocount = lists.count(0)
    #For loop removes value if == 0
    lists = [value for value in lists if value != 0]
    #Append zerocount # of 0s at end
    for zeros in range(zerocount):
        lists.append(0)

    print(lists)

def move_zeros_v3(lists):
    i = 0
    x = len(lists)
    #if index is 0, delete index, decrease range by 1, append 0 to end of list
    #else increase i by 1
    while i < x:
        if lists[i] == 0:
            del lists[i]
            lists.append(0)
            x-=1
        else:
            i+=1

    print(lists)

