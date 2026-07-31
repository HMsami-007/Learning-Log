import csv
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    highs=[]
    for row in reader:   #The loop looks at where the pointer is currently waiting (which is the start of Row 2). It automatically calls the internal equivalent of next(reader) for you.
        highs.append(int(row[1]))
    print(highs)

##The file reader pointer is initialized at the absolute beginning of the file (index 0), right before the first character of the header row.
#When Python executes next(reader), the reader tool scans forward through the text, character by character, consuming everything it sees. It keeps reading until it hits the first newline marker (\n).
#The reader stops scanning right after the newline character. It packages everything it just scanned into a list (['STATION', 'NAME', 'DATE', 'TMAX']) and assigns it to header_row.The file pointer is left resting at the very next character, which happens to be the start of Row 2.