person = {"name" : "Jenn", "age" : 23}

sentence = "My name is " + person["name"] + " and I am " + str(person["age"]) + " years old."
print(sentence)

sentence = "My name is {} and I am {} years of old".format(person["name"], person["age"])
print(sentence)

#date time

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

print(my_date)

#march 01, 26

sentence = "{:%B %d, %y}".format(my_date)
print(sentence)

#find all things on datetime official website 

