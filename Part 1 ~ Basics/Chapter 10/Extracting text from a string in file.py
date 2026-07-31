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
print(PiString[:5]+"......")     ##The slice does extract exactly 5 characters, but it only looks like 4 digits because the decimal point (.) counts as a character.