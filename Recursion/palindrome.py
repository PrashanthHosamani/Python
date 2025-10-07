
def palindrom(str1, start, end):
    if start >= end:
        return True
    
    if str1[start] == str1[end]:
        return palindrom(str1, start + 1, end - 1)
    else:
        return False
    
def palindromin(str1):
    return palindrom(str1, 0, len(str1) - 1)

print(palindromin("madam"))
        
        

def palin(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palin(string[1:-1])
        else:
            return False
        
print(palin("madam"))
        
    
