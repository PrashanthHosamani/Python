#block of statements which perfoms a set of instructions

def sum_cal(a,b):
    sum = a+b
    return sum

a = int(input())
b = int(input())

print((sum_cal(a, b)))


nums = ["delhi", "mumbai", "bangalore", "chennai"]

def print_len(nums):
    print(len(nums))
    
print_len(nums)


'''factorial of n'''

def sum_fact(n, fact):
    for i in range(1, n+1):
        fact = fact * i
    return fact

n = int(input())
fact = 1
print(sum_fact(n, fact)) 




 
 










