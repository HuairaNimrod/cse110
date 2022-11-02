import random
import os
i=0
number = random.randint(1, 10)
os.system("clear")
print(number)
not_match = True
while not_match :
    i += 1
    guess = int(input("What is your guess? "))
    if number == guess:
        print("Match!!!")
        not_match= False
    elif guess < number:
        print("Higher")
    else:
        print("Lower")

print(f"the number was {number}")
print(f"guesses:{i} ")