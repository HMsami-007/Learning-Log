##The One-Argument RuleIf you pass only one list to plt.plot(), Matplotlib automatically assumes those numbers are your Y-axis (vertical) data points.
##The Two-Argument RuleIf you want to explicitly dictate what goes on the horizontal axis, you must pass two lists separated by a comma. The order is always X first, then Y:
import csv 
from datetime import datetime
from matplotlib import pyplot as plt
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs=[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red")
plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()   #The fourth-to-last line is fig.autofmt_xdate().This line automatically rotates and formats the date labels on the X-axis so they tilt diagonally and do not overlap with each other.
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
##Your graph plots 31 individual data points (one for every day in July). 
#However, if Matplotlib tried to print all 31 date labels along the bottom, the axis would still be too crowded, even with the text slanted.To keep things readable, Matplotlib automatically decides to only print a text label every 4 days (2014-07-01, 2014-07-05, 2014-07-09, etc.).
