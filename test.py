import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256)

sine = np.sin(x)
cosine = np.cos(x)

plt.plot(x,sine,color="r")
plt.plot(x,cosine,color="b")
#plt.plot(x,x**2)

#Punto
t = np.pi/ 4
plt.plot([t,t],[np.sin(t),0], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),],color="b")

plt.annotate(r"$\sin(\frac{\pi}{4})$" ,fontsize=16, xy=(t,np.sin(t)),xytext=(+0, +35),
             textcoords="offset points",
             arrowprops=dict(arrowstyle="->")
             )

##Axes
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

#ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data",0))

#ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data",0))


plt.legend()

plt.show()
