#same as Q 7 but the format should be in key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(name = "Krishna", weapon = "Sudharshan chakra")
print_kwargs(name = "Shiv", weapon = "Trishul")
    