from math import sin, cos
print("Calculator")
status = True
user_selection1 = int(input("Give the first number: "))
user_selection2 = int(input("Give the second number: "))
while status:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5)sin(number1/number2)")
    print("(6)cos(number1/number2)")
    print("(7)Change numbers")
    print("(8)Quit")
    print("Current numbers: ", user_selection1, user_selection2)
    user_selection3 = int(input("Please select something (1-6): "))
    if user_selection3 < 0 or user_selection3 > 8:
        print("Selection was not correct.")
    elif user_selection3 == 1:
        print("The result is: ", (user_selection1 + user_selection2))
    elif user_selection3 == 2:
        print("The result is: ", (user_selection1 - user_selection2))              
    elif user_selection3 == 3:
        print("The result is: ", (user_selection1 * user_selection2))
    elif user_selection3 == 4:
        print("The result is: ", (user_selection1 / user_selection2))
    elif user_selection3 == 5:
        print("The result is: ", (sin(user_selection1 / user_selection2)))
    elif user_selection3 == 6:
        print("The result is: ", (cos(user_selection1 / user_selection2)))
    elif user_selection3 == 7:
        user_selection1 = int(input("Give the first number: "))
        user_selection2 = int(input("Give the second number: "))
    elif user_selection3 == 8:
        print("Thank you!")
        status = False
      
    