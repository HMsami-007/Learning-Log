class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,Name,Age):
        """Initialize name and age attributes"""
        self.__Name=Name
        self.__Age=Age

    def Sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.__Name.title() + " is now sitting.")

    def RollOver(self):
        """Simulate rolling over in response to a command"""
        print(self.__Name.title()+ " rolled over!")        

