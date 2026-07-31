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
    def __init__(self,Make,Model,Year):
        super().__init__(Make,Model,Year)

MyTesla=ElectricCar("tesla","model s",2016)
print(MyTesla.GetDescriptiveName())