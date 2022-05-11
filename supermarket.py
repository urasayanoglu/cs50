import sys
prices = [10,14,22,33,44,13,22,55,66,77]
status = True
totalsum = 0
print("Supermarket")
print("===========")
while status:
    userinput = int(input("Please select product (1-10) 0 to Quit: "))
    if userinput < 0 or userinput > 10:
        print("Incorrect selection.")
        continue
    elif userinput == 0:
        print(f"Total: {totalsum}")
        userpayment = int(input("Payment: "))
        print(f"Change: {userpayment - totalsum}")
        status = False
        sys.exit()
    else:
        print(f"Product: {userinput}" + f"Price: {prices[userinput-1]}")
        totalsum += prices[userinput-1]
        continue


