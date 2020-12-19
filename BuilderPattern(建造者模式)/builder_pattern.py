# coding=utf-8

"""
使用多个简单的对象一步一步构建成一个复杂的对象。
适用于一些基本部件不会变，而其组合经常变化的时候。
"""

from abc import ABCMeta, abstractmethod


class Iteam(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def packing(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Packing(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def pack(self):
        pass


class Wrapper(Packing):

    def __init__(self):
        pass
        # print("Wrapper object")

    @property
    def pack(self):
        return "Wrapper"


class Bottle(Packing):

    def __init__(self):
        pass
        # print("Bottle object")

    @property
    def pack(self):
        return "Bottle"


class Burger(Iteam):

    def packing(self):
        return Wrapper()

    def price(self):
        pass


class ColdDrink(Iteam):

    def packing(self):
        return Bottle()

    def price(self):
        pass


class VegBurger(Burger):

    def price(self):
        return 25.0

    def name(self):
        return "Veg Burger"


class ChickenBurger(Burger):

    def price(self):
        return 50.5

    def name(self):
        return "Chicken Burger"


class Coke(ColdDrink):

    def price(self):
        return 30.0

    def name(self):
        return "Coke"


class Pepsi(ColdDrink):

    def price(self):
        return 35.0

    def name(self):
        return "Pepsi"


class Meal(Iteam):

    def __init__(self):
        self.__iteams = []

    def add_iteam(self, iteam):
        self.__iteams.append(iteam)

    def get_cost(self):
        cost = 0
        for iteam in self.__iteams:
            cost += iteam.price()
        return cost

    def show_iteams(self):
        for iteam in self.__iteams:
            print("Iteam:{0}\nPacking:{1}\nPrice:{2}\n".
                  format(iteam.name(), iteam.packing().pack, iteam.price()))


class MealBuilder:

    def __init__(self):
        self.meal = Meal()

    def prepareveg_meal(self):
        self.meal.add_iteam(VegBurger())
        self.meal.add_iteam(Coke())
        return self.meal

    def preparez_nonveg_meal(self):
        self.meal.add_iteam(ChickenBurger())
        self.meal.add_iteam(Pepsi())
        return self.meal


if __name__ == "__main__":
    mealbuilder = MealBuilder()

    vegmeal = mealbuilder.prepareveg_meal()
    print("Veg Meal")
    vegmeal.show_iteams()
    print("Total Cost:{}\n".format(vegmeal.get_cost()))

    mealbuilder = MealBuilder()
    nonvegmeal = mealbuilder.preparez_nonveg_meal()
    print("Non-Veg Meal")
    nonvegmeal.show_iteams()
    print("Total Cost: {}\n".format(nonvegmeal.get_cost()))


