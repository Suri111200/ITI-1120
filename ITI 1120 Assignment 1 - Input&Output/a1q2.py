def a1q2():

    change = float(input("Enter the amount of change owed in $: "))
    moneyback = 0
    while (change > 0.25):
                   change = change-0.25
                   moneyback = moneyback+1
    while (change > 0.10):
                   change = change-0.1
                   moneyback = moneyback+1
    while (change > 0.05):
                   change = change-0.05
                   moneyback = moneyback+1
    while (change > 0.01):
                   change = change-0.01
                   moneyback = moneyback+1

    print ("The minimum number of coins the cashier can return is ",moneyback)
