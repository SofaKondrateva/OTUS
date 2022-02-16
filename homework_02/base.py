from abc import ABC
from homework_02 import exceptions


class Vehicle:
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # добавьте метод start, который, если ещё не состояние started,
    # проверяет, что топлива больше нуля, и обновляет состояние started,
    # иначе выкидывает исключение exceptions.LowFuelError
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    # добавьте метод move, который проверяет, что достаточно топлива для
    # преодоления переданной дистанции, и изменяет количество оставшегося топлива,
    # иначе выкидывает исключение exceptions.NotEnoughFuel
    def move(self, distance):
        if self.fuel >= distance * self.fuel_consumption:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel

