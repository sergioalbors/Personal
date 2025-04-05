import numpy as np
import matplotlib.pyplot as plt
n = 100
x = np.random.uniform(-1,1,n)
y = (x-.95)*(x-.2)*(x+.89)*(x-.9)*(x+.4)+ 0.1*np.random.randn(n)
p = 4
X = np.vstack([np.ones(len(x)),x]).T
alpha = 1.0

I = np.eye(X.shape[1])
r4 = np.matmul(np.linalg.inv(np.matmul(X.T, X) + alpha * I ),np.matmul(X.T, y))
yh4 = np.matmul(X, r4)

print()
plt.scatter(x, y)
plt.plot(x, yh4)
plt.show()