def GetFormattedName(FirstName,LastName):
    FullName=FirstName + ' ' +LastName
    return FullName.title()
while True:
    print("Enter your names below and if you want to quit enter 'Quit' at any point------->")
    FirstName=input("Enter your first name:") 
    if FirstName=='Quit':
        break
    LastName=input("Enter your last name:") 
    if LastName=='Quit':
        break
    FormattedName=GetFormattedName(FirstName,LastName)
    print(f"Hello {FormattedName}!")