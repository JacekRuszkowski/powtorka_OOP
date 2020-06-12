"""
Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee.
Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi.

> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
> employee.register_time(5)
> employee.give_bonus(1000.0)
> employee.pay_salary()
1500.0

UML: http://yuml.me/preview/7416f5e4
"""

#
# class Employee:
#     def __init__(self, first_name: str, last_name: str, rate: float):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.rate = rate
#         self.work_time = 0.0
#         self.work_time_overhours = 0.0
#
#     def register_time(self, hours: float):
#         if hours <= 8:
#             self.work_time += hours
#         else:
#             self.work_time += 8
#             self.work_time_overhours = self.work_time_overhours + hours - 8
#
#     def pay_salary(self) -> float:
#         salary = self.work_time * self.rate
#         salary = salary + 2 * self.rate * self.work_time_overhours
#
#         self.work_time = 0.0  # trzeba wyzerować work time, żeby nie liczył cały czas nadgodzin
#         self.work_time_overhours = 0
#
#         return salary

from zad_3 import Employee


class PremiumEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, rate: float):
        super().__init__(first_name, last_name, rate)
        self.bonus = 0.0

    def daj_bonus(self, bonus_amount: float):
        self.bonus += bonus_amount

    def pay_salary(self) -> float:
        salary = super().pay_salary()
        salary += self.bonus
        return salary


Jacek = PremiumEmployee("Jacek", "Ruszkowski", 150.00)
Jacek.register_time(12)
Jacek.daj_bonus(1000.0)
print(Jacek.pay_salary())
