import csv
from matplotlib import pyplot as plt
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    highs=[]
    for row in reader:   #The loop looks at where the pointer is currently waiting (which is the start of Row 2). It automatically calls the internal equivalent of next(reader) for you.
        highs.append(int(row[1]))

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')
plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()

##Step 3: Drawing the Line (plt.plot(...))
##    -plt.plot(highs, c='red'): Because you only passed a single list (highs), Matplotlib automatically treats it as the Y-axis values.
##    -Automatic X-axis: For the missing X-axis parameters, Matplotlib automatically generates sequential index numbers matching the list position, running from 0 to 30 (representing the index points of the 31 days in July).
##    -c='red': Dictates that the connected path between those coordinates must be colored red.
    