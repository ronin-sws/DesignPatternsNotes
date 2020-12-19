# _*_ coding:utf-8 _*_

"""
迭代器模式：
    迭代器模式是一种通用性的可以遍历容器类型（序列类型，集合类型），的实现方式，
    不关心遍历的对象是什么，也不需要关心遍历的实现算法是什么，它关心的是从容器中遍历取出来的元素的结果；
    提到迭代器，首先它是与集合相关的，集合也叫聚集、容器等，我们可以将集合看成是一个可以包容对象的容器，
    例如List，Set，Map，甚至数组都可以叫做集合，而迭代器的作用就是把容器中的对象一个一个地遍历出来。
"""


# 创建Iterator接口(抽象类)
class Iterator(object):
    def first(self):  # 取第一个元素的方法
        pass

    def next(self):  # 取下个元素的方法
        pass

    def hasNext(self):  # 判断是否还有下一个元素
        pass


# 创建Container接口
class Container(object):
    def getIterator(self):
        pass


# 迭代器实体类
class NameIterator(Iterator):
    def __init__(self, container):
        self.container = container
        self.index = 0

    def first(self):
        return self.container[0]

    def next(self):
        ret = None
        self.index += 1
        if self.index < len(self.container):
            ret = self.container[self.index]
        return ret

    def hasNext(self):
        return True if self.index + 1 >= len(self.container) else False


# 创建实现Container的实体类
class NameRepository (Container):
    def __init__(self):
        self.name_list = []

    def getIterator(self):
        return NameIterator(self)


if __name__ == "__main__":

    nr = NameRepository()
    nr.name_list.append('Robert')
    nr.name_list.append('John')
    nr.name_list.append('Julie')
    nr.name_list.append('Lora')
    nr.name_list.append('wss')
    iter = NameIterator(nr.name_list)
    print(iter.first())
    while not iter.hasNext():
        print(iter.next())





