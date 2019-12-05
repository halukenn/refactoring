from vending import VendingMachine
from vending import Drink


def execute():
    vm = VendingMachine()

    drink = vm.buy(500, Drink.COKE)
    charge = vm.refund()

    if drink is not None and drink.kind == Drink.COKE:
        print("コーラを購入しました。")
        print("おつりは " + str(charge) + " 円です。")
    else:
        raise Exception("コーラ買えんかった(´ﾟдﾟ｀)")


if __name__ == "__main__":
    execute()
