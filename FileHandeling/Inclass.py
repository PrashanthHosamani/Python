class Person:
    
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        
#format to printed in
# -> Nitish Singh age -> 33 gender -> male

person = Person('Nitish', 'Singh', 33, 'Male')
    
import json

def show_object(person):
    if isinstance(person, Person):
        return "{} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)
    
    
with open('obj.json', 'w') as f:
    json.dump(person, f, default=show_object)