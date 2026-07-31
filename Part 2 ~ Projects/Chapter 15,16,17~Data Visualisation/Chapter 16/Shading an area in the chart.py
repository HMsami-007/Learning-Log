import csv 
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib import pyplot as plt
filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)    
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily high and low temperatures,2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()   #The fourth-to-last line is fig.autofmt_xdate().This line automatically rotates and formats the date labels on the X-axis so they tilt diagonally and do not overlap with each other.
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())              # Force a tick for every month
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))   # Force format to 'Jan 2014'
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()