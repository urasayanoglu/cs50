def main():
    x = int(input("Type your first number to check for parity. "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return  n % 2 == 0 
    
main()