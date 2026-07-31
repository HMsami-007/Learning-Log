import matplotlib.pyplot as plt
from RandomWalkClass import RandomWalk
while True:
    RW=RandomWalk()
    RW.fill_walk()
    point_numbers=list(range(RW.num_points))
    plt.scatter(RW.x_values,RW.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(RW.x_values[-1],RW.y_values[-1],c='red',edgecolors='none',s=100)     #edgecolor and edgecolors is same just singular and plural difference. Just use edgecolors next time.
    # 1. Grab the active layout first
    ax = plt.gca() 
    # 2. Hide the axes using that specific layout layer
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("Make another walk? (y/n):")
    if keep_running=='n':
        break


##The issue is caused by calling plt.axes() multiple times on lines 10 and 11.
# Every time you call plt.axes(), Matplotlib creates a brand-new, empty set of axes and stacks it directly on top of your previous plot. 
# This is hiding your random walk data under blank layers and scrambling the axis numbers.
# The FixInstead of creating new axes, you need to grab the current active axes using plt.gca() (Get Current Axes).
# Change lines 10 and 11 to this:ax = plt.gca() 
                                 # 2. Hide the axes using that specific layout layer
                                 #ax.get_xaxis().set_visible(False)
                                 #ax.get_yaxis().set_visible(False)

#An Even Simpler AlternativeIf your goal is to completely hide both axes and the surrounding border box, you can replace both of those lines with a single, much cleaner command:
#plt.axis('off')
