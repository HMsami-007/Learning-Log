def CountWords(Filename):
    try:
        with open(Filename) as File:
            Contents=File.read()
    except FileNotFoundError:
        Message="Sorry, the file does not exist."
        print(Message)
    else:
        Words=Contents.split()
        NumWords=len(Words)
        print(f"The file has {NumWords} words in total.")

Filename="Sample1.txt"
CountWords(Filename)
Filenames=["Sample1.txt","Siddart.txt","Sample2.txt"]
for Filename in Filenames:
    CountWords(Filename)