class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,Name,Age):
        """Initialize name and age attributes"""
        self.Name=Name
        self.Age=Age

    def Sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.Name.title() + " is now sitting.")

    def RollOver(self):
        """Simulate rolling over in response to a command"""
        print(self.Name.title()+ " rolled over!")        

MyDog=Dog("willie",6)
print("My dog's name is " + MyDog.Name.title()+ ".")
print(f"My dog's age is {MyDog.Age} years old.")