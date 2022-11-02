print()
age = int(input("What is the age of the first rider? "))
height = int(input("What is the height of the first rider? "))
rider = input("is there a second rider (yes/no)? ")

if rider == "yes":
    age2 = int(input("What is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider? "))

if height<36 :
    accept= False
else: 
    # single
    if rider.lower() == "no":
        if age >=18 and height >=62:
            accept= True
        else:
            accept = False
    # second rider 
    elif rider.lower() == "yes":
        if (age >=18 or age2>=18):
            accept= True
    else:
        accept = False




if accept:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")