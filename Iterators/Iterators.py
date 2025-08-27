#it is an object that allows the programmer to traverse through a sequance of data without having to store the entire data in the memory

L = [x for x in range(1, 10)]

for i in L:
    print(i * 2)
import sys
print(sys.getsizeof(L)/64)

x = range(1, 10)
for i in x:
    print(i**2)
print(sys.getsizeof(x)/64)