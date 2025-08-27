#A decorators in python is a function that receives another function as input and adds some functionality(decoration) to and it and returns it
#This can happen only because python functions are 1st class citizens
#There are 2 types of decorators available in python

#Python are 1st class citizen

def modify2(func, num):
    return func(num)

def square(num):
    return num**2

modify2(square, 2)


#simple example 1

def my_decorator(func):
    def wrapper():
        print('************************')
        func()
        print('************************')
    return wrapper

def hello():
    print('hello')

@my_decorator 
def display():
    print("Hey guys")
    
display()
    
# a = my_decorator(hello)
# a()

# b = my_decorator(display)
# b()


