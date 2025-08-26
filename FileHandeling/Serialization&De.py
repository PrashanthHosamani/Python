#Serialization and Deserialization
#serialization - Process of converting python data type to JSON format
#Deserialization - Process of converting JSON to python data types 

#JSON -> Javascript on notation, universal data format (text format)

d = {
    'name' : "Nitish",
    'age' : 33,
    'gender' : 'male'
}


import json
L = [1,2,3,4,5]

with open('demo.json', 'w') as f:
    json.dump(L, f)
    
    
#Deserialization

with open('FileHandeling/dict.json', 'r') as f:
    print(json.load(f))
    print(type(d))
    
    
    