def GetFormattedName(FirstName,LastName,MiddleName=""):
    if MiddleName:
        FullName=FirstName + ' ' + MiddleName + ' ' + LastName
    else:
        FullName=FirstName + ' ' + LastName
    return FullName.title()

print(GetFormattedName('jimi','hendrix'))
print(GetFormattedName('john','hooker','lee'))    