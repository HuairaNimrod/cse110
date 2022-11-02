import os

print()    

child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))


subtotal = child_price*children + adult_price*adults
sales_tax = tax*subtotal/100
total = subtotal+sales_tax

print()
print("-"*30)
print("RECEIPT")
print("-"*30)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

# Show the customer a suggested tip and ask him if he want to tip
print(f"\nSuggested tip: ${0.15*total:.2f}")
print("-"*30)
print()
want_tip = input("Would you like to tip? (y/n) ")

if want_tip.lower()== "y":
    tip = float(input("Enter tip: "))
    total = tip + total

payment = float(input("What is the payment amount? "))
change = payment - total
print()
print("*"*30)
print(f"Total after tip: ${total:.2f}")
print(f"Change: ${change:.2f}")
print("*"*30)
print()
