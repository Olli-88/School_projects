# Account manager with menu:
# User can make deposits
# Do withdrawal
# Check the balance

sum = 0
menu = 0

while menu != 4:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")
    menu = int(input("\n(1-4):"))
    # Deposit
    if menu == 1:
        sum = sum + float(input("Give amount you want to deposit: "))
    # Withdrawal
    if menu == 2:
        withdraw = float(input("Give amount you want to withdraw: "))
        if withdraw > sum:
            print("Not enough balance on your account!")
            input("press enter to continue")
        else:
            sum = sum - withdraw
    # Balance
    if menu == 3:
        print(sum)
        input("Press enter to continue")