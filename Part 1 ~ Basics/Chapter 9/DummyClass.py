class Car():
    def __init__(self,Make,Model,Year):
        self.Make=Make 
        self.Model=Model
        self.Year=Year
        self.Miles=0

    def GetDescriptiveName(self):
        LongName=str(self.Year)+" "+str(self.Make)+" "+str(self.Model)
        return LongName.title()

    def ReadOdometer(self):
        print(f"This car has {self.Miles} miles on it.")    

    def IncreamentMiles(self,Mileage):
        self.Miles+=Mileage

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,Make,Model,Year,Battery):
        super().__init__(Make,Model,Year)
        self.Battery=Battery

    def DescribeBattery(self):
        print(f"The car has {self.Battery} Kw of power in battery.")

    def FillGas(self):
        print("This car does not need gas.")
        