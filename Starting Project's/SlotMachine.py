def deposite():
    while True:
        amount = input("what would you like to deposite? $: ")
        if amount.isdigit():           
            amount = int(amount)
            if amount > 0:
                 break
            else:
                 print("Amount must be greater than 0.")
        else:
            print("please enter the number")
    return amount

def main():
    balance = deposite()
    
def checkbalance():
    checkbalance = deposite
    check_balance = input("wanna see your balance?: ")
    if check_balance == "yes".lower():
        return main()
 
checkbalance()
    
    
    



     
            

     
    