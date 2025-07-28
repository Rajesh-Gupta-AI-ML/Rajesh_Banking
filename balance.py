import pandas as pd
def balance_check():
    data=pd.read_csv("data.csv")
    ac=int(input("Enter account number:- "))
    if(ac in list(data["account"])):
        ind=list(data["account"]).index(ac)
        m=int(input("Enter mobile number:- "))
        if(m==data["mobile"][ind]):
            print("account balance: ", data["amount"][ind])
        else:
            print("mobile number in invalid")
    else:
        print("account invalid")  
            




        