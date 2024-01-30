#!/usr/bin/python3
""" calculates area and perimeter and returns a square string """


class square():
    """ calculates area and perimeter and returns a square string """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes a square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ returns a square string """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creates a square class """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
