import json
Numbers=[1,2,3,4,5,6,7,8,9,10]
Filename="Numbers.json"
with open(Filename,"w") as File:
    json.dump(Numbers,File)