names = []
for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")

name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

"""with open("names.txt", "a") as file:
    file.write(f"{name}\n")"""

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line, end="") #instead of end="" line.rstrip() can be used


