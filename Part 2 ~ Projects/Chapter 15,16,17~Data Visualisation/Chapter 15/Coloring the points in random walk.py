import matplotlib.pyplot as plt
from RandomWalkClass import RandomWalk
while True:
    RW=RandomWalk()
    RW.fill_walk()
    point_numbers=list(range(RW.num_points))
    plt.scatter(RW.x_values,RW.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    plt.show()
    keep_running=input("Make another walk? (y/n):")
    if keep_running=='n':
        break