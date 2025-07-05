#repeating something in the instruction(set of instructions are repeating)

# n = int(input("Enter the number: "))

for i in range(1,7):
    for j in range(1,7):
        print(i,j)
    print("_________________\n")

"If u are rolling 2 deices and this output will be the possible outcome"

            
            
#print(round((number/36)*100,2))


for i in range(1,7):
    for j in range(1,7):
        if i + j == 8:
            print(i, j)
            
            
for i in range(1, 101):
    print(i)       
    
for i in range(101, 0, -1):
    print(i)
    
m = 2
for i in range(1, 11):
    print(m, "*", i, "=", i*2 )

    
    
# natural = 30
summ = 0
for i in range(1, 10):
    summ = summ+i
print(summ)
print("_________________\n")
    
n = 5
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact) 
    
   

fruits = ["apple", "banana", "mango", "Cherry"]
for fruit in (fruits):
    print(fruit)
    
student = {"name": "Alice", "age": 25, "course": "Math"}
for key in student:
    print(key, student[key])


#iterates from items() 
student = {"name": "Alice", "age": 25, "course": "Math"}
for key, value in student.items():
    print(key, "->", value)

    
    
    
