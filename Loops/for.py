# #probelm = Store monthly expesnses in a list and find out total expenses for all months

# # exp = [2340, 2500, 2100, 3200, 2800]
# # total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
# # print(total)

# # total = 0
# # for item in exp:
# #     total = total + item
# # print(total)

# '''for loop'''

# # n = 1
# # for i in range (n, 11):
# #     print(i)
    
# '''print tables of 2 '''

# # n = 2
# # for i in range (1, 11):
# #     print(n, "*", i, "=", i*n)
    
# '''another parameter'''

# # n = int(input("Enter a number"))
# # for i in range (1, 11, 2):
# #     print(i)
    
# '''tables of 4'''

# # for i in range(4, 41,4):
# #     print(i)

# '''same the above thing with input n'''

# # n = int(input("Enter a number : "))
# # for i in range(n, (n*10)+1, n):
# #     print(i)


# numbers = [4,5,7,8,2,3,9]
# for i in numbers:
#     sq = i ** 2
#     print(sq)

# n = int(input())
# for i in range(n):
#         sq = i ** 2
#         print(sq)
    
    
# mult = lambda x, y: x * y
# onemult = mult(3, 4)
# print(onemult)


# list1 = [2,4,5,6,7,8,3]
# for element in list1:
#     if element == 7:
#         continue 
#     print(element)
    
# sum = 0 
# count = 1
# for i in range(count, 6):
#     print(i * count)
#     count = count + 1

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=" ")

# total = 0
# for i in range(1, 9):
#     total += i 
# print(total)

# fact = 1
# for i in range(1, 6):
#     fact = fact * i 
# print(fact)

word = 'PYTHON'
rw = word[::-2]
print(rw)
# for i in range(len(word) - 1, -1, -1):
#     print(word[i])


vowels = "aeiou"
word = "python"
count = 0

for char in word:
    if char in vowels:
        count = count + 1
print(count)
        
        
    
    

