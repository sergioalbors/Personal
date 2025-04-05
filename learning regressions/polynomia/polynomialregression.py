import numpy as np
import matplotlib.pyplot as plt
n = 100
x = np.random.uniform(-1, 1, n)
x = np.sort(x)
x[0] = -1
x[n-1] = 1

y = (x-.95)*(x-.2)*(x+.89)*(x-.9)*(x+.4)+ 0.1*np.random.randn(n)

#lets start our regression 
p = 4
X = np.vstack([np.ones(len(x)), x, x**2, x**3, x**4]).T

r4 = np.array(p+1)
r4 = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)),X.T),y)
yh4 = np.matmul(X, r4)

plt.scatter(x, y)
plt.plot(x, yh4)
plt.show()