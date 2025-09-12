print("Welcome to the Insurance Company, If you are looking for Car Insurance, You must required these following!\n-Age must be at least 18.\n-Must have a driver's licence.\n-Must have no more than 1 accident in the past 3 years")
drive =  int(input("How old are you? : "))
if drive >= 18:
    licence = input("Do you have driver's licence? (Yes/No)").lower()
    if licence == 'yes':
        accident = eval(input("How many accidents do you have in the past 3 years? (Only number is applicable) : "))
        if accident > 1:
            print("Due to an inappropriate diving that cause an accident, You are not eligible to have car insurance!!")
        else:
            print("Congratulations, You pass the requiremets to have a car insurance!\nYou are now have a car insurance!!")
    else:
        print("Due to lack of driver's licence, You are not eligible to have car insurance!!")
else:
    print("Due to under age, You are not eligible to have car insurance!!")