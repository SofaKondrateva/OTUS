"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, message='Low Fuel!'):  # errors
        super().__init__(message)
        # self.errors = errors


class NotEnoughFuel(Exception):
    def __init__(self, message='Not enough fuel!'):  # errors):
        super().__init__(message)
        # self.errors = errors


class CargoOverload(Exception):
    def __init__(self, message='Cargo Over load'):  # errors):
        super().__init__(message)
        # self.errors = errors
