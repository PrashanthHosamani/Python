#Given a list of numbers, count how many total positive numbers are there 

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_of_PN = 0
for num in numbers:
    if num > 0:
        count_of_PN += 1
print("The total positive numbers are: ", count_of_PN)
        