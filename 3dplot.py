import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.linspace(-5,5)
Y = np.linspace(-5,5)

X,Y = np.meshgrid(X,Y)


ax.plot_surface(X,Y,Y)
ax.plot_surface(X,Y,X)




plt.show()
