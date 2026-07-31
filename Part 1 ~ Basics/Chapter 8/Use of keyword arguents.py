def DescribePet(AnimalType,PetName):
    """Display information about pets"""    #It is called docstring
    print(f"I have a {AnimalType}.")
    print(f"My {AnimalType}'s name is {PetName}.")

DescribePet(AnimalType="dog",PetName="Leo")
DescribePet(PetName="Leo",AnimalType="dog")