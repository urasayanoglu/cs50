import sys

def greeting_user(name="User"):
    try:
        print(f"Hello, my name is {name}", sys.argv[1])
    except IndexError:
        print("Too few arguements")

greeting_user("Uras")


