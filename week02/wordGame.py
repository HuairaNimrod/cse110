#program that create a text based in the inputs received


print("please enter the following:")
print()
adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation= input("exclamation: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
noun = input("noun: ")
adjective2 = input("adjective: ")

first_char=noun[0].lower()
#one way to do the  or logical comparison
#if first_char=='a' or first_char=='e' or first_char=='i' or first_char=='o' or first_char=='u': 
if first_char in ("a", "e", "i", "o", "u"):
    aoran="an"
else:
    aoran="a"


print(f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do was to {verb1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2} right in front of my family.")
print(f"After that experience, I got hunger so I decided to {verb3} {aoran} {noun}, and I headed home. It was a {adjective2} day.")
