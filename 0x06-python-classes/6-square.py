#!/usr/bin/python3
""" Square module """


class Square:
    """ defines a square class """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        Intializes the attributes
        Args:
            size: size of square
            position:  position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ gets the private attribute:size """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ get the private attribute:position """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ calculate the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ print to the stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            count = 0
            p1, p2 = self.__position
            for _ in range(p2):
                print()
            while count < self.__size:

                j = 0
                while j < p1:
                    # replace position with space
                    print(" ", end='')
                    j += 1

                num = 0
                while num < self.__size:
                    print("{}".format("#"), end='')
                    num += 1
                print()
                count += 1
