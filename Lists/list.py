'''collection of different data types , basically known as data structure '''

list = [1, 'ashish', 123, 23, 30,40,50]
#access the element through indxing
print(list[0])
print(list[2])
print(list[1])

print('-----------------\n')

#access from backward

print(list[-1])

#modify the values 

print('-----------------\n')

list[2] = 'sakshi'
print(list)

#slicing 

print('-----------------\n')

print(list[2:5])

#reverse a strng

print('-----------------\n')

print(list[::-1]) #for no skipping any elemt in the list
print(list[::-2])# for skipping 1 elmt in the list

#append (add)

print('-----------------\n')

print(list)
list.append("data")
print(list)

print('-----------------\n')

#length of list

print(len(list))

list.append(6) #adds one element at the end
#list.sort() sorts in asceding order
#list.sort(reverse = True) #sorts in descending order 
list.reverse() #reverses list
list.insert(1, 5)  # insert element at index 
print(list)
list.remove('ashish')
list.pop(1) #index 
print(list)


