print()
shopping_list = []
print("Please enter the items of the shopping_list list (type quit to finish): ")
item = input("Item: ")
while item != "quit":
    shopping_list.append(item)
    item = input("Item: ")

print()
print("The shopping_list list is: ")
for i in shopping_list:
    print(i)

print()
print("The shopping_list list with index is: ")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")


print()
indexChange = int(input(("Which item would you like to change?: ")))
itemToChange = input("What is the new item? ")

shopping_list[indexChange] = itemToChange

print()
print("The shopping_list list is: ")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")