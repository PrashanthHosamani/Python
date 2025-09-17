import os
#allows us to interact with underlying operating system 

#print(dir(os))

print(os.getcwd())

os.chdir('/Users/apple/Library/Mobile Documents')

print(
    os.listdir()
)

#make directory 
print(os.getcwd())

os.chdir('/Users/apple/')
print(os.listdir())

os.rmdir('Os_Demo')

os.mkdir("OS_Demo")

# print(os.listdir())


#rename

# os.rename('ai project chatbot', 'Ai Project Chatbo')

print(os.stat('Ai Project Chatbo'))

