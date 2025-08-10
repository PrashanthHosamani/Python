# Pascal Case (HelloWorld) (MyAtm)

class Atm:
    
    #constructor (Special function) -> superpower ->
    def __init__(self): #self -> obj, through the obj we talk with functions and all (calling) independent parameter
        # print(id(self))
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit 
        """)
        
        if user_input == '1':
            self.create_pin()
            #create pin
        elif user_input == '2':
            self.change_pin()
            #change pin
        elif user_input == '3':
            self.check_balance()
            #check balance
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
            
    def create_pin(self):
        user_pin = input("enter your pin: ")
        self.pin = user_pin
            
        user_balance = int(input('enter the balance: '))
        self.balance = user_balance
            
        print("pin created successfully!")
        self.menu()
        
    def change_pin(self):
        previous_pin = input("Enter old pin: ")
        
        if previous_pin == self.pin:
            #let change the pin
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("pin change successfully!")
            self.menu()
        else:
            print("Wrong pin")
            self.menu()
            
    def check_balance(self):
        user_pin = input("Enter the pin: ")
        if user_pin == self.pin:
            print("your balance is ", self.balance)
        else:
            print("wrong pin")
            self.menu()
            
    def withdraw(self):
        user_pin = input("Enter the pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("withdrawl successful, collect your amount")
                user = int(input("press 0 to go back to menu: "))
                if user == 0:
                    self.menu()
                else:
                    pass
            else:
                print("Not enough balance")
                self.menu()
        else:
            print("wrong pin, please try again")
            self.menu()
            
            
obj = Atm()
# print(id(obj))

#self is a deafult argument and it is obj itself (in a class only obj can access each and everything hence)
