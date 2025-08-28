import My_module
L = [1,2,3,4,5,6,7,8]

index = My_module.find_index(L, 5)
print(index)

#specifically works only for find_index function
from My_module import find_index
import sys

index = find_index(L, 2)
print(index)


