def is_even(num):
    """This code is a function which checks the integer is an even or odd"""
    if type(num) == int:
        if num % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        print("enter positive integer")
    

for i in range(1,11):
    x = is_even(i)
    print(x)
    
print("\n")
    
list = [1,3,4,5,6,7,9,9,7,4,3,3,5,6,77]
    
for nums in list:
    x = is_even(nums)
    print(x)
    
print("\n")

is_even("a")
    

    