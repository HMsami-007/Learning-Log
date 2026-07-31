Filename="SampleText.txt"
with open(Filename) as File:
    for Line in File:
        print(Line.rstrip())