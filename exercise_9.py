# Exercise 9

import random as ran
num = int(input("Enter a number: "))
rn = ran.randint(1,9)
while True:
    if num > rn:
        num = int(input("Too high! Try again: "))
    elif num < rn: 
        num = int(input("Too low! Try again: "))
    else:
        print("Congratulations, you guessed the number!")
        break
