#del

l = [1,2,3,4,6,7]
del l[-1]
print(l)

#slicing

del l[1:3]
print(l)

#remove

l.remove(4) #values se remove karna
print(l)

#pop
l1 = [3,4,5,6,8,7,9,0]
l1.pop() #default function is to delete the last element or item
print(l1)
l1.pop(2)
print(l1)