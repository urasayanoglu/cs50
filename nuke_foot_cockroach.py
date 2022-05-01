import random, sys

nuke_foot_cockroach = {1: "foot", 2: "nuke", 3:"cockroach"} 

user = 0
computer = 0
tie = 0
rounds = 0
status = True

def main():
    who_wins()
    print(f"You played {rounds} rounds, and won {user} rounds, playing tie in {tie} rounds.")

def who_wins():
    global user
    global computer
    global tie
    global rounds
    if userselection == "quit":
        status = False
    elif userselection not in nuke_foot_cockroach.values():
        print("Incorrect selection.")
    elif userselection == "nuke" and nuke_foot_cockroach[computerselection] == "nuke":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("Both LOSE!")
    elif userselection == nuke_foot_cockroach[computerselection]:
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("It is a tie!")
        tie = tie + 1
        rounds = rounds + 1
    elif userselection == "foot" and nuke_foot_cockroach[computerselection] == "nuke":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("You LOSE!")
        computer = computer + 1
        rounds = rounds + 1
    elif userselection == "foot" and nuke_foot_cockroach[computerselection] == "cockroach":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("You WIN!")
        user = user + 1
        rounds = rounds + 1
    elif userselection == "nuke" and nuke_foot_cockroach[computerselection] == "foot":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("You WIN!")
        user = user + 1
        rounds = rounds + 1
    elif userselection == "nuke" and nuke_foot_cockroach[computerselection] == "cockroach":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("You LOSE!")
        computer = computer + 1
        rounds = rounds + 1
    elif userselection == "cockroach" and nuke_foot_cockroach[computerselection] == "foot":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("You LOSE!")
        computer = computer + 1
        rounds = rounds + 1
    elif userselection == "cockroach" and nuke_foot_cockroach[computerselection] == "nuke":
        print(f"You chose: {userselection}")
        print(f"Computer chose: {nuke_foot_cockroach[computerselection]}")
        print("You WIN!")
        user = user + 1
        rounds = rounds + 1

while status:
    userselection = input("Foot, Nuke or Cockroach? (Quit ends): ").lower()
    if userselection == "quit":
        status = False
        main()
        sys.exit
    computerselection = random.randint(1,3)
    who_wins()
    




    










