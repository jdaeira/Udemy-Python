# Fill in the Line class methods to accept coordinates as a 
# pair of tuples and return the slope and distance of the line.

import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        sumX = (self.coor2[0] - self.coor1[0])
        sumY = (self.coor2[1] - self.coor1[1])
        sumXY = (math.pow(sumX, 2)) + (math.pow(sumY, 2))
        print(math.sqrt(sumXY))

    def slope(self):
        sumX = (self.coor2[0] - self.coor1[0])
        sumY = (self.coor2[1] - self.coor1[1])
        print(sumY / sumX)

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)


li = Line(coordinate1,coordinate2)

li.distance()

li.slope()

# Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        print(3.14 * math.pow(self.radius, 2) * self.height)
    
    def surface_area(self):
        print((2 * 3.14 * self.radius * self.height) + (2 * 3.14 * math.pow(self.radius, 2)))  

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()

c.surface_area()



