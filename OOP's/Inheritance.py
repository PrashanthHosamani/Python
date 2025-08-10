# A class (child class) can aquire the properties and behaviour (attributes and methods) of another class (parent class)
#benefits : Code resuability

#constructor example (if there is not constructor with child class than parent class constructor will be called)

class Phone:
    
    def __init__(self, price, brand, camera):
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("buying the mobile")
    
    #getter
    def show(self):
        print (self.__price)
        
class Smartphone(Phone):
    pass

s = Smartphone("2000", "apple", "20PX")
s.buy()       

#child can not access the private attribute of the parent

#s.price (Error)
print(s.brand)
s.show()


#Method Overriding

#if we have same (name of the method) method in both the classes (parent and child) than child class method will be called, as same in with constructor so which is why that is constructor overriding
        

 
        
    
        