import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

np.random.seed(40)
X = np.linspace(-3, 3, 100).reshape(-1, 1)
noise = np.random.randn(100, 1) * 3
y = 2 * X**3 - 5 * X**2 + X + noise

#alpha equals lambda, that is the penalty of the sum of squared coefficients of our model,
#this penalty discourages the model from assigning too high values to any one feature
degree = 5
ridge_model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha = 1000))
ridge_model.fit(X, y)

X_pred = np.linspace(-3, 3, 100).reshape(-1, 1)
y_pred = ridge_model.predict(X_pred)

plt.scatter(X, y)
plt.plot(X_pred, y_pred)
plt.show()