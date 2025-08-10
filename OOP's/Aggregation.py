#Aggregation (Has a relationship) one class will a owner of another class which will be the property of owner 

#example
class Customer: #owner
    
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def print_address(self):
        print(self.address.city, self.address.pin, self.address.state)
        
class Address: #property
    
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state
        
add1 = Address('gurgaon', 122022, 'hariyana')

cust = Customer('Nitish', 'male', add1)
cust.print_address()

#we are performing aggregation we can not access the private variable even from property class for this we use getter 

"""With getter, because of private attributes or variables"""

class Customer: #owner
    
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)
        
class Address: #property
    
    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state
        
    def get_city(self):
        return self.__city
        
add1 = Address('gurgaon', 122022, 'hariyana')

cust = Customer('Nitish', 'male', add1)
cust.print_address()