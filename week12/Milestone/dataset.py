import csv
from os import system

country_name = 0
country_abreviation = 1
year = 2
expectancy = 3
expectancy_List = []
system("clear")

year_of_interest = int(input("Enter the year of interest: "))
country_of_interest = input("Enter the country of interest: ")

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

# elected year
total = 1
total_expectancy = 0
max_life_expect = 0
max_life_country = ""
min_life_expect = 1000
min_life_country = ""
# elected country
max_country_life_expect = 0
min_country_life_expect = 999

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

# year of interest
    if int(row[year]) == year_of_interest:
        total_expectancy += exp_curr
        total+=1
        if exp_curr > max_life_expect: 
          max_life_expect  = exp_curr
          max_life_country = row[country_name]
        if exp_curr < min_life_expect: 
          min_life_expect  = exp_curr
          min_life_country = row[country_name]
        
# country of interest

    if row[country_name] == country_of_interest:
        
        if exp_curr > max_country_life_expect: 
          max_country_life_expect  = exp_curr
          max_country_year = year_curr
        if exp_curr < min_country_life_expect: 
          min_country_life_expect  = exp_curr
          min_country_year = year_curr


  
print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")
print()

print(f"For the year {year_of_interest}:")
average_expectancy = total_expectancy/(total-1)
print(f"The average life expectancy across all countries was {average_expectancy:.2f}")
print(f"The max life expectancy was in {max_life_country} with {max_life_expect}")
print(f"The min life expectancy was in {min_life_country} with {min_life_expect}")
print()

print(f"For the country {country_of_interest}:")
print(f"The max life expectancy was {max_country_life_expect} in {max_country_year}")
print(f"The min life expectancy was {min_country_life_expect} in {min_country_year}")
print()