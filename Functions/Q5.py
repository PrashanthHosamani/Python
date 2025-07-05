#write a function that greets user, if no name is provided than it should greet using default name
def greet(name = "User"):
    return "Hello, " + name + "!"

print(greet("python"))
print(greet())