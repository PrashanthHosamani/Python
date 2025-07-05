
#Type conversion in Python refers to the process of converting one data type into another. \
    # Python provides two types of type conversion:
#Implicit type conversion: Python automatically converts types when necessary 


a = 10   # Integer
b = 2.5  # Float
c = a + b  # Python automatically converts 'a' to float before addition
print(c)  # Output: 12.5
print(type(c))  # Output: <class 'float'>


#Explicit type conversion: Can be  convert the type using functions 

# Converting float to int (loses decimal part)
x = 10.6
y = int(x)
print(y)  # Output: 10

# Converting int to float
a = 5
b = float(a)
print(b)  # Output: 5.0

# Converting int to string
num = 100
text = str(num)
print(text)  # Output: '100'
print(type(text))  # Output: <class 'str'>

# Converting list to tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)  # Output: (1, 2, 3)

# Converting string to int
s = "123"
n = int(s)
print(n)  # Output: 123

# Converting boolean to integer
print(int(True))   # Output: 1
print(int(False))  # Output: 0
