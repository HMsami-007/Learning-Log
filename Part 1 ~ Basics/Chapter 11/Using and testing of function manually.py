from DummyFunction import GetFormattedName
print("Enter 'Quit' at any time to quit.")
while True:
    First=input("\nPlease enter the first name:")
    if First=="Quit":
        break
    Last=input("\nPlease enter the last name:")
    if Last=="Quit":
        break
    FormattedName=GetFormattedName(First,Last)
    print("Formatted Name:",FormattedName)
