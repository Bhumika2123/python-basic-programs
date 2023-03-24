class Rectangle:
    def __init__(self, l, b):
        self.l=l
        self.b=b

class Square(Rectangle):
    def __init__(self, l, b):
        super().__init__(l, b)
    def area(self):
        return self.l*self.b
class Cube(Rectangle):
    def __init__(self, l, b,h):
        super().__init__(l, b)
        self.h=h
        
    def volume(self):
        return self.l*self.b*self.h

sq= Square(2,3)
cu=Cube(2,3,4)
print(sq.area())
print(cu.volume())
