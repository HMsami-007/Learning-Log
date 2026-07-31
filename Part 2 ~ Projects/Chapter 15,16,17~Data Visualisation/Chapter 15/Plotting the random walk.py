import matplotlib.pyplot as plt
from RandomWalkClass import RandomWalk
RW=RandomWalk()
RW.fill_walk()
plt.scatter(RW.x_values,RW.y_values,s=15)
plt.show()