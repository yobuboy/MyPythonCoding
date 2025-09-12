ent = input("Enter Number: ")
if ent.isdigit():
    ent = int(ent)
    print(ent % 10)
else:
    print("Error")