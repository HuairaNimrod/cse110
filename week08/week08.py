# 1) loop to print 1 through 5 (using a range)

for i in range(5):
    print(i)


# 2) loop to print "Hello World" a user specified number of times
print()
num_print = int(input("How many times?"))
for i in range(num_print):
    print("Hello world")



# 3) loop to print each letter in a string (three ways)
print()
my_string = "Hello World"

for index in range(len(my_string)):
    print(my_string[index])

for index in range(len(my_string)):
    print(my_string[index], end = " ")


# 4) loop to print each item in a list
print()
my_list = [1,3,5,7,9]

for i in my_list:
    print(i)


# team activity - looping through strings 

# stretch
first_name = "Brigham"
last_name = "Younger"

# use range and len to loop through the string
for i in range(len(first_name)):
    print(f"The letter {first_name[i]} is at position {i} in the first name")
    print(f"The letter {last_name[i]} is at position {i} in the last name")
    # we could also use if statements to check if the letters are the same