#List of objects 

class Person:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
        
p1 = Person('Nitish', 'male')
p2 = Person('ankit', 'male')
p3 = Person('kjdn', 'female')

L = [p1,p2,p3] #if we print it we get the address of the elements

for i in L:
    print(i.name, i.gender)
