import matplotlib.pyplot as plt
from RandomWalkClass import RandomWalk
while True:
    RW=RandomWalk()
    RW.fill_walk()
    point_numbers=list(range(RW.num_points))
    plt.scatter(RW.x_values,RW.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(RW.x_values[-1],RW.y_values[-1],c='red',edgecolors='none',s=100)     #edgecolor and edgecolors is same just singular and plural difference. Just use edgecolors next time.
    plt.show()
    keep_running=input("Make another walk? (y/n):")
    if keep_running=='n':
        break