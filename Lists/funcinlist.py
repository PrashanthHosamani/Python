#most functions are done

# len/min/max/sorted

l = [2,1,5,7,0]

print(len(l))

print(min(l)) #only for homo items 

print(sorted(l)) #temporary operation
print(l) #prints the original list 
print(sorted(l,reverse =True))


print(l.index(5))


l.reverse() #permanent 
print(l)
l1 = l.copy()
print(l1)
print(id(l1))


