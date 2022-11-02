print()
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
phone_number = input("What is your phone number? ")
job_title = input("What is your first job title? ")
id_number = input("What is your ID number? ")

#extra
hair = input("Enter hair color:")
eyes = input("Enter eyes color:  ")
month = input("enter month started: ")
training = input("training was finished: ")


# print part
print()
print("The ID card is:")
print ("-"* 20)
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone_number)
print ("-"* 20)

# extra
print(f"Hair:{hair:15} Eyes:{eyes}")
print(f"Month:{month:14} trainig:{training}")