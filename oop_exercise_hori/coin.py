from abc import ABCMeta, abstractmethod
from enum import Enum


class CoinEnum(Enum):
    Y100 = 0
    Y500 = 1


class Coin(metaclass=ABCMeta):
    @abstractmethod
    def no(self):
        pass

    @abstractmethod
    def value(self):
        pass


class Y100(Coin):

    def no(self):
        return CoinEnum.Y100

    def value(self):
        return 100


class Y500(Coin):

    def no(self):
        return CoinEnum.Y500

    def value(self):
        return 500
