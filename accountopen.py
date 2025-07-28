import pandas as pd
import os
import random

def open_account():
    # Check if the file exists
    file_path = "data.csv"
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
    else:
        # If file doesn't exist, create an empty DataFrame with correct columns
        data = pd.DataFrame(columns=["name", "account", "amount", "mobile"])

    print("\n=== Open New Bank Account ===")
    name = input("Enter full name: ")
    
    try:
        mobile = int(input("Enter 10-digit mobile number: "))
        amount = float(input("Enter initial deposit (min ₹500): "))

        if amount < 500:
            print("❌ Minimum deposit should be ₹500.")
            return

        # Generate a unique 10-digit account number
        while True:
            account = random.randint(10**9, 10**10 - 1)  # 10-digit number
            if account not in data["account"].astype(str).values:
                break

        # Append the new account info
        new_data = pd.DataFrame([[name, account, amount, mobile]], columns=data.columns)
        updated_data = pd.concat([data, new_data], ignore_index=True)

        # Save back to the CSV file
        updated_data.to_csv(file_path, index=False)

        print(f"✅ Account created successfully!\n🔢 Your Account Number is: {account}")

    except ValueError:
        print("❌ Invalid input. Please enter correct numeric values.")
