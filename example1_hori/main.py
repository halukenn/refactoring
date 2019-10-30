from video_rental import Movie
from video_rental import Customer
from video_rental import ChildrenPrice
from video_rental import RegularPrice
from video_rental import NewReleasePrice


def execute():
    customer = Customer('TestCustomer')
    customer.add_rental(Movie('child1', ChildrenPrice()), 5)
    customer.add_rental(Movie('child2', ChildrenPrice()), 2)
    customer.add_rental(Movie('regular', RegularPrice()), 3)
    customer.add_rental(Movie('new1', NewReleasePrice()), 3)
    customer.add_rental(Movie('new2', NewReleasePrice()), 4)
    print(customer.statement())


if __name__ == "__main__":
    execute()
