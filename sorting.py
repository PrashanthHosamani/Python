'''Sorting is a common task in Python, and there are multiple ways to perform sorting operations depending on the data structure you're dealing with'''
'''built-in methods to sort lists either in-place or by creating a new sorted list.'''

#using sort()

numbers = [4,2,6,7,3]
numbers.sort()
print(numbers)

print('-'*20)

#descending order 

numbers = [4,2,6,7,3,]
numbers.append(9)
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print('-'*20)


'''Using sorted():
This function returns a new sorted list and leaves the original list unchanged.
'''

numbers = [6,7,4,6,9,3,2]
del numbers[3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

#how can we reverse this sorted_numbers
sorted_numbers.sort(reverse=True)
print(sorted_numbers)

#fiding the index of element

print('-'*20)

numbers = [6,7,4,6,9,3,2]
print(numbers.index(4))

#count how many values or elements are there 

numbers = [6,7,4,6,9,3,2]
print(numbers.count(4))

#joining two lists or extending list

numbers = [6,7,4,6,9,3,2]
name = ['adarsh','mani', 'yoga']
numbers.extend(name)
print(numbers)