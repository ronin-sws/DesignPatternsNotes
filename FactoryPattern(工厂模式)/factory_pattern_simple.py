# -*- coding:utf-8 -*-

"""
简单工厂模式：在工厂中传入图纸和材料，就能生产出对应的设备对象，让设备做能做的事
"""

class ParentClass(object):
   """
   计算机运行的父类
   """
   def __init__(self, a, b):
       self.a = a
       self.b = b
       pass

   def operation(self):
       """
       操作函数
       :return:
       """
       pass


class AddOp(ParentClass):
   """
   加法
   """
   def __init__(self, a, b):
       super(AddOp, self).__init__(a, b)
       pass

   def operation(self):
       return self.a + self.b


class JianOp(ParentClass):
   """
   减法
   """
   def __init__(self, a, b):
       super(JianOp, self).__init__(a, b)
       pass

   def operation(self):
       return self.a - self.b


class FactoryClass(object):
   """
   简单工厂类
   """
   def __init__(self):
       pass

   def create_class(self, op, a, b):
       if op == "+":
           return AddOp(a, b)
       elif op == "-":
           return JianOp(a, b)


if __name__ == '__main__':
   factory = FactoryClass()
   add = factory.create_class("+", 23, 34)
   print(add.operation())
   jian = factory.create_class("-", 34, 55)
   print(jian.operation())
