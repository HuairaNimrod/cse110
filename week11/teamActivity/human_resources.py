name = 0
id_number = 1
job_title = 2
salary = 3
employee_List = []
print()
with open("hr_system.txt") as hr_file:
    for element in hr_file:
        employee = element.strip()
        employee_List.append(employee.split())
        print(employee.split())

    # for person in employee_List:
    #     paycheck = float(person[salary])/24
    #     if person[job_title] == "Engineer":
    #         paycheck += 1000 
    #     print(f"{person[name]} (ID:{person[id_number]}), {person[job_title]} - ${paycheck:.2f}")
print()