# -*- coding:utf-8 -*-

import math

#定义4个图形类，并且每一个图形都有一个可以计算面积的方法
class Circle:
    def Area(self,radius):
        return math.pow(radius,2)*math.pi

class Rectangle:
    def Area(self,longth,width):
        return 2*longth*width

class Triangle:
    def Area(self,baselong,height):
        return baselong*height/2

class Ellipse:
    def Area(self,long_a,short_b):
        return long_a*short_b*math.pi

#=================================
#定义创建对象的工厂接口，因为python中并没有接口的概念，所以，这里打算通过“类的继承”加以实现
class IFactory:  #模拟接口
    def create_shape(self):  #定义接口的方法，只提供方法的声明，不提供方法的具体实现
        pass

class CircleFactory(IFactory): #模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  #重写接口中的方法
        if name =='Circle':
            return Circle()

class RectangleFactory(IFactory): #模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  #重写接口中的方法
        if name =='Rectangle':
            return Rectangle()

class TriangleFactory(IFactory): #模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  #重写接口中的方法
        if name =='Triangle':
            return Triangle()

class EllipseFactory(IFactory): #模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  #重写接口中的方法
        if name =='Ellipse':
            return Ellipse()


if __name__=='__main__':
    factory1=CircleFactory()
    factory2=RectangleFactory()
    factory3=TriangleFactory()
    factory4=EllipseFactory()

    circle=factory1.create_shape('Circle')
    circle_area=circle.Area(2)
    print(f'这是一个圆，它的面积是：{circle_area}')

    rectangle=factory2.create_shape('Rectangle')
    rectangle_area=rectangle.Area(2,3)
    print(f'这是一个长方形，它的面积是：{rectangle_area}')

    triangle=factory3.create_shape('Triangle')
    triangle_area=triangle.Area(2,3)
    print(f'这是一个三角形，它的面积是：{triangle_area}')

    ellipse=factory4.create_shape('Ellipse')
    ellipse_area=ellipse.Area(3,2)
    print(f'这是一个椭圆，它的面积是：{ellipse_area}')