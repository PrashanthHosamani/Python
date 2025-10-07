def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
    
mult(5, 5)


def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)
    
    

    
    