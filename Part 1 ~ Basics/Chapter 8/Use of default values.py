def DescribePet(PetName,AnimalType="dog"):
    print(f"I have a {AnimalType}.")
    print(f"My {AnimalType}'s name is {PetName}.")

DescribePet(PetName="Leo")
DescribePet("Leo")
DescribePet(PetName="Sharon",AnimalType="Kangaroo")
DescribePet("Pinky","cat")