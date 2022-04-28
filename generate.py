import random

coin = random.choice(["Heads", "Tails"]) #choice func. can be called like from random import choice
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Jack", "Queen", "King", "Ace"]
print(random.shuffle(cards)) #shuffle just shuffles the list, returns None
print(cards)