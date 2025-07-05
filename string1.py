#string is a data type which is used to manipulate different kind of information in programs

'''string slicing''' #cutting a part of srting and printing it out however you want it to be printed 
print("prashanth"[:2])
print("akshata" [2:])
print("akshata" [2:5])
print("akshata" [:-2])

'''case conversion''' #converting srtings into upper and lower case 
print("Akshata" .lower())
print("Akshata" .upper())

'''string stripping''' #String stripping in Python refers to removing unwanted characters from the beginning and/or end of a string. These unwanted characters are typically whitespace characters like spaces, tabs, or newlines.

# IMP 

'''Python provides a built-in method called strip() for strings.

You call this method on a string variable to remove leading and trailing whitespace characters.

Optionally, you can specify the characters you want to remove within the strip() function's parentheses.
'''
print("  prashanth    ")# we will be printing this with space
print("  prashanth    " .strip())
print("  prashanth      " .rstrip())
print("  prashanth      " .lstrip())

'''replacing string''' #can replace any word from the string with anything
print("prashanth".replace('h','-'))

text = "Hello world, How is your world"
new_text = text.replace("world","python")
print(new_text)

#replacing only the first occurrance 
text = "Hello world, How is your world"
new_text = text.replace("world","python", 1)
print(new_text)

'''string count''' #counting anything from the string , words / leters , 
#using count()
print('prashanth'.count('s'))
print("prashanth".count('a'))

#The len() function is a built-in function in Python that returns the length of an object. For strings, it counts the total number of characters in the string.

text = input("enter your name : ")
length = text.count('s')
char_count = len(text)
print("total no of characters in text : ", char_count)
print("enter the no of s in char : ", length)

print("prAshanth".lower().count('a'))

'''string check'''

print("prashanth".isalpha())
print("prashanth".isdigit())
print("prashanth".isupper())
print("prashanth".islower())
print('1234'.isdigit())

'''string capialization'''
print("prashanth".capitalize())
print("prashanth".title())

a = "Hello"[::-1]
print(a)
    


