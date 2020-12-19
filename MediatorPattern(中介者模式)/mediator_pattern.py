# _*_ coding:utf-8 _*_
import time
"""
中介者模式，用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。

和代理模式有点类似，代理模式是结构型模式，侧重于对对象调用的接口进行控制，而中介者模式是行为型模式，主要解决对象和对象之间相互调用的行为问题；
"""
from datetime import datetime


class ChatRoom(object):
    """中介者类"""
    @staticmethod
    def showMessage(user, message):
        print("%s [%s]:%s" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user, message))


class User(object):
    """用户类"""
    def __init__(self, name):
        self.name = name


    def getName(self):
        return self.name

    def sendMessage(self, message):
        return ChatRoom.showMessage(self.name, message)


if __name__ == "__main__":
    robert = User("Robert")
    bobo = User("BoBo")
    robert.sendMessage(" Hi! John")
    time.sleep(3)
    bobo.sendMessage(" Hello! Robert")










