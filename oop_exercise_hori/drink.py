from abc import ABCMeta, abstractmethod
from enum import Enum


class DrinkEnum(Enum):
    COKE = 0
    DIET_COKE = 1
    TEA = 2


class Drink(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        pass


class Coke(Drink):

    def name(self):
        return 'Coke'

    def __str__(self):
        return self.name()


class DietCoke(Drink):

    def name(self):
        return 'DietCoke'

    def __str__(self):
        return self.name()


class Tea(Drink):

    def name(self):
        return 'Tea'

    def __str__(self):
        return self.name()
