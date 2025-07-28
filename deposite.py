import pandas as pd
import os

def deposit_money():
    file_path = "data.csv"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("❌ Data file not found.")
        return

    # Load the CSV data
    data = pd.read_csv(file_path)

    try:
        ac = int(input("🔢 Enter your account number: "))
        
        if ac in data["account"].astype(int).values:
            index = data[data["account"].astype(int) == ac].index[0]
            m = int(input("📱 Enter registered mobile number: "))

            if m == int(data.loc[index, "mobile"]):
                deposit = float(input("💰 Enter amount to deposit: "))
                if deposit <= 0:
                    print("❌ Deposit amount must be greater than 0.")
                    return

                # Add to balance
                data.loc[index, "amount"] += deposit
                data.to_csv(file_path, index=False)
                print(f"✅ ₹{deposit} deposited successfully.")
                print(f"📊 New Balance: ₹{data.loc[index, 'amount']}")
            else:
                print("❌ Mobile number does not match.")
        else:
            print("❌ Account number not found.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")



