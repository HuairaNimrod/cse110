import csv

country_name = 0
country_abreviation = 1
year = 2
expectancy = 3
expectancy_List = []

print()
with open("life-expectancy.csv") as csv_file:
    next(csv_file)
    expectancy_csv = csv.reader(csv_file, delimiter=",")
    for row in expectancy_csv:
        # row = float(row[expectancy])
        expectancy_List.append(row)
        # print(row)



# year_interest = print("Enter the year of interest: ")
max_life = 0
min_life = 100

for row in expectancy_List:
    exp_curr = float(row[expectancy])
    country_curr = row[country_name]
    year_curr = row[year]

    if exp_curr > max_life:
        max_life = exp_curr
        max_country = country_curr
        max_year = year_curr
    
    if exp_curr < min_life:
        min_life = exp_curr
        min_country = country_curr
        min_year = year_curr

  
print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

print()
