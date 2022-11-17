

print()
bank_accounts_list = []
balances_list =[]
account_name = ""
total = 0
print("Enter the names and balances of bank accounts (type: quit when done)")

while account_name!= "quit":
    account_name = input("What is the name of this account? ")
    if account_name!= "quit":
        balance = float(input("What is the balance? "))
        bank_accounts_list.append(account_name)
        balances_list.append(balance)
print()
print("Account Information: ")
num_elements = len(bank_accounts_list)
for i in range(num_elements):
    print(f"{bank_accounts_list[i]} - ${balances_list[i]}")
    total += balances_list[i]

print()
print(f"Total: ${total}")
average = total/num_elements
print(f"Average: ${average:.2f}")