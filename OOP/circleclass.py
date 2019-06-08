
class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__ (self, radius = 1):
        self.radius = radius
        self.area = radius*radius*Circle.pi  #Circle.pi refers to the class object attribute
    
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2  #Circle.pi refers to the class object attribute

myCircle = Circle(30)
print(myCircle.get_circumference())
print(myCircle.area)