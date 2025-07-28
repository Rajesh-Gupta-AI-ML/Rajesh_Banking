import pandas as pd
import os

def close_account():
    file_path = "data.csv"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("❌ No data file found.")
        return

    # Load the data
    data = pd.read_csv(file_path)

    try:
        ac = int(input("🔢 Enter account number to close: "))

        # Check if account exists
        if ac in data["account"].astype(int).values:
            index = data[data["account"].astype(int) == ac].index[0]
            m = int(input("📱 Enter registered mobile number: "))

            # Match mobile number
            if m == int(data.loc[index, "mobile"]):
                confirm = input("⚠️ Are you sure you want to close the account? (yes/no): ").lower()
                if confirm == "yes":
                    data.drop(index, inplace=True)
                    data.to_csv(file_path, index=False)
                    print("✅ Account closed successfully.")
                else:
                    print("ℹ️ Account closure cancelled.")
            else:
                print("❌ Incorrect mobile number.")
        else:
            print("❌ Account number not found.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")



