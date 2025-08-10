#instance varibale -> Instance variable is a special kind of varible, its value depends on object, in one varibale we can store different values depending on the objects
#For every object the value of instance variable is different

class Person:
    
    def __init__(self, input_name, input_country):
        self.name = input_name
        self.country = input_country
        
    
p1 = Person('Nitish', 'India')
p2 = Person("Marry", "Australia")

print(p2.name)


#static variable
#class ka variable
#defined inside the class