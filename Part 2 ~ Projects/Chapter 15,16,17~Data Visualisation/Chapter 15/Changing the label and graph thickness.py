import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
plt.plot(squares,linewidth=5)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14,length=10)
plt.show()

#To clear up the confusion completely, here is exactly what the part plt.tick_params(axis='both',labelsize=14) mean in plain language:
#The values/numbers on the axes = Matplotlib calls these labels (or tick_labels).
#The tiny dash marks next to the numbers = Matplotlib calls these ticks.