from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
from scipy import integrate
fig = plt.figure()
style.use('ggplot')
ax = plt.axes(projection = '3d') # 3d graph projection
plt.title("Graph Of A Multi-Variable Function\nf(x, y)")
def f(x, y):
    return np.sin(x**2+y**2)
    
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X,Y) #defines the value of Z as the output of the function f
ax.contour3D(X,Y,Z, 50, cmap='viridis') # purple is the lowest point, bright green is highest point
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(30, 60)   #change the angle you view at
fig.show()
g = lambda x, y: np.sin(x**2) + np.sin(y**2)
i, j = integrate.dblquad(g, 0, 2, lambda y: 0, lambda y: 2)
print("The volume of this function in the given bounds is",i, "units cubed")#gives you area 

#This simulation and graph can tell physicists a lot about charge distribution of a certain function, or give them an idea of where the center of mass is potentially located
#this type of distribution can be used in statistics as well
