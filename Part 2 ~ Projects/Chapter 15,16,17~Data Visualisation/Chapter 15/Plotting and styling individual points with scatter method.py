import matplotlib.pyplot as plt
plt.scatter(2,4,s=200)
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()

#The s stands for size (specifically, the area of the marker in points squared).It sets how large your plotted dot will look on the graph.Changing it to a higher number (like s=500) makes the dot bigger. Lowering it (like s=20) makes it tiny.
#Adding which='major' guarantees that your labelsize=14 change only affects the main numbers and ignores any minor sub-marks. Since your graph only has main numbers anyway, adding this doesn't change how your current graph looks, but it is good practice for advanced plots!
