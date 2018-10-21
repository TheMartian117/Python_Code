from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
from scipy import integrate
fig = plt.figure()
style.use('ggplot')
ax = fig.add_subplot(2, 1, 1, projection = '3d') # 3d graph projection
plt.title("Graph Of A Multi-Variable Function\nf(x, y)\nLook at the console for more details")
def f(x, y):
    return np.sin(x**2)+np.sin(y**2)
    
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
print("This is a multi-variable function represent by the equation sin(x^2)+sin(y^2)")
print("The volume of this function in the given bounds is",i, "units cubed. This function models real life situations that happen periodically, and knowing the area under the curve, helps scientists figure out meaningful statistics such as impulse (the area/volume under the curve) ")#gives you area 
#===========Second Subplot======================#
#========Calculate Mass or Combined Charge======#

ax = fig.add_subplot(2, 1, 2, projection='3d')
plt.title("Finding the mass\nof a lamina using physics")
x = [0, 0, 1, 0]
y = [0, 1, 0, 0]
x1 = [0, 0, 1, 1, 0, 0 ]
y1 = [0, 0, 0, 0, 1, 1]
z1 = [-0.06, 0, -0.06, 0, -0.06, 0]
# plot a 3D wireframe 
plt.plot(x, y)
plt.plot(x1, y1, z1)
def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    text.set_position((xdata[ind], ydata[ind]))
    text.set_text(zip(xdata[ind], ydata[ind]))
fig.canvas.mpl_connect('pick_event', onpick)

fig.show()
plt.show()
one_var = lambda x: ((1-x)**2)/2
mass_lamina, e = integrate.quad(one_var)
print("The mass of this lamina, given the density function of p(x, y) = d, is", mass_lamina, ", To find this, you need to look at the coordinates of the lamina, then take the integral of the function taking into consideration the domain.")
print("Also, you could think of this as the combined charge of the lamina, and the density function could be the charge distribution")
#This simulation and graph can tell physicists a lot about charge distribution of a certain function, or give them an idea of where the center of mass is potentially located
#this type of distribution can be used in statistics as well
