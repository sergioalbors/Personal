#LINEAR REGRESSION EXAMPLE   

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados: horas de estudio (x) y nota (y)
m = 0.7
b = 1.2
n = 20
noise = 0.2 *np.random.randn(n)

x = np.random.uniform (0, 12.5, n)
y = m*x + b + noise
y = np.clip(y, 0, 18)
X = np.vstack([np.ones(len(x)), x]).T  # shape: (n, 2)

w = np.linalg.inv(X.T @ X) @ X.T @ y
y_pred = X @ w

print(f"m: {w[1]:.3f}")
print(f"b: {w[0]:.3f}")

plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, color='red', label='regression line')
plt.xlabel('nº study hours')
plt.ylabel('exam score')
plt.title('student grade prediction')
plt.legend()
plt.grid(True)
plt.show()
def compute_cost_lasso(X, y, theta, lambda_):
    m = len(y)
    predictions = X @ theta
    errors = predictions - y
    mse = (1 / (2 * m)) * np.sum(errors ** 2)
    l1_penalty = lambda_ * np.sum(np.abs(theta[1:]))  # no penalizamos el bias
    return mse + l1_penalty