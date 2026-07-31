Responses={}
PollingActive=True
while PollingActive:
    Name=input("Enter Your Name:")
    Response=input("Enter the mountain name you would like to climb:")
    Responses[Name]=Response
    Repeat=input("Do you want to continue? Yes or No --->")
    if Repeat=='No':
        PollingActive=False


print("\n-----Poll Results------")
for Name,Response in Responses.items():
    print(f"{Name} wants to climb Mount {Response}")