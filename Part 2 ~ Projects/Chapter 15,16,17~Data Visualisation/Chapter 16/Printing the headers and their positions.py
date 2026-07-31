import csv
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)


##The enumerate() function automatically numbers each item in your list as you loop through it.Instead of just giving you the column name, it paired each name with its exact column position index (starting at 0).

##When you run enumerate(header_row), Python secretly pairs up your headers like this behind the scenes:
# (0, 'STATION')
# (1, 'NAME')
# (2, 'DATE')
# (3, 'TMAX')