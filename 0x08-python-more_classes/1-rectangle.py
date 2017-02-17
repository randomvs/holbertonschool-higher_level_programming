#!/usr/bin/python3
class Rectangle:
    widthType = "width must be an integer"
    widthValue = "width must be >= 0"
    heightType = "height must be an integer"
    heightValue = "height must be >= 0"

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError(widthType)
        if width < 0:
            raise ValueError(widthValue)
        if isinstance(height, int) is False:
            raise TypeError(heightType)
        if height < 0:
            raise ValueError(heightValue)
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError(widthType)
        if value < 0:
            raise ValueError(widthValue)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError(heightType)
        if value < 0:
            raise ValueError(heightValue)
        self.__height = value
