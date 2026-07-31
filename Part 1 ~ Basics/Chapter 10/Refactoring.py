##Refactoring is breaking code into smaller and simpler functions so that code looks clean,understandable and simple.
import json
def GreetUser():
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

def GetStoredUsername():
    Filename="Username.json"
    try:
        with open(Filename) as File:
            Username=json.load(File)
    except FileNotFoundError:
        return None
    else:
        return Username
def GetNewUsername():
    Username=input("Enter your name:")
    Filename="Username.json"
    with open(Filename,"w") as File:
        json.dump(Username,File)
    return Username
GreetUser()    
            
                                           
