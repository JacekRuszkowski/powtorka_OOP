# bez sumowania zniżek. Promocje nie łączą się

from abc import ABC, abstractmethod


# class Discount(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def calculate(self, basket_total_price):
#         pass
#
#
# class AmountDiscount(Discount):
#     def calculate(self, basket_total_price):
#         return basket_total_price - self.value
#
#
# class PercentageDiscount(Discount):
#     def calculate(self, basket_total_price):
#         return basket_total_price - basket_total_price * (self.value / 100)


class Product:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self):
        return f"({self.id}){self.name}, cena: {self.price}"

    def __str__(self):
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = dict()
        self._discount = []

    def add_products(self, product: Product, amount):
        if not product in self._items:
            self._items[product] = amount
        else:
            self._items[product] += amount

    def add_discount(self, discount):
        self._discount.append(discount)

    def calkowita_cena(self):
        total_price = 0.0
        for product, amount in self._items.items():
            total_price += product.price * amount

        for discount in self._discount:
            total_price -= discount

        return total_price

    def wypisz_cene(self):
        print(f"{self.calkowita_cena()}")

    def wypisz_raport_koncowy(self):
        for product, amount in self._items.items():
            print(f"{product} x {amount}")
        print(f"Koszt: {self.calkowita_cena():.2f}")


basket = Basket()
produkt1 = Product("1", "Pączek", 1.50)
produkt2 = Product("2", "Woda", 1.22)
basket.add_products(produkt1, 5)
basket.add_products(produkt1, 3)
basket.add_products(produkt2, 3)
basket.add_discount(5)

basket.wypisz_raport_koncowy()


def test_discount():
    basket = Basket()
    produkt1 = Product("1", "Pączek", 1.50)
    produkt2 = Product("2", "Woda", 1.22)
    basket.add_products(produkt1, 5)
    basket.add_products(produkt1, 3)
    basket.add_products(produkt2, 3)
    basket.add_discount(10)
