import os
os.system('clear')
print()
replay = True
while replay == True:
    print("Your mom is sick first you need to go to the pharmacy to pick up some medicines")
    print("Is your first time leaving home alone, choose how will you fo the pharmacy?")
    print("WALK")
    print("BIKE")
    print("CAR")
    choice_1 = input("type choice:  ")
    os.system('clear')
    if choice_1.lower() == "walk":
        print("You begin to walk to go to the pharmacy")
        print("You see a dog ahead, would you want to change sidewalk or keep walking?")
        print("KEEP")
        print("CHANGE")
        choice_2a = input("type choice: ")
        os.system('clear')
        if choice_2a.lower() == "keep":
            print("the dogs barks you and scares you, you decided to change your sidewalk to avoid being bite")
            print("After walking for some minutes, you arrive to the pharmacy. The Chashier ask your your type of payment:")
            print("CASH")
            print("CARD")
            choice_3a = input("type choice: ")
            os.system('clear')
            if choice_3a.lower() == "cash" or choice_3a.lower() == "card":
                print("You got the medicine!! you found a frieNd in the line before you paid and He offered you a ride to your home")
                print("You're Mom gets better! :)")
                replay = False
            else:
                print("You noticed that you don't have a payment method, You decided going back home and come back to the pharmacy")
                replay = True

        elif choice_2a.lower() == "change":
            print("You avoid the dog and are on your way to the Pharmacy") 
            print("When you cross the street you heard someone saying your name")
            print("It's your friend in his car and He mentioned you that he is going to the Pharmacy. You enter to his car")
            print("When you arrive to the pharmacy. The Chashier ask your your type of payment:")
            print("CASH")
            print("CARD")
            choice_3a = input("type choice: ")
            os.system('clear')
            if choice_3a.lower() == "cash" or choice_3a.lower() == "card":
                print("You got the medicine!! Your friend also offered you a ride to your home")
                print("You're Mom take the medice. After some hours she feels better! :)")
                replay = False
            else:
                print("You noticed that you don't have a payment method, You decided going back home, but your friend helps you.")
                print("You're back home")
                print("You're Mom take the medice. After some hours she feels better! :)")
                replay = False

        else:
            print("You are so scared for the dog, so You decided to go back home")
            print()
            print("Do you want to try again?")
            print("TRUE")
            print("FALSE")
            input_replay= input("answer: ")
            if input_replay.lower() == "true":
                replay = True
            else: 
                replay = False


    elif choice_1.lower() == "bike":
        print("You are heding to the Pharmacy in your bike")
        print("you see a dog ahead, do you want turn away and go fo the other route?")
        print("KEEP")
        print("TURN")
        choice_2a = input("type choice: ")
        os.system('clear')
        if choice_2a.lower() == "keep":
            print("the dog scares you, you fell from your bike the dog bites you ")
            print("The pain in more than you can tolerate, and Ambulance is coming to assist you")
            print("The owner of the Dog offers you his help")
            print("ACCEPT")
            print("DECLINE")
            choice_3a = input("type choice: ")
            os.system('clear')
            if choice_3a.lower() == "accept":
                print("The owner of the dog goes to buy your Mom's medicine. He also brings you to Home")
                print("You're Mom gets better with the medicine. You learn that you must be aware of dogs")
                replay = False
            elif choice_3a.lower() == "decline":
                print("You cannot continue your travel to the pharmacy. The ambulance brings you to Home")
                print("You need to rest")
                print("Your Father arrives home, and he goes to buy medicine for you and for your mother.")
                print("After taking the medicine, you and your Mon feel better.")
                replay = False
            else:
                print("You're confused, some people decided to bring you home, and  help you with your Mom's medicine.")
                print("You're mom take her medicine, after some hours she felts better and takes care of your wound.")
                replay = False

        elif choice_2a.lower() == "turn":
            print("You avoid the dog and are on your way to the Pharmacy") 
            print("When you arrive to the pharmacy. The Chashier ask your your type of payment:")
            print("CASH")
            print("CARD")
            choice_3a = input("type choice: ")
            os.system('clear')
            if choice_3a.lower() == "cash" or choice_3a.lower() == "card":
                print("You got the medicine!! you go as fast as you can to your home")
                print("You're Mom gets better! :)")
                replay = False
            else:
                print("You noticed that you don't have a payment method, You decided going back home and come back to the pharmacy")
                replay = True

        else:
            print("You are so scared for the dog, so You decided to go back home")
            print()
            print("Do you want to try again?")
            print("TRUE")
            print("FALSE")
            input_replay= input("answer: ")
            if input_replay.lower() == "true":
                replay = True
            else: 
                replay = False

    elif choice_1.lower() == "car":
        os.system('clear')
        print("You don't know how to drive, you must decide betweet going in your bike or by walk.") 
        replay = False
    else:
        os.system('clear')
        print("You decided to remain at home and ask the medicine by Doordash")
        print()
        print("Do you want to try again?")
        print("TRUE")
        print("FALSE")
        input_replay= input("answer: ")
        if input_replay.lower() == "true":
            replay = True
        else: 
            replay = False
        
print()




