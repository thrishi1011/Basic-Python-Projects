# BANK OF PYTHON

bal = 100
def balance():
    print(f"Your current balance is {bal}")
def deposite():
    deposite_amount = int(input("How much amount do you want to deposite: "))
    if deposite_amount < 0:
        print("That is not a vaild amount")
    else:
        return deposite_amount
def withdraw():
    withdraw_amount = int(input("How numch amount do you want to withdraw: "))
    if withdraw_amount > bal:
        print('Insufficent amount')
    else:
        return withdraw_amount

while True:
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        balance()
    elif choice == '2':
        bal += deposite()
        print("Your new balance is", bal)
    elif choice == '3':
        bal -= withdraw()
        print("Your new balance is", bal)
    elif choice == '4':
        break
    else:
        print('Invalid number')

# End of the bank of python

