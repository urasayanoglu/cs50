from sys import exit

def tester(givenstring="Too short"):
    if givenstring == "quit":
        exit()
    elif "X" in givenstring and len(givenstring) >= 10:
        print(givenstring)
        print("X spotted!")
        return True
    elif len(givenstring) >= 10:
        print(givenstring)
    elif len(givenstring) < 10:
        print("Too short")
def main():
    userinput = input("Write something (quit ends): ")
    tester(userinput)
while True:
    if __name__ == "__main__":
        main()

phrase = "Is Xavier here"
if "X" in phrase:
    print("X spotted!")


	