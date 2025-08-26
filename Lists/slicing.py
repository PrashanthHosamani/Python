lst = ['abc', 'xyz', 'pqr', 134, 9090, 1.5]
print(lst)
print(lst[2:4])
print(lst[3:])
print(lst[:4])


#accessing parts of strings, lists ....

'''str[starting_idx : ending_idx]'''#ending index char or element is not included in result 

str1 = "Prashanth"
print(str1[3:8]) #index 8 is not included 
part_1 = str1[0:5]
print(part_1)
part_2 = str1[:3] #index 3 is not included 
print(part_2)
part_3 = str1[3:] #index 3 is included 
print(part_3)

'''Negative Index[-1,-2,-3]'''
str3 = "Apple"
part_str3 = str3[-5:-2]
print(part_str3)

l = [10, 20, 30, 40, 50, 60]
print(l[-2:-4])