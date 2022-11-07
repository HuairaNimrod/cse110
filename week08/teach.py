print()

word = "Commitment"
favorite_letter = input("enter your favorite letter: ")
for i, letter in enumerate(word):
    if letter == favorite_letter:
        print("_", end="")
    else:
        letter = letter.lower()
        print(letter.lower(),end="")
print()

