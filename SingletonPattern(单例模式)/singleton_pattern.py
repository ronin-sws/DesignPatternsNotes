# coding = utf-8

"""
该模式的类负责创建自己的对象，同时确保只有单个对象被创建。
单例模式需要注意线程安全。
"""

class Singleton(object):
    def __new__(cls, *args, **kwd):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kwd)
        return cls._instance


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    print(id(a), id(b))