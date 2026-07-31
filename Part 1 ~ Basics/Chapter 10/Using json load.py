import json 
Filename="Numbers.json"
with open(Filename) as File:
    Numbers=json.load(File)
print(Numbers)