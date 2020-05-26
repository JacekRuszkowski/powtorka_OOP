"""
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego.
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu
zdefiniowanego dla samochodu. Samochód powinien mieć także możliwość naładowania baterii.

car = ElectricCar(100)
car.drive(70)
70
car.drive(50)
30
car.drive(50)
0
car.charge()
car.drive(50)
50

UML: http://yuml.me/diagram/nofunky;scale:180/class/edit/%5BElectricCar%7Cmax_range:%20int;%20battery_level:%20int%7C__init__(max_range:%20int);%20charge();%20drive(distance:%20int):%20int%5D
"""
# jak przesuwanie głazów.
# teraz wymyśl metodę do ładowania.

class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.battery_level = max_range

    def drive(self, distance):
        if distance <= self.max_range:
            self.max_range -= distance

        else:
            distance = self.max_range
            self.max_range = 0

        return distance

    def charge(self):
            self.max_range = self.battery_level



car = ElectricCar(100)
print(car.drive(90))
print(car.drive(15))
print(car.drive(30))
car.charge()
print(car.drive(110))
print(car.drive(80))
car.charge()
print(car.drive(80))

def test_zasieg():
    auto = ElectricCar(200)
    assert auto.drive(200) == 200

def test_poza_zasiegiem():
    auto = ElectricCar(200)
    assert auto.drive(250) == 200

def test_battery_charge():
    auto = ElectricCar(200)
    auto.drive(200)
    assert auto.drive(40) == 0
    auto.charge()
    assert auto.drive(40) == 40

def test_random_drive():
    auto = ElectricCar(200)
    assert auto.drive(110) == 110
    assert auto.drive(80) == 80
    assert auto.drive(10) == 10


