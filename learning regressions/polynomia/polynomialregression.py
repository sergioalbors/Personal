import numpy as np
import matplotlib.pyplot as plt
n = 100
x = np.random.uniform(-2, 2, n)
x = np.sort(x)
#x[0] = -1
#x[n-1]= 1

y = np.sin(2*x)  + 0.4*np.random.randn(n)

#lets start our regression 
degree = 6
X = X = np.vstack([x**i for i in range(degree + 1)]).T

r4 = np.array(degree+1)
r4 = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)),X.T),y)
yh4 = np.matmul(X, r4)

plt.scatter(x, y, label = "data")
plt.plot(x, yh4, color = 'red',  label = "prediccion de Speedy")
plt.legend()
plt.show()