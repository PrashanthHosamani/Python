
class Person:
    
    def __init__(self, input_name, input_country):
        self.name = input_name
        self.country = input_country
        
    def greet(self):
        if self.country == "India":
            print("Namaste", self.name)
        else:
            print("Hello", self.name)
        
P = Person("Nitish", "India")
P2 = Person("Pramod", "USA")
print(P.greet())
print(P2.greet())


#Referance variable 

class Person:
    
    def __init__(self):
        self.name = "nitish"
        self.gender = "male"
        
#Object as been created at some address but does not accssed through any variable
    """When we call an class obj has been created inside the memory"""

Person()
P = Person() #we are storing the obj as in reference variable P
