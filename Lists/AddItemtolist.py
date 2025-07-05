#append is for only to add one element or item
l =[1,2,3,4,5,6,7]
l.append("Hello")
print(l)
l.append(0)
print(l)

#we use exted for adding multiple items or elements
l1 = [2,3,4]
l1.extend([4,5,6])
print(l1)

#extend alwys adds the items on by one hence this does not work for strings

#insert

l1.insert(1,100) 
print(l1)
