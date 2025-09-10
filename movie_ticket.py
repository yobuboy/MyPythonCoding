stud = input("Welcome to the movie theater!!\nAre you a student? (yes/no): ").lower().strip()
if stud == 'yes':
    age = eval(input("How old are you? : "))
    if age >= 1 and age < 13:
        print("Sorry, This age is not eligible for a student discount!!")
    elif age >= 13 and age <= 17:
        kal = eval(input("You are eligible for a student discount\nThe ticket price is $10!\nHow manny of these would you like to get? : "))
        total = 10 * kal
        disc = 2 * kal
        distotal = total - disc
        print("Here are the", kal, "ticket that you needed!\nThe original price is", total, "dollars\nNow, The total price is", distotal, "dollars")
    elif age >= 18 and age <= 25:
        kal = eval(input("You are eligible for a student discount\nThe ticket price is $10!\nHow manny of these would you like to get? : "))
        total = 12 * kal
        disc = 2 * kal
        distotal = total - disc
        print("Here are the", kal, "ticket that you needed!\nThe original price is", total, "dollars\nNow, The total price is", distotal, "dollars")
    elif age >= 26:
        print("Sorry, This age is not eligible for a student discount!!")
    else:
        print("Sorry I cant understand what you are talking about!!")
elif stud == 'no':
    age = eval(input("How old are you? : "))
    if age >= 1 and age < 5:
        kal = eval(input("The ticket price is free\nHow manny of these would you like to get? : "))
        if kal > 0:
            print("These are the", kal, "ticket that you are needed")
    elif age >= 5 and age <= 12:
        kal = eval(input("The ticket price is $8!\nHow manny of these would you like to get? : "))
        print("Here are the", kal, "ticket that you needed!\nThe total price will be",8 * kal, "dollars")
    elif age >= 13 and age <= 17:
        kal = eval(input("The ticket price is $10!\nHow manny of these would you like to get? : "))
        print("Here are the", kal, "ticket that you needed!\nThe total price will be",10 * kal, "dollars")
    elif age >= 18 and age <= 59:
        kal = eval(input("The ticket price is $12!\nHow manny of these would you like to get? : "))
        print("Here are the", kal, "ticket that you needed!\nThe total price will be",12 * kal, "dollars")
    elif age >= 60:
        kal = eval(input("The ticket price is $7!\nHow manny of these would you like to get? : "))
        print("Here are the", kal, "ticket that you needed!\nThe total price will be",7 * kal, "dollars")
    else:
        print("Sorry I cant understand what you are talking about!!")
else:
    print("Sorry I cant understand what you are talking about!!")