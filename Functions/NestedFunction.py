#Function inside the function which is called the nested functions

def f():
    def g():
        print('inside function g')
    g()
    print('inside function f')
    
f() #if we call the outside function than only we can access the inside function


def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(X): x =',  x)
    h()
    return x
x = 3
g(x)

# del g --> used to delete the function


