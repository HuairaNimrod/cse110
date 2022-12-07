from math import pi
option = "none"

# def square(side):
#     return side**2

def rectangle(side1, side2):
    return side1*side2

def circle(radius):
    return pi*(radius**2)

def compute_area(shape, side):
    if shape =="square"


while option.lower() != "quit":
    print("what is the shape you want to calculate its area: ")
    print("a. square")
    print("b. rectangle")
    print("c. circle")
    option = input("Type your option: ")
    print()
    

    if option.lower() == "a":
        side = int(input("Enter the side value: "))
        area = rectangle(side, side)
        print(f"The area of the square is {area}")

    if option.lower() == "b":
        side1 = int(input("Enter the value of side 1: "))
        side2 = int(input("Enter the value of side 2: "))
        area = rectangle(side1, side2)
        print(f"The area of the square is {area}")

    if option.lower() == "c":
        radius = int(input("Enter the radius value: "))
        area = circle(radius)
        print(f"The area of the square is {area:.2f}")    
    
    print()
