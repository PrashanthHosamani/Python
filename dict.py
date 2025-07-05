# my_dict = {"number": 1234, "name": "prshanth", "city": "bangalore"}
# name = my_dict["name"] #accessing the value for key name 
# print(name) #printing the value 
# age = my_dict.get("age",0)  # Returns 30, or 0 if "age" is not found
# print(age) 
# print(my_dict["city"])

# '''adding or modifying elements'''

# my_dict["state"] = "karnataka" #adding a key value pair
# my_dict["age"] = 31 #updating the value 

# for key, value in my_dict.items(): #using for loop and f string to print only keys and values of the dict
#     print(f"{key} : {value}")
# del my_dict["number"] #removing the key value pair from my_dict with key number
# print(my_dict)
# '''pop method to remove the key value pair and returns the value'''

# #keys must be unique in dictionaries can not be duplicated 
# #values can be duplicated 
# #dictionaries are mutable (you can change their contents)

# '''Methods'''
# my_dict.keys() #return keys 
# print(my_dict.values()) #return values
# my_dict.items() #return all the keys and values in the  form of tuple 
# my_dict.get("age") #return the value of key
# #my_dict.update() insert the specified items to the dictionary  


# def soundex(name: str) -> str:
#   """Convert a name to its soundex code."""
#   #Soundex dictionary for letter to digit mapping

#   soundex_dict = {
#     'BFPV': '1',
#     'CGJKQSXZ': '2',
#     'DT': '3',
#     'L': '4',
#     'MN': '5',
#     'R': '6', 'AEIOUHWY': '.' #Indicates ignored char
#   } 

#   #step1: Retain the first letter (uppercase)
#   soundex_code = name[0].upper()

#   #step2: Replace all other characters with digits
#   prev_digit = ''
#   for char in name[1:].upper():
#     for key, value in soundex_dict.items():
#       if char in key:
#         digit = value
#         if digit != '.' and digit != prev_digit:
#           soundex_code += digit
#           prev_digit = digit
#           break

#   #step3: Pad with zeros or truncate to 4 characters
#   return (soundex_code + '000')[:4]

#   name = "Robert"
#   print(f"soundex code for {name}: {soundex(name)}")

#   name = "Repert"
#   print(f"soundex code for {name}: {soundex(name)}")


def soundex(name: str) -> str:
    """Convert a name to its Soundex code."""
    #Soundex dictionary for letter to digit mapping
    soundex_dict = {
        'BFPV':'1','CGJKQSXZ':'2','DT':'3','L':'4','MN':'5','R':'6','AEIOUHWY':'.'
        # '.' INDICATES IGNORED CHARACTERS
        }
    #Step 1: Retain the first letter (uppercase)
    soundex_code = name[0].upper()
    
    #Step 2: Replace letters with corresponding digits
    prev_digit = ''
    for char in name[1:].upper():
        for key, value in soundex_dict.items():
            if char in key:
                digit = value
                if digit != '.' and digit != prev_digit: #Avoid duplicates
                    soundex_code += digit
                prev_digit = digit
                break
    # Step 3: Pad with zeros or truncate to 4 characters
    return (soundex_code + '000')[:4]

#Example usage
name= "Robert"
print(f"Soundex code for {name}:{soundex(name)}")        


name= "Rupert"
print(f"Soundex code for {name}:{soundex(name)}")

name= "Ashcraft"
print(f"Soundex code for {name}:{soundex(name)}")