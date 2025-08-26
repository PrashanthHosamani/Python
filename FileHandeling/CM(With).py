#its good to close the file after usage as it will free up the resources 

#with
with open('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/VS code /Python,DS & ML/sample.txt', 'w') as f:
    f.write('selmon bhai')
    
#tru f.read()

with open('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/VS code /Python,DS & ML/sample.txt', 'r') as f:
    print(f.read())
    
with open('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/VS code /Python,DS & ML/sample.txt', 'r') as f:
    print(f.read(10)) #first 10 char of the content will print
    print(f.read(10)) #next 10 char will print
    
    
big_L = ['\nHello world ' for i in range(1000)]

with open('big.txt', 'w') as f:
    f.writelines(big_L)
    
with open('big.txt', 'r') as f:
    
    chunk_size = 100
    
    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end = '')
        f.read(chunk_size)


#tell function

with open('sample.txt', 'r') as f:
    print(f.read(10))
    print(f.tell()) # this returns at what text you are currently processing 
    

    f.seek(0) #goes back to zero
    print(f.read(10))
    print(f.tell())
    
    f.seek(15) #srats from anywhere 
    print(f.read(10))
    print(f.tell())


    #seek during write
    
    with open('sample.txt', 'w') as f:
        f.write('hello')
        f.seek(0)
        f.write('Xa') #replaces the char
        
        
        