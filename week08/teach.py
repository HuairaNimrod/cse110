print()

word = "Commitment"
favorite_letter = input("enter your favorite letter: ")
for i in word:
    if i == favorite_letter:
        # print(i.upper(),end="")
        print("_", end="")
    else:
        i = i.lower()
        print(i.lower(),end="")
print()

