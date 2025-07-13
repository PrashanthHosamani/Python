#These are special python keywords that are used to pass the variable length of arguments to a function

def multiply(*args):
    """ *args allows us to pass a variable number of non-keyword arguments to a function 
    This function gives the product of any number of arguments """
    prod = 1
    
    for i in args:
        prod = prod * i
        
    print(args) #printing tuple to prove that it creates tuple when we use *args 
    return prod


print(multiply(1,2,3,4,5,6))

#Behind the scene (when we write * python understands there will be variable number of inputs) 
# Internally it will create a tuple then it adds up the items


#Documentation of the code 

print(multiply.__doc__)
print('\n')

# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# keyword arguments mean that they contain a key-value pair, like a python dictionary.

def display(**kwargs):
    
        
    for (key, value) in kwargs.items():
        print(key, "->", value)
        
display(india='delhi', srilanka = 'colombo', nepal = 'kathmandu')
    

        
        