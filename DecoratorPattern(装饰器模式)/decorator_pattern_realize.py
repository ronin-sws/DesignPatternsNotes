#coding=utf-8

from abc import abstractmethod, ABCMeta
from functools import wraps

def RedShapeDecorator(decoratedShape):
    def _RedShapeDecorator(func):
        @wraps(func)
        def __RedShapeDecorator(self, *args, **kwargs):
            func(self)
            print("set %s Border Color : Red" % decoratedShape)
            
        return __RedShapeDecorator
    return _RedShapeDecorator

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def drow(self):
        pass

class Rectangle(Shape):
    def drow(self):
        print("Shape: Rectangle")

    def __str__(self):
        return 'Rectangle'   

class Circle(Shape):
    def drow(self):
        print("Shape: Circle")

    def __str__(self):
        return 'Circle'

class RedRectangle(Shape):
    @RedShapeDecorator(decoratedShape=Rectangle())
    def drow(self):
        print("Shape: Rectangle")

class RedCircle(Shape):
    @RedShapeDecorator(decoratedShape=Circle())
    def drow(self):
        print("Shape: Circle")

class DecoratorRealizeDemo():
    def main(self):
        circle = Circle()
        rectangle = Rectangle()

        redCircle = RedCircle()
        redRectangle = RedRectangle()

        print("Circle with normal border")
        circle.drow()

        print("Rectangle with normal border")
        rectangle.drow()

        print("\nCircle with red border")
        redCircle.drow()

        print("rectangle with red border")
        redRectangle.drow()

demo = DecoratorRealizeDemo()
demo.main()
