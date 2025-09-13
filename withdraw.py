balance = int(input("Enter account balance: "))
withd = int(input("Enter withdraw amount: "))
if withd // 100 and withd % 100 == 0:
    amount = balance - withd
    total_bal = amount - 15
    print("Transaction successful. $",withd + 15,"deducted ($15 fee included).")
    if withd > 20000:
        print("Daily withdraw limit exceed")
    elif total_bal < 1000:
        print("Remaining Balance: $",total_bal,"(Warning:Low balance)")
    elif balance == withd:
        print("Sorry, the withdrawal cannot be proceed due to lack of $15 fee!")
    elif balance <= 115:
        print("Sorry, Your", balance,"balance is not enough to support your withdrawal!")
    else:
        print("Remaining Balance: $",total_bal)
elif withd > balance:
    print("Insuficient Funds")
else:
    print("This withdraw amount cannot be proceed, It should be divident with 100.")