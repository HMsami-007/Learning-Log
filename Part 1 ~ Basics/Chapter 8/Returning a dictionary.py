def BuildPerson(FirstName,LastName,Age=""):
    Person={'First Name': FirstName,'Last Name':LastName}
    if Age:
        Person['Age']=Age
    return Person

print(BuildPerson('Jimi','hendrix',Age=27))    