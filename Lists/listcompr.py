
#List comprehension provides a concise way to create lists in Python. \
    # Can generate a new list in a single, readable line. This not only makes your code shorter but can also make it clearer and more "Pythonic"

# Syntax : [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print(squared)


List1 = [0, 1, 2, 3, 4]
sqnum = [x ** 2 for x in List1]
print(sqnum)

#Adding conditions into this comprehension

#[expression for item in iterable if conditon]

even_sqr = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_sqr)

nums = [1,2,3,4,5,6,7,8,9]

list = []
for i in nums:
    list.append(i)
print(list)

list = [n for n in nums]
print(list)


