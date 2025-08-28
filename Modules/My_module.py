print("Imported My_module")
test = 'Test string'

def find_index(to_search, target):
    '''Find the index of the value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1

import datetime
import calendar

today = datetime.date.today()
print(today)