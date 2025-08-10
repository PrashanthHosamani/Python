#Used to call the parent class attributes or method despite having constructor and method in the child class 
class Phone:
    def __init__(self, price, brand, camera):
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("buying the mobile")
        
class Smartphone(Phone):
    def buy(self):
        print("buying a smartphone")
        #sytanx to call parent ka buy method (using super keyword)
        super().buy() 

s = Smartphone("2000", "apple", "20PX")
s.buy()      


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price #Private
        self.brand = brand
        self.camera = camera
        
class Smartphone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print("Inside smartphone construtor")
        #sytanx to call parent ka buy method (using super keyword)
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram

s = Smartphone("2000", "apple", "20PX", "android", 2)
print(s.os)
print(s.brand)


#we can not use super keyword outside the child class at all