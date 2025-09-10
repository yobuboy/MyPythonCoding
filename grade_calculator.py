grade = eval(input("Welcome to the Grade Calculator!, This program will calculate if your general average is belong to this grade level indication: (A,B,C,D,F)\nNow lets proceed, Enter yor general average: "))
if grade >= 90 and grade <= 100:
    print("Congratulations, Your grade level is A")
elif grade >= 80 and grade <= 89:
    print("Congratulations, Your grade level is B")
elif grade >= 70 and grade <= 79:
    print("Very Good, Your grade level is C")
elif grade >= 60 and grade <= 69:
    print("Nice Try, Your grade level is B")
elif grade < 60:
    print("Sad to say but your grade level is F\nAt this rate, You fail as a student\nBetter Luck Next Time!!!")
else:
    print("Error Calculation, Only numbers will be accepted in this program")