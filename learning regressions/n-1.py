import numpy as np
import matplotlib.pyplot as plt
n = 10
x = np.random.uniform(0, 100, n)
y = np.random.uniform(-100,100, n) 
#a = np.polyfit(x, y, n-1)

V = np.vander(x, N=len(x), increasing = False)
# v*a=y
a = np.linalg.solve(V, y)
polinomio = np.poly1d(a)

x_fit = np.linspace(min(x), max(x), 100)
y_fit = polinomio(x_fit)

plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.show()
print(polinomio)