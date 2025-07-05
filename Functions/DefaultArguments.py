def power(a, b):
    return a**b


#print(power(2)) this will trow positional argument error

print(power(2,3))


def power(a = 1, b = 1):  #Defualt argument
    return a**b


#print(power(2)) this will trow positional argument error

print(power())