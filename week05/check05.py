animal = "dog"
print()
first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if first_number>second_number:
    print(f"The first number is greater")
    print(f"The numbers are not equal")
    print(f"The second number is not greater")

elif first_number == second_number:
    print(f"The first number is not greater")
    print(f"The numbers are equal")
    print(f"The second number is not greater")
else:
    print(f"The first number is not greater")
    print(f"The numbers are not equal")
    print(f"The second number is greater")
print()
fav_animal = input("What is your favorite animal? ")
if fav_animal.lower == animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
    