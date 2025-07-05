a = 0
b = 1
print(a , b, end=" ")

for i in range(8):
    next_term = a + b
    print(next_term,end=" ") 
    a,b = b, next_term

    

print("\n")
word = "programming"
char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
for char, count in char_count.items():
    print(char + ":", count)