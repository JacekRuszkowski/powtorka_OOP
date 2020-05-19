"""
Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu.
Zaimplementuj metodę wypisującą informację o produkcie na konsolę.

Przykład użycia:
product = Product(1, 'Woda', 10.99)
product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN

Scenariusz:
- tworzymy klase
- tworzymy metode __init__
    - uzupelniamy atrybuty
- tworzyme metode print_info()
- extra: dodać type hinting i dokumentcje metod
"""


class Product:
    def __init__(self, product: str, id: str, price: float):
        self.product = product
        self.id = id
        self.price = price

    def print_info(self):
        print(f"Produkt: {self.product}\nid: {self.id}\ncena: {self.price}")

    def get_info(self):
        return f"Produkt: {self.product}\nid: {self.id}\ncena: {self.price}"

    def __str__(self):
        return self.get_info()


woda = Product("Woda", "1", 5.88)

info = woda.get_info()

print(info)


def test_atrybutow():
    produkt = Product("Lód", "4", 7.45)
    assert produkt.product == "Lód"
    assert produkt.id == "4"
    assert produkt.price == 7.45


