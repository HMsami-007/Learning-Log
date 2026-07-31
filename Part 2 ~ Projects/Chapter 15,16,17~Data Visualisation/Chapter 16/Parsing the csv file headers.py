import csv
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)

##You are completely right to think that. The name next() sounds like it should skip the first line and go straight to the second line.
# However, it gives you the very first line because of how Python initializes the reader:
#         -The reader starts at position zero: When you first create reader = csv.reader(f), it is sitting before any data has been read. No lines have been fetched yet.
#         -next() means "Give me the immediate next available item": Since no rows have been pulled out yet, the immediate next item available in the file stream is Row 1 (the headers).