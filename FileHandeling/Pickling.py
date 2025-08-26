#Pickling is the process whereby a python object hierarchy is converted into a byte stream, and 
# unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes like object) is converted back to a object hierarchy

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        def display_info(self):
            print('Hi My name is', self.name, 'and I am', self.age, 'year old')
            
p = Person("Nitish", 33)

import pickle
with open("person1.pkl", 'wb') as f:
    pickle.dump(p, f)