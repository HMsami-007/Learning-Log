import matplotlib.pyplot as plt
from RandomWalkClass import RandomWalk
while True:
    RW=RandomWalk()
    RW.fill_walk()
    plt.scatter(RW.x_values,RW.y_values,s=15)
    plt.show()
    keep_running=input("Make another walk? (y/n):")
    if keep_running=='n':
        break