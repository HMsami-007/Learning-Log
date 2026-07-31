def BuildProfile(FirstName,LastName,**UserInfo):
    Profile={}
    Profile['First']=FirstName
    Profile['Last']=LastName
    for Key,Value in UserInfo.items():
        Profile[str(Key)]=Value
    return Profile

print(BuildProfile('Albert','Einstein',Location='Princeton',Field='Physics'))    ##You cannot put quotes around Location and Field inside the function call because they are keyword arguments, not string literals.In Python, keyword arguments must follow the exact same naming rules as variable names.