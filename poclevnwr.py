class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side


# Creating objects
rect = Rectangle(4, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

square = Square(4)
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())