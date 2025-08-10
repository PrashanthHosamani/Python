class Person:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
        
# outside the class -> so it is function not a method
def greet(self):
    print('Hi my name is', self.name, 'and I am a', self.gender)
    p1 = Person('ankit', 'male')
    return(p1)
    
p = Person("nitish", "male")
greet(p)
x = greet(p)
print(x.gender)