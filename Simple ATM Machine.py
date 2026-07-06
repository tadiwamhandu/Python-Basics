correct_pin = "1234"
balance = 5000

print("=== Welcome to ATM Machine ===")
pin = input("Enter your PIN: ")

if pin == correct_pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            deposit = float(input("Enter amount to deposit: "))
            balance += deposit
            print("Deposit successful.")
            print("New balance is:", balance)

        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Withdrawal successful.")
                print("Remaining balance is:", balance)
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")