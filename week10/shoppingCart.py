import os

cart = []
price_list = []
action = -1

print()
print("Welcome to the Shopping Cart Program")
while action != "5":
    print()
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ")
    os.system("clear")
    if action=="1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of {item}: "))
        cart.append(item)
        price_list.append(price)
        print(f"{item} has been added to the cart.")

    elif action == "2":
        print(f"The contents of the shopping cart are:")
        for i, item in  enumerate(price_list):
            i+=1
            print(f"{i}. {cart[i-1]:<20}  ${item:>6.1f}")
            
    elif action == "3":
        remove_index = int(input("Which item would you like to remove? "))
        remove_index-=1
        # pop() removes the last element if an index is not provided
        cart.pop(remove_index)
        price_list.pop(remove_index)
        print("Item removed")

    elif action == "4":
        total = 0
        for i, item in  enumerate(price_list):
            total += price_list[i]
        print(f"The total price of the items in the shopping cart is {total}")

    elif action == "5":
        print("Thank you, Goddbye.")
    
