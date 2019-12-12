from coin import CoinEnum
from coin import Y100
from drink import DrinkEnum
from drink import Coke
from drink import DietCoke
from drink import Tea


class DrinkRepository:

    quantity = {}

    def __init__(self):
        self.quantity[DrinkEnum.COKE] = [
            Coke(), Coke(), Coke(), Coke(), Coke()]
        self.quantity[DrinkEnum.DIET_COKE] = [
            DietCoke(), DietCoke(), DietCoke(), DietCoke(), DietCoke()]
        self.quantity[DrinkEnum.TEA] = [
            Tea(), Tea(), Tea(), Tea(), Tea()]

    def has_stock(self, drinkEnum):
        drink = self.quantity[drinkEnum]
        if not drink:
            return False
        return True

    def get(self, drinkEnum):
        drinks = self.quantity.get(drinkEnum)
        return drinks.pop(0)


class CoinRepository:

    coin_dic = {}

    def __init__(self):
        self.coin_dic[CoinEnum.Y100] = [Y100(), Y100(), Y100(), Y100(),
                                        Y100(), Y100(), Y100(), Y100(),
                                        Y100(), Y100()]

    def add(self, coin):
        coins = self.coin_dic.get(coin.no())
        if coins:
            coins.append(coin)
            return
        self.coin_dic[coin.no()] = [coin]

    def num(self, coin_enum):
        coins = self.coin_dic.get(coin_enum)
        if not coins:
            return 0
        return len(coins)

    def get(self, coin_enum, num):
        coins = self.coin_dic.get(coin_enum)
        result = []
        for _ in range(num):
            result.append(coins.pop(0))
        return result


class UserCoin:

    inserted_coins = []
    changes = []

    def put(self, inserted_coin):
        self.inserted_coins.append(inserted_coin)

    def add_change(self, coins):
        self.changes.extend(coins)

    def accept(self):
        if not self.inserted_coins:
            return None
        return self.inserted_coins.pop()

    def refund(self):
        refund = []
        refund.extend(self.changes)
        self.changes = []
        refund.extend(self.inserted_coins)
        self.inserted_coins = []
        return refund


class Payment:

    def __init__(self):
        self._user_coin = UserCoin()
        self._coin_repository = CoinRepository()

    def put(self, inserted_coin, has_stock):
        if not has_stock or not self.has_change(inserted_coin):
            self._user_coin.add_change([inserted_coin])
            return
        self._user_coin.put(inserted_coin)

    def has_change(self, inserted_coin):
        if inserted_coin.no() == CoinEnum.Y100:
            return True
        if inserted_coin.no() == CoinEnum.Y500 \
                and self._coin_repository.num(CoinEnum.Y100) > 4:
            return True
        return False

    def transaction(self):
        coin = self._user_coin.accept()
        if coin is None:
            return False
        self._coin_repository.add(coin)
        if coin.no() == CoinEnum.Y500:
            coins = self._coin_repository.get(CoinEnum.Y100, 4)
            self._user_coin.add_change(coins)
        return True

    def refund(self):
        return self._user_coin.refund()


class VendingMachine:

    def __init__(self):
        self._payment = Payment()
        self._drink_repository = DrinkRepository()

    def buy(self, drink_enum, coin):
        has_stock = self._drink_repository.has_stock(drink_enum)
        self._payment.put(coin, has_stock)
        result = self._payment.transaction()
        if not result:
            return None
        return self._drink_repository.get(drink_enum)

    def refund(self):
        return self._payment.refund()
