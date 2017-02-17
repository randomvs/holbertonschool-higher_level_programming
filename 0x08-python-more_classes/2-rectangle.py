#!/usr/bin/python3
class Rectangle:
    widthType = "width must be an integer"
    widthValue = "width must be >= 0"
    heightType = "height must be an integer"
    heightValue = "height must be >= 0"

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError(self.widthType)
        if width < 0:
            raise ValueError(self.widthValue)
        if isinstance(height, int) is False:
            raise TypeError(self.heightType)
        if height < 0:
            raise ValueError(self.heightValue)
        self.__height = height
        self.__width = width

    def perimeter(self):
        return (self.__width + self.__height) * 2

    def area(self):
        return self.__width * self.__height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError(self.widthType)
        if value < 0:
            raise ValueError(self.widthValue)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError(self.heightType)
        if value < 0:
            raise ValueError(self.heightValue)
        self.__height = value
