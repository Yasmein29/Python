class square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print('Area is =' , self.side * self.side)

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print('Area is =' , 3.14 * self.radius * self.radius) 

s = square(6)
c = circle(7)
for shape in (s, c):
    shape.area()