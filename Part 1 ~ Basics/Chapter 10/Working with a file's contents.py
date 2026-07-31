Filename="SampleText.txt"
with open(Filename) as File:
    Lines=File.readlines()

PiString=""
for Line in Lines:
    PiString+=Line.rstrip()

print(PiString)
print(len(PiString))

PiString=""
for Line in Lines:
    PiString+=Line.strip()

print(PiString)
print(len(PiString))
