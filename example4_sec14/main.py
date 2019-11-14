from save_user_info import Database
from save_user_info import AddressFile


def execute():
    file = AddressFile('address.txt')
    file.database.set('Yuki', 'hyuki@example.com')
    file.database.set('Tomura', 'tomura@example.com')
    file.database.set('Hanako', 'hanako@example.com')
    file.database.update()

    for name in file.names():
        email = file.database.get(name)
        print('name={}, email={}'.format(name, email))


if __name__ == "__main__":
    execute()
