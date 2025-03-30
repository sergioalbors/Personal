#LINEAR REGRESSION EXAMPLE   

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("C:\\Users\\salbo\\Desktop\\Personal\\learning regressions\\linear\\regressiondata.csv")
x = data["STUDYTIME"].astype(float)
y = data["SCORE"].astype(float)

m , b = np.polyfit(x, y, 1)

yi = m * x + b
plt.scatter(x,y)
plt.plot(x, yi, linestyle='-', color="red", label=f"y = {m}x + {b}")

plt.text(min(x), max(y), f"m = {m:.2f}\nb = {b:.2f}", fontsize=12, color="blue")


plt.xlabel("X")
plt.ylabel("Y")
plt.title("First example of a linear regression")
plt.show()