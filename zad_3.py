"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy
oraz wypłacanie pensji na podstawie zadanej stawki godzinowej.
Jeżeli pracownik będzie pracował więcej niż 8 godzin (podczas pojedynczej rejestracji czasu)
to kolejne godziny policz jako nadgodziny (z podwójną stawką godzinową).

Przykład użycia:
employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.pay_salary()
500.0
employee.pay_salary()
0.0
employee.register_time(10)
employee.pay_salary()
1200.0

UML: http://yuml.me/diagram/nofunky;scale:180/class/edit/%5BEmployee%7Cfirst_name:%20str;last_name:%20str;rate:%20float%7Cregister_time(hours:%20float);pay_salary():%20float%5D
"""


class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.work_time = 0.0
        self.work_time_overhours = 0.0



    def register_time(self, hours: float):
        if hours <= 8:
            self.work_time += hours
        else:
            self.work_time += 8
            self.work_time_overhours = self.work_time_overhours + hours - 8

    def pay_salary(self) -> float:
        salary = self.work_time * self.rate
        salary = salary + 2 * self.rate * self.work_time_overhours

        self.work_time = 0.0  # trzeba wyzerować work time, żeby nie liczył cały czas nadgodzin
        self.work_time_overhours = 0

        return salary


pracownik_1 = Employee("Jan", "Kowalski", 100)
pracownik_1.register_time(12)


print(pracownik_1.pay_salary())


def test_zwykle_godziny():
    emp1 = Employee("Jan", "Kowalski", 100)
    emp1.register_time(8)
    assert emp1.pay_salary() == 800.0


def test_dwie_wyplaty():
    emp1 = Employee("Jan", "Kowalski", 100)
    emp1.register_time(10)
    assert emp1.pay_salary() == 1200.0
    assert emp1.pay_salary() == 0.0


def test_nadgodziny():
    emp1 = Employee("Jan", "Kowalski", 100)
    emp1.register_time(12)
    assert emp1.pay_salary() == (8 * 100.0 + 4 * 100.0 * 2)

def test_dwa_dni_pracy():
    emp1 = Employee("Jan", "Kowalski", 100)
    emp1.register_time(12)
    emp1.register_time(5)
    assert emp1.pay_salary() == 2100.0


