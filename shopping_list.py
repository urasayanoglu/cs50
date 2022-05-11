import sys
status = True
shopping_list = []
while status:
    print("Would you like to")
    print("(1)Add or")
    print("(2)Remove items or")
    userinput = int(input("(3)Quit?: "))
    if userinput == 3:
        print("The following items remain in the list:")
        for item in shopping_list:
            print(item)
        status = False
        sys.exit()
    elif userinput <= 0 or userinput > 3:
        print("Incorrect selection.")
        continue
    elif userinput == 1:
        added_items = input("What will be added?: ")
        shopping_list.append(added_items)
    elif userinput == 2:
        print(f"There are {len(shopping_list)} items in the list.")
        deleted_item = int(input("Which item is deleted?: "))
        if deleted_item < 0 or deleted_item > (len(shopping_list) - 1):
            print("Incorrect selection.")
            continue
        else:
            shopping_list.pop(deleted_item)
    


