#Take a user input till the user enters the number between 1 to 10

while True:
    number = int(input("Enter the number: "))
    if 1 <= number <= 10:
        print("Thank you")
        break
    else:
        print("Please try again!, enter the valid number")