def calculate_factorial(n):  # Function definition (calculate factorial)  
    if n == 0 :              # Base case when 'n = 0', since the factoria         
        return 1              
    else :                    # Recursive Case, multiply "number" with                  
       return n * calculate_factorial (n-1)          
    
print("The factorial of 5 is:",calculate_factorial(5))   # Call function 
