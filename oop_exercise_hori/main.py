from vending import VendingMachine
from drink import DrinkEnum
from coin import Y100, Y500


def execute():
    vending_machine = VendingMachine()
    drink = vending_machine.buy(DrinkEnum.DIET_COKE, Y500())
    print(str(drink))
    coins = vending_machine.refund()
    print('お釣り：' + ' '.join([str(coin.value()) for coin in coins]))
    drink = vending_machine.buy(DrinkEnum.COKE, Y500())
    print(str(drink))
    drink = vending_machine.buy(DrinkEnum.COKE, Y100())
    print(str(drink))
    drink = vending_machine.buy(DrinkEnum.TEA, Y500())
    print(str(drink))
    coins = vending_machine.refund()
    print('お釣り：' + ' '.join([str(coin.value()) for coin in coins]))


if __name__ == "__main__":
    execute()
