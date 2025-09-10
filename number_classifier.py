done = int(input("Welcome, This is Number Classifier!!\nEnter a number --> "))
if done < 0 and done % 2 == 0:
    print("Negative Even")
elif done > 0 and done % 2 == 0:
    print("Positive Even")
elif done < 0 and done % 2 == 1:
    print("Negative Odd")
elif done > 0 and done % 2 == 1:
    print("Positive Odd")
else:
    print("Zero")