#anything meaningful? : how much time does a function takes to get executed 
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print('tim taken by', func.__name__,time.time() - start, 'secs')
    return wrapper

@timer
def hello():
    print('hello world')
    time.sleep(2)

@timer
def square(num):
    time.sleep(1)
    print(num**2)
    
hello()
square(2)
    
