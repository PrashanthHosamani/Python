#case one if the file is not present
f = open('sample.txt', 'w')
f.write('Hello world')
f.close()

f = open('sample1.txt', 'w')
f.write('hello world')
f.write('\nhow are you')
f.close()

#case 2 - if the file is already present 

f = open('sample.txt', 'w')
f.write('salman')
f.close()

#keeping old content with a mode 
f = open('sample1.txt', 'a') #a mode is append mode 
f.write('\nI am fine')
f.close()

#write lines
L = ['hello', '\nhi', '\nhow are you', '\nI am fine']
f = open('sample.txt', 'w')
f.writelines(L)
f.close()
