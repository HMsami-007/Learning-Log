Filename="SampleText.txt"
with open(Filename) as File:
    Lines=File.readlines()

for Line in Lines:
    print(Line.rstrip())