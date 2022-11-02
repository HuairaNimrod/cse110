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
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

print()
payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")
print()
