#!/usr/bin/python3
""" Defines a module that implements Square class """


class Square():
    """ Defines a square Class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes a square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Square perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Square string """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Initializes a Square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
