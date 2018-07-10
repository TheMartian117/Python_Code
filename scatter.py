import random as r
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
x = np.arange(11)
y = [1, 5, 25, 125, 13, 28, 54, 62, 12, 21, 26]

b,m = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.title("Line Of Best Fit")
plt.xlabel("X-Coordinates")
plt.ylabel("Y-Coordinates")
plt.plot(x, b + m * x, '-', label="Line of Best Fit", color="r")
plt.legend()
print("Best Fit:", m, "x+", b)
plt.show()
