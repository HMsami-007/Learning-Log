import matplotlib.pyplot as plt
x_values=list(range(1,1001))    #In Python, list(range(1, 1001)) generates a complete, sequential list of integers starting from 1 and ending at 1000.
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)    #or use c=(0,0,0.8) a argument tuple with 3 decimal place values
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100, 0,1100000])
plt.show()