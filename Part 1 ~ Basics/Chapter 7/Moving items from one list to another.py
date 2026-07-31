UncomfirmedUsers=['Alice','Brian','Candace']
ConfirmedUsers=[]
while UncomfirmedUsers:
    CurrentUser=UncomfirmedUsers.pop()
    print(f"Verifying user:{CurrentUser}")
    ConfirmedUsers.append(CurrentUser)

print("\nThe following users have been verified:")
for Count in range(len(ConfirmedUsers)):
    print(ConfirmedUsers[Count])
