def sort_by_insertion(values):
    for i in range(len(values)):

        index = values[i]
        j = i-1

        while j>-1 and values[j]>index:
            values[j+1]=values[j]
            j-=1
        values[j+1] = index
    print(values)
    
