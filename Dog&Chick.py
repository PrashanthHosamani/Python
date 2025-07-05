heads = 4
legs = 10

# Solve the equations:
#   dogs + chickens = heads
#   4 * dogs + 2 * chickens = legs
#
# Express chickens in terms of dogs:
#   chickens = heads - dogs
#
# Substitute in the legs equation:
#   4*d + 2*(heads - d) = legs
#   4*d + 2*heads - 2*d = legs
#   2*d + 2*heads = legs
#   2*d = legs - 2*heads
#   d = (legs - 2*heads) / 2




# Heads = int(input("No of heads: "))
# Legs = int(input("No of legs: "))

heads = 4
legs = 10

dogs = (legs - 2 * heads) // 2
chickens = heads - dogs

print("Dogs:", dogs)
print("Chickens:", chickens)




