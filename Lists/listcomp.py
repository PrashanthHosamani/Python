#List comprehension provides a concise way of creating lists 
# or shortcut way of creating list

# Add 1 to 10 numbers to a list

l = []
for i in range(1, 11):
    l.append(i)
print(l)  #normal way 

l1 = [i for i in range(1,11)]
print(l1)

#Syntax  : list = [expression for item in iterable if condition == True]
    
v = [2,3,4]
s = -3

#simple for loop
x = []
for i in v:
    x.append(i*s)
print(x)

#List comprehension
x = [i*s for i in v]
print(x)

#Simple for loop
l2 = [1,2,3,4,5]
y = []
for i in l2:
    y.append(i ** 2)
print(y)
    
    
#List comprehension
y = [i ** 2 for i in l2]
print(y)

#print all the numbers divisible by 5 in the range of 1 to 50
print([i for i in range(1, 51) if i % 5 == 0])

#find the languages which start with letter p
languages = ["java", "python", "php", "c", "c++"]
print([language for language in languages if language.startswith("c")])

#Using for loop
result = []
for language in languages:
    if language.startswith("p"):
        result.append(language)   
print(result)
    
        
print([language for language in languages if language.startswith("p")])

basket = ['apple', 'guava', 'cherry', 'banana']
my_fruit = ['apple', 'kiwi', 'grapes', 'banana']

#add new list from my_fruit and items if the fruit exists in basket and also starts with 'a'

print([fruit for fruit in my_fruit if fruit in basket and fruit.startswith("a")])

#Using for loop
result1 = []
for fruit in my_fruit:
    if fruit in basket and fruit.startswith("a"):
        result1.append(fruit)
print(result1)

#print 3*3 metrix using list comprehension
print([[i * j for i in range(1,4)] for j in range(1,4)])
        
        