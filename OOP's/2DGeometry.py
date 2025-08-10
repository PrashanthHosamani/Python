""" Write OOP class to handle the following scenarios:

1. A user can create and view 2D coordinates
2. A user can find out the distance bet 2 coordinates
3. A user can find the distance of a coordinate from origin
4. A user can check if a point lies on a given line
5. A user can find the distance bet a given 2D point and a given line

"""

class Point:
    
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self, other): #self = (x1, y1) other = (x2, y2)
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_orign(self):
        return self.euclidean_distance(Point(0, 0))
        
class Line:
    
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A, self.B, self.C)
        
    def line_point(line, point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lies on the line"
    
p1 = Point(1, 1)
p2 = Point(10, 10)
p3 = Point(1, 3)
#<x, y>
print(p1)
print(p2)
print(p1.euclidean_distance(p2))
print(p1.distance_from_orign())

l1 = Line(1,1,-2)
print(l1)
print(l1.line_point(p1))
print(l1.line_point(p3))



