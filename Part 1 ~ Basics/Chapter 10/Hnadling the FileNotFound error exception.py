Filename="Alice.txt"
try:
    with open(Filename) as File:
        Contents=File.read()
except FileNotFoundError:
    print("File not found or does not exist")