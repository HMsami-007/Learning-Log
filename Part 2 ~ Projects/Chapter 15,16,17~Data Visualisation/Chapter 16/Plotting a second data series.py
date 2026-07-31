import csv 
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib import pyplot as plt
filename='sitka_weather_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
        low=int(row[3])
        lows.append(low)    
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red")
plt.plot(dates,lows,c="blue")
plt.title("Daily high and low temperatures,2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()   #The fourth-to-last line is fig.autofmt_xdate().This line automatically rotates and formats the date labels on the X-axis so they tilt diagonally and do not overlap with each other.
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())              # Force a tick for every month
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))   # Force format to 'Jan 2014'
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()