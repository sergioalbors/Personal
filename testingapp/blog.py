import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
n = 100
x = np.random.uniform(-6, 6, n)
x = np.sort(x)
y = 4*x**4 + 3*x**2 - 4*x + 1
yi = 4*x**4 + 3*x**2 - 4*x + 1 + 8*np.random.rand(n)  # datos no lineales con ruido

# Matriz de diseño para grado 19 (overfitting)
degree_over = 8
X_over = np.vstack([x**i for i in range(degree_over + 1)]).T
r_over = np.linalg.inv(X_over.T @ X_over) @ X_over.T @ yi
yh_over = X_over @ r_over

# Matriz de diseño para grado 5 (underfitting)
degree_under = 2
X_under = np.vstack([x**i for i in range(degree_under + 1)]).T
r_under = np.linalg.inv(X_under.T @ X_under) @ X_under.T @ yi
yh_under = X_under @ r_under

# Visualización
plt.scatter(x, yi, label="True data", s=40,)
plt.scatter(x, y)
plt.plot(x, yh_over, color='red', label="Overfitting (deg=19)")
plt.plot(x, yh_under, color='green', label="Underfitting (deg=5)")
plt.title("Underfitting vs Overfitting with Least Squares")
plt.legend()
plt.show()

