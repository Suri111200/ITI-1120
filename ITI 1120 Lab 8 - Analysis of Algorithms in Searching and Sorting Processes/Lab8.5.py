def MySort(values):
    Ascending = False
    while Ascending == False:
        Ascending == True
        for i in range(1,len(values)):
            if values[i] < values[i-1]:
                temp = values[i]
                values[i] = values[i-1]
                values[i-1] = temp
                print(values)
                Ascending = False
                
