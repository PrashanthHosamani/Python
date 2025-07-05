#Calculate the sum of even number up to the given range n
n = 10
sum_of_even_no = 0
for num in range(1, n+1):
    if num % 2 == 0:
        sum_of_even_no += 1
print("The sum of even number's is: ",sum_of_even_no)