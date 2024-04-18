# if_statements embedded in for loop
actual_number = 5
 
 
max_guess = 5
 
 
for loop in range(max_guess):
    guess = int(input("Guess the number between 1 - 10: "))
    if guess == actual_number:
        print("bang on")
        break
    if guess <actual_number:
        print("more fool")
    if guess >actual_number:
        print("less fool")