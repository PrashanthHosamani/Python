num = int(input("Enter the number: "))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()
    
print()

for i in range(1, num+1):
    for j in range(1, num+1):
        print("*", end = " ")
    print()
    
print()

for i in range(num-1, -1, -1):
    for j in range(i, -1, -1):
        print("*", end = " ")
    print()
    
    
