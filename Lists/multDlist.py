#having more then one lists in a one list

stud_1 = [['ashish', 123456,'bangalore','student'],[123,25,40,35,50,46,'A+','10th']]
print(stud_1[1])
print(stud_1[0])
print(stud_1[0][0])
print(stud_1[1][4])

#we can have any dimensional list

list_1 = [[1,2,3],[4,5,6,7],[7,8,9,0],['a','v','b','h'],['ashish',350,'many']]
print(list_1)

print(list_1[2])
print(list_1[0])

print(list_1[2][0])

list_1[2][3]=1
print(list_1[2])

list_1[3] = ['ashish','match',3,4,5]
print(list_1)

list_1[0].append(4) 
print(list_1[0])

del list_1[3]
print(list_1)

#for loop

print(list_1)
for i in list_1:
    for j in i:
        print(j)
        
