secret_word="mosiah"
attempts = 1
print("")
print("Welcome to the word guessing game!")
word_guess = input("What is your guess? ") 


while secret_word!=word_guess: 
    print("Your guess was not correct.")
    word_guess = input("What is your guess? ") 
    attempts+=1

print("Congratulations! You guessed it!")
print(f"It took you {attempts} guesses.")
