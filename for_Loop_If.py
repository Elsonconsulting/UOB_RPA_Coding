# Guess number

import random

attempts = 5

print(f'You have {attempts} to guess the number I am thinking of')

num = random.randint(1, 10)

for guesses in range(1, attempts):
    guess = input("Guess which number I'm thinking off 1-10: ")
    player_guess = int(guess)
    
    if player_guess == num:
        print(f"{num} is spot On!!")
        break
    else:
        if player_guess < num:
            print(f"{player_guess} is too low, hint number is {num}")
        if player_guess > num:
            print(f"{player_guess} is too high, hint number is {num}")
    
