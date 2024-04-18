# Guess number

import random


guess = input("Guess which number I'm thinking off 1-10: ")
player_guess = int(guess)
num = random.randint(1, 10)
if player_guess < num:
    print("too low")
elif player_guess > num:
    print("too high")
else:
    print("Spot On!!")

