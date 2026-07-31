from random import randint
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        return randint(1,self.num_sides)      #randint returns an integer from 1 to num_sides=6 inclusive