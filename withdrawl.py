import pandas as pd

def withdraw():
    # Read CSV
    data = pd.read_csv("data.csv")

    # Get user input
    ac = int(input("Enter account number: "))
    
    if ac in data['account'].values:
        ind = data.index[data['account'] == ac][0]
        m = int(input("Enter mobile number: "))
        
        if m == data.at[ind, 'mobile']:
            print("Current Balance:", data.at[ind, 'amount'])
            amt = int(input("Enter withdrawal amount: "))
            
            if amt <= data.at[ind, 'amount']:
                data.at[ind, 'amount'] -= amt
                print("Withdrawal successful. New Balance:", data.at[ind, 'amount'])
                data.to_csv("data.csv", index=False)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid mobile number.")
    else:
        print("Account not found.")

# Call function

