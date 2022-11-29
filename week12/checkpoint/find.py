people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 9999
min_name = ""

for line in people:
    person_detail = line.split() 
    name = person_detail[0]
    age = int(person_detail[1])

    if age < min_age:
        min_age = age
        min_name = name

print()
print(f"{min_name} has the minimum age of {min_age}")
print()
    