import os


class Point:

    def __init__(self, default_point=1):
        self._default_point = default_point

    def get(self, days_rented):
        return self._default_point


class NewReleasePoint(Point):

    def __init__(self):
        super().__init__()

    def get(self, days_rented):
        if days_rented > 1:
            return self._default_point + 1
        return self._default_point


class Price:

    def __init__(self, point, default_price=0.0):
        self._point = point
        self._default_price = default_price

    def get(self, days_rented):
        pass

    def get_point(self, days_rented):
        return self._point.get(days_rented)


class ChildrenPrice(Price):

    def __init__(self, default_price=1.5):
        super().__init__(Point(), default_price)

    def get(self, days_rented):
        if days_rented > 3:
            return self._default_price + (days_rented - 3) * 1.5
        return self._default_price


class RegularPrice(Price):

    def __init__(self, default_price=2.0):
        super().__init__(Point(), default_price)

    def get(self, days_rented):
        if days_rented > 2:
            return self._default_price + (days_rented - 2) * 1.5
        return self._default_price


class NewReleasePrice(Price):

    def __init__(self):
        super().__init__(NewReleasePoint())

    def get(self, days_rented):
        return days_rented * 3

    def get_point(self, days_rented):
        return self._point.get(days_rented)


class Movie:

    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    def price(self, days_rented):
        return self.__price.get(days_rented)

    def point(self, days_rented):
        return self.__price.get_point(days_rented)

    @property
    def title(self):
        return self.__title


class Rental:

    def __init__(self, movie, days_rented):
        self.__movie = movie
        self.__days_rented = days_rented

    @property
    def title(self):
        return self.__movie.title

    def price(self):
        return self.__movie.price(self.__days_rented)

    def point(self):
        return self.__movie.point(self.__days_rented)


class Customer:

    rentals = []
    results = []

    def __init__(self, name):
        self.__name = name
        self.results.append('Rental Record for ' + name)

    def add_rental(self, movie, days_rented):
        self.rentals.append(Rental(movie, days_rented))

    def statement(self):
        self.results.append('Amount owed is ' + str(self.total_price()))
        self.results.append(
            'You earned ' + str(self.total_point()) + ' frequent renter points')
        return os.linesep.join([str(result) for result in self.results])

    def total_price(self):
        total_price = 0.0
        for rental in self.rentals:
            price = rental.price()
            self.results.append('\t' + rental.title + '\t' + str(price))
            total_price += price
        return total_price

    def total_point(self):
        total_point = 0
        for rental in self.rentals:
            total_point += rental.point()
        return total_point
