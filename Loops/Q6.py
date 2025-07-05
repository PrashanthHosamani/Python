#Find the factorial of the number 

n = 5
fact = 1

while n > 0:
    fact = fact * n
    n = n - 1
print(fact)

#using for loop

for i in range(1, n+1):
    fact = fact * i
print(fact)