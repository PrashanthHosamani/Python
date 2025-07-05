#function having multiple values 
import math

def circle_stat(radius):
    area =  math.pi * radius ** 2
    circumference =  math.pi * radius ** 2 * 2
    return area, circumference

a, b = circle_stat(2)
print("area : ", round(a, 2))
print("circum : ", round(b, 2))

