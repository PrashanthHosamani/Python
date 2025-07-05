#find the non repeating character 

str1 = "kateer"
for char in str1:
    if str1.count(char) == 1:
        print("char is: ", char)
        