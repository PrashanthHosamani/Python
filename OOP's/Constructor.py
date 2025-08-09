#Magic method 

#constructor is used to write configuration realted code
#we write all the code in constructor which is not accessed or asked to the user before executing  EX: conneting the application to database, internet, cloud etc
# not leaving the control in the hand of user 
#automatically executated or triggered when the object of the class created 

class Car:
    
    def __init__(self): #constructor
        self.wheel = ''

