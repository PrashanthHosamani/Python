# l = [1,2,3,4,5]
# print(l[1:4])

# l1 = [2,9,4,5,6,[3,4,5,7]]
# print(l1[-1][2]) #to access the numbers inside another list

L = [1,2,3,4,5] #manual way to get reversed elements of list 
RL = []
for i in range(len(L) - 1, -1, -1):
    RL.append(L[i])
print(RL)

print(L[::-1]) #through slicing


def leapyear (year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return "Leap year"
			else:
				return "Not leap year"
		else:
			return "Leap year"
	else:
		return "Not leap year"

print(leapyear(2001))


n = int(input())
str1 = ""
for i in range(1, n+1):
    str1 += str(i)
print(str1)
			