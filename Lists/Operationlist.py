l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

#concatination/merge

print(l1+l2)

print(l1*3) # 3 time repeats and merged together in 1 list 

print(5 in l1)

print(5 not in l1)

l3 = [1,2,3,4,5,[7,8]]
print(8 in l3) #false 
print([7,8] in l3) # true


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    highest_score = max(arr)
    remaining_score = [s for s in arr]
    print(remaining_score)