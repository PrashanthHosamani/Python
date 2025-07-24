'''Basically dealing with soft copy data,
In python there are two types of files,
1: text files : Store the data in the form of characters.
2: binary files : Store entire data in the form of bytes, i;e. a group of 8 bits each,
can used to store texts, img, music,video.
'''

'''operations in file handling :
- READ, READ LINE, READ LINES
- WRITE, WRITE LINES
- APPEND'''

'''MODES OF FILE HANDLING:
1. WRITE = To write data into file. if any data is alredy present it will be stored 
2. READ = only to fetch the data
3. APPEND ='''

#Opening file
file=open("helo.txt", "r") #synatx to open a file
print(file.readline())   # readline gives output of only one line but readlines output will be in the form of list

file.close() #syntax to close a file 

''''''
file=open("helo.txt", "r") 
z= file.readlines()
print(z)
for i in z:
    print(i)
    file.close
    
    #WITH KEYWORD, This we use as 2nd method to open the file, in this method no need to close the file 
     #with open("file.txt","rb")as file : SYNTAX
    
    '''write a program that accepts file name as an input 
    from the user open the file and count the number of times a character appears in the file'''
    
    file=input("Enter the filename")
    with open(file,"r") as f:
        text=f.read()
        c=input("Enter the character you want to search")
        count=0
        for i in f:
            if i==c:
                count=count+1
        print(c,"appears",count,"times")
        
    
    '''Write a program that reads data from a file and calulates the percentage of vowels and consonants in the file'''
    
    file=input("Enter the filename")
    with open(file,"r") as f:
        text=f.read()
        for i in text:
            if i in "aeiouAEIOU":
                vowels=vowels+1
            
#condiments of restored values 
    
    
    