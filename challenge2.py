ent = input("Enter Number: ")
if ent.isdigit():#(.isdigit) Declare's that the text is int, not a str.
    ent = int(ent)
    print(ent % 10)
else:
    print("Error")

