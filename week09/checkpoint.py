
friends_list = []
do_loop = True

while do_loop:
    friend = input("Type the name of a friend: ")
    if(friend.lower()!= "end"):
        friends_list.append(friend)
    else:
        do_loop = False

print()
print("Your friends are: ")
for i in friends_list:
    print(i)
