#Fibonacci Discovered Problem

#printing series

def fibonicci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fibonicci_series(10))
    
    #Inefficient code 
    
def fibo(m):
    if m == 1 or m == 0:
        return 1
    else:
        return fibo(m-1) + fibo(m-2)
        
    
print(fibo(12))

#Solving Rabbit problem


    

    


    