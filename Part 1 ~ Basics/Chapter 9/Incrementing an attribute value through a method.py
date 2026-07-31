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


MyCar=Car('audi','a4',2016)            
print(MyCar.GetDescriptiveName())
MyCar.IncreamentMiles(120)
MyCar.ReadOdometer()