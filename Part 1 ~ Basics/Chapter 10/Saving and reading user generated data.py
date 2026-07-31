import json
Filename="Username.json"
try:
    with open(Filename) as File:
        Username=json.load(File)
except FileNotFoundError:
    Username=input("Enter your name:")
    with open(Filename,"w") as File:
        json.dump(Username,File)
        print(f"We will remember you when you come back {Username}.")
else:
    print(f"Welcome back {Username}!")