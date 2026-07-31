class Car():
    def __init__(self,Make,Model,Year):
        self.Make=Make 
        self.Model=Model
        self.Year=Year

    def GetDescriptiveName(self):
        LongName=str(self.Year)+" "+str(self.Make)+" "+str(self.Model)
        return LongName.title()

MyCar=Car('audi','a4',2016)            
print(MyCar.GetDescriptiveName())