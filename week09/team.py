numberlist=[]
has_zero=True
while has_zero:
    number = int(input("enter number: "))
    numberlist.append(number)
    if number == 0:
        has_zero = False
        
for i in numberlist:
    print(i, end=" ")
print()

# average
sum=0
total =0
for i in numberlist:
    sum = sum + i
    total +=1
average  = sum/total
print(f"sum: {sum}")
print(f"average: {average}")
print(f"numbers: {total}")
