#Function for Greeting the User
def main():
    name = input("What is your name? ")
    hello(name)
    
def hello(to="World"):
    return f"Hello, {to}."

if __name__ == "__main__":
    main()