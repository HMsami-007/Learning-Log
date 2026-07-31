def DescribePet(AnimalType,PetName):
    """Display information about a pet"""
    print("\nI have a " + AnimalType + "." )
    print(f"My {AnimalType}'s name is {PetName}.")

DescribePet('Hamster','Harry')