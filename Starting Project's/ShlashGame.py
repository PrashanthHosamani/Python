print("welcome to my first game!")
name = str(input("What is yout name?: "))
age = int(input("Enter your age: "))

print("Hello", name, "you are", age, "year old.")

health = 10


if age >= 18:
    print("Good News! You are eligible to play this game, All the best!")
    take_permission = str(input("Do you wants to play?: ")) #We can actually use .lower() method here 
            #but its very fun to have while loop and ask them to write it in smaller again
    permission = "yes" or "Yes"
    while take_permission != permission:
        if take_permission == "YES":
            print("Write yes in small letter's")
        elif(take_permission == "no"):
            print("Think agin, If you really do not want to play write No with N capital")
        else:
            print("Get lost, send your friend")
        take_permission = str(input("Hey him's friend do you want to play?: "))
        
    else:
        print("Let's play!")
        print("You are starting with", health, "health")
        
        left_or_right = input("First choice.... Left or Right \
(left/right)?: ").lower()
        if left_or_right == "left":
            answer = input("Nice, you have followed the path and reach a lake.. \
Do you want to go across or around (across/around)?: ").lower() 
            if answer == "around":
                print("you went around and reached the other side of the lake ")
            elif answer == "across":
                print("You managed to get across, but were bite by fish and lost 5 health.")
                health = health - 5   
            house_river = input("You notice a house and a river. Which one do you go to \
(river/house)?: ").lower()
            if house_river == "house":
                print("You went to the house and you are greeted by the owner...\
but he does not like you and you lost 5 health again!'")           
                health = health - 5
                if health <= 0:
                    print("You now have 0 health you lost the game.")
                else:
                    print("You have survived... You win!")
            else:
                print("You fell in the river abd lost.")
            
        else:
            print("You fell down and lost")   
else:
    print("Opps!, You are not there to play this game please get lost")
    

    
