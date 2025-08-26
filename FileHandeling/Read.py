#reading from files
# -> using read()
f = open('sample.txt', 'r')
s = f.read()
print(s)
f.close()

#reading upto n chars
f = open('sample.txt', 'r')
s = f.read(10) #reading only 10 char
print(s)
f.close()

#readline() -> to read line by line
f = open('sample.txt', 'r')
print(f.readline(), end = "")
print(f.readline(), end = "")
f.close()

#redaing entire using readline
f = open('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/VS code /Python,DS & ML/sample.txt', 'r')

while True:
    data = f.readline()
    
    if data == " ":
        break
    else:
        print(data, end='')