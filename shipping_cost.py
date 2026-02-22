cost = eval(input("Welcome to the Shipping Cost Calcutor!!\nWhat is the total weight of the package in kg? : "))
if cost < 0.000001:
    print("Invalid weight!!\nThis weight is not valid for transfer")
elif cost >= 0.000001 and cost <= 5:
    print("The total cost of your package is $5")
elif cost >5 and cost <= 20:
    print("The total cost of your package is $10")
else:
    print("Cannot ship!!\nThis weight is to heavy to tranfer!!")
