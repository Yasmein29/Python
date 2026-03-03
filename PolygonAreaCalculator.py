class shape:
    def __init__(self, perimeter, area):
        self.perimeter = perimeter
        self.area = area

class rectangle(shape):
    def __init__(self, length, width):
        super().__init__(perimeter=2*(length+width), area=length*width)

class triangle(shape):
    def __init__(self, base, height):
        super().__init__(perimeter=None, area=0.5*base*height)

rect = rectangle(length=8, width=3)
print("Rectangle Perimeter:", rect.perimeter)
print("Rectangle Area:", rect.area) 