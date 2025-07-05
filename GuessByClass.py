'''write a number game programm ask the user to enter the number. 
if the number is greater than number to be guessed rise a value 2 large expection. 
if the value is smaller than the number to be guessed than rise a value to small expection and promote more the user enter the value again 
quite the programm only when the user enters the correct number'''

class valuetoosmallerror(Exception):
    def display(self):
        print("input value is too small")
class valuetoolargeerror(Exception):
    def display(Self):
        print("input value is too large")

r=100
try:
    num=int(input("enter the number"))
    if num == r :
        print("your guess is right")
        
    if num<r:
        raise valuetoosmallerror
    elif num > r :
        raise valuetoolargeerror
except valuetoosmallerror as n:
    n.display()
except valuetoolargeerror as s:
    s.display()