''' 
Week 2: More variables, input, and output
Sister Hansen
What kind of comment is this?
'''

# this is a line comments
print("hi")

#### variables (and good names)
# create a string variable
name ="hill"
print(name)
name = input("what's your name: ")
print("user's name is:", name)


# create an integer variable
number = 10
print(number)

# create a float variable
float_number = 10.5
print(float_number)

#### input
# get input from the user and store it in a variable
name= input("What's your name: ")

# get a number from the user (decide if you want to convert now or later)
age= int(input("Enter your age:"))
print(age)
print("your age in 10 years will be", age +10)

#### output and f-strings
# output all the variables with a single print statement
print("all of the variables: ",age, name, number, float_number)

# now use an f-string to output all the variables
print(f"All of the variable: name:{name.upper()}, age: {age}, number: {number}, float: {float_number:.5f}")

# output all the variables again, but use a string method on one 
# so that it prints in upper case, lower case, or title case





