class Shape():

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length


my_shape = Shape()
print('Area of shape:', str(my_shape.area()))
my_square = Square(4)
print('Area of square:', str(my_square.area()))