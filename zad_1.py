"""
Napisz klasę Osoba, która ma:
- atrybuty imie, nazwisko, wiek
- metode przedstaw_sie, ktora ma wypisac imie, nazwisko i wiek na konsole

Stworz dwie osoby:
- Jan Kowalski, 21 lat
- Ala Nowak, 30 lat

i niech się przedstawią
"""


class Osoba:
    def __init__(self, imie: str, nazwisko: str, wiek: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Cześć. Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")

    def pozegnaj_sie(self):
        print(f"{self.imie} mówi papa")



pierwsza_osoba = Osoba("Jan", "Kowalski", 35)
druga_osoba = Osoba("Krzystof", "Nowak", 57)

pierwsza_osoba.przedstaw_sie().przedstaw_sie()
druga_osoba.przedstaw_sie()

druga_osoba.pozegnaj_sie()