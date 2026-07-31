import matplotlib.pyplot as plt
from RandomWalkClass import RandomWalk
while True:
    RW=RandomWalk(50000)
    RW.fill_walk()
    point_numbers=list(range(RW.num_points))
    plt.figure(dpi=128,figsize=(10,6))    #or plt.figure(figsize=(10,6))   #Should be at beginning before scatter as Yes, exactly! plt.figure(figsize=(10, 6)) tells Matplotlib to create a brand-new window frame with a specific width and height before you draw anything inside it.
    plt.scatter(RW.x_values,RW.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
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