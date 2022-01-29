from abc import ABC
from homework_02 import exceptions


class Vehicle:
    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # добавьте метод start, который, если ещё не состояние started,
    # проверяет, что топлива больше нуля, и обновляет состояние started,
    # иначе выкидывает исключение exceptions.LowFuelError
    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
                # print("Let's go!")
            else:
                raise exceptions.LowFuelError
        # else:
        #     print("Let's go!")

    # добавьте метод move, который проверяет, что достаточно топлива для
    # преодоления переданной дистанции, и изменяет количество оставшегося топлива,
    # иначе выкидывает исключение exceptions.NotEnoughFuel
    def move(self, distance):
        fuel = distance / self.fuel_consumption
        if self.fuel >= fuel:
            self.fuel = fuel
        else:
            raise exceptions.NotEnoughFuel

