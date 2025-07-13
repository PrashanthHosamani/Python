#1. Default arguments 

def power(a, b):
    return a**b

#print(power(2)) this will trow positional argument error
print(power(2,3))

def power(a = 1, b = 1):  #Defualt argument
    return a**b

#print(power(2)) this will trow positional argument error
print(power())


#2. Positional arguments  
# Arguments follow the sequence, so the first argument will get into first parameter and so on respectively 

#3. Keyword Argument
print(power(b=3, a=2)) #Irrespective of position value gets into the keyword parameter

