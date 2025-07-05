#write a function that takes variable number of arguments and returns their sum (*args)

def sum_all(*args):
    # print(*args)
    # print(args)
    
    # for i in args:
    #     print(i * 2, end = " ")
        
    return sum(args)
    
    # add = 0
    # for i in args:
    #     add = add + i
    # print(add)
        
print(sum_all(1, 2, 3))
    