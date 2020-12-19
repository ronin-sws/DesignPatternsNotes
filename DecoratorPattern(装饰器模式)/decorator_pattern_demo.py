#coding=utf-8

from abc import abstractmethod, ABCMeta

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

class ShapeDecorator(Shape, metaclass=ABCMeta):
    def __init__(self, decoratedShape):
        self.decoratedShape = decoratedShape 

    @abstractmethod
    def drow(self):
        self.decoratedShape.drow()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decoratedShape):
        super().__init__(decoratedShape)
    
    def drow(self):
        self.decoratedShape.drow()
        self.setRedBorder(self.decoratedShape)

    def setRedBorder(self, decoratedShape):
        print("set %s Border Color : Red" % decoratedShape)

class DecoratorPatternDemo():
    def main(self):
        circle = Circle()
        rectangle = Rectangle()

        redCircle = RedShapeDecorator(circle)
        redRectangle = RedShapeDecorator(rectangle)

        print("Circle with normal border")
        circle.drow()

        print("Rectangle with normal border")
        rectangle.drow()

        print("\nCircle with red border")
        redCircle.drow()

        print("rectangle with red border")
        redRectangle.drow()

demo = DecoratorPatternDemo()
demo.main()
        
