import accountopen
import account_close
import balance
import deposite
import withdrawl

def main():
    while True:
        print("\n--- Welcome to Banking System ---")
        print("1. Open Account")
        print("2. Close Account")
        print("3. Check Balance")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            accountopen.open_account()
        elif choice == '2':
            account_close.close_account()
        elif choice == '3':
            balance.balance_check()
        elif choice == '4':
            deposite.deposit_money()
        elif choice == '5':
            withdrawl.withdraw()
        elif choice == '6':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 
