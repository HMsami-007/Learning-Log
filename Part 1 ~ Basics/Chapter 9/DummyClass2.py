from DummyClass import Car
class Battery():
    def __init__(self,BatterySize=70):
        self.BatterySize=BatterySize

    def DescribeBattery(self):
        print(f"This car has {self.BatterySize} Kwh of battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,Make,Model,Year):
        super().__init__(Make,Model,Year)
        self.battery=Battery()

    def FillGas(self):
        print("This car does not need gas.")