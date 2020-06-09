"""
KOlejna wersja koszyka, w którym robie zakupy, dodaje do koszyka w jakiejść ilości i liczę całkowitą cenę.
Dodaj metodę na wydawanie reszty zależne od podanej przez klienta kwoty.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}, cena: {self.price} zł"

    def __str__(self):
        return self.get_info()

class Basket:
    def __init__(self):
        self._items = dict()

    def add_product(self, product: Product, amount):
        if not isinstance(product, Product):
            raise TypeError("Product has to be in class Product")
        if product in self._items:
            self._items[product] += amount
        self._items[product] = amount
        return self._items

    # def remove_product(self, product: Product, amount):
    #     if product in self._items:
    #         self._items[product] -= amount

    # liczenie dodanych elementów
    def count_products(self):
        product_amount = 0
        for product, amount in self._items.items():
            product_amount += amount
        return product_amount

    def count_total_price(self):
        total_price = 0.0
        for product, amount in self._items.items():
            total_price += product.price * amount
        return total_price

    def generate_report(self):
        print(f"Produkty w koszyku:")
        for product, amount in self._items.items():
            print(f"- {product} x {amount}")
        print(f"Całkowity koszt: {self.count_total_price():.2f} zł")




basket = Basket()
p1 = Product("Jabłko", 1.20)
p2 = Product("Pączek", 1.50)
p3 = Product("Chleb", 4.30)
basket.add_product(p1, 5)
basket.add_product(p2, 4)
basket.add_product(p3, 3)
basket.generate_report()

# def test_adding():
#     basket = Basket()
#     p1 = Product("Jabłko", 1.20)
#     p2 = Product("Pączek", 1.50)
#     p3 = Product("Chleb", 4.30)
#     basket.add_product(p1, 5)
#     basket.add_product(p1, 5)
#     basket.add_product(p2, 3)
#     basket.add_product(p3, 2)
#     assert basket.count_products() == 10





