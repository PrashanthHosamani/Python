#There are 2 stage where error may happen in a program
#1. During Compilation -> Syntax Error
""" 
1. Something in the program is not written according to the program grammer
2. Error is raised by the interpreter/compiler
3. You can solve it by rectifying the program 
 
 There are more types of error 
 
"""
#2. During Execution -> Exceptions
"""
If things go wrong during the execution of the program(runtime), it generally happens when something unforeseen has happened
- Exception are raised by python runtime
- you have to takle is on the fly

Memory overflow
Devide by 0 -> Logical error
Database error
"""
#why is its imp to handle exception
# -> User experiance and breach of security
#how to handle
# -> Try except block

with open('file.txt', 'w') as f:
    f.write('Hello world')
    
#try catch demo
try:
    with open('file.txt', 'r') as f:
        print(f.read())
except:
    print("sorry file not found")
    
try:   
    f = open('sample1.txt', 'r')
    print(f.read())
    print(m)
except FileNotFoundError:
    print("file not found")
except NameError:
    print("variable not defined")


#Else block
try:
    f = open('sample1.txt', 'r')
except FileNotFoundError:
    print("file not found")
except Exception:
    print('Some error occured')
else:
    print(f.read())
    
    
#finally
#else
try:
    f = open('sample1.txt', 'r')
except FileNotFoundError:
    print("file not found")
except Exception:
    print('Some error occured')
else:
    print(f.read())
finally:
    print("This will definately execute")

#raise exception

# raise NameError("simply trying")
# raise ModuleNotFoundError("Just to see")



class Bank:
    
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self,amount):
        if amount < 0:
            raise Exception('amount can not be in negative')
        if self.balance < amount:
            raise Exception("you do not have money")
        self.balance = self.balance - amount
        
obj = Bank(10000)
try:
    obj.withdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)
    
