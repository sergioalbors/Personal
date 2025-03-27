
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#first I'll start doing a simple linear regression of just two variables (x,y), with random variables that change every time. 

data = pd.read_csv("C:\\Users\\salbo\\Desktop\\Personal\\learning regressions\\regressiondata.csv")
studytime = data["STUDYTIME"]
score = data["SCORE"]

x = data[["STUDYTIME"]]
y = data["SCORE"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.scatter(X_test, y_test, color="blue", label="Datos Reales")
plt.plot(X_test, y_pred, color="red", linewidth=3, label="Línea de Regresión")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared: {r2:.4f}")