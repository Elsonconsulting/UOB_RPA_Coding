# Creating an array by capturing words from user

numFruit = int(input('how many fruit do you want to name?: '))

fruitName = []

for itt in range(numFruit):
    fruit = input(f'Enter fruit {itt+1}: ')
    fruitName.append(fruit)
    
print(fruitName)
