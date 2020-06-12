"""
Zaimplementuj klasy odpowiedzialne za różne typy promocji -
opartą o stałą wartość i procent od wartości.

Promocje można dodawać do koszyka.
Koszyk może mieć aktywnych wiele promocji.
Pamiętaj o obsłużeniu przypadku gdy wartość koszyka spadnie poniżej zera.

Przykład użycia:
basket = Basket()
discount = ValueDiscount(10.0)
basket.add_discount(discount)
"""

# Stworzyć klasę abstrakcyją discount (po co abstraKCYJNĄ?) zeby mozna jej bylo uzywac dla innych klas?
# KLasa ta będzie miała 2 abstraksyjne metody (oblicznie, calkowitej ceny oraz dodawanie znizek)
# stworzyć 2 klasy (2 rozne rodzaje znizek), ktore będą dziedziczyć po klasie abstrakcyjnej
# kazda z dwoch znizek będzie uzywała abstrakcyjnych metod do liczenia i dodawania
# dodajemy zniżki do koszyka - robimy lisę w klasie Basket poniewaz zniżki mogą się dodawać.
# tworzymy metodę dodawania zniżek do listy
# i teraz, kurwa, uważaj: w count total price robimy całą mechanikę dodawania zniżek. Czyli obliczmy calculate total_basket

from abc import ABC, abstractmethod


class Discount(ABC):
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def calculate(self, basket_total_price):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class AmountDiscount(Discount):
    def calculate(self, basket_total_price):
        return basket_total_price - self.value

    def __add__(self, other):
        return AmountDiscount(self.value + other.value)


class PercentageDiscount(Discount):
    def calculate(self, basket_total_price):
        return basket_total_price - basket_total_price * (self.value / 100)

    def __add__(self, other):
        return PercentageDiscount(self.value + other.value)


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
        self._discounts = []

    def add_discount(self, discount: Discount):
        self._discounts.append(discount)

    def add_products(self, product: Product, amount):
        if not product in self._items:
            self._items[product] = amount
        else:
            self._items[product] += amount

    def calkowita_cena(self):
        total_price = 0.0
        for product, amount in self._items.items():
            total_price += product.price * amount

        temp_ad = AmountDiscount(0)
        temp_pd = PercentageDiscount(0)

        for discount in self._discounts:
            if isinstance(discount, AmountDiscount):
                temp_ad += discount
            elif isinstance(discount, PercentageDiscount):
                temp_pd += discount

        total_price = temp_ad.calculate(total_price)
        total_price = temp_pd.calculate(total_price)

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
z1 = AmountDiscount(10)
# z2 = PercentageDiscount(20)
basket.add_discount(z1)
# basket.add_discount(z2)

# basket.calkowita_cena()

basket.wypisz_raport_koncowy()
