"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka.
Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka.
Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję.

Przykład użycia:
> basket = Basket()
> product = Product(1, 'Woda', 10.00)
> basket.add_product(product, 5)
> basket.count_total_price()
50.0
> basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
"""


# 1. Stwóz klsasę Product (id, nazwa produktu, cena
# 2. Stwórz klasę Basket, która jest po prosdtu słownikiem (__init__ dict)
# 3. Stwórz metodę, która będzie dodawała obiekty klasy Product (produkty) do koszyka w odpowiedniej ilości (na razie bez żadnych warunkó)
#         3.1 Dodaj warunki - jak juz jest jakis produkt to nie dodawaj (tylko zmien ilosc)
# 4. Stwórz metodę, która będzie liczyć całkowitą cenę za produkty
# 5. stwórz metodę, któa będzie generowała raport - rodzaj produktu, ilość cena całkkowita

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

    def add_products(self, product: Product, amount):
        if not product in self._items:
            self._items[product] = amount
        else:
            self._items[product] += amount

    def calkowita_cena(self):
        total_price = 0.0
        for product, amount in self._items.items():
            total_price += product.price * amount

        return total_price

    def wypisz_cene(self):
        print(f"{self.calkowita_cena()}")

    def wypisz_raport_koncowy(self):
        for product, amount in self._items.items():
            print(f"{product} x {amount}")
        print(f"Koszt: {self.calkowita_cena()}")


basket = Basket()
produkt1 = Product("1", "Pączek", 1.50)
produkt2 = Product("2", "Woda", 1.22)
basket.add_products(produkt1, 5)
basket.add_products(produkt1, 3)
basket.add_products(produkt2, 3)
# basket.calkowita_cena()

basket.wypisz_raport_koncowy()

# def test_cena():
#     basket = Basket()
#     produkt1 = Product("1", "Pączek", 1.50)
#     produkt2 = Product("2", "Woda", 1.22)
#     basket.add_products(produkt1, 5)
#     assert basket.calkowita_cena() == 7.5

