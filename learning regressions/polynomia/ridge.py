import numpy as np
import matplotlib.pyplot as plt
n = 100
x = np.random.uniform(-2, 2, n)
x = np.sort(x)

def f(x):
    return np.sin(2*x)
y = f(x)
y_t = f(x) + 10*np.random.randn(n)
degree = 6
X = np.vstack([x**i for i in range(degree + 1)]).T
alpha = 1

I = np.eye(X.shape[1])
I[0, 0] = 0
#r4 = np.matmul(np.linalg.inv(np.matmul(X.T, X) + alpha * I ),np.matmul(X.T, y_t))
r4 = np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, y_t))
yh4 = np.matmul(X, r4)

plt.scatter(x, y, label = 'data')
plt.plot(x, yh4, color = 'red', label = 'predicted values')
plt.legend()
plt.show()
