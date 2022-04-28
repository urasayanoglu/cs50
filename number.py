from cmd import PROMPT


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("The value you put for x is not an integer. ") #pass statement could be used instead of printing a statement about the exception

main()