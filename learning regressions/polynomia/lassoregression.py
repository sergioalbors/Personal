import numpy as np
import matplotlib.pyplot as plt


# 1. Generar datos
np.random.seed(0)
n = 100
x = np.random.uniform(-2, 2, n)
x = np.sort(x)
y_true = np.sin(2*x)
y = y_true + 0.4* np.random.rand(n)

# 2. Crear características polinómicas
degree = 6
X = np.vstack([x**i for i in range(degree + 1)]).T

# 3. Inicializar parámetros
theta = np.zeros(degree + 1)
learningra = 0.1   # learning rate
lmbda = 0.001    # regularización L1
epochs = 1000

# 4. Gradient Descent con Lasso (L1)
for _ in range(epochs):
    y_pred = np.matmul(X, theta)
    error = y_pred - y
    grad = 2 * X.T @ error / len(x)

    # L1: Subgradiente para regularización
    lasso_grad = lmbda * np.sign(theta)
    theta -= learningra * (grad + lasso_grad)

# 5. Mostrar resultados
plt.scatter(x, y, label='Noisy data')
#plt.plot(x, y_true, label='True function', color='red')
plt.plot(x, y_pred, color='red')
plt.legend()
plt.title("Lasso Polynomial Regression (Degree 5)")
plt.show()