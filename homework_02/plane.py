"""
создайте класс `Plane`, наследник `Vehicle`
"""
# в модуле plane создайте класс Plane
# класс Plane должен быть наследником Vehicle
# добавьте атрибуты cargo и max_cargo классу Plane
# добавьте max_cargo в инициализатор (переопределите родительский)

# объявите метод load_cargo, который принимает число, проверяет,
# что в сумме с текущим cargo не будет перегруза,
# и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload

# объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, started, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, started, fuel, fuel_consumption, max_cargo)
        self.max_cargo = max_cargo

    def load_cargo(self, number=int):
        if self.cargo + number > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += number

    def remove_all_cargo(self):
        return self.cargo
        self.cargo = 0
